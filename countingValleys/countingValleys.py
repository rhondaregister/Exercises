
n = 8
s = 'UDDDUDUU'

def countingValleys(n, s):
    list_of_steps = list(s)
    incline = 0
    valleys = 0
    for step in list_of_steps:
        if step == 'U':
            incline += 1
            if incline == 0:
                valleys += 1
        elif step == 'D':
            incline += -1
    return valleys

print(countingValleys(n,s))


