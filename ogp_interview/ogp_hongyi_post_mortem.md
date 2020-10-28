## Introduction

This is my post-mortem recollection of my interview with Hongyi,
director of GovTech

## Questions Hongyi asked

### Tell me about yourself

I recited my prepared spiel:

> I'm Zhenghong and I've just graduated from the University of Oxford
> where I read Philosophy, Politics, and Economics. Despite what my degree
> might suggest, I've always been incredibly interested in computer
> science and so I've done courses in algos and DS, computer architecture,
> functional programming and so on.

> I like SWE a lot because I like to design and build things with
> measurable impact, and I love delighting my users. (It also scratches my
> creative itch).

> Previously, I built an Electron app for a civil engineering firm which
> streamlined their building inspection process a lot. It saved about 300
> engineer-hours a month. I found this very rewarding because I could see
> directly how my app improved their workflow and delighted the engineers.

> In a previous internship I designed and built an automated SMS sender.
> It uses Bayesian statistics and unique tracking URLs to send optimal
> reminder messages. Seeing the number of active users increase day-by-day
> was really wonderful.

> I always have a backlog of new ideas and love building side projects.
> I'm currently building a real-time, multiplayer board game engine with
> TypeScript, React, and ExpressJS, and am trying to write and sell the
> best puzzle books that money can buy on Amazon.

> I think the work OGP does aligns very well with my own desire to delight
> users and build software that matters.

### Which project do you want to talk about?

launched into my prepared spiel my taxonomy and all this.
I mentioned that complexity is king, but sometimes you have to add complexity
in order to get some features you want.
I gave some examples, including my choice to use React in my army CRUD app
(bad example of adding complexity with no gain),
and my choice to rewrite our codebase in TypeScript for my board game project
(good example of adding complexity for gains in maintainability).

He listened politely and said:

### Okay so I understand the theoretical part of software engineering, can we talk about a project you actually did?

Went back and forth a bit where I explained that I don't really remember the
specifics of the technical decisions that I made a long time ago, the board
game engine is relatively fresher in my mind, but when I spoke with Nikhil and
Chin Ying about it, they weren't very impressed with it.

### Okay, so since you've talked about the board game engine with Nikhil and Chin Ying, tell me about the work you've done in a commercial context.

So I told him about the Bayesian SMS sender. I gave him the background with
Inzura being an insurtech company, us having signed a contract with Thailand's
second largest insurer, etc etc... and so I built a system to send optimal SMSes
to users.

I then walked through the architecture using the two diagrams that I had prepared:
[here](https://lieuzhenghong.com/img/sms_pipeloop/sms_pipeloop_0.png)
and
[here](https://lieuzhenghong.com/img/sms_pipeloop/sms_pipeloop_1.png)
I asked if everything made sense and he said that it did, and he asked:

### Can you explain this multi-armed bandit?

He didn't know what a multi-armed bandit was so I explained what it was:
I gave the example of a row of slot machines and you need to find the best-paying one,
and mentioned the explore-exploit tradeoff.

He asked some good questions here. First he asked about minimising uncertainty,
and I said that's at the core of the explore-exploit tradeoff.
I said that if you were a scientist/psychologist/economist what you want
is to minimise the uncertainty of which arm is best, and so you would divide
the SMSes equally to do so.
But since we were doing business here. we want to strike a balance between
the two extremes of dividing the SMSes equally vs exploiting a local optimum
greedily losing out on gains.
I think I explained this quite well and he got it.

### Does your MAB code do the message sending automatically?

Didn't really understand what he meant by "automatically", there were a couple of
clarifying questions and attempts before I got what he was trying to ask.
So basically he was asking if my code decides how many SMSes of each type to send
automatically, or I have to manually tell the code to send X of this type,
Y of that type, etc. I said that it all happens magically/mathematically:
I tell the code to send 1,000 SMSes and it will calculate the magic numbers to send
X of this type, Y of that type, etc.

### How does your code decide what to send/how much of each message to send?

I asked him to refer to the series of graphs I drew on the page
[here](https://lieuzhenghong.com/2019/09/16/using-thompson-sampling-to-optimise-SMS-effectiveness/),
and explained it to him. It was OK overall, I think there was a bit of confusion
when I talked about sampling the curves, but he got it in the end.
I feel like I should have impressed upon him more how magical this sampling solution
was, but oh well.

### Okay so you've gone through the architecture and I get that, but were there any specific difficult technical decisions that you had to make? What was the hardest part of this project?

I said that the hardest part of this project was building all the disparate
parts and keeping in mind how they fit together, but he interrupted me and said---

### Yes, yes, I get the general difficulty of software engineering, but were there any specific technical difficulties that you encountered?

I can't remember what answer I gave to this but it wasn't very good.
He prompted me a bit:

### Did you run into any issues? Like for instance if the API was rate limited, or if you had to do the database calls a certain way?

Yes, now that he mentioned it, the API was indeed rate-limited.
I called the Ant API folks to ask if they could raise the limits
(they couldn't)
but the way I solved it was simply to sleep 0.5 seconds between POST requests.
But I said this was not that exciting.

This was the only part I smoked him a bit: I talked about batching the queries
to reduce the number of database calls---but I didn't really explain this well---
and also sorting the indices since I knew that the user IDs were indexed,
and I said "I think it's called a cache hit". This was true, but only for
a different project. This ended a bit lamely, he didn't ask any follow up questions.

I could have communicated my difficulty better by saying something along these lines:
"I understand what you're trying to ask, and what signal you're trying to get from me,
but unfortunately I can't remember the specific technical decisions I made
in this project. If you prompt me then it will come to mind but otherwise I tend
to forget these small roadblocks once I solve them because they seem trivial
in hindsight."

### Would you do anything differently in this project?

I said that if I had more time, I would have fixed two things:

1. I spoke about how much of a bodge the Nginx server log-`grepping` was,
   it was fragile, etc. I said that someone suggested that I use a AWS Lambda
   function to update the SQL database on GET request.
   This would certainly have been more robust, more scalable, etc,
   but of course this would mean that I had to learn AWS Lambda and set up a gateway
   and all that and this was time I did not have.
2. Dry run CLI: I accidentally sent the same batch of SMSes twice to the same users
   because I didn't have a proper CLI, I just commented out the line of code in
   the main function that actually sent the SMSes. One time I forgot to
   comment it out and
   So I should have done `argparse` and added a `actually-send` flag
   to prevent such a mistake.

### Okay so I get that you would have done things differently had you had more time. Like it's understandable that you wouldn't have a proper CLI since you had no time. But suppose I gave you the same amount of time to build this same project again. What would you do differently?

I thought very long about this question and really blanked.
Nothing I thought of seemed good: I said
"I would like to say I would write tests... but that takes time.
Do I need a DB? Can I get rid of it? ... probably not... I don't know,
I don't see how my architecture can be made even simpler".

So he started to prompt me:

### So there are two parts of your architecture, correct?

I said, yes --- essentially, there's the automated SMS sending bit,
and there's the Bayesian SMS tracker business that maximises the SMS effectiveness.

### What were the results of your three different SMSes?

I said that it was a null finding: all three types of SMSes were equally effective.
I said that this contradicted my priors which were informed by behavioural economics
literature --- I expected the loss-aversive SMS to do better.

### How would you be able to find out if the SMSes were better or worse than each other?

Now I finally understood what he was getting at.
He was trying to make the following point: since the automated-SMS-sending
part is very easy, and the Bayesian stuff is hard, you should first try
and find out whether you even _need_ the Bayesian stuff.
So I said, yes actually you're right, we could first send out a thousand SMSes or so
to get initial priors to see if we needed it (but see my note after this para).
I said that I wanted to push back against this suggestion a little bit,
because while I agreed that he was right,
but if I had done that, my CEO would not have been able to tell the Thai CEO
that we were using "advanced statistical techniques" to "maximise user uplift"
(I used my hands to do air quotes). He laughed and said, OK, point taken.

I think that was the end of the resume deep dive, at this point it was 1650
(ten minutes until the scheduled end of the interview).
He said that he's conscious of time but he's willing to go over if I was too.
I said yes definitely. I took this as a good sign.

### Why don't you like your job at IMDA?

This was the easiest question for me because I have been thinking about it a lot!

- I can see the writing on the wall: they've pigeonholed me as a policy scholar
  and will want to rotate me around
- Incorrect Job title symptomatic of management-focused culture
- Bloated organisation with few developers
- Bad development culture (waterfall, requirement-gathering by "strategy teams")

And also I said:

> There are some not-very-flattering questions that occasionally come to my mind
> when working at IMDA:
>
> - Why are we doing this?
> - Is this project actually useful for Singapore, or is it just sexy
>   with a lot of buzzwords?
> - Are we doing this to meet some Senior Director's KPI/make them look
>   good?
>   To be clear, I do
>   believe that the people up top in IMDA care a lot too: it's just that
>   the message may have gotten lost in transit after passing through the
>   Byzantine civil service apparatus.

I think he liked this answer because he agreed with everything I said and
it echoed his experience some years ago.

### What are you doing to change it?

This was quite a curveball question! Was not expecting this.

I told him the first day of work I spoke to my immediate superior and asked him
whether or not we were maximising our impact working on this autonomous robot
project rather than doing something like form OCR which would save a lot of
hours doing data entry for many SMEs.
I also said that I'm trying to push to work on some projects but I have no idea
how this could be done.

I actually flipped the question on him and asked him what he would do if he
were in my situation. He actually gave a pretty good answer, a "four-step approach"
which he said is what he did himself when he was a scholar at IDA.

1. Demonstrate competence by doing the nonsense projects much quicker than they expect
2. Carve out space for yourself: "I can do your stupid project really quickly,
   can I have some time to do an alternative project?"
3. Start personal projects and demonstrate competence
4. Use that demonstrated competence to spin off your own team

He mentioned that don't think of the bureaucracy as an immovable object,
but rather a puzzle box that can be undone with the right tugs and pulls in the
right places. You don't need to rotate if your supervisor loves you, for instance.

I said that all sounds good, but why would I rather push hard against the cogs
of the bureaucracy when I can join an organisation that empowers and supports
me to do alternative projects?

This question was quite interesting!
On analysis,
I think he's trying to find out whether I am a typical sinkie
who will just give up when faced with the bureaucracy.
He's probably looking for people with low Agreeableness.
So I think that the fact I challenged my superior on the first day probably
reflected well on me.

I should have linked to my work on Inspector's Gadget as an idea of how some
low-hanging fruit projects can improve the efficiency of private industry.

### Why do you want to work at OGP?

Thank god Celine nudged me to prepare this question!
I very quickly ran through the four pre-prepared reasons:

> The more I read about and hear about OGP from the people I've spoken
> with and interviewed with, the more I want to be part of the team.
>
> I want to be on a team working on meaningful projects,
> I want to be on a team that delights users rather than phoning it in

(and here I mentioned XY problems and OGP's work on JARVIS),

> I appreciate the autonomy and the fact that engineers are expected to push for change,
> I appreciate the flat hierarchy and I believe in you.

On the last point, I referenced what I said about IMDA, and said that in contrast,

> From everything that I've seen and heard, I believe that you really care
> about benefiting Singapore and don't care about more venal
> considerations like looking good/getting promoted.

I think this was a good answer.

### If I took you on at OGP and gave you latitude, what sort of projects would you do?

I said that I don't know because I don't know much about the public service
and would need to do research/look around at what OGP is doing before having an idea
myself.

### Sure, I get that, but what are some suggestions you have anyway?

I told him about my frustrations with Data.gov.sg, the difficulty with getting
updated EMA data when I wanted it this year, and I said I didn't know if the problem
was solvable but I would like it to be solved.

I also said that I didn't know if government was still using paper forms
despite FormSG and maybe we could prototype the OCR thingy I mentioned earlier.

These are pretty lame suggestions but I had already told him that I didn't
know because I would need to do some research before having ideas,
so I think it's acceptable.

In hindsight I should have prepared for this question.

Finally he asked if I had any questions for him, and I had prepared a couple:

### _Where do you see yourself and OGP in five years? Will OGP survive your departure?_

lieu, [27.10.20 17:13]
Three yaers from now stilla t OGP, five years after

lieu, [27.10.20 17:14]
OGP is in a pretty strong position, key infrastructure in place, forms, website, link-sharing etc

lieu, [27.10.20 17:14]
Five years from now all of the IT teams will be obsolete

lieu, [27.10.20 17:15]
150-250 people

lieu, [27.10.20 17:15]
working websites, digital forms, payments, etc

lieu, [27.10.20 17:15]
10 years —- singapore as a model of what modern government looks like

lieu, [27.10.20 17:17]
the civil service stopped enforcing values as an exclusionary criteria

lieu, [27.10.20 17:20]
kids in school —- why can't they view materials online? why can't compare prices across hospitals? can't compare prices across HDB flats?
if you're trying to find data on scammers, police can't understand whatsapp

### _OGP is moving fast, breaking things, scooping scholars --- are you stepping on anyone's toes? How do you deal with that?_

lieu, [27.10.20 17:23]
Most of the IT teams stonewall OGP because OGP are moving them out of the job

lieu, [27.10.20 17:23]
If they were doing anything good they would not be in that scenario

lieu, [27.10.20 17:26]
the one thing I can do is that I am willing to lose —- you have outside options

lieu, [27.10.20 17:30]
Look at bureaucracy as a puzzle box , as something you can move in the right way

## Conclusion

Overall, I think this interview went reasonably well.
I would give it a 70% probability that I get accepted.
I really enjoyed this interview even though it was quite hard,
I really vibed with Hongyi and I appreciated his
piercing questions,
his frankness,
and his willingness to go over time in the interview for me.

I think I could have prepared a bit better.
I think I should have expected the question of what sort of projects
I would like to do at OGP, or paused a bit before answering this question.
But overall I explained most questions well,
I was quite well prepared for most of the questions he asked,
and I'm quite happy with the things that I said off-the-cuff.

I remained positive throughout the interview
(it was easier because I thought it was going well),
I was able to admit when I didn't know something,
I made sure to check understanding ("does that make sense") when explaining things,
and I didn't lie or smoke him.

Something I could have done better is to pause for a bit before answering questions,
and try to speak slowly. I think he probably has a higher tolerance for speaking
quickly than most (he seems pretty smart) but I should pause/slow down for impact.
