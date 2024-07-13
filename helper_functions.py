def exportToFile(algoName, path, time, memory, output):
    with open(output, 'a') as f:
        f.write(f'{algoName}:\n')
        f.write('Path: ')
        for i in range(len(path)):
            f.write(str(path[i]))
            if i != len(path) - 1:
                f.write(' ->  ')
        f.write('\n')
        f.write(f'Time in seconds: {time}\n')
        f.write(f'Memory in KB: {memory / 1024}\n\n')
    f.close()