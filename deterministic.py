import modules

import copy

size = (5, 5)
environment = modules.environment.Environment(size)
place_cell = modules.place_cell.DeterministicPlaceCell(size)
agent = modules.agent.DeterministicAgent(place_cell)

environment.maze.display_cui()

while not environment.exit():
    agent.set_wall(environment.wall())
    environment.move(agent.choose_action())
    print(environment.current_coordinate)
