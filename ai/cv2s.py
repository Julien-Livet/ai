from brain import Brain
from neuron import Neuron
import numpy as np
import cv2

def cvtColor_cv2(img: np.ndarray, code: int) -> np.ndarray:
    return cv2.cvtColor(img, code)

def flip_cv2(img: np.ndarray, flipCode: int) -> np.ndarray:
    return cv2.flip(img, flipCode)

def rotate_cv2(img: np.ndarray, flag: int) -> np.ndarray:
    return cv2.rotate(img, flag)

def erode_cv2(img: np.ndarray, kernel: np.ndarray, iterations: int) -> np.ndarray:
    return cv2.erode(img, kernel, iterations)

def dilate_cv2(img: np.ndarray, kernel: np.ndarray, iterations: int) -> np.ndarray:
    return cv2.dilate(img, kernel, iterations)

def morphologyEx_cv2(img: np.ndarray, op: int, kernel: np.ndarray) -> np.ndarray:
    return cv2.morphologyEx(img, op, kernel)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["cvtColor_cv2"] = brain.add(Neuron(cvtColor_cv2, "cvtColor_cv2", module = "cv2.functions"))
    neuronIds["flip_cv2"] = brain.add(Neuron(flip_cv2, "flip_cv2", module = "cv2.functions"))
    neuronIds["rotate_cv2"] = brain.add(Neuron(rotate_cv2, "rotate_cv2", module = "cv2.functions"))
    neuronIds["erode_cv2"] = brain.add(Neuron(erode_cv2, "erode_cv2", module = "cv2.functions"))
    neuronIds["dilate_cv2"] = brain.add(Neuron(dilate_cv2, "dilate_cv2", module = "cv2.functions"))
    neuronIds["morphologyEx_cv2"] = brain.add(Neuron(morphologyEx_cv2, "morphologyEx_cv2", module = "cv2.functions"))

    return neuronIds

def add_value(brain: Brain, x: np.ndarray, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> np.ndarray:
        return x if type(x) is np.ndarray else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "cv2.variables"))

    return neuronIds
