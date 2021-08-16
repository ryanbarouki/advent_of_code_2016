keypad = [['1','2','3'], 
        ['4','5','6'],
        ['7','8','9']]

realKeypad = [[-1, -1, '1', -1, -1],
              [-1, '2', '3', '4', -1],
              ['5', '6', '7', '8', '9'],
              [-1, 'A', 'B', 'C', -1],
              [-1, -1, 'D', -1, -1]]
lines = []
with open('input.txt') as f:
	line = f.readline()
	while line:
		line = line.strip('\n')
		lines.append(line)
		line = f.readline()

def readInstruction(i0, j0, line, keypad):
    i = i0
    j = j0
    for step in line:
        if step == 'U':
            if j > 0 and keypad[j - 1][i] != -1:
                j -= 1 
        elif step == 'R':
            if i < len(keypad) - 1 and keypad[j][i + 1] != -1:
                i += 1
        elif step == 'D':
            if j < len(keypad) - 1 and keypad[j + 1][i] != -1:
                j += 1
        elif step == 'L':
            if i > 0 and keypad[j][i - 1] != -1:
                i -= 1

    return keypad[j][i]

def calcCode(i0, j0, input, keypad):
    output = ''
    for line in input:
        output += readInstruction(i0, j0, line, keypad)

    return output
        
print("First part: {}".format(calcCode(1, 1, lines, keypad)))
print("Second part: {}".format(calcCode(0, 2, lines, realKeypad)))