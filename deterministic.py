import modules

import copy

environment = modules.environment.Environment()
place_cell = modules.place_cell.DeterministicPlaceCell(copy.deepcopy(environment))
agent = modules.agent.DeterministicAgent(place_cell)

environment.maze.display_cui()

while not environment.exit():
    agent.set_wall(environment.wall())
    environment.move(agent.choose_action())
    print(environment.current_coordinate)
