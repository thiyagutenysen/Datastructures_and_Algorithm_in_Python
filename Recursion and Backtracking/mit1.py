caps = ['F', 'B', 'B', 'F', 'B', 'F', 'F', 'B', 'B', 'B', 'F']


def intervals(caps):
    keys = list(set(caps))
    commands = dict()
    for i in keys:
        commands[i] = 0
    ref = caps[0]
    commands[ref] += 1
    for i in range(len(caps)):
        if caps[i] == ref:
            continue
        else:
            ref = caps[i]
            commands[ref] += 1
    return commands


print(intervals(caps))
