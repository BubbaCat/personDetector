from typing import Iterator

import cv2  # type: ignore

from example.interfaces.decoder import Decoder
from utils.models import Frame


class OpenCVVideoDecoder(Decoder):
    def __init__(self, video_path: str, process_each: int):
        self._video_path = video_path
        self._process_each = process_each
        self._number_frame = 0

    def decode(self) -> Iterator[Frame]:
        cap = cv2.VideoCapture(self._video_path)
        ret, img = cap.read()
        self._number_frame += 1

        while ret:
            ret, img = cap.read()
            self._number_frame += 1
            if self._number_frame % self._process_each == 0:
                yield Frame(image=img, number_image=self._number_frame)

