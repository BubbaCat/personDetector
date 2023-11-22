import cv2  # type: ignore

from example.interfaces.visualizer import Visualizer
from utils.models import Image, Detections, GREEN


class OpenCVVizualizer(Visualizer):
    def __init__(self, delay_ms):
        self._delay_ms = delay_ms

    def visualize(self, image: Image, detections: Detections) -> None:
        # image = cv2.resize(image, (512, 512))
        for det in detections:
            x1, y1, x2, y2 = det.absolute_box.as_tuple
            cv2.rectangle(image, (x1, y1), (x2, y2), GREEN, 2)

        cv2.namedWindow('Press "Q" to exit', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Press "Q" to exit', 1200, 800)
        cv2.imshow('Press "Q" to exit', image)
        cv2.waitKey(self._delay_ms)


