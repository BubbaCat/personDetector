from example.interfaces.visualizer import Visualizer
from utils.models import Image, Detections, GREEN


class DummyVisualizer(Visualizer):
    def visualize(self, image: Image, detections: Detections) -> None:
        pass
