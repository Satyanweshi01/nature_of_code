from random import choice

class Perceptron():
    def __init__(self,length):
        self.weights = []
        self.length = length
        self.learningConstant = 0.01
        for i in range(self.length):
            self.weights.append(choice([-1,1]))

    def feedForward(self,input_arr):
        summation = 0
        for i in range(self.length):
            summation+= input_arr[i]*self.weights[i]
        return self.activate(summation)

    def activate(self,summation):
        if summation>0:
            return 1
        else:
            return 0
    
    def train(self, inputs, desired):
        guess = self.feedForward(inputs)
        error = desired - guess

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + error * inputs[i] * self.learningConstant 

if __name__ == "__main__":
    def output():
        input1 = eval(input("Enter input of A,B as list: "))
        output1 = perceptron1.feedForward(input_arr=input1)
        print(f"Here is the Y: {output1}")

    perceptron1 = Perceptron(2)

    try: gate_input = int(input('''What gate you want?
    Type 1 for AND
    Type 2 for OR
    Enter your choice: '''))
    except ValueError:
        print("<Enter integer as input>")
        gate_input = "error"

    if gate_input == 1:
        for i in range(100): #training loop
            #making and gate
            perceptron1.train([0,0],0)
            perceptron1.train([0,1],0)
            perceptron1.train([1,0],0)
            perceptron1.train([1,1],1)
        output()
    elif gate_input == 2:
        for i in range(100): #training loop
            #making or gate
            perceptron1.train([0,0],0)
            perceptron1.train([0,1],1)
            perceptron1.train([1,0],1)
            perceptron1.train([1,1],1)
        output()
    else:
        print("Invalid Input")
