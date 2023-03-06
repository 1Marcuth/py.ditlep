from ..base import BaseFetcher

class TemporaryQuestsFetcher(BaseFetcher):
    __url = "https://www.ditlep.com/Tournament/GetAll"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ TemporaryQuestsFetcher ]