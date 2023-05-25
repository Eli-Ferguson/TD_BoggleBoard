import random, string, time
from collections import defaultdict

possible_words = ['able', 'acid', 'ache', 'acts', 'aged', 'ahoy', 'airy', 'ajar', 'akin', 'alas', 'ally', 'alms', 'also', 'amid', 'ammo', 'amok', 'ants', 'aqua', 'arch', 'area', 'army', 'arts', 'atom', 'aunt', 'avid', 'away', 'axes', 'axis', 'baby', 'back', 'bake', 'bald', 'balm', 'band', 'bank', 'bare', 'bark', 'base', 'bash', 'bath', 'beak', 'beam', 'bean', 'bear', 'beat', 'beef', 'beer', 'bees', 'belt', 'word', 'list', 'four', 'play', 'game', 'code', 'time', 'tree', 'park', 'work', 'city', 'book', 'love', 'mind', 'rock', 'team', 'song', 'idea', 'zone', 'baby', 'girl', 'hero', 'data', 'home', 'land', 'help', 'rain', 'road', 'baby', 'ship', 'east', 'west', 'moon', 'fire', 'fish', 'lake', 'sand', 'bird', 'door', 'face', 'hand', 'milk', 'mind', 'star', 'baby', 'idea', 'test', 'trip', 'year', 'cool', 'crap', 'aba', 'aca', 'ada', 'aea']
n = len(possible_words)


class Solution:
    board = None
    letter_dict = None
    traversed = None

    def create_board(self, rows, cols):
        self.board = [[random.choice(string.ascii_lowercase) for _ in range(cols)] for _ in range(rows)]

    def create_letter_dict(self):
        self.letter_dict = defaultdict(list)
        for y, row in enumerate(self.board):
            for x, letter in enumerate(row):
                self.letter_dict[letter].append((x, y))

    def substring_exists(self, sub, pos):
        first_letter = sub[0]
        # Check adjacency of the current letter to the position of the previous letter
        oldx, oldy = pos
        for coord in self.letter_dict[first_letter]:
            # Check whether this space was already used
            if coord in self.traversed:
                continue
            newx, newy = coord
            if (abs(oldx - newx) <= 1) and (abs(oldy - newy) <= 1) and (not (oldx == newx and oldy == newy)):
                # Base case
                if len(sub) == 1:
                    return True
                # Otherwise, recurse
                self.traversed.append(coord)
                if self.substring_exists(sub[1:], coord):
                    return True
        return False

    def word_exists(self, word):
        # Check whether any letters are missing
        for letter in word:
            if letter not in self.letter_dict:
                return False

        # Iterate over all starting positions, searching for the word
        found = False
        for start_pos in self.letter_dict[word[0]]:
            self.traversed = [start_pos]
            if self.substring_exists(word[1:], start_pos):
                found = True
                break
        return found

    def find_words(self, words):
        found_count = 0
        for word in words:
            if self.word_exists(word):
                found_count += 1
        return found_count


# Testing
time_start = time.time()
range_min = 5
range_max = 100
batch_size = 5

for i in range(range_min, range_max):
    for _ in range(batch_size):
        time_batch = time.time()
        S = Solution()
        S.create_board(i, i)
        S.create_letter_dict()
        count = S.find_words(possible_words)
        print(f'For Board Size {i}x{i}\nFound {count}/{n} words in {time.time() - time_batch:.5f} seconds\n')

print(f'Boards for size {range_min}..{range_max} done {batch_size}x times using {n} words completed in {time.time() - time_start} seconds')
