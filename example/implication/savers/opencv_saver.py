import cv2  # type: ignore

from example.interfaces.saver import Saver
from utils.models import Detections, Frame


class OpenCVSaver(Saver):
    def __init__(self, save_dir):
        self._save_dir = save_dir

    def save(self, frame: Frame, detections: Detections) -> None:
        for detection in detections:
            x1, y1, x2, y2 = detection.absolute_box.as_tuple
            cv2.imwrite(f'{self._save_dir}/{frame.number_image:06d}.jpg', frame.image[y1:y2, x1:x2])
