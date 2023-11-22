from typing import Iterator

import cv2  # type: ignore

from example.interfaces.decoder import Decoder
from utils.models import Image


class OpenCVCameraDecoder(Decoder):
    def __init__(self):
        pass

    def decode(self) -> Iterator[Image]:
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()

        while ret:
            ret, img = cap.read()
            yield img
