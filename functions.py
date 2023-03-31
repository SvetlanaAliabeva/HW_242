from typing import Iterable, Any, re


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any):
    return set(data)


def limit_query(value, data: Iterable[str]):
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value, data: Iterable[str]):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def regex_query(value, data: Iterable[str]):
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
