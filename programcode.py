from itertools import product
initial={"C":0.6,"N":0.4}
transition={
    "C":{"C":0.8, "N":0.2},
    "N":{"C":0.3,"N":0.7}
}
emission={
    "C": {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2},
    "N": {"A": 0.4, "C": 0.1, "G": 0.1, "T": 0.4}
}
def probability(path, bases):
    s1, s2 = path
    b1, b2 = bases

    return (
        initial[s1]
        * emission[s1][b1]
        * transition[s1][s2]
        * emission[s2][b2]
    )

def calculate(bases):
    paths = list(product(["C", "N"], repeat=2))
    total = 0

    print("\nSequence:", bases[0], "->", bases[1])

    for path in paths:
        p = probability(path, bases)
        total += p
        print(path[0], "->", path[1], ":", round(p, 4))

    best = max(paths, key=lambda path: probability(path, bases))

    print("Total probability:", round(total, 4))
    print("Best path:", best[0], "->", best[1])
print("Initial probabilities:", sum(initial.values()))

for state in transition:
    print("Transition", state, "row:", sum(transition[state].values()))

for state in emission:
    print("Emission", state, "row:", sum(emission[state].values()))

calculate(("A", "G"))
calculate(("T", "T"))