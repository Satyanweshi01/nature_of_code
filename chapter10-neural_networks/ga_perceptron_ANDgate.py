from random import choice,random,randrange
# mainly the entire training a perceptron here will happen with help of genetic algorithm
# so weights of each perceptron will be its dna 
# and fitness function will be successful cases of being a gate such as AND, OR
class Perceptron():
    def __init__(self,length):
        self.weights = [] # this is the DNA
        self.length = length
        #self.learningConstant = 0.01
        self.fitness = 0
        for i in range(self.length):
            self.weights.append(choice([-1,1]))

    def feedForward(self,input_arr):
        summation = 0
        for i in range(self.length):
            summation+= input_arr[i]*self.weights[i]
        return self.activate(summation)

    def activate(self,summation): #step function
        if summation>0:
            return 1
        else:
            return 0    
    # def train(self, inputs, desired):
    #     guess = self.feedForward(inputs)
    #     error = desired - guess

    #     for i in range(len(self.weights)):
    #         self.weights[i] = self.weights[i] + error * inputs[i] * self.learningConstant 
    def fitness_cal(self):
        hit = 0
        attempt = 4
        # for the AND gate
        if self.feedForward([0,0,1]) == 0:
            hit += 1
        if self.feedForward([0,1,1]) == 0:
            hit += 1
        if self.feedForward([1,0,1]) == 0:
            hit += 1
        if self.feedForward([1,1,0]) == 1:
            hit += 1
        self.fitness = (hit*hit)/attempt
    def weight_crossover(parentA,parentB):
        child = Perceptron(parentA.length)
        for weight in range(child.length):
            parentApart = parentA.weights[weight]
            parentBpart = parentB.weights[weight]
            child.weights[weight] = choice([parentApart,parentBpart])
        return child
    def weight_mutate(self,mutationRate):
        random_index = randrange(0,self.length)
        #mutation
        delta_weight = self.weights[random_index]*mutationRate
        self.weights[random_index] = self.weights[random_index] + choice([delta_weight,-delta_weight])


class GATrain():
    def __init__(self,populationSize,mutationRate):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        #initial generation
        self.population = []
        for i in range(self.populationSize):
            perceptron = Perceptron(3) # here two inputs and one bias
            self.population.append(perceptron)
    def populationFitness(self):
        for i in self.population:
            i.fitness_cal()
    def selection(self):
        self.populationFitness()
        childpopulation = []
        for i in range(self.populationSize):
            # finding the fittest parents
            def randomParent():
                    while True:
                        parent = choice(self.population)
                        r2_num = random()
                        if parent.fitness > r2_num:
                            return parent
            parentA = randomParent()
            parentB = randomParent()
            #weight crossover
            child = Perceptron.weight_crossover(parentA,parentB)

            #weight mutation
            child.weight_mutate(self.mutationRate)
            child.fitness_cal()
            print(child.fitness)
            if child.fitness == 4:
                return True,child #returning flag and the trained perceptron
            childpopulation.append(child)
        self.population = childpopulation
        return False,Perceptron(0)
    
        


if __name__ == "__main__":
    menu = True
    while menu:     
        ga = GATrain(populationSize=100,mutationRate=0.01)
        training = False
        while training == False:
            training, perceptron1 = ga.selection()
        print("Genetic algorithmic training is done")
        print(f"Here is the weights of the perceptron: {perceptron1.weights}")
        submenu = True
        while submenu:
            input1 = (input("Enter input of A,B as list\ntype 'exit' to exit: "))
            if input1 == "exit":
                quit()
            else:
                input1 = eval(input1)
                input1.append(1) # for bias as 1
                output1 = perceptron1.feedForward(input_arr=input1)
                print(f"Here is the Y: {output1}")

