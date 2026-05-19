class CSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors

    def is_consistent(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor in assignment:
                if assignment[neighbor] == value:
                    return False
        return True

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var
        return None

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]

        return None

    def solve(self):
        return self.backtrack({})


variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

domains = {
    "WA": ["red", "green", "blue"],
    "NT": ["red", "green", "blue"],
    "SA": ["red", "green", "blue"],
    "Q": ["red", "green", "blue"],
    "NSW": ["red", "green", "blue"],
    "V": ["red", "green", "blue"],
    "T": ["red", "green", "blue"]
}

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

csp = CSP(variables, domains, neighbors)
solution = csp.solve()
print("Solution:", solution)