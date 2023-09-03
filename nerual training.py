import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


y = np.array([[0], [1], [1], [0]])

np.random.seed(1)


input_neurons = 2
hidden_neurons = 4
output_neurons = 1


weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))


weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))

learning_rate = 0.1
epochs = 10000

for _ in range(epochs):
  
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output_layer_output = sigmoid(output_layer_input)

    error = y - output_layer_output

    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

print("Output after training:")
print(output_layer_output)
