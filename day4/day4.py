class Room:
    def __init__(self, roomName, id, checkSum):
        self.roomName = roomName
        self.id = id
        self.checkSum = checkSum
        

lines = []
with open('input.txt', 'r') as file:
	lines = [line.strip('\n') for line in file]

def parseRooms(roomStrings):
    rooms = []
    for room in roomStrings:
        room = room.split('-');

        roomName = ''
        # all but the last part
        for i in range(0, len(room) - 1):
            roomName += room[i]

        # last part looks like id[checkSum]
        idAndCheckSum = room[-1].split('[')
        id = int(idAndCheckSum[0])
        checkSum = idAndCheckSum[1].strip(']')
        rooms.append(Room(roomName, id, checkSum))
    
    return rooms

def letterFrequency(string):
    letterCount = {}
    for char in string:
        if char in letterCount:
            letterCount[char] += 1
        else:
            letterCount[char] = 1

    # stable sorting, sort by alphabet first
    alphaSort = sorted(letterCount.items(), key=lambda x: x[0])
    return sorted(alphaSort, key=lambda x: x[1], reverse=True)

def createCheckSum(letterFreq):
    if len(letterFreq) < 5:
        return ''

    checkSum = '' 
    for i in range(0, 5):
        checkSum += letterFreq[i][0]
    return checkSum
    
def isRealRoom(room):
    letterFreq = letterFrequency(room.roomName)
    realCheckSum = createCheckSum(letterFreq)
    if realCheckSum == '':
        return False
    else:
        return realCheckSum == room.checkSum

def rotateLetter(letter, number):
    return chr((ord(letter) - ord('a') + number) % 26 + ord('a'))

def rotateWord(word, number):
    rotatedWord = ''
    for letter in word:
        rotatedWord += rotateLetter(letter, number)
    return rotatedWord 


## main
sumIds = sum([room.id for room in parseRooms(lines) if isRealRoom(room)])
northPoleObjectStorageId = [room.id for room in parseRooms(lines) if isRealRoom(room) and 'northpole' in rotateWord(room.roomName, room.id)][0]

print("Sum of real room ids is: {}".format(sumIds))
print("North pole storage id: {}".format(northPoleObjectStorageId))