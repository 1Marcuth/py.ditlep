from ..base import BaseFetcher

class PermanentQuestsFetcher(BaseFetcher):
    __url = "https://www.ditlep.com/Tournament/GetPermanentQuests"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ PermanentQuestsFetcher ]