'''
211. Design Add and Search Words Data Structure
Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 

Constraints:

    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of  '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.

Accepted
233,973
Submissions
606,440
'''

# Started solving this at Tuesday 29th September, 12pm
# Took about 90 minutes to get a correct solution
# because of edge cases and stuff
# Also, it was hard to trace this because it was complicated
# I should improve my tracing skills so I can trace things like this
# Or use a smaller test case

from collections import deque


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr_trie = self.words
        for i, char in enumerate(word):
            if i == len(word) - 1:
                if char not in curr_trie:
                    curr_trie[char] = {'': None}
                else:
                    curr_trie[char][''] = None
            if char not in curr_trie:
                curr_trie[char] = {}
            # Go one level down
            curr_trie = curr_trie[char]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        stack = deque([(self.words, word)])
        foundWord = False
        while stack:
            curr_trie, substring = stack.pop()
            if curr_trie is None:
                continue
            if substring == '':
                if '' in curr_trie:
                    return True
                else:
                    continue
            else:
                char = substring[0]
                if char == '.':  # Wildcard: check all elements
                    for elem in curr_trie:
                        stack.append((curr_trie[elem], substring[1:]))
                elif char in curr_trie:
                    stack.append((curr_trie[char], substring[1:]))
                else:
                    continue
        return foundWord


w = WordDictionary()
w.addWord("a")
print(w.words)  # addWord("a") -> {'a': {'':''}}
assert(w.search(".") is True)
assert(w.search("..") is False)

w = WordDictionary()
w.addWord("ran")
w.addWord("rune")
w.addWord("runner")
# assert(w.search("r.n") is True)
assert(w.search("....e.") is True)

'''
w = WordDictionary()
w.addWord("bat")
w.addWord("bax")
w.addWord("ba")
print(w.words)
assert(w.search('bat') is True)
assert(w.search('bar') is False)
assert(w.search('.at') is True)
assert(w.search('...') is True)
assert(w.search('c..') is False)
assert(w.search('') is False)
assert(w.search('.') is False)
assert(w.search('b.t.') is False)
assert(w.search('b.') is True)
'''


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Idea is to have a dictionary of dictionaries
# Everytime we add a word we traverse the dictionary to see if it already exists
# If not then add it
