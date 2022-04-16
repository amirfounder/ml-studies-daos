from typing import TypeVar, Generic, List

from pgsql_repository.extensions.pagination.pageable import BasePageable

T = TypeVar('T')


class PagedResult(Generic[T]):
    def __init__(self, pageable: BasePageable, results: List[T], count: int):
        self.pageable = pageable
        self.count = results
        self.results = count
