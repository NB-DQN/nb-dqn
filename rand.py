import modules

size = (9, 9)
environment = modules.environment.Environment(size)
agent = modules.agent.RandomAgent(environment)

environment.maze.display_cui()

f = open('rand.log', 'w')

f.write(",".join(str(i) for i in size))
f.write("\n")
f.write(environment.maze.dump_params())
f.write("\n")
f.write("0,0")
f.write("\n")

while not environment.exit():
    environment.move(agent.choose_action())
    f.write(",".join(str(i) for i in environment.current_coordinate))
    f.write('\n')

f.close()
