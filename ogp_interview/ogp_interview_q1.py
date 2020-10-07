import typing

'''
1630 start
1640 solved Part 1
1644 solved Part 2
1703 solved Part 3


"This is <3"

# Might dot he following
# string split?
# or do character by character?
# FSM
# enter into a "replacement" state

'''

'''
Templating Engine

Implement a string templating engine
1. Implement a function fillTemplate(s, m), which takes as input a string s and a key-value map m which replaces snippets surrounded by < and > with their corresponding value in m. 

Do not use regular expressions to solve this problem as it makes solving subsequent parts of the problem unnecessarily difficult.

For example:
s = "Hello my name is <firstname> <lastname> child of <father>"
m = {
  firstname: "Luke",
  lastname: "Skywalker",
  father: "Anakin"
}
fillTemplate(s,m) // "Hello my name is Luke Skywalker child of Anakin"


2. Modify your code to work with partially defined maps. If a replacement value is not given the keys in the original template should not be replaced.

For example:
s = "Hello my name is <firstname> <lastname> child of <father>"
m = {
  lastname: "Skywalker",
  father: "Anakin"
}
fillTemplate(s,m) // "Hello my name is <firstname> Skywalker child of Anakin"


3. Sometimes you want to actually show angle brackets instead of having them be replaced. Modify your code to allow users to "escape" characters by preceding them with a semicolon.

Before you start implementing your solution, discuss with your interviewer what edge cases there are when implementing escape characters. Then come up with a list of test cases and desired outputs based on the discussion.

For example:
s = "Hello my name is <firstname> <lastname> child of ;<father;>"
m = {
  firstname: "Luke",
  lastname: "Skywalker",
  father: "Anakin",
}
fillTemplate(s,m) // "Hello my name is Luke Skywalker child of <father>"
'''


'''
Post-mortem:

This was a string replacement question
I managed to get through three parts of the question.

The first part was simple string replacement: this was done pretty quickly.

The second part was not string replacing something if the key wasn't
in the dictionary. This was also OK: pretty quick, 4 minutes.

The third part is where I struggled. This is about escaping
the replacement with a semicolon and there are a couple of cases
to think about. I got a correct solution

At the end I mentioned that the code was getting very difficult
to reason about because of all the cases and checks.
Nikhil agreed and asked me what I would do. I said if I had more
time I would refactor it: take a good hard look at the 
checks and make sure they aren't redundant. I don't think
that was the answer he was looking for, though.
I also considered splitting up into helper functions but couldn't see a good way
to do it.

Nikhil asked me what the time complexity of the solution was
and I said it was O(N) or O(N^2) depending on the time complexity
of replacedString += char.
If the concatenation operation is O(1) then since we only walk through
the string once, the overall time complexity is O(N).
I Googled and checked and the first answer 
[here](https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python)
seemed to say that 
the concatenation operation was O(N).
So I wasted a bit of time trying to get str.join working.
By the time I was done time was over.
It turns out that there is no difference:
[this SO answer](https://stackoverflow.com/a/32773353/4850979)
gives empirical evidence. 
So I needn't have bothered actually and should have moved to step 4...

In general,
I feel like I don't do very well when the requirements of the question
keep changing under me.

Before writing this post-mortem I thought I bombed this question.
After writing this post-mortem I guess doing three parts in 40 minutes 
is not too bad. I correctly identified the time complexity and I believe
my solution is asymptotically optimal.
My thinking was a bit muddled when it came to the third part.
And I should have thought a bit more about how to refactor the function---
but I was pretty frazzled at that point.

'''

# todo type hinting for dictionary


def fillTemplate(s: str, m):
    replacedString = ''
    tokenToLookUp = ''
    inReplaceMode = False
    escapeNextChar = False
    for idx, char in enumerate(s):
        if char == ';':
            # Check if we haven't reached the end of the string.
            # Then we need to peek at the next character to see if it is
            # an angle bracket
            # Only if that's the case do we escape the next character
            if idx < len(s) - 1 and (s[idx+1] == '<' or (s[idx+1] == '>')):
                escapeNextChar = True
            else:
                replacedString = "".join((replacedString, char))
        elif escapeNextChar:
            replacedString = "".join((replacedString, char))
        else:
            # We are not in escapeNextChar
            if char == '<' and not inReplaceMode:
                inReplaceMode = True
                # We are now in ReplaceMode
                tokenToLookUp += char
            elif inReplaceMode:
                tokenToLookUp += char
                if char == '>':  # We've hit the end
                    if tokenToLookUp[1:-1] not in m:
                        replacedString += tokenToLookUp
                    else:
                        replacedString += m[tokenToLookUp[1:-1]]
                    tokenToLookUp = ''
                    inReplaceMode = False
            else:
                replacedString += char
    print(replacedString)
    return replacedString


assert(fillTemplate(
    s="Hello my name is <firstname> <lastname> child of <father>",
    m={
        "firstname": "Luke",
        "lastname": "Skywalker",
        "father": "Anakin"
    }
) == "Hello my name is Luke Skywalker child of Anakin")

assert(fillTemplate(
    s="Hello my name is <firstname> <lastname> child of <father>",
    m={
        "lastname": "Skywalker",
        "father": "Anakin"
    }
) == "Hello my name is <firstname> Skywalker child of Anakin")

assert(fillTemplate(
    s="Hello my name is <firstname> <lastname> child of ;<father;>",
    m={
        "firstname": "Luke",
        "lastname": "Skywalker",
        "father": "Anakin"
    }
) == "Hello my name is Luke Skywalker child of <father>")

assert(fillTemplate(
    s="Hello my name is <firstname> <lastname> child of <father>; I am here",
    m={
        "firstname": "Luke",
        "lastname": "Skywalker",
        "father": "Anakin"
    }
) == "Hello my name is Luke Skywalker child of Anakin; I am here")
