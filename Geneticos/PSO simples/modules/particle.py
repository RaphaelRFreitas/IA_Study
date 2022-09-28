import random


class Particle:
    def __init__(self, num_dimension, bounds):
        self.num_dimension = num_dimension
        self.bounds = bounds
        self.position = []
        self.velocity = []

        for i in range(self.num_dimension):
            self.position.append(random.uniform(self.bounds[i][0], self.bounds[i][1]))
            self.velocity.append(random.uniform(self.bounds[i][0], self.bounds[i][1]))
