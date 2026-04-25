import random
import math

class GA:
    def __init__(self, individualSize, populationSize):
        # Initialize population dictionary to store individuals [chromosome, fitness]
        self.population = dict()   # empty but eg {0: [[1,0,1,0,0,0,0,1], 3], 1: [[0,0,1,1,1,0,0,0], 3]}
        # Size of each individual's chromosome (number of bits) 
        self.individualSize = individualSize
        # Number of individuals in the population
        self.populationSize = populationSize
        # Total fitness of the entire population
        self.totalFitness = 0

        # Create initial population
        i=0
        while i<populationSize: #run 10 times if size is 10
            # Create a list of bits initialized to 0, i.e., [0, 0, 0, 0, 0, 0, 0, 0]
            listOfBits = [0] * individualSize      #starting chromosome
            # Create list of all possible bit positions i.e., [0, 1, 2, 3, 4, 5, 6, 7]
            listOfLocations = list(range(0, individualSize))
            # Randomly decide how many 1s this individual will have
            numberOfOnes = random.randint(0, individualSize-1)  #eg 3
            # Randomly select positions for the 1s, i.e., if numberOfOnes = 3, it might select [2, 5, 7] 
            # .sample() randomly selects (numberofones) unique elements from the (listoflocations) argument).
            # random.sample(population, k) returns a list of k unique elements chosen from population
            onesLocations = random.sample(listOfLocations, numberOfOnes)    # eg, [2,5,7]
            # Set selected positions to 1
            for j in onesLocations:
                listOfBits[j] = 1

            # Store individual in population: [chromosome, fitness], whereas key is index of individual and value is a list of two elements.
            # e.g., [ [0, 1, 0, 1, 0, 0, 1, 0], 3 ]
            self.population[i] = [listOfBits, numberOfOnes]
            # Update total fitness
            self.totalFitness = self.totalFitness + numberOfOnes
            i = i + 1

    def updatePopulationFitness(self):
        """Recalculates the fitness of the entire population"""
        self.totalFitness = 0       #reset before suming
        # Loops over the dictionary keys (0,1,2,…,9)
        for individual in self.population:  # individual is the index
            # Calculate fitness as sum of bits (count of 1s in the chromosome)
            individualFitness = sum(self.population[individual][0])
            # The fitness is stored as the second element in the individual's value (first is the chromosome).
            # Update individual's fitness value in the population dictionary
            self.population[individual][1] = individualFitness
            # Add to total fitness
            self.totalFitness = self.totalFitness + individualFitness

    def selectParents(self):
        """Selects parents using roulette wheel selection"""
        rouletteWheel = []
        # Determine size of roulette wheel (5x population size)
        wheelSize = self.populationSize * 5
        # List to store all fitness values
        h_n = []
        # Collect all fitness values
        for individual in self.population:
            h_n.append(self.population[individual][1])
        
        # Build roulette wheel
        j = 0
        for individual in self.population:
            # Calculate proportional length on wheel for this individual
            individualLength = round(wheelSize*(h_n[j]/sum(h_n)))
            # lets say Total fitness = sum(h_n) = 10, wheelSize = 20 So for individual 0 with fitness 3:
            # individualLength = round(20 * (3/10)) = round(6.0) = 6
            # This means individual 0 will occupy 6 slots on the wheel.
            j=j+1
            # Append individual to wheel based on its fitness
            if individualLength > 0:
                # If individual 0 has individualLength = 6, then: rouletteWheel = [0, 0, 0, 0, 0, 0] Over all individuals,
                # final rouletteWheel might be: [0,0,0,0,0,0,1,1,1,1,1,1,2,3,3,3,3,3,3,3]
                i=0
                while i<individualLength:
                    rouletteWheel.append(individual)
                    i=i+1
        
        # Shuffle the wheel for random selection
        random.shuffle(rouletteWheel)
        parentIndices = []
        # Select parents from roulette wheel
        i=0
        while i<self.populationSize:   #If populationSize = 4, then you select 4 parents.
            # Select random index from the roulette wheel
            parentIndices.append(rouletteWheel[random.randint(0, len(rouletteWheel)-1)])
            i=i+1
        
        # Create new generation from selected parents
        newGeneration = dict()
        i=0
        while i<self.populationSize:
            newGeneration[i] = self.population[parentIndices[i]].copy()
            # If parentIndices = [1, 0, 3, 1], then new generation will be made of copies of those individuals.
            i=i+1
        
        # Replace old population with new generation
        del self.population
        self.population = newGeneration.copy()

        # Update fitness values for new population
        self.updatePopulationFitness()

    def generateChildren(self, crossoverprobability):   # performs crossover on a subset of individuals in the population based on a specified crossover probability.
        """Performs crossover to create new offspring"""
        # Calculate number of pairs to crossover
        numberofPairs = round(crossoverprobability * self.populationSize / 2)
        # If crossoverprobability = 0.8 and populationSize = 10 Then, numberofPairs = round(0.8 * 10 / 2) = round(4.0) = 4

        # Create list of individual indices and shuffle
        individualIndices = list(range(0, self.populationSize))
        random.shuffle(individualIndices)
        
        i=0     # i counts how many individuals have been processed (in pairs)
        j=0     # j tracks the index in the population used to select two parents (j and j+1)
        # Loop through the shuffled indices in pairs
        while i<numberofPairs:
            # Select random crossover point
            crossoverPoint = random.randint(0, self.individualSize-1)
            # Create children by swapping genetic material
            child1 = self.population[j][0][0:crossoverPoint] + self.population[j+1][0][crossoverPoint:]
            child2 = self.population[j+1][0][0:crossoverPoint] + self.population[j][0][crossoverPoint:]
            #   Example:If individual size is 8 and crossover point is 5:
            #   Child1 = Parent1[0:5] + Parent2[5:] = [1, 0, 1, 1, 0] + [0, 1, 1]
            #   Child2 = Parent2[0:5] + Parent1[5:] = [0, 1, 0, 1, 1] + [1, 0, 0]

            # Replace parents(j,j+1) with children
            # Also update fitness (count of 1s)
            self.population[j] = [child1, sum(child1)]
            self.population[j+1] = [child2, sum(child2)]
            # move to next pair of parents
            i=i+2
            j=j+2

        # Update fitness values after crossover: Each individual's fitness, and The total population fitness
        self.updatePopulationFitness()


    def mutateChildren(self, mutationProbability):
        """Mutates one bit in each individual with a given probability"""
        for i in range(self.populationSize):    # Loop over all individuals (0 to 9)
            # Randomly decide whether to mutate this individual
            # We want mutation to happen only 3% of the time if prob is 0.03
            if random.random() < mutationProbability: #random.random() returns a float between 0 and 1. If it’s less than the mutation probability (e.g., 0.1), mutation happens.
                # Pick a random bit to flip
                bitIndex = random.randint(0, self.individualSize - 1)
                # Flip the bit
                if self.population[i][0][bitIndex] == 0:
                    self.population[i][0][bitIndex] = 1
                else:
                    self.population[i][0][bitIndex] = 0
        # Update fitness values after mutation
        self.updatePopulationFitness()

# Main execution
individualSize, populationSize = 8, 10
i = 0
# Create GA instance
instance = GA(individualSize, populationSize)
while True:
    # Run one generation of GA
    instance.selectParents()
    instance.generateChildren(0.8)  # 80% crossover probability
    instance.mutateChildren(0.03)   # 3% mutation probability
    # Print current population and fitness
    print(instance.population)
    print(instance.totalFitness)
    print(i)
    i=i+1
    # Check for perfect solution (all 1s)
    found = False
    for individual in instance.population:
        if instance.population[individual][1] == individualSize:
            found = True
            break
    if found:
        break