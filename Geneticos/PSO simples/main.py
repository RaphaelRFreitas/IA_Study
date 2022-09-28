from modules.particle import Particle
from modules.plot_utils import PlotUtils
from modules import pso_operators

if __name__ == '__main__':
    print('Starting PSO')

    num_iterations = 50
    num_particles = 100
    num_dimension = 2
    bounds = [(-30,10),(-30,10)]
    swarm = []

    for i in range(num_particles):
        swarm.append(Particle(num_dimension, bounds))

    for i in range(num_iterations):
        print(f'Iteration {i}')
        swarm = pso_operators.adjust_velocity(swarm)
        swarm = pso_operators.crazyness(swarm, bounds, num_dimension)
        swarm = pso_operators.update_position(swarm)

        for particle in swarm:
            PlotUtils.plot_particle(particle)
        PlotUtils.plot_iteration(i)

    PlotUtils.save()
    PlotUtils.play()
