import cv2  # type: ignore
import numpy as np
from nptyping import Float32, NDArray, Shape

from example.interfaces.detector import Detector
from utils.models import Box, Detection, Detections, Image, Point
from utils.openvino_adapter import OpenvinoAdapterMixin


Output = NDArray[Shape['1, 1, 200 max_total_detections, [image_id, label, score, x_min, y_min, x_max, y_max]'], Float32]
OutputNew = NDArray[Shape['1, N num detection, [x_min, y_min, x_max, y_max]'], Float32]
FilteredOutput = NDArray[Shape['* num_detections, [image_id, label, score, x_min, y_min, x_max, y_max]'], Float32]
Boxes = NDArray[Shape['* num_detections, [x_min, y_min, x_max, y_max]'], Float32]


class DensenetDetector(OpenvinoAdapterMixin, Detector):
    def _post_processing(self, output: Output, image_height: int, image_width: int) -> Detections:

        detections: Detections = []

        for (x1, y1, x2, y2, score) in output[0]:
            print(x1, y1, x2, y2)
            if score > self._score_threshold:
                detections.append(
                    Detection(
                        absolute_box=Box[int](top_left=Point(x=int(x1), y=int(y1)), bottom_right=Point(x=int(x2), y=int(y2))),
                        relative_box=Box[float](top_left=Point(x=0.1, y=0.1), bottom_right=Point(x=0.1, y=0.1)),
                        score=score,
                        label_as_str='person',
                        label_as_int=1,
                    )
                )
                print(score)

        return detections

    def detect(self, image: Image) -> Detections:
        detections: Detections = self._predict(image=image)
        return detections
