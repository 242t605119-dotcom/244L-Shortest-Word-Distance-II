from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict):
        self.positions = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.positions[word].append(i)

    def shortest(self, word1, word2):
        list1 = self.positions[word1]
        list2 = self.positions[word2]

        i = 0
        j = 0
        minimum = float('inf')

        while i < len(list1) and j < len(list2):
            minimum = min(minimum, abs(list1[i] - list2[j]))

            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1

        return minimum
