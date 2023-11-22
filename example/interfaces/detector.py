from abc import ABC, abstractmethod

from utils.models import Detections, Image


class Detector(ABC):

    @abstractmethod
    def detect(self, image: Image) -> Detections:
        raise NotImplementedError
