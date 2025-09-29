from brain import Brain
from connection import Connection
import cv2
import cv2s
import digits
from neuron import Neuron

brain = Brain()
digits.add(brain)
cv2s.add(brain)

img_src = cv2.imread("img_src.jpg")

img_dst = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)
img_dst = cv2.flip(img_dst, 0)

brain.clear_connections()
brain.activate_all_modules()

neuronIds = cv2s.add_value(brain, img_src, "img_src")

answers = brain.learn(img_dst, depth = 10, compact_name = "img_dst", compact_module = "cv2.constants", module = "cv2.functions", timeout = 30 * 1000)

if (isinstance(answers[0], Connection)):
    print(brain.connection_str(answers[0]).replace("\n", "").replace("\\", "").replace(" ", ""), "->", brain.connection_output(answers[0]))
else:
    print(brain.neuron_name(answers[0]), "->", answers[0].output())

try:
    brain.show2d(seed = 0, title = "Image transform", colorBy = "weight")
except:
    pass

brain.show3d(seed = 0, title = "Image transform", colorBy = "weight")
