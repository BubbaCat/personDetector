from abc import ABC, abstractmethod

from utils.models import Detections, Image


class Painter(ABC):

    @abstractmethod
    def paint(self, image: Image, detections: Detections) -> Image:
        raise NotImplementedError
