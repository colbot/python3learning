import network
import idxLoader

train_data, test_data = idxLoader.load('data')
net = network.Network([784, 30, 10])

net.SGD(train_data, 30, 10, 3.0, test_data=test_data)