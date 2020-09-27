---
---
title: Project talk template
date: 25th September 2020
---

# Introduction

I've confirmed the interview date with OGP on 7th October 2020, 4pm to 6pm.

> We will be looking at your resume and getting you to share more about what
> you have worked on in the past. We’re interested in depth instead of breadth,
> so err on the side of specificity. Be prepared to share technical details
> about what you’ve worked on, including drawing diagrams on the whiteboard if
> necessary (for on-site interviews).

> In particular, we’re trying to answer the following questions about you:
>
> - What did you do?
> - How is it impressive?
> - How did you do it?

> In addition, we’re very interested in finding out how you think and how you
> work, so it would be useful to come prepared to explain any interesting
> engineering decisions that you had to make in the course of your work.

So what I'm going to do:

1. Keep practicing leetcode (but i think this is lower priority atm)
2. Write "talking points" for each of my projects:
   - what was it?
   - why was it important?
   - what was the architecture?
     - prepare diagram, talk about data flow.
     - what was the stack?
     - what were the interesting technical decisions I
       made?
   - any interesting technical challenges?
   - what mistakes did I make/what would I change if I were doing it now?
   - what have I learned?
3. Prepare answers to behavioural questions:
   - favourite project?
   - tell me about a time you had a disagreement/made a mistake ...

---

## Board game engine

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

---

## Parallel processing package (R3PO)

### Brief background/motivation

The first step in the data science pipeline is to gather and process data.
We had about 3 million JSON files we needed to process and a serial solution
would take way too long. I wrote a parallel processing package using Ray
that sped up the time taken to process all the files by ~12x.

The library automatically handles the distribution of tasks to processes.
Because we didn't want to lose any progress if e.g. the machine failed, the
library also saves your progress so you can stop and restart the job anytime,
and logs all errors automatically. I have already extensively documented the
library and how to use it elsewhere and will not repeat it here.

config.yaml:

```yaml
job_name: count_produce
output_path: /home/lieu/dev/r3po/sample/output_dir
processes: 2
source_file_part: .json
source_path: /home/lieu/dev/r3po/sample/produce_log
working_dir: /home/lieu/dev/r3po/sample/working_dir
```

main.py:

```python
from r3po import jobbuilder, jobrunner

# Import the function that will be called by your processes

from count_fruits import count_fruits

CONFIG_YAML_FP = './config.yaml'

# Build jobs

jobbuilder.build_jobs(CONFIG_YAML_FP)

# Run jobs

jobrunner.run_jobs(CONFIG_YAML_FP, count_fruits)
```

This will run the function count_fruits on all the .json files in
source_path, and save the results as CSVs in output_path (one row per JSON
file).

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

---

## MGGG flagship webapp

### Brief background/motivation

Districtr is a districting app where you can
"colour in" districts using a brush tool.
The team wanted to give users some additional context about the
districts they drew:
is your plan valid, and
how "good" is your plan compared to other districting plans?
So I built a new feature to calculate and display this info in real time.

### What it was

My contribution can be seen in the bottom right corner of the below GIF. As
you draw the districts with the brush, three metrics update in real time:

- the contiguity status (whether districts drawn are one continuous whole or get broken up in the middle);
- The number of cut edges;
- How the number of cut edges compares to a sample of plans generated by the Recom redistricting algorithm

### Why it was impressive/ why it was important

This was something the team thought would improve the user experience
greatly and improve the quality of submitted districting plans.

### What was the architecture?

A very simple client-server architecture.
I set a server up with Flask living on `pythonanywhere.com` for \$20 a month
and it was good enough to serve all of the users.

#### Diagram

Too simple to merit a proper diagram.

```
+-----------------+                  +-------------------+
|                  | POST request    |                   |
|                  +----------------->                   |
|  SPA MGGG Webapp |                 |  Flask server     |
|                  |   JSON response |                   |
|                  <-----------------+                   |
| Render response  |                 |                   |
+-----------------+                  +-------------------+
```

#### Dataflow and stack

The Webapp was using a stack I didn't choose: something called LitHTML
which is similar to React in purpose.

I used the Fetch API to send the POST request,
Flask for the server,
Gerrychain to calculate the metrics,
and Vega + HTML5 Canvas to display the dynamic histogram.

There's an SPA Webapp that sends a POST request to the Flask server
as the user draws the districts.

The Flask server receives the district assignment
and calculates the metrics using a Python library called Gerrychain,
then responds to the request with the calculated metrics.

#### Interesting technical decisions I made?

The most interesting technical decision was actually a counterintuitive choice
to keep things as simple as possible.

1. Calculate on client-side or server-side?
2. Send deltas or full district assignment?

Send client-side vs server-side: we were worried about latency when sending
large amounts of cut edges through and thought it would be better to offload
the computation to the client. But calculating client-side would mean a
longer first-load latency as it needs to download the dual graphs, and it would
also mean rewriting many of the functions already available in Python again in
Javascript. Eventually ruled in favour of server-side computation.

Another way I considered to increase performance was to not send the full
district assignment (a dictionary of int:int pairs) but rather only the
deltas (the assignments that have changed since the last district assignment).
I decided that this was more trouble than it was worth since that would mean
the server would have to maintain state.

### Interesting technical challenges?

The app and my contribution are both quite simple but the most difficult bit was
trying to understand the dataflow of the existing application.
When you build something from scratch you have a tacit or explicit understanding
of how the data flows through the entire architecture. But when trying to contribute
you don't have this understanding. Which components talk to which other components?
What does a component need to render? Etc. Before writing a single line of code
I needed to wrap my head around this, and it was especially difficult because I
had no experience working with existing codebases as large as this.

### What mistakes did I make and what would I change if I were doing it now?

1. Autoformatter autoformatted the entire file when I added my own code to the file
   and the SWE was not able to review my PR properly --- had to manually undo
   all the autoformatting, which was quite painful.
2. Spent a day thinking about how to horizontally scale up the server,
   thinking about load balancers and so on, changing to Julia,
   when the first thing I should have done
   was to immediately start benchmarking how long each bit takes. It turned out
   that the main bottleneck was converting the JSON file into a dual graph format
   and it sufficed to simply cache that converted dual graph to get >50x speedups.

### What have I learned?

- How to understand an external codebase --- need more practice on this
- How to collaborate with other developers using GitHub forks, `git branch`,
  `git merge` etc.
- Always benchmark before thinking too hard:
  they say "premature optimisation is the root of all evil",
  and "premature _thinking about_ optimisation" must come a close second.

---

## Bayesian SMS sender

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

## Distributed Raspberry Pi cluster

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

---

## Blocktrain (Blockchain demonstrator)

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

---

## Bespoke building inspection software (Inspector's Gadget)

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?

---

## Dropship Chess

### Brief background/motivation

### What it was

### Why it was impressive/ why it was important

### What was the architecture?

#### Diagram

#### Dataflow and stack

#### Interesting technical decisions I made?

### Interesting technical challenges?

### What mistakes did I make and what would I change if I were doing it now?

### What have I learned?