Title: Rethinking my excuses about hiring for Test Automation
Date: 2013-10-12 02:19
Author: Alec Munro
Tags: automation, career, job, python, testing
Slug: rethinking-my-excuses-about-hiring-for-test-automation

<div style="text-align: center;">

  

<div style="text-align: center;">

"Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it."

<div style="text-align: right;">

--Brian Kernighan

  

For a long time, I've made the excuse that it's hard to hire QA Engineers, etc. because of stigma based on the desired career path going from testing to development, not the other way around. That may be part of it, but I'm beginning to realize that there might be something much more significant.

  

Being a good Automator is HARD. As Kernighan says, debugging is hard, and automation is all debugging.

  

Practically speaking, the act of debugging is the investigation of a behaviour to determine it's cause. You know the software does a thing, but you don't know why, and you need to figure out how to stop it (usually). So you run it in a controlled environment and try to get that behaviour to happen.

  

What Automators do, most of the time, is write software that interfaces with other software. Automation is it's own integration point, but generally speaking, it's a low-priority client, so you frequently have to exploit one or more other integration points in order to get the software to behave as desired for your automation. Usually, what you want the software to do is on the margins of what it was expected to do, so you do a lot of debugging to identify and simulate the conditions that might generate the desired behaviour.

  

Ok, so that's a lot of horn tooting, but I've met nearly a dozen good Automators, and without exception they are fantastic software developers. That's not to say there aren't other factors that drive people away from automation, but consider this a call to action for those who want to prove their mettle as software craftspeople. 

  

Be an Automator, spend your days debugging everyone else's software, drive the art forward, and enjoy (in the long run) incredible job security!

  

As an aside, I think the headline quote is also what binds me to the Python community. The Zen of Python guides us to avoid "clever" solutions whenever possible, out of the shared recognizance that in the long run, software spends a lot more time being debugged than developed.

