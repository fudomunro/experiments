Title: Aegis: it's your (agents) data
Date: 2026-10-11 00:10
Category: Writing
Slug: its-yer-agents-data
Lang: en

A good dozen years ago, as one of my last pieces of public writing before shutting up, I wrote about the growing asymetry between how service providers were collecting data, and the proper ownership of that data.
I called it ["It's yer data" and you can read a copy archived here](/its-yer-data.html).

# If you're not paying for it, someone's paying for you

The internet evolved around "free" services, with an idea that attracting enough people to your service would result in money somehow. Advertising, mostly, but it was generally pretty fuzzy, and the core was selling your users. While users had some understanding that this was happening, Silicon Valley's allergy to regulation made sure it stayed ambiguous exactly what the companies were "allowed" to do.

![Photo]({attach}ryan.jpeg)

*"The first lesson of Silicon Valley, actually, is that you only think about the user, the experience. You actually don't think about the money. Ever."*

Beyond the murkiness of the service transaction itself, this also made it hard to move your data between services, because "your data" wasn't clearly defined anywhere, and different services offered unique import/export options. This was a decent moat for vendors, but bad for competition and overall user experience.

# The Opportunity

Middle of last year, Tailscale asked me if I had any ideas for what they could do better. I had been doing some agentic development, and I mentioned it would be nice to constrain agent connectivity. A couple months later, they announced Aperture, which provides some of that functionality, among others, and I started using it. I didn't do all that much, but I appreciated how Aperture appeared as a service in *my* network, with very little setup. I thought that could be an interesting approach to data governance as well.

Which led me to create [Aegis](https://github.com/fudomunro/aegis)

![Photo]({attach}aegis.svg)

Aegis has two very simple pieces. The first is a library API, providing standard methods for working with your data. The second is a prompt interceptor that watches for agents looking for your data, and injects guidance about using the library API. By default, anyone inside your Tailnet is granted full access to the data library, but you're free to adjust that how you like.

Aegis is built to help you take back control of your data and manage it going forward, while enabling secure agentic access to that data. The usage model for Aegis is to start working with your data in agents, and Aegis will learn about it and guide you to establish and maintain canonical stores.

# Why now?

The biggest piece of work required for success is a robust data syncing system, so users aren't second guessing where their data is, because they will stop using it if that happens. We need to support a lot of different service providers, which will have varying methods for synching data, which may be more or less stable over time, and possibly even hostile to us. Maintaining those integrations will be significant ongoing work.

I can't say I've done much in the way of concrete estimations, but in the past I estimated 10-20 people would be necessary to maintain this at a sufficient level of reliability to be appealing to the average user. LLM-based development is incredibly well suited to this type of maintenance, to the point that I think a single person part-time with $1000 of tokens could cover a year.

# Next steps?

I've got [some relatively ambitious issues](https://github.com/fudomunro/aegis/issues) created already, so I expect I'll have a couple of notable releases in the near future. Besides that, for this to move forward:

1. I need to get more familiar with the code. I used an agent to write Aegis, with only very light review by myself. I've still put in a couple dozen hours of testing and decision making, but at least for the core of Aegis, I think it's important I understand it better before I ask more folk to use it.
2. Set up the sync maintenance project.
3. Write a more general post about "bring your own data" as a concept
