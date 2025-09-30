from brain import Brain
import copy
import itertools
from neuron import Neuron
import numpy as np
import random
import typing

def add_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x + y

def sub_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x - y

def mul_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x * y

def truediv_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x / y

def floordiv_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x // y

def mod_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x % y

def pow_ndarray(x: np.ndarray, y: typing.Union[np.ndarray, int, float]) -> np.ndarray:
    return x ** y

def mulmat_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return x @ y

def abs_ndarray(x: np.ndarray) -> np.ndarray:
    return abs(x)

def neg_ndarray(x: np.ndarray) -> np.ndarray:
    return -x

def len_ndarray(x: np.ndarray) -> int:
    return len(x)

def reversed_ndarray(x: np.ndarray) -> np.ndarray:
    return np.array(list(reversed(x)))

def ndarray_to_list(x: np.ndarray) -> list:
    return list(x)

def ndarray_to_set(x: np.ndarray) -> set:
    return set(x)

def ndarray_to_tuple(x: np.ndarray) -> tuple:
    return tuple(x)

def shuffle_ndarray(x: np.ndarray) -> np.ndarray:
    y = copy.deepcopy(x)

    random.shuffle(y)

    return y

def sqrt_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sqrt(x)

def log_ndarray(x: np.ndarray) -> np.ndarray:
    return np.log(x)

def exp_ndarray(x: np.ndarray) -> np.ndarray:
    return np.exp(x)

def cos_ndarray(x: np.ndarray) -> np.ndarray:
    return np.cos(x)

def sin_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sin(x)

def tan_ndarray(x: np.ndarray) -> np.ndarray:
    return np.tan(x)

def acos_ndarray(x: np.ndarray) -> np.ndarray:
    return np.acos(x)

def asin_ndarray(x: np.ndarray) -> np.ndarray:
    return np.asin(x)

def atan_ndarray(x: np.ndarray) -> np.ndarray:
    return np.atan(x)

def cosh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.cosh(x)

def sinh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.sinh(x)

def tanh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.tanh(x)

def acosh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.acosh(x)

def asinh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.asinh(x)

def atanh_ndarray(x: np.ndarray) -> np.ndarray:
    return np.atanh(x)

def logical_not_ndarray(x: np.ndarray) -> np.ndarray:
    return np.logical_not(x)

def logical_and_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.logical_and(x, y)

def logical_or_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.logical_or(x, y)

def logical_xor_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.logical_xor(x, y)

def bitwise_and_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_and(x, y)

def bitwise_or_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_or(x, y)

def bitwise_xor_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.bitwise_xor(x, y)

def invert_ndarray(x: np.ndarray) -> np.ndarray:
    return np.invert(x)

def dot_ndarray(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.dot(x, y))

def cross_ndarray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.cross(x, y)

def ndarray_to_str(x: np.ndarray) -> str:
    return str(x)

def ceil_ndarray(x: np.ndarray) -> np.ndarray:
    return np.ceil(x)

def floor_ndarray(x: np.ndarray) -> np.ndarray:
    return np.floor(x)

def inv_ndarray(x: np.ndarray) -> np.ndarray:
    return np.linalg.inv(x)

def eye_ndarray(x: int) -> np.ndarray:
    return np.eye(x)

def trace_ndarray(x: np.ndarray) -> float:
    return np.trace(x)

def any_ndarray(x: np.ndarray) -> bool:
    return np.any(x)

def all_ndarray(x: np.ndarray) -> bool:
    return np.all(x)

def where_ndarray(condition: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.where(condition, x, y)

def shape_ndarray(x: np.ndarray) -> tuple:
    return x.shape

def tile_ndarray(a: np.ndarray, reps: typing.Union[np.ndarray, tuple, list, int]) -> np.ndarray:
    return np.tile(a, reps)

def flip_ndarray(a: np.ndarray, axis: typing.Union[int, tuple]) -> np.ndarray:
    return np.flip(a, axis)

def rot90_ndarray(a: np.ndarray) -> np.ndarray:
    return np.rot90(a)

def flipud_ndarray(a: np.ndarray) -> np.ndarray:
    return np.flipud(a)

def fliplr_ndarray(a: np.ndarray) -> np.ndarray:
    return np.fliplr(a)

def put_ndarray(at: typing.Union[np.ndarray, tuple, list], src: np.ndarray, dst: np.ndarray) -> np.ndarray:
    begin = np.array(at)
    end = np.array(at) + np.array(src.shape)
    slices = tuple(slice(b, e) for b, e in zip(begin, end))
    m = copy.deepcopy(dst)
    m[slices] = src

    return m

def put_value_ndarray(at: typing.Union[np.ndarray, tuple, list], value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[at] = value

    return m

def segment_ndarray(begin: tuple, end: tuple, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)

    u = np.array(end) - np.array(begin)
    v = u / np.linalg.norm(u)

    if (min(v)):
        v *= min(v)

    step = np.linalg.norm(v) / np.linalg.norm(u)

    for t in np.arange(0, 1, step):
        m[int(begin[0] + t * u[0]), int(begin[1] + t * u[1])] = value

    return m

def hline_ndarray(at: int, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[at, :] = value

    return m

def hlineright_ndarray(at: tuple, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[at[0], at[1]:] = value

    return m

def hlineleft_ndarray(at: tuple, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[at[0], :at[1]] = value

    return m

def vline_ndarray(at: int, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[:, at] = value

    return m

def vlinedown_ndarray(at: tuple, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[at[0]:, at[1]] = value

    return m

def vlineup_ndarray(at: tuple, value: typing.Union[int, float], dst: np.ndarray) -> np.ndarray:
    m = copy.deepcopy(dst)
    m[:at[0], at[1]] = value

    return m

def transpose_ndarray(a: np.ndarray) -> np.ndarray:
    return np.transpose(a)

def zeros_ndarray(shape: typing.Union[int, tuple]) -> np.ndarray:
    return np.zeros(shape)

def ones_ndarray(shape: typing.Union[int, tuple]) -> np.ndarray:
    return np.ones(shape)

def empty_ndarray(shape: typing.Union[int, tuple]) -> np.ndarray:
    return np.empty(shape)

def replace_ndarray(x: typing.Union[int, float], y: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)
    b[b == x] = y

    return b

def move_ndarray(from_: tuple, shape: tuple, to: tuple, a: np.ndarray) -> np.ndarray:
    begin = np.array(from_)
    end = np.array(from_) + np.array(shape)
    slices = tuple(slice(b, e) for b, e in zip(begin, end))

    b = copy.deepcopy(a[slices])

    a[slices] = np.zeros(shape)

    return put_ndarray(to, b, a)

def copy_ndarray(a: np.ndarray) -> np.ndarray:
    return np.copy(a)

def fill_ndarray(x: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)

    return b.fill(x)

def neighbors(idx, exclude_self = True, diagonals = True):
    dims = len(idx)
    deltas = [-1, 0, 1]

    for delta in itertools.product(deltas, repeat=dims):
        if (exclude_self and all(d == 0 for d in delta)):
            continue

        if (not diagonals and sum(d != 0 for d in delta) != 1):
            continue

        t = tuple(i + d for i, d in zip(idx, delta))

        if (any([x < 0 for x in t])):
            continue

        yield t

class Region:
    def __init__(self, indices: list = []):
        self.indices = indices

def region_ndarray(at: tuple, a: np.ndarray) -> Region:
    s = set()
    stack = set()
    stack.add(at)
    v = a[at]
    indices = []

    while (len(stack)):
        loc = stack.pop()

        if (not loc in s):
            s.add(loc)

            try:
                if (a[loc] == v):
                    indices.append(loc)

                    for n in neighbors(loc):
                        stack.add(n)
            except:
                pass

    return Region(indices)

def region2_ndarray(at: tuple, a: np.ndarray) -> Region:
    s = set()
    stack = set()
    stack.add(at)
    v = a[at]
    indices = []

    while (len(stack)):
        loc = stack.pop()

        if (not loc in s):
            s.add(loc)

            try:
                if (a[loc] == v):
                    indices.append(loc)

                    for n in neighbors(loc, diagonals = False):
                        stack.add(n)
            except:
                pass

    return Region(indices)

def fill_region_ndarray(region: Region, x: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)

    for t in region.indices:
        try:
            b[t] = x
        except:
            pass

    return b

def place_region_ndarray(at: tuple, region: Region, x: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)

    for t in region.indices:
        try:
            b[at[0] + t[0] - region.indices[0][0], at[1] + t[1] - region.indices[0][1]] = x
        except:
            pass

    return b

def fill_region_at_ndarray(at: tuple, x: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)

    s = set()
    stack = set()
    stack.add(at)
    v = a[at]

    while (len(stack)):
        loc = stack.pop()

        if (not loc in s):
            s.add(loc)

            try:
                if (b[loc] == v):
                    b[loc] = x

                    for n in neighbors(loc):
                        stack.add(n)
            except:
                pass

    return b

def fill_region2_at_ndarray(at: tuple, x: typing.Union[int, float], a: np.ndarray) -> np.ndarray:
    b = copy.deepcopy(a)

    s = set()
    stack = set()
    stack.add(at)
    v = a[at]

    while (len(stack)):
        loc = stack.pop()

        if (not loc in s):
            s.add(loc)

            try:
                if (b[loc] == v):
                    b[loc] = x

                    for n in neighbors(loc, diagonals = False):
                        stack.add(n)
            except:
                pass

    return b

def min_ndarray(a: np.ndarray) -> float:
    return a.min()

def max_ndarray(a: np.ndarray) -> float:
    return a.max()

def mean_ndarray(a: np.ndarray) -> float:
    return a.mean()

def cumsum_ndarray(a: np.ndarray) -> float:
    return a.cumsum()

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_ndarray"] = brain.add(Neuron(add_ndarray, "add_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["sub_ndarray"] = brain.add(Neuron(sub_ndarray, "sub_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["mul_ndarray"] = brain.add(Neuron(mul_ndarray, "mul_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["mod_ndarray"] = brain.add(Neuron(mod_ndarray, "mod_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["truediv_ndarray"] = brain.add(Neuron(truediv_ndarray, "truediv_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["floordiv_ndarray"] = brain.add(Neuron(floordiv_ndarray, "floordiv_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["pow_ndarray"] = brain.add(Neuron(pow_ndarray, "pow_ndarray", module = "ndarrays.operators.arithmetic"))
    neuronIds["mulmat_ndarray"] = brain.add(Neuron(mulmat_ndarray, "mulmat_ndarray", module = "ndarrays.operators.linearalgebra"))
    neuronIds["abs_ndarray"] = brain.add(Neuron(abs_ndarray, "abs_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["neg_ndarray"] = brain.add(Neuron(neg_ndarray, "neg_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["len_ndarray"] = brain.add(Neuron(len_ndarray, "len_ndarray", module = "ndarrays.functions.conversion"))
    neuronIds["reversed_ndarray"] = brain.add(Neuron(reversed_ndarray, "reversed_ndarray", module = "ndarrays.functions"))
    neuronIds["ndarray_to_list"] = brain.add(Neuron(ndarray_to_list, "ndarray_to_list", module = "ndarrays.functions.conversion"))
    neuronIds["ndarray_to_set"] = brain.add(Neuron(ndarray_to_set, "ndarray_to_set", module = "ndarrays.functions.conversion"))
    neuronIds["ndarray_to_tuple"] = brain.add(Neuron(ndarray_to_tuple, "ndarray_to_tuple", module = "ndarrays.functions.conversion"))
    neuronIds["shuffle_ndarray"] = brain.add(Neuron(shuffle_ndarray, "shuffle_ndarray", module = "ndarrays.functions"))
    neuronIds["sqrt_ndarray"] = brain.add(Neuron(sqrt_ndarray, "sqrt_ndarray", module = "ndarrays.functions"))
    neuronIds["log_ndarray"] = brain.add(Neuron(log_ndarray, "log_ndarray", module = "ndarrays.functions"))
    neuronIds["exp_ndarray"] = brain.add(Neuron(exp_ndarray, "exp_ndarray", module = "ndarrays.functions"))
    neuronIds["cos_ndarray"] = brain.add(Neuron(cos_ndarray, "cos_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["sin_ndarray"] = brain.add(Neuron(sin_ndarray, "sin_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["tan_ndarray"] = brain.add(Neuron(tan_ndarray, "tan_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["acos_ndarray"] = brain.add(Neuron(acos_ndarray, "acos_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["asin_ndarray"] = brain.add(Neuron(asin_ndarray, "asin_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["atan_ndarray"] = brain.add(Neuron(atan_ndarray, "atan_ndarray", module = "ndarrays.functions.trigonometric"))
    neuronIds["cosh_ndarray"] = brain.add(Neuron(cosh_ndarray, "cosh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["sinh_ndarray"] = brain.add(Neuron(sinh_ndarray, "sinh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["tanh_ndarray"] = brain.add(Neuron(tanh_ndarray, "tanh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["acosh_ndarray"] = brain.add(Neuron(acosh_ndarray, "acosh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["asinh_ndarray"] = brain.add(Neuron(asinh_ndarray, "asinh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["atanh_ndarray"] = brain.add(Neuron(atanh_ndarray, "atanh_ndarray", module = "ndarrays.functions.hyperbolic"))
    neuronIds["logical_not_ndarray"] = brain.add(Neuron(logical_not_ndarray, "logical_not_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_and_ndarray"] = brain.add(Neuron(logical_and_ndarray, "logical_and_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_or_ndarray"] = brain.add(Neuron(logical_or_ndarray, "logical_or_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["logical_xor_ndarray"] = brain.add(Neuron(logical_xor_ndarray, "logical_xor_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["bitwise_and_ndarray"] = brain.add(Neuron(bitwise_and_ndarray, "bitwise_and_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["bitwise_or_ndarray"] = brain.add(Neuron(bitwise_or_ndarray, "bitwise_or_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["bitwise_xor_ndarray"] = brain.add(Neuron(bitwise_xor_ndarray, "bitwise_xor_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["invert_ndarray"] = brain.add(Neuron(invert_ndarray, "invert_ndarray", module = "ndarrays.operators.bitwise"))
    neuronIds["dot_ndarray"] = brain.add(Neuron(dot_ndarray, "dot_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["cross_ndarray"] = brain.add(Neuron(cross_ndarray, "cross_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["ndarray_to_str"] = brain.add(Neuron(ndarray_to_str, "ndarray_to_str", module = "ndarrays.functions"))
    neuronIds["ceil_ndarray"] = brain.add(Neuron(ceil_ndarray, "ceil_ndarray", module = "ndarrays.functions.arithmetic"))
    neuronIds["floor_ndarray"] = brain.add(Neuron(floor_ndarray, "floor_ndarray", module = "ndarrays.functions.arithmetic"))
    neuronIds["inv_ndarray"] = brain.add(Neuron(inv_ndarray, "inv_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["trace_ndarray"] = brain.add(Neuron(trace_ndarray, "trace_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["eye_ndarray"] = brain.add(Neuron(eye_ndarray, "eye_ndarray", module = "ndarrays.functions.linearalgebra"))
    neuronIds["any_ndarray"] = brain.add(Neuron(any_ndarray, "any_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["all_ndarray"] = brain.add(Neuron(all_ndarray, "all_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["where_ndarray"] = brain.add(Neuron(where_ndarray, "where_ndarray", module = "ndarrays.operators.logical"))
    neuronIds["shape_ndarray"] = brain.add(Neuron(shape_ndarray, "shape_ndarray", module = "ndarrays.functions"))
    neuronIds["tile_ndarray"] = brain.add(Neuron(tile_ndarray, "tile_ndarray", module = "ndarrays.functions.array"))
    neuronIds["flip_ndarray"] = brain.add(Neuron(flip_ndarray, "flip_ndarray", module = "ndarrays.functions.array"))
    neuronIds["rot90_ndarray"] = brain.add(Neuron(rot90_ndarray, "rot90_ndarray", module = "ndarrays.functions.array"))
    neuronIds["fliplr_ndarray"] = brain.add(Neuron(fliplr_ndarray, "fliplr_ndarray", module = "ndarrays.functions.array"))
    neuronIds["flipud_ndarray"] = brain.add(Neuron(flipud_ndarray, "flipud_ndarray", module = "ndarrays.functions.array"))
    neuronIds["put_ndarray"] = brain.add(Neuron(put_ndarray, "put_ndarray", module = "ndarrays.functions.array"))
    neuronIds["transpose_ndarray"] = brain.add(Neuron(transpose_ndarray, "transpose_ndarray", module = "ndarrays.functions.array"))
    neuronIds["zeros_ndarray"] = brain.add(Neuron(zeros_ndarray, "zeros_ndarray", module = "ndarrays.functions.array"))
    neuronIds["ones_ndarray"] = brain.add(Neuron(ones_ndarray, "ones_ndarray", module = "ndarrays.functions.array"))
    neuronIds["empty_ndarray"] = brain.add(Neuron(empty_ndarray, "empty_ndarray", module = "ndarrays.functions.array"))
    neuronIds["replace_ndarray"] = brain.add(Neuron(replace_ndarray, "replace_ndarray", module = "ndarrays.functions.array"))
    neuronIds["move_ndarray"] = brain.add(Neuron(move_ndarray, "move_ndarray", module = "ndarrays.functions.array"))
    neuronIds["copy_ndarray"] = brain.add(Neuron(copy_ndarray, "copy_ndarray", module = "ndarrays.functions.array"))
    neuronIds["fill_ndarray"] = brain.add(Neuron(fill_ndarray, "fill_ndarray", module = "ndarrays.functions.array"))
    neuronIds["min_ndarray"] = brain.add(Neuron(min_ndarray, "min_ndarray", module = "ndarrays.functions.array"))
    neuronIds["max_ndarray"] = brain.add(Neuron(max_ndarray, "max_ndarray", module = "ndarrays.functions.array"))
    neuronIds["mean_ndarray"] = brain.add(Neuron(mean_ndarray, "mean_ndarray", module = "ndarrays.functions.array"))
    neuronIds["cumsum_ndarray"] = brain.add(Neuron(cumsum_ndarray, "cumsum_ndarray", module = "ndarrays.functions.array"))
    neuronIds["put_value_ndarray"] = brain.add(Neuron(put_value_ndarray, "put_value_ndarray", module = "ndarrays.functions.array"))
    neuronIds["fill_region_at_ndarray"] = brain.add(Neuron(fill_region_at_ndarray, "fill_region_at_ndarray", module = "ndarrays.functions.array"))
    neuronIds["fill_region2_at_ndarray"] = brain.add(Neuron(fill_region2_at_ndarray, "fill_region2_at_ndarray", module = "ndarrays.functions.array"))
    neuronIds["fill_region_ndarray"] = brain.add(Neuron(fill_region_ndarray, "fill_region_ndarray", module = "ndarrays.functions.array"))
    neuronIds["region_ndarray"] = brain.add(Neuron(region_ndarray, "region_ndarray", module = "ndarrays.functions.array"))
    neuronIds["region2_ndarray"] = brain.add(Neuron(region2_ndarray, "region2_ndarray", module = "ndarrays.functions.array"))
    neuronIds["hline_ndarray"] = brain.add(Neuron(hline_ndarray, "hline_ndarray", module = "ndarrays.functions.array"))
    neuronIds["hlineright_ndarray"] = brain.add(Neuron(hlineright_ndarray, "hlineright_ndarray", module = "ndarrays.functions.array"))
    neuronIds["hlineleft_ndarray"] = brain.add(Neuron(hlineleft_ndarray, "hlineleft_ndarray", module = "ndarrays.functions.array"))
    neuronIds["vline_ndarray"] = brain.add(Neuron(vline_ndarray, "vline_ndarray", module = "ndarrays.functions.array"))
    neuronIds["vlinedown_ndarray"] = brain.add(Neuron(vlinedown_ndarray, "vlinedown_ndarray", module = "ndarrays.functions.array"))
    neuronIds["vlineup_ndarray"] = brain.add(Neuron(vlineup_ndarray, "vlineup_ndarray", module = "ndarrays.functions.array"))
    neuronIds["place_region_ndarray"] = brain.add(Neuron(place_region_ndarray, "place_region_ndarray", module = "ndarrays.functions.array"))
    neuronIds["segment_ndarray"] = brain.add(Neuron(segment_ndarray, "segment_ndarray", module = "ndarrays.functions.array"))

    return neuronIds

def add_value(brain: Brain, x: np.ndarray, name = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> np.ndarray:
        return x if type(x) is np.ndarray else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "ndarrays.variables"))

    return neuronIds
