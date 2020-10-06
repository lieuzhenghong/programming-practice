'''
Busiest Time in The Mall

The Westfield Mall management is trying to figure out what the busiest moment
at the mall was last year. You’re given data extracted from the mall’s door
detectors. Each data point is represented as an integer array whose size is
3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors,
and whether the visitors entered or exited the mall (0 for exit and 1 for
entrance), respectively. Here’s an example of a data point: [ 1440084737, 4,
0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative
integer holding the number of seconds that have elapsed since 00:00:00 UTC,
Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that
returns the time at which the mall reached its busiest moment last year. The
return value is the timestamp, e.g. 1480640292. Note that if there is more
than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp.
Explain your solution and analyze its time and space complexities.

Example:

input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378 # since the increase in the number of people
                   # in the mall is the highest at that point

Constraints:

    [time limit] 5000ms

    [input] array.array.integer data
        1 ≤ data.length ≤ 100

    [output] integer
'''

# Two-pass, O(n) solution:
# Step 1:
# Initialise a dictionary of [Timestamp]: int which is the numebr of people who entered at that timestamp (can be negative)
# Go down the array
# If timestamp in timestamp_dict:
# plus or minus
# Else then we create a new entry

# Step 2:
# Go through the dictionary, keep a running count, and then return the timestamp with the highest count


def find_busiest_period(data):
    last_timestamp = data[0][0]
    peak_timestamp = data[0][0]
    peak_visitors = 0
    curr_visitors = 0
    for (timestamp, number, io) in data:
        # If timestamp == last_timestamp, then we append number to curr_visitors
        # Otherwise, we set last_timestamp = timestamp and we set curr_visitors = number
        # -number if io == 0, number otherwise
        delta_visitors = number if io else -number
        if timestamp == last_timestamp:
            curr_visitors += delta_visitors
        else:
            if peak_visitors < curr_visitors:
                peak_visitors = curr_visitors
                peak_timestamp = last_timestamp

            last_timestamp = timestamp
            curr_visitors += delta_visitors

    if peak_visitors < curr_visitors:
        peak_visitors = curr_visitors
        peak_timestamp = last_timestamp

    return peak_timestamp


'''
# [[0,5,1]] 
  => timestamp = last_timestamp 
      curr_visitors += delta_visitors # curr_visitors = 5
    peak_visitors = 5
    
    return 5
    
[0 14, 1], 
[0, 4,  0],
[0 2,  0],
[1, 10, 1],

last_timestamp = 0, peak, current = 0

for loop:
  [0, 14, 1]
  delta = 14
  timestamp IS EQUAL == last_timestamp:
    curr += delta # curr = 14
  peak = 0
  
  [1,4,0]
  delta = -4
  timestamp NIS EQUAL 
    curr += delta # curr = 10
  peak not updated
  
  [0,2,0]
  delta = -2
    curr += delta # curr = 8
  peak not updated
  
  [1,10,1]
  delta = 1
  peak = curr = 8
  last_timestamp = 1
  curr_visitors = 9

'''

data = [[1487799425, 14, 1],
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 7,  1],
        [1487901211, 7,  0]]
print(find_busiest_period(data))  # 1487800378
