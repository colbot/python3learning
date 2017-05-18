import sys
import random
import numpy as np


class Network:

    def __init__(self, layer_sizes):
        self.num_layer = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.biases = [np.random.randn(y) for y in layer_sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]

    @staticmethod
    def sigmod(z):
        return 1.0/(1.0+np.exp(-z))

    @staticmethod
    def sigmod_prime(z):
        return Network.sigmod(z)*(1-Network.sigmod(z))

    def feed_forward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = Network.sigmod(np.dot(w, a)+b)
        return a

    def SGD(self, train_data, num_iter, batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)
        n = len(train_data)
        for loop in range(num_iter):
            random.shuffle(train_data)
            mini_batch = [train_data[k:k+batch_size] for k in range(0, n, batch_size)]
            for batch in mini_batch:
                self.update_batch(batch, eta)
            if test_data:
                print('Epoch {0}: {1} / {2}'.format(loop, self.evalute(test_data), n_test))
            else:
                print('Epoch {0} complete'.format(loop))

    def update_batch(self, batch, eta):
        n_b = [np.zeros(b.shape) for b in self.biases]
        n_w = [np.zeros(w.shape) for w in self.weights]
        learning_ratio = eta/len(batch)
        for x, y in batch:
            delta_b, delta_w = self.backprop(x, y)
            n_b = [n_b + b for n_b, b in zip(n_b, delta_b)]
            n_w = [n_w + w for n_w, w in zip(n_w, delta_w)]
            self.biases = [b-learning_ratio*nb for b, nb in zip(self.biases, n_b)]
            self.weights = [w-learning_ratio*nw for w, nw in zip(self.weights, n_w)]

    def backprop(self, x, y):
        value = x
        values = [x]
        zs = [] # z = sum(w*x) + b
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, value) + b
            zs.append(z)
            value = Network.sigmod(z)
            values.append(value)
        n_b = [np.zeros(b.shape) for b in self.biases]
        n_w = [np.zeros(w.shape) for w in self.weights]
        delta = self.cost_derivative(values[-1], y) * Network.sigmod_prime(zs[-1])
        n_b[-1] = delta
        n_w[-1] = np.dot(delta[np.newaxis,:].transpose(), values[-2][np.newaxis, :])

        for l in range(2, self.num_layer):
            z = zs[-l]
            sp = Network.sigmod_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            n_b[-l] = delta
            n_w[-l] = np.dot(delta[np.newaxis,:].transpose(), values[-l-1][np.newaxis,:])
        return (n_b, n_w)

    def evalute(self, data):
        result = [(np.argmax(self.feed_forward(x)), np.argmax(y)) for (x, y) in data]
        return sum(int(x==y) for (x, y) in result)

    def cost_derivative(self, output, y):
        return (output - y)

