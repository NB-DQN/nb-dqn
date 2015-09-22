import modules

import copy
from multiprocessing import Process, Queue

import warnings;warnings.filterwarnings('ignore')

def experiment_maze(size, environment, next_environment, queue):
    environment.maze.display_cui()

    csvstr = ''

    # Depth-first binary-tree
    # =========================================================================
    print('binary...')
    env = copy.deepcopy(environment)
    agent = modules.agent.DepthFirstAgent(env)
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.choose_action()
        turn += 1
    csvstr += str(turn) + ','

    # Q-agent
    # =========================================================================
    print('q...')
    env = copy.deepcopy(environment)
    agent = modules.agent.QAgent(env)

    # training
    for t in range(0, 1000):
        while not env.exit():
            agent.choose_action()
        env.reset()

    # trained
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.choose_action()
        turn += 1
    csvstr += str(turn) + ','

    # untrained
    env = copy.deepcopy(next_environment)
    agent.environment = env
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.choose_action()
        turn += 1
    csvstr += str(turn) + ','

    # Rand
    # =========================================================================
    print('rand...')
    env = copy.deepcopy(environment)
    agent = modules.agent.RandomAgent(env)
    turn = 0
    while (not env.exit()) and turn < thresh:
        env.move(agent.choose_action())
        turn += 1
    csvstr += str(turn) + ','

    # Novelty search with DeterministicPlaceCell
    # =========================================================================
    print('deterministic...')
    env = copy.deepcopy(environment)
    place_cell = modules.place_cell.DeterministicPlaceCell(size)
    agent = modules.agent.NoveltyAgent(place_cell)
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.set_wall(env.wall())
        action = agent.choose_action()
        agent.place_cell.move(action)
        env.move(action)
        turn += 1
    csvstr += str(turn) + ','

    # Novelty search with PathIntegratingCell
    # =========================================================================
    print('path...')
    env = copy.deepcopy(environment)
    place_cell = modules.place_cell.PathIntegratingCell(size)
    agent = modules.agent.NoveltyAgent(place_cell)
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.set_wall(env.wall())
        action = agent.choose_action()
        agent.place_cell.move(action, env.current_coordinate)
        env.move(action)
        turn += 1
    csvstr += str(turn) + ','

    # Novelty search with VisualPlaceCell
    # =========================================================================
    print('visual...')
    env = copy.deepcopy(environment)
    place_cell = modules.place_cell.VisualPlaceCell(size)
    agent = modules.agent.NoveltyAgent(place_cell)
    turn = 0
    while (not env.exit()) and turn < thresh:
        agent.set_wall(env.wall())
        action = agent.choose_action()
        agent.place_cell.move(action, env.visual_image())
        env.move(action)
        turn += 1
    csvstr += str(turn) + '\n'

    queue.put(csvstr)

size = (9, 9)

f = open('experiment.csv', 'w')
f.write('depth,q_train,q_untrain,rand,deterministic,path,visual\n')

length = 100
training_set = [modules.environment.Environment(size) for i in range(length)]

thresh = 1500

jobs = []
queue = Queue()
for i in range(length):
    if i == length - 1:
        p = Process(target=experiment_maze, args=(size, training_set[i], training_set[0], queue))
    else:
        p = Process(target=experiment_maze, args=(size, training_set[i], training_set[i + 1], queue))
    jobs.append(p)
    p.start()

for proc in jobs:
    val = queue.get()
    f.write(val)
    proc.join()
