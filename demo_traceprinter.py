from stackprinter import trace, TracePrinter
import numpy as np

def dosomething(x):
    return dosomethingelse(x)

def dosomethingelse(y):
    a = 2*y
    # raise Exception('ahoi')
    return doYetAnotherThing(y)

def doYetAnotherThing(z):
    a = z
    b = {'a': np.ones(1)}
    return np.ones(0)



# with TracePrinter(style='color', suppressed_paths=[r"lib/python.*/site-packages/numpy"]):
with TracePrinter(style='plaintext'):
    a = np.ones(123)
    dosomething(a)
