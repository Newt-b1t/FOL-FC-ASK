# GROUP ID : AI-16
# TOPIC : 9.3 FOL-FC-ASK
# Simulated Knowledge Base (KB) class
class KB:
    def __init__(self):

        self.facts = set() # stores known facts as a set (no duplicates).
        self.rules = [] # stores rules like implications 

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

# Simulated fol_fc_ask function for forward-chaining
def fol_fc_ask(kb, query):
    """
    Forward-chaining to check if query is provable in KB.
    Query: ['Mortal', 'socrates'] means "Is Mortal(socrates) true?"
    Returns substitution (dict) if provable, None otherwise.
    """
    predicate, term = query  # Unpack query: ['Mortal', 'socrates']

    # Check facts first
    if (predicate, term) in kb.facts:
        return {'x': term}  # Substitution: x = socrates

    # Check rules: e.g., Human(x) → Mortal(x)
    for premise, conclusion in kb.rules:
        prem_pred, prem_var = premise
        conc_pred, conc_var = conclusion
        
        # Match rule: if query matches conclusion, try to prove premise
        if conc_pred == predicate and conc_var == 'x':
            # Substitute term into premise
            substituted_premise = (prem_pred, term) # creating a new statement: Human(socrates) by substituting x with socrates in the rule's premise
            if substituted_premise in kb.facts:
                return {'x': term}  # Rule applies: x = socrates
    
    return None  # No proof found

# Create and populate the Knowledge Base
KB = KB()

# Add facts and rules
KB.add_fact(('Human', 'socrates'))          # Fact: Human(socrates)
KB.add_rule(('Human', 'x'), ('Mortal', 'x')) # Rule: ∀x Human(x) → Mortal(x)

# Main query logic
query = ['Mortal', 'socrates']
result = fol_fc_ask(KB, query)

if result:
    print("Answer substitution found:", result)
else:
    print("No answer found.")

