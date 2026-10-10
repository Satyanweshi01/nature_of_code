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

    def activate(self,summation): #step function
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
    menu = True
    while menu:
        

        try: gate_input = int(input('''What gate you want?
Type 1 for AND
Type 2 for OR
Type 3 to exit
Enter your choice: '''))
        except ValueError:
            print("<Enter integer as input>")
            gate_input = "error"

        if gate_input == 1:
            perceptron1 = Perceptron(3)
            for i in range(200): #training loop
                #making and gate
                perceptron1.train([0,0,1],0) # input1,input2,bias
                perceptron1.train([0,1,1],0)
                perceptron1.train([1,0,1],0)
                perceptron1.train([1,1,1],1)
            
        elif gate_input == 2:
            perceptron1 = Perceptron(3)
            for i in range(200): #training loop
                #making or gate
                perceptron1.train([0,0,1],0)
                perceptron1.train([0,1,1],1)
                perceptron1.train([1,0,1],1)
                perceptron1.train([1,1,1],1)

        elif gate_input == 3:
            menu = False
            continue
        else:
            print("Invalid Input")
            continue
        print("Training is done")
        print(f"Here is the weights of the perceptron: {perceptron1.weights}")
        submenu = True
        while submenu:
            input1 = (input("Enter input of A,B as list\nor type 'retrain' to train the perceptron again\ntype 'exit' to exit: "))
            if input1 == "retrain":
                submenu = False
            elif input1 == "exit":
                quit()
            else:
                input1 = eval(input1)
                input1.append(1) # for bias as 1
                output1 = perceptron1.feedForward(input_arr=input1)
                print(f"Here is the Y: {output1}")

