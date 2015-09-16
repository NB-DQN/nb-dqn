import modules

import copy

size = (9, 9)
environment = modules.environment.Environment(size)
place_cell = modules.place_cell.DeterministicPlaceCell(size)
agent = modules.agent.DeterministicAgent(place_cell)

environment.maze.display_cui()

f = open('deterministic.log', 'w')

try:
    while not environment.exit():
        agent.set_wall(environment.wall())
        environment.move(agent.choose_action())
        f.write(str(environment.current_coordinate))
        f.write('\n')
except KeyboardInterrupt:
    print(agent.wall_information)
    print(agent.place_cell.history)
    print(environment.history)

f.close()
