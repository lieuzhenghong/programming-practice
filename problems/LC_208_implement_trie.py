'''
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

Accepted
353,034
Submissions
702,432
'''

#

from collections import defaultdict


class Trie:
    def __init__(self):
        self.words = defaultdict(defaultdict)

    def insert(self, word) -> None:
        curr_trie = self.words
        for i, char in enumerate(word):
            if char not in curr_trie:
                curr_trie[char] = defaultdict(defaultdict)
            if i == len(word) - 1:
                # print(curr_trie)
                curr_trie[char][None] = None
            curr_trie = curr_trie[char]

    def search(self, word) -> bool:
        curr_trie = self.words
        for i, char in enumerate(word):
            if char not in curr_trie:
                return False
            curr_trie = curr_trie[char]
        # the last char looks like {'t': {None: None}}
        # on the last character you get curr_trie == {None: None}
        return None in curr_trie

    def startsWith(self, word) -> bool:
        curr_trie = self.words
        for i, char in enumerate(word):
            if char not in curr_trie:
                return False
            curr_trie = curr_trie[char]
        return True

# Reattempted a cleaner solution after reading the solution
# Rather than faffing around with Nones, better to just have a class and
# then have an actual Boolean flag


class TrieNode:
    def __init__(self, letter: str, letters: defaultdict(defaultdict), isTerminal: bool):
        self.letter = letter
        self.letters = letters
        self.isTerminal = isTerminal


class Trie:
    def __init__(self):
        self.letters = defaultdict(TrieNode)

    def insert(self, word) -> None:
        curr_trie = self
        for i, char in enumerate(word):
            if char not in curr_trie.letters:
                curr_trie.letters[char] = TrieNode(char, {}, False)
            if i == len(word) - 1:
                curr_trie.letters[char].isTerminal = True
            curr_trie = curr_trie.letters[char]

    def search(self, word) -> bool:
        curr_trie = self
        for i, char in enumerate(word):
            if char not in curr_trie.letters:
                return False
            curr_trie = curr_trie.letters[char]
        return curr_trie.isTerminal

    def startsWith(self, word) -> bool:
        curr_trie = self
        for i, char in enumerate(word):
            if char not in curr_trie.letters:
                return False
            curr_trie = curr_trie.letters[char]
        return True


t = Trie()
t.insert("bat")
t.insert("bats")
t.insert("b")
# print(t.words)
print(t.letters)
assert(t.search("bat") == True)
assert(t.search("ba") == False)
assert(t.startsWith("a") == False)
assert(t.startsWith("b") == True)
assert(t.startsWith("ba") == True)
assert(t.startsWith("bat") == True)
assert(t.search("battery") == False)
assert(t.search("batt") == False)
assert(t.startsWith("battery") == False)
