from pydantic import validate_arguments
from typing import Optional
import asyncio
import httpx

from ..utils.decrypt_data import decrypt_data

class BaseFetcher:
    @validate_arguments
    def __init__(
        self,
        url: str,
        params: dict = {}
    ) -> None:
        self.__url = url
        self.__params = params

    def get(self) -> dict:
        response = httpx.get(url=self.__url, params=self.__params)
        encrypted_data = response.text
        decrypted_data = decrypt_data(encrypted_data)
        return decrypted_data

class BaseAsyncFetcher:
    @validate_arguments
    def __init__(
        self,
        urls_params: list[tuple[str, Optional[dict]]],
    ) -> None:
        self.__urls_params = urls_params

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    async def get(
        self,
        url_params: tuple[str, dict | None],
        client: httpx.AsyncClient
    ):
        url, params = url_params
        response = await client.get(url=url, params=params)
        encrypted_data = response.text
        decrypted_data = decrypt_data(encrypted_data)

        return decrypted_data

    @validate_arguments
    async def fetch(self):
        async with httpx.AsyncClient(http2=True) as client:
            tasks = [
                self.get(url_params, client)
                for url_params in self.__urls_params
            ]

            responses = await asyncio.gather(*tasks)
            return responses

    def run(self):
        return asyncio.run(self.fetch())

__all__ = [
    BaseFetcher,
    BaseAsyncFetcher
]