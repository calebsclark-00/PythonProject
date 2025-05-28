def createList():
    chars = []

    for i in range(100):
        chars.append(RandomCharacter.getRandomLowerCase())

def displayList(chars):
    for i in range(len(chars)):
        print(chars(x))
    else:
        print(chars[i], end = '')
def countLetters(char):
    counts = 26 * [0]
    for i in range(len(chars)):
        counts[ord(chars[i] - ord('a'))] += 1
    return counts
def displayCounts(counts):
    for i in range(len(counts)):
        if (i + 1) % 10 == 0:
            print(counts[i], chr(i = ord('a')))
        else:
            print(chars[i], end = '')
def main():
    chars = createlist()

    print("The lowercase letters are:")

    displayList(chars)

    counts
