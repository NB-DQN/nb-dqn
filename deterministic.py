import modules

import copy

size = (9, 9)
environment = modules.environment.Environment(size)
place_cell = modules.place_cell.DeterministicPlaceCell(size)
agent = modules.agent.DeterministicAgent(place_cell)

environment.maze.display_cui()

f = open('deterministic.log', 'w')

f.write(",".join(str(i) for i in size))
f.write("\n")
f.write(environment.maze.dump_params())
f.write("\n")
f.write("0,0")
f.write("\n")

try:
    while not environment.exit():
        agent.set_wall(environment.wall())
        action = agent.choose_action()
        agent.place_cell.move(action)
        environment.move(action)
        f.write(",".join(str(i) for i in environment.current_coordinate))
        f.write('\n')
except KeyboardInterrupt:
    print(agent.wall_information)
    print(agent.place_cell.history)
    print(environment.history)

f.close()
