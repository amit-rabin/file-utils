from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
