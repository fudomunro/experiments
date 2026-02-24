Title: The Automator's Manifesto, Part One
Date: 2013-08-21 13:55
Author: Alec Munro
Tags: automation, development, process, quality, tdd, testing
Slug: the-automators-manifesto-part-one

In my career in the software field, I've had to teach myself about what quality software was. What the differences were between successful software projects, and unsuccessful ones. It's been a long and often frustrating journey, but I feel like I've come out of it with some principles that could be helpful in guiding people in the field.

  

My principle strength in software development is pattern recognition, especially behavioural. I've used this over the years to refine my approach to software development, by analyzing my own behaviour and that of those around me. For this topic, I've tried to apply that at a higher level to my experience with test automation. What is it about automation that most consistently delivers value? What consistently doesn't? Are there practices can guide us towards the former and away from the latter?  

  

Certainly, to a degree, everything here is derived from common software best practices, but I believe I am able to tailor them in a way that is uniquely suited to the automator. That's why this part is sub-titled…  

  

<h3>

Automation is Software

</h3>

(I use the term "automator" as a generalization of test automation developer, quality engineer, software engineer in test, and a dozen other titles).

<h4>

 

</h4>

<h4>

Apply Best Practices, as best you can

</h4>

I'm sure we've all heard the statistics about how 50%, 75% or 90% of all software projects fail in some way. If we've been around the block, we may even understand some of the steps to take to improve our chances, commonly called "best practices". Automation projects are almost always directly dependent on some other software project, and when they go down, the automation often goes with them.  

  

So from the start, the odds aren't good with your automation. But then consider that of all software projects, automation seems to be the place where best practices are least… practiced. I'm talking about things like:  

<ul>

<li>

Requirements gathering

</li>

<li>

Structured development process

</li>

<li>

Documentation

</li>

<li>

Unit, etc. tests

</li>

<li>

Source control (I've seen this missing several times)

</li>

</ul>

Not to say that every piece of automation needs all of these, just that an automation project is like any other software project, and if we fail to apply common knowledge about software projects to it, we are shooting ourselves in the foot.  

What's more, by practicing these things, you become better equipped to ensure they get applied to the project you are developing automation for, primarily because it can help you establish credibility with the developers working on it. Walking the walk, and all that.  

  

<h4>

Have a Client

</h4>

A key aspect of most successful software projects is the presence of an engaged client. As in most aspects, Automation is no different. Someone who understands the value that you are supposed to be delivering is in the best position to help you understand what needs to be done to deliver that value. Do not simply write tests because there was a decree "we need tests for X".  

  

Instead, you need to understand where the desire for tests comes from? Is it that developers are hesitant to make changes because they have no safety net? Is it that there are lots of regressions in production? Is it that there's a performance optimization project underway, and metrics are needed? Each case would suggest a different focus, and there are many more cases.  

  

But in order to get to this point where you have identified the need, and make progress against meeting it, you need a partner who will vet requirements and validate progress. You need a client. This can be a team of developers, a particular developer, someone in management, or others. But they need to understand the value you are expected to deliver, and have the time to confirm that you are doing so.  

  

<h4>

Fight on the best terrain available to you

</h4>

As I believe is common to anyone who has been in this field for a while, actually automating tests is not always the best way you can improve the quality of the software. As described in "[Test is Dead](http://www.youtube.com/watch?v=X1jWe5rOu3g)", many companies have user bases that accept being used for beta testing. Sure, it might not always be so, but if that is the situation you find yourself in, attempting to keep bugs from those beta testers will not be an ideal use of your time.  

  

A robust functional test suite for a rapidly changing product might cost more in maintenance then it delivers in the first few years. A development team without a mature development process will gain little by forcing them to write unit tests.  Sometimes there's more value to be gained in doing SysAdmin or DevOps type work, such as creating continuous integration infrastructure. The important thing about being an automator is establishing processes that will make producing higher quality software easier. Whether those are actual automated tests run against software, or merely conventions established to improve communication during development is not important. What is important is that you make producing quality software the easiest thing for the developers.  

  

In order of priority, I would suggest:  

<ul>

<li>

Establish a development process

</li>

<li>

Establish a development environment

</li>

<li>

Automate tests

</li>

<li>

Automate monitoring

</li>

</ul>

Each of these makes the following item easier and more valuable.  

  

<h3>

Summary

</h3>

Automation is Software, so:  

<ul>

<li>

Follow best practices, as best you can

</li>

<li>

Have a client, who can validate the value you deliver

</li>

<li>

Understand the terrain of the project you are automating against, and tailor your focus to that

</li>

</ul>

Join me next time as I dive into the value of Proactive Transparency, the danger of Entropy Factors, and the deceptive bliss of Measuring Everything.
