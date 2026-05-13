Title: A bunch of thoughts on AI
Date: 2026-03-17 00:10
Category: Writing
Slug: ai-missing-pieces
Lang: en

# Preface

I've spent my entire life trying to understand how humans and computers work together, because for 35 years, I got along better with the latter.

I've mostly been employed in positions that give me direct exposure to how humans and computers work together:

 - Building/fixing computers for humans
 - Building software for humans to interact with computers
 - Teaching humans to build computers, and software
 - Teaching humans to use computers to connect with other humans

 But the internet has also been 70% of my personal life for 30 years now, and I've connected with people over BBS', forums, blogs, social media. I have a lot more to say on that in general, but suffice to say that I've always taken some responsibility for the way computers connect us all, which results in my spending a lot of time thinking about it.
 
## The missing pieces
 
 I echo a lot of skepticism out there, but the thing that gets me, as a System Thinker, are the missing pieces.
 
 (Focusing mostly on software engineering)
 
 If AI actually can deliver on most of the promises, what then? There are several specific what thens:
 
  1. If we're able to produce the same quality code at 10X the rate, what are the product management changes that can identify changes at that rate, what are the architectural assumptions most of us make about the cost of code, what are the observability and scaling implications of 10X as many changes? What then?
  2. If we start producing 10X code, without answering the previous questions, does history suggest executive leadership will invest later in answering them?
  3. One of the obvious benefits of really cheap coding and refactoring is cleanup and optimization. We very often choose not to invest in adopting "better" coding practices, at least not all across the codebase at once, leading to internal fragmentation, and slowing external adoption of better patterns. If adopted at scale, this would change software engineering worldwide, because you could rely on that faster adoption of a new version or piece of tooling. If the AI decides that Cypress is better than Selenium, it will just start using it everywhere.
  4. This one only came after I did some real work with an LLM, writing code for another LLM. It went into review, and I felt ridiculous, because it was both janky and overbuilt, but was perfect for what I needed. Every instinct I had told me even if it met every technical requirement, it would be bad to merge, because it would mean less of the codebase understood by a human. But what if my instincts are based on outdated assumptions? What if there's code that humans don't need to understand? Does it have the same testing and observability requirements? More? Less?
  5. UBI, duh!
    
More thoughts on each of these below, but the overall thrust of my writing is that on each of these issues, the AI heavyweights have failed to lead, which suggests to me that they aren't really planning for the success they claim.
  
  
### The Max Power way
  
I have seen a lot of very interesting writing on this, but most of it has been in the past year, and I think of this question as being relatively obvious table stakes for the promises being made. I would have expected OpenAI and Anthrophic to have been building communities to answer these questions 5 years ago, rather than Amazon's Bedrock team posting about them last year (https://blog.joemag.dev/2025/10/the-new-calculus-of-ai-based-coding.html?m=1), and here's [a similar take from Andrew Murphy today](https://andrewmurphy.io/blog/if-you-thought-the-speed-of-writing-code-was-your-problem-you-have-bigger-problems). Very interesting stuff that definitely informs my perspective, but it feels like something that is happening reactively, and definitely unevenly.

(I haven't seen anything about Product Management process changes, but I'm sure it's out there.)

### We'll fix that later

I like to be optimistic, but I also think that absent any push to change, people don't change. Right now, every software engineer knows that there's a lot of stuff less than ideal in the codebase that could have been prioritized in the past, and wasn't. So if all this reliance on AI does bite us in the ass once we're live for 10 million people, by making some other part of our lives more difficult, will we just have to live with it?

Honestly, this is the question we need to address as a technology community. I have no expectation that anyone "selling" AI would also advise you to have a contigency plan.

This might be right time for an industry-wide unionization of some sort, as a way to apply some leverage on how AI will be "sustainably" implemented.

### Building a smarter genius

If we have a tool that reproduces patterns it has seen before, how do we make sure the patterns it sees before are the best ones? What is the abstraction where we are managing pattern lifecycles?

If we can make all the coding patterns in our codebase 'the best" at a trivial cost, that means a new pattern being introduced is a higher value event for us. Something that is good for us to see, because the marginal impact of the pattern itself is now greater than the cost. So more changes means even more value for us, so we will probably do what we can to encourage more changes. We might send our improvements upstream more reliably, knowing they could instantly be of benefit to everyone, resulting in ever more high quality libraries being developed and utilized.

Now, some of the above are more "maybes" then definitelys, but I think they are influencable. For example, we can create skills and agents.md files that encourage agents to behave in this way, and perhaps embed them in tools for library management, even allowing the agents maintaining the codebase the directive to push changes upstream for their peers to grab, rather than patching things locally. Those upstream libraries could even have some mechanism for automatically merging these changes, perhaps by waiting for multiple identical change requests from downstream agents, suggesting general support for the change.

Another concern in this area, though perhaps it deserves its own bullet point, is the change in tooling and process that successful LLM-supported development will provoke. [This LinkedIn post has the gist](https://www.linkedin.com/feed/update/urn:li:share:7436598186993106944/). While there's an abundance of patterns already emerging, it again feels reactive and unequal, as well as incredibly hard to guage for likelihood of success. I think one reason this wasn't a separate bullet for me is that is feels TOO obvious.

### Ephemeral code

[Simon Willison wrote a couple of weeks ago](https://simonwillison.net/2026/Jan/28/the-five-levels/) that he witnessed a team working under these principles:

 - Nobody reviews AI-produced code, ever. They don't even look at it.
 - The goal of the system is to prove that the system works. A huge amount of the coding agent work goes into testing and tooling and simulating related systems and running demos.
 - The role of the humans is to design that system - to find new patterns that can help the agents work more effectively and demonstrate that the software they are building is robust and effective.

So this is happening at a very small scale. But what does it mean at a larger scale? What if most teams start operating like this? What are the infrastructural implications?

Do we need a Github specifically for AI code? Is git even the right vcs for AIs to use to share code? How do we take what we learned about sustainable software patterns in code and apply them to the "design of the system"?

### Universal Basic Income

For the past several years, folks at the top of the AI movement have crowed about all the jobs it would displace. Folk who are themselves incredibly rich and well-connected, who regularly influence policy nationally and internationally on many issues.

So what are they doing to support the 20-90% of the workforce whose jobs they are trying to take?

Anyone who has done serious thinking about this knows that something akin to a Universal Basic Income is the only real approach. Even at the productivity levels of a couple of decades ago, it was clear UBI would be necessary sooner or later.

Just a couple weeks ago, we had [Vinod Khosla talking about 5 year-olds never needing to find a job](https://fortune.com/2026/03/04/why-wont-five-year-olds-have-to-work-as-adults-ai-vinod-khosla-openai/). Not a single mention of how this next generation will pay for food or housing.

# Conclusion

The most involved AI-boosters didn't believe their own claims, and had some other reason for trying to inflate this bubble. I personally believe it's an attempt to avoid being left holding the bag when the Crypto bubble burst, but that's just speculation, and not otherwise relevant to the conclusion.
