from abc import ABC, abstractmethod

from utils.models import Image, Detections


class Visualizer(ABC):

    @abstractmethod
    def visualize(self, image: Image, detections: Detections) -> None:
        raise NotImplementedError
