from setup import *
from config import *
with open(r"./table1.pickle", 'rb') as f:
    df = pickle.load(f)

toolbox.register("evaluate", evalSymbReg, data=df)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=MaxInitialSize, max_=MaxSize)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MaxSize))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MaxSize))

def main():
    pop = toolbox.population(n=PopulationSize)
    hof = tools.HallOfFame(1)
    
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", np.mean)
    mstats.register("std", np.std)
    mstats.register("min", np.min)
    mstats.register("max", np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb= CrossoverProbability, mutpb= MutationProbability,
                                   ngen = MaxGenerations, stats=mstats,
                                   halloffame=hof, verbose=True)
    # print log
    return pop, log, hof

if __name__ == "__main__":
    a,b,c = main()
    expres = c[0]
    out = stringify_for_sympy(expres)
    final = sympy.simplify(out)
    print(final)