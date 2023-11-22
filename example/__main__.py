import cv2
import numpy as np
import streamlit as st

from abc import ABC, abstractmethod

from example.interfaces.decoder import Decoder
from example.interfaces.detector import Detector
from example.interfaces.saver import Saver
from example.interfaces.visualizer import Visualizer
from example.interfaces.painter import Painter


class BaseAnalytics(ABC):
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class Example(BaseAnalytics):
    def __init__(
            self,
            detector: Detector,
            decoder: Decoder,
            visualizer: Visualizer,
            saver: Saver,
            painter: Painter
    ) -> None:
        self._detector = detector
        self._decoder = decoder
        self._visualizer = visualizer
        self._saver = saver
        self._painter = painter

    def run(self) -> None:
        # for frame in self._decoder.decode():
        #     detections = self._detector.detect(image=frame.image)
        #     self._saver.save(frame=frame, detections=detections)
        #     self._visualizer.visualize(image=frame.image, detections=detections)

        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            image = cv2.imdecode(np.frombuffer(img_file_buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR)
            detections = self._detector.detect(image=image)
            image_with_det = self._painter.paint(image=image, detections=detections)
            st.image(image_with_det)

