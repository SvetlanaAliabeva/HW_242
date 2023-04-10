import re
from typing import Iterable, Iterator, Any, Set


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def limit_query(value, data: Iterable[str]) -> list[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value, data: Iterable[str]) -> Iterator[str]:
    col_number: int = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value, data: Iterable[str]) -> list[str]:
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)


def regex_query(value, data: Iterable[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
