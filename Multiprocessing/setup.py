import pandas as pd
import numpy as np
import pickle

import random
import operator
import math
import sympy
import copy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

from utils import *
from config import *

with open(r"table1.pickle", 'rb') as f:
    df = pickle.load(f)

pset = gp.PrimitiveSet("MAIN", 1)
pset.addEphemeralConstant("rand2", lambda: get_random(np.random.random_sample(), 0,3))# , type(p)
pset.addEphemeralConstant("rand1", lambda: np.random.randint(1,9))# , type(p)
pset.renameArguments(ARG0='z')
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(protectedPow, 2)
pset.addPrimitive(math.exp, 1)
pset.addPrimitive(operator.neg, 1)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

from dask.distributed import Client
client = Client(processes=False)

def dask_map(*args, **kwargs):
    return client.gather(client.map(*args, **kwargs))

# Required for multiprocessing
#import dask.bag as db
# def dask_map(func, iterable):
#   bag = db.from_sequence(iterable).map(func)
#   return bag.compute()

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_= MaxInitialSize, max_= MaxSize)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)
# toolbox.register("map", dask_map)


def evalSymbReg(individual,data):
    func = toolbox.compile(expr=individual)
#     scale_fact = scale_H(func)
    values = []
    try :
        for ii in range(len(data)):
            if(valid(func,data["z"][ii])):
                values.append( ((data["H"][ii] - func(data["z"][ii]))/(data["sigma"][ii])) ** 2)
            else:
                return np.inf,
        return math.fsum(values), 
    except OverflowError:
        return np.inf,