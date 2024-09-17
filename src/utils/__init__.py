from collections.abc import Callable
from os import path
from time import process_time
from typing import TypeVar, TextIO, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def measure_t(fn: Callable[P,R]) -> Callable[P,(R, float)]:
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> (R, float):
        t = process_time()
        r = fn(*args, **kwargs)
        return r, process_time() - t

    return _wrapper

def open_local(__file: str, *paths: str) -> TextIO:
    return open(_local_path(__file, *paths), "r")

def _local_path(__file: str, *paths: str) -> str:
    return path.join(path.dirname(path.realpath(__file)), *paths)

def cmls(s: str) -> str:
    return _clear_multiline_literal_string(s)

def _clear_multiline_literal_string(s: str) -> str:
    return s.strip(" \r\n")