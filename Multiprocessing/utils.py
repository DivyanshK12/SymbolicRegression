import copy 
import math 
from scipy.misc import derivative

def convert_inverse_prim(prim, args):
    """
    Convert inverse prims according to:
    [Dd]iv(a,b) -> Mul[a, 1/b]
    [Ss]ub(a,b) -> Add[a, -b]
    We achieve this by overwriting the corresponding format method of the sub and div prim.
    """
    prim = copy.copy(prim)
    #prim.name = re.sub(r'([A-Z])', lambda pat: pat.group(1).lower(), prim.name)    # lower all capital letters

    converter = {
        'sub': lambda *args_: "Add({}, Mul(-1,{}))".format(*args_),
        'protectedDiv': lambda *args_: "Mul({}, Pow({}, -1))".format(*args_),
        'mul': lambda *args_: "Mul({},{})".format(*args_),
        'add': lambda *args_: "Add({},{})".format(*args_)
    }
    prim_formatter = converter.get(prim.name, prim.format)

    return prim_formatter(*args)

def stringify_for_sympy(f):
    """Return the expression in a human readable string.
    """
    string = ""
    stack = []
    for node in f:
        stack.append((node, []))
        while len(stack[-1][1]) == stack[-1][0].arity:
            prim, args = stack.pop()
            string = convert_inverse_prim(prim, args)
            if len(stack) == 0:
                break  # If stack is empty, all nodes should have been seen
            stack[-1][1].append(string)
    return string

def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

def protectedPow(a, b):
    if a<0 and type(b)!=int:
        return np.inf
    try:
        return math.pow(a, b)
    except ValueError:
        return np.inf
    except OverflowError:
        return np.inf

def scaler(number):
    if number < 1 and number > -1:
        return math.fabs(number)
    else:
        return math.fabs(1/number)

def get_random(number, lower, upper):
    return ((upper - lower) * scaler(number)) + lower

def scale_H(func):
    try :
        H0 = func(0)
        Hubbles_const = 70
        return (Hubbles_const/H0)
    except Exception as e:
        return 1
    
def valid(func, z):
    try :
        x = derivative(func, z, 1e-6)
        if x is not None:
            return True
    except Exception:
        return False