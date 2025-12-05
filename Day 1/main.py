with open('input.txt', 'r') as f:
    readF = f.read()

    currentDial = 50

    timesZero = 0

    for line in readF.split('\n'):
        if line[0] == 'R':
            # right turn
            currentDial += int(line[1:])
            while currentDial > 99:
                currentDial -= 100
            if currentDial == 0:
                timesZero += 1
        else:
            # left turn
            currentDial -= int(line[1:])
            while currentDial < -100:
                currentDial += 100
            if currentDial < 0:
                currentDial = 100 + currentDial  # currentDial must be negative
            if currentDial == 0:
                timesZero += 1
        print('Solution for #1:', currentDial)

with open('input.txt', 'r') as f:
    readF = f.read()

    currentDial = 50

    timesZero = 0

    for line in readF.split('\n'):
        if line[0] == 'R':
            for i in range(int(line[1:])):
                currentDial += 1
                if currentDial == 100:
                    timesZero += 1
                    currentDial = 0
        else:
            # left turn
            for i in range(int(line[1:])):
                currentDial -= 1
                if currentDial == 0:
                    timesZero += 1
                if currentDial == -1:
                    currentDial = 99
        print('Solution for #2:', currentDial, timesZero)
