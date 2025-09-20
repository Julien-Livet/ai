from brain import Brain
from neuron import Neuron
import sympy

def add_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x + y

def sub_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x - y

def mul_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x * y

def div_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x / y

def mod_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x % y

def pow_sympy(x: sympy.Expr, y: sympy.Expr) -> sympy.Expr:
    return x ** y

def sympify_sympy(expr: str) -> sympy.Expr:
    return sympy.sympify(expr)

def simplify_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.simplify(expr)

def expand_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.expand(expr)

def factor_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.factor(expr)

def cancel_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.cancel(expr)

def expr_to_str(expr: sympy.Expr) -> str:
    return str(expr)

def trigsimp_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.trigsimp(expr)

def expand_trig_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.expand_trig(expr)

def expand_log_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.expand_log(expr)

def diff_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.diff(expr)

def integrate_sympy(expr: sympy.Expr) -> sympy.Expr:
    return sympy.integrate(expr)

def add(brain: Brain):
    neuronIds = {}

    neuronIds["add_sympy"] = brain.add(Neuron(add_sympy, "add_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["sub_sympy"] = brain.add(Neuron(sub_sympy, "sub_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["mul_sympy"] = brain.add(Neuron(mul_sympy, "mul_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["div_sympy"] = brain.add(Neuron(div_sympy, "div_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["mod_sympy"] = brain.add(Neuron(mod_sympy, "mod_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["pow_sympy"] = brain.add(Neuron(pow_sympy, "pow_sympy", module = "sympy.operators.arithmetic"))
    neuronIds["sympify_sympy"] = brain.add(Neuron(sympify_sympy, "sympify_sympy", module = "sympy.functions"))
    neuronIds["simplify_sympy"] = brain.add(Neuron(simplify_sympy, "simplify_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["expand_sympy"] = brain.add(Neuron(expand_sympy, "expand_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["factor_sympy"] = brain.add(Neuron(factor_sympy, "factor_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["cancel_sympy"] = brain.add(Neuron(cancel_sympy, "cancel_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["expr_to_str"] = brain.add(Neuron(expr_to_str, "expr_to_str", module = "sympy.functions.conversion"))
    neuronIds["trigsimp_sympy"] = brain.add(Neuron(trigsimp_sympy, "trigsimp_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["expand_trig_sympy"] = brain.add(Neuron(expand_trig_sympy, "expand_trig_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["expand_log_sympy"] = brain.add(Neuron(expand_log_sympy, "expand_log_sympy", module = "sympy.simplifaction.functions"))
    neuronIds["diff_sympy"] = brain.add(Neuron(diff_sympy, "diff_sympy", module = "sympy.functions"))
    neuronIds["integrate_sympy"] = brain.add(Neuron(integrate_sympy, "integrate_sympy", module = "sympy.functions"))

    return neuronIds

def add_value(brain: Brain, x: sympy.Expr, name: str = None):
    neuronIds = {}

    if (name is None):
        name = str(x)

    def value(x = x) -> sympy.Expr:
        return x if type(x) is sympy.Expr else x()

    neuronIds[name] = brain.add(Neuron(value, name, module = "sympy.variables"))

    return neuronIds
