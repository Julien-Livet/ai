from brain import Brain
from connection import Connection
import numpy as np
import os
import time
import sympy as sp
import sympys
import words

tasks = [
    {"name": "numeric_simple", "input": None, "target": "3.1*x+y", "type": str},
    {"name": "numeric_complex", "input": None, "target": "-2.1*x+4.5*y", "type": str},
    {"name": "symbolic_diff", "input": sp.sin(sp.Symbol("x"))*sp.exp(sp.Symbol("x")),
     "target": sp.cos(sp.Symbol("x"))*sp.exp(sp.Symbol("x")) + sp.sin(sp.Symbol("x"))*sp.exp(sp.Symbol("x")),
     "type": sp.Expr},
    {"name": "word", "input": None, "target": "pourtant", "type": str},
]

def run_brain_task(brain: Brain, task):
    start = time.time()

    try:
        brain.clear_connections()
        brain.deactivate_all_modules()

        for module in brain.modules:
            if ("sympy" in module or "chars" in module or "digits" in module or "symbols" in module or "words.functions" in module or "strs" in module):
                brain.activate_module(module)

        brain.activate_str(task["target"])

        if (task["type"] == sp.Expr and task["input"] != None):
            ids = sympys.add_value(brain, task["input"], "input")

        answers = brain.learn(task["target"])
        elapsed = time.time() - start

        if (isinstance(answers[0], Connection)):
            out = brain.connection_output(answers[0])
        else:
            out = answers[0].output()

        success = (out == task["target"])
    except Exception as e:
        elapsed = time.time() - start
        success = False
        out = str(e)

    return {"task": task["name"], "success": success, "time": elapsed, "output": out}

def benchmark(tasks):
    brain = Brain()
    filename = "benchmark_brain.bin"
    
    if (os.path.exists(filename)):
        brain.load(filename)
    else:
        brain.load("expression_brain.bin")
        sympys.add(brain)
        words.add(brain)
        
        brain.save(filename)

    results = []

    for task in tasks:
        res = run_brain_task(brain, task)
        results.append(res)
        print(f"{res['task']}: success={res['success']} time={res['time']:.2f}s")

    return results

if (__name__ == "__main__"):
    results = benchmark(tasks)
