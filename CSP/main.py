
class CSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables      # self.variables = ["WA", "NT", "SA"]

        # dictionary mapping variable to possible values
        self.domains = domains       # Example: { "WA": ["red", "green"], "NT": ["red", "blue"] }

        # dictionary mapping variable to its neighbors
        self.neighbors = neighbors   # Example:{ "WA": ["NT", "SA"], "NT": ["WA"] }

    def is_consistent(self, var, value, assignment):        # Check if assigning value to var is valid
        # Loop over all neighbors of 'var'
        for neighbor in self.neighbors[var]:
            # Example: if var = "WA" then self.neighbors["WA"] returns ["NT", "SA"]

            if neighbor in assignment:
                # Example: assignment = {"WA": "red"} then "NT" in assignment returns False

                if assignment[neighbor] == value:       # dictionary lookup: assignment["NT"] is "green"
                    return False    # If neighbor has SAME value then conflict

        # If no conflicts found
        return True

    def select_unassigned_variable(self, assignment):
        # Pick first unassigned variable (can be replaced with MRV)

        for var in self.variables:      # loops through list ["WA", "NT", "SA"]
            if var not in assignment:   # checks if variable not assigned yet
                # Example: assignment = {"WA": "red"}, "NT" not in assignment returns True
                return var  # return first unassigned
        
        return None

    def order_domain_values(self, var, assignment):     # Return possible values for variable
        return self.domains[var]
        # Example: if var = "WA" then self.domains["WA"] is ["red", "green", "blue"]

    def backtrack(self, assignment):
        # STEP 1: Check if complete
        if len(assignment) == len(self.variables):      #If equal means all assigned
            return assignment  # solution found

        # Step 2: Select variable
        var = self.select_unassigned_variable(assignment)
        # Example: assignment = {"WA": "red"} returns next variable eg "NT"

        # step 3: Try each value
        for value in self.order_domain_values(var, assignment):         # Example: value = "red", then "green", then "blue"
            # STEP 4: Check consistency
            if self.is_consistent(var, value, assignment):
                # steP 5: Assign value
                assignment[var] = value
                # Example: assignment["NT"] = "green" then {"WA": "red", "NT": "green"}

                # step 6: Recursive call
                result = self.backtrack(assignment)     # tries to complete rest of assignment

                # stp 7: If solution found
                if result is not None:  # None means failure
                    return result   # anything else is solution

                # STEP 8: Backtrack (UNDO)
                del assignment[var]                # removes key from dictionary
                # Example:del assignment["NT"] then assignment becomes: {"WA": "red"}

        # STEP 9: if no solution then backtrack
        return None

    def solve(self):
        # starting from from empty assignment
        return self.backtrack({})


# PROBLEM SETUP
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# domains: each variable and its list of values
domains = {
    "WA": ["red", "green", "blue"],
    "NT": ["red", "green", "blue"],
    "SA": ["red", "green", "blue"],
    "Q": ["red", "green", "blue"],
    "NSW": ["red", "green", "blue"],
    "V": ["red", "green", "blue"],
    "T": ["red", "green", "blue"]
}

# neighbors define constraints (must not be same)
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
# Example output:
# {'WA': 'red', 'NT': 'green', 'SA': 'blue'}