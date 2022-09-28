import random
from modules import pso_utils

CRAZINESS_PROBABILITY = 0.02


def adjust_velocity(population):
    population_adjusted = []

    for particle in population:
        closest = pso_utils.find_closest(particle, population)
        particle.velocity = closest.velocity
        population_adjusted.append(particle)

    return population_adjusted


def crazyness(population, bounds, num_dimentions):
    population_crazy = []

    for particle in population:
        if random.uniform(0, 1) < CRAZINESS_PROBABILITY:
            new_velocity = []
            for i in range(num_dimentions):
                new_velocity.append(random.uniform(bounds[i][0], bounds[i][1]))
            particle.velocity = new_velocity
        population_crazy.append(particle)

    return population_crazy


def update_position(population):
    population_updated = []

    for particle in population:
        for i in range(len(particle.position)):
            particle.position[i] += particle.velocity[i]
        population_updated.append(particle)

    return population_updated
