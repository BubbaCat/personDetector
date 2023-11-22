from abc import ABC, abstractmethod

from utils.models import Detections, Image


class Saver(ABC):

    @abstractmethod
    def save(self, image: Image, detections: Detections) -> None:
        raise NotImplementedError
