def export(algoName, path, time, memory):
    print(f'{algoName}:')
    print('Path: ', end='')
    for i in range(len(path)):
        print(path[i], end='')
        if i != len(path) - 1:
            print(' ->  ', end='')
    print()
    print(f'Time in seconds: {time}')
    print(f'Memory in KB: {memory / 1024}')