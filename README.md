

# Python Dig


#### *Improve your Python mental model when working with agents*

Get a deeper grasp of Python’s more advanced language features by tinkering with small demo scripts for a few minutes a day.

### Why?

Sure, agents write the code.

That makes a deeper understanding of the language’s core principles and mental model more important, not less.

And sometimes all you need to grasp an idea is to play around with some code. 
Run a script, add a breakpoint, change a line or two, and run it again.

You’ll have a better mental harness for working with agents. 
When you say LGTM, you’ll actually know what you’re approving — it will mean more than “the agent says it works”.



### The Python Vibe Coder's Mental Model

The value shifts from “I need to remember how to write this” to
“I need to recognise what the agent just generated, judge whether it is correct,
and know when the abstraction is starting to leak.”

* Faster code review of generated code
* Better prompts because you can name the mechanism precisely
* Easier debugging when generated code behaves unexpectedly
* Less chance of accepting plausible-looking but semantically wrong code
* Better ability to simplify overengineered agent output

For a vibe/agent-assisted workflow, you do not need to memorise every detail.

You need enough of a mental model to say: “this works, but the shared mutable state is unsafe”,
“this async code is still blocking”, “this inheritance relies on a fragile MRO”,
“this attribute lookup is not doing what it appears to”, “this resource lifetime is not actually controlled”, etc.

That makes small runnable demo scripts useful: they are less a syntax reference and more a set of *executable mental models*.

### How to use this repo?

Just clone this repo next to your work stuff. Every now and then take 10-15 minutes to tinker with a single script. Run it, debug it, modify the code, add some comments.
This should fit even to a busy schedule, one step at a time.

The scripts aren't really helpful on their own, and don't lead to a complete system - they're just to demonstrate a point.
Helpful features become apparent with progress, and are eventually used often.


### Python's advanced features

Python is pretty powerful even with its basic features. Usually, you don't need the fancy stuff. So why bother?

* Even if you mostly vibe-code with agents, knowing what Python *can* actually do makes you much better at steering them, reviewing what they produce, spotting unnecessary complexity, and debugging when things go wrong.

* Once in a while, a tricky case can be handled elegantly with an advanced language feature.

* Developing libraries, tools, utilities, and frameworks often requires a deeper understanding of the language.

* Refactoring large amounts of messy, repetitive “plain Python” into smaller,
cleaner abstractions using the right advanced language features.

* It’s fun! Python is brilliantly designed, and digging into how it works develops
a better feel for software design and architecture.



### Credits
These snippets are based-on/inspired-by countless videos, blog posts, courses, documentation, books &  Stackoverflow answers. The primary Guru’s are David Beazley, Raymond Hettinger, Martijn Pieters & Brandon Rhodes.

In order not to get the busy programmer bogged down by a ton of further readings, 
only when a reference is absolutely necessary to better understand the snippet, it’s there.
There is also a list of recommended resources, if you got the time, but the idea is just to jump to a random snippet at a time and tinker with it.

### Run the code
Use Python 3.14, but most of the scripts will probably run w/o an issue on earlier versions. 

Easiest would be: use uv

Note: For asyncio, the `a_task.py` script in `concurrency/asyncio` is especially useful to understand how asyncio works


### Env vars
For asyncio, recommended:
```
PYTHONASYNCIODEBUG=1
PYTHONTRACEMALLOC=1
```