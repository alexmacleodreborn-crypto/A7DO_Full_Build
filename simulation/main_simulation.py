from core.world_core import World
from systems.multi_agent_system import Population
import matplotlib.pyplot as plt

world = World(size=(50,50))
world.initialize_random()

pop = Population(world, n=30)

for step in range(200):
    world.step()
    pop.step()

    print(f"Step {step} | Alive: {pop.count()}")

    if step % 10 == 0:
        plt.imshow(world.energy)
        xs = [e.body.position[0] for e in pop.entities]
        ys = [e.body.position[1] for e in pop.entities]
        plt.scatter(ys, xs, c='blue', s=10)
        plt.pause(0.01)
        plt.clf()

    if pop.count() == 0:
        print("Extinction")
        break
