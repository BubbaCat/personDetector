from abc import ABC, abstractmethod

from utils.models import Image, Frame
from typing import Iterator


class Decoder(ABC):

    @abstractmethod
    def decode(self) -> Iterator[Frame]:
        raise NotImplementedError
