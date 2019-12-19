from sys import exit
from typing import List


class GSSetting:
    headers: List[str] = []
    indices: List[int] = []

    def __init__(self) -> None:
        if not (len(self.headers) or len(self.indices)):
            print("Must set headers or indices of model.")
            exit(1)

    @classmethod
    def is_cls_headers(cls) -> bool:
        if len(cls.headers):
            return True

        return False

    @classmethod
    def is_cls_indices(cls) -> bool:
        if len(cls.indices):
            return True

        return False
