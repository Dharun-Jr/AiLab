
import re

def parse_fol(statement):
    return re.findall(r'\w+\([^)]*\)', statement)

def evaluate_fol(statement, facts):
    predicates = parse_fol(statement)

    for pred in predicates:
        name = pred.split('(')[0]
        if name not in facts:
            facts[name] = []

        facts[pred] = []

facts = {
    'Person(John)': [],
    'Person(Mary)': [],
    'Likes(John, IceCream)': [],
    'Likes(Mary, Chocolate)': []
}

statement = 'Likes(x, IceCream)'
evaluate_fol(statement, facts)
for p in facts:
    print(p, "\n")
