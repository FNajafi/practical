#write a python code for addition of  two numbers
def add(a,b):
    return a+b

#wirte a python code for subtraction of two numbers
def sub(a,b):
    return a-b

#write a python code for multiplication of two numbers
def mul(a,b):
    return a*b


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num1 = 5
num2 = 7

factorial_num1 = factorial(num1)
factorial_num2 = factorial(num2)

print(f"The factorial of {num1} is {factorial_num1}")
print(f"The factorial of {num2} is {factorial_num2}")


import pandas as pd

# Read the .csv file into a dataframe
df = pd.read_csv('file.csv')

# Display the dataframe
print(df)


import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, hidden_size)
        self.output_layer = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.output_layer(x)
        return x

# Define the input size, hidden size, and output size
input_size = 10
hidden_size = 20
output_size = 2

# Create an instance of the neural network
model = NeuralNetwork(input_size, hidden_size, output_size)

# Print the model architecture
print(model)

