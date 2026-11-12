
rules = [
    {'name': 'Rule 1', 'conditions': ['A'], 'conclusion': 'B'},
    {'name': 'Rule 2', 'conditions': ['B'], 'conclusion': 'C'},
    {'name': 'Rule 3', 'conditions': ['C'], 'conclusion': 'D'},
    {'name': 'Rule 4', 'conditions': ['E', 'F'], 'conclusion': 'A'}
]

facts = ['E', 'F']

def applicable(rule):
    return all(c in facts for c in rule['conditions'])

def forward_chaining():
    while True:
        added = False

        for rule in rules:
            conclusion = rule['conclusion']

            if applicable(rule) and conclusion not in facts:
                facts.append(conclusion)
                added = True
                print("Applied rule:", rule['name'])
                print("Facts:", facts)

        if not added:
            break

forward_chaining()
