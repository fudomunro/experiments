Title: AI Coding FOMO? That's a no-go! (Bro)
Date: 2026-04-07 00:10
Category: Writing
Slug: ai-coding-fomo
Lang: en

**TLDR**: AI coding is changing fast enough that anything you learn today might not matter tomorrow.

Both when I had a job and when I'm searching for a job, I've talked to a lot of people about the current state of the industry. I've got a lot to say about many aspects of that, some which of which I've already [written about here](/ai-missing-pieces.html).

But for now, I wanted to address the anxiety I keep hearing from people in the industry, that they are missing the AI coding shift.

Some worry that the way they enjoyed working in the past is simply not compatible with how work will be done in the future. It's not the focus of this post, but I don't think that's generally true. The general challenges that made coding interesting will still exist, we will just interact with them at different levels.

Also, despite the title of this post, you might be missing out on opportunities to work in fun ways if you have been completely avoiding AI coding tools. It's been a very interesting ~2 years.

But the focus of this post is demolishing the idea that people or groups who have not yet adopted AI coding tools are incurring some sort of knowledge deficit. While these tools are incredibly powerful, they are also still changing at a rapid clip, and it's not clear which concepts and approaches will be valuable to know in the long run.

So if you're building something that is working for its purpose, without AI coding tools, keep doing that. Don't invest time into adding AI tooling unless it's solving a problem.

# Inflecting

As [Simon Willison talked about](https://simonwillison.net/2026/Apr/2/lennys-podcast/), we recently "passed the inflection point". He was referring to the last 6 months or so, where coding tools have jumped forward once again, but if we pull out to a larger view, I think we can see several inflection points.

I've been directly responsible for adopting and facilitating the adoption of AI tooling as the lead of a platform engineering team, and also in my personal development and mentorship. I've been watching the field very closely.

But I've also been building engineering organizations for almost 30 years, and I understand that an inflection is only the first step in realizing benefit in an organizational change. It takes time and effort to understand and optimize the benefits to your particular needs, and further time and effort to extract generalized learnings from those optimizations that can be applied beyond your situation.

That's to say nothing of resolving the entirely [new class of problems that emerge when AI tools work as advertised](https://www.thestar.com.my/tech/tech-news/2026/04/07/the-big-bang-ai-has-created-a-code-overload). While some of those are predictable and will have generalizable solutions, [we're remarkably behind in preparing for them](/ai-missing-pieces.html).

Lots of stuff has been improving very fast, but it will a long time before we have generalized best practices for AI coding tools.

## In Usage

Before 2 years ago, AI coding tools were mostly improving autocomplete, where a skilled practitioner could focus on defining types and interfaces and the tooling was very good at generating all the boilerplate. It was an interesting shift, and made several live coding demos much more successful than they might have otherwise been. But while impressive, it wasn't great for much beyond boilerplate, which there are lots of other ways to avoid, and still required the coder to be familiar with all the code.

As the code generation improved, vibe coding emerged, where LLMs were prompted to generate specific functions or files, that the coder would copy somewhere and run, often pasting the results back to the LLM for refinement. This dramatically lowered the cost of developing prototypes, especially in areas where you didn't have a lot of domain knowledge.

(Skipping over lots of neat but smaller innovations)

Then came Claude Code and "agentic engineering", where we essentially moved the LLM inside our codebase, and automated the feedback loop so it could make and test changes independently. Now, we directed the LLM to modify our codebase, but rarely concerned ourselves with the details of those modifications. Robust validation pipelines and documentation became increasingly valuable.

Now, we have teams of agents, operating in a mesh of sorts to tranform specifications into functionality. Some of these are incredibly tightly verified, where every line of code must be traced to an automatically validated spec. Others focus entirely on user experience metrics, ignoring the code as long as users are getting what they need.

## In Tech

While the changes to usage were definitely driven by model updates, that's not the whole story as far the tech goes.

Beyond simply getting better in general terms, LLMs are expanding and being optimized to be applicable in new ways.

There are a lot of very capable models being made outside of the big ones. Chinese companies are putting out models that can get close to the best OpenAI and Anthropic have to offer, at 1/4 the cost, better open source support, and with fewer usage restrictions.

On-device models have also been leaping ahead. With the release of Gemma 4 last week, it's generally feasible to run your own models that are competitive with what Claude and Codex could do 6 months ago. Running your own also provides a lot more options for long term stability, which has been lacking in general, limiting adoption in more conservative cases.

These changes themselves are driven by super-neat innovations like ["streaming mixture-of-experts"](https://simonwillison.net/2026/Mar/18/llm-in-a-flash/), which I barely understand, but are happening out in the open, and I could experiment with if I wanted. But I don't need to in order to get the benefits, and 99.9999% of people who do experience some benefit will have never even heard of it.

# So What?

There's been lots of change, in the tech and ways we adopt it, and there will probably be more. Each change has been adopted by various teams to deliver software more successfully. But adoption takes work, and there's limited evidence that this work is producing generally-applicable improvements.

Great autocompleting skills didn't transfer to great prompting skills for vibe coding, and great prompting skills didn't transfer to great agent context management skills.

The only approaches that have been generally helpful at all levels of LLM adoption have been those based on engineering best practices, like typing, testing, and documentation.

Advances to models and related tech, while based on incredibly cool techniques and opening up new usage models, are trending towards simpler and more open, building on each other to greater heights.

So if you're just getting started with LLM-assisted coding, great! If your projects don't have a need for it now, also great! They probably will eventually, but what that looks like shouldn't be driven by a desire to keep up.
