Title: Aegis: it's your (agents) data
Date: 2026-10-11 00:10
Category: Writing
Slug: its-yer-agents-data
Lang: en

A good dozen years ago, as one of my last pieces of public writing before shutting up, I wrote about the growing asymetry between how service providers were collecting data, and the proper ownership of that data. (Insert link here)

# If you're not paying for it, someone's paying for you

The internet evolved around "free" services, with an idea that attracting enough people to your service would result in money somehow. Advertising, mostly, but it was generally pretty fuzzy.

(think Ryan from The Office "the first rule of silicon valley is you never think about the money.")

As these free services became massive and entrenched, some of them did find a paying user base, but most relied on selling their users to other companies in some form. While users had some understanding that this was happening, Silicon Valley's allergy to regulation made sure it stayed ambiguous exactly what the companies were "allowed" to do.

# What Data?

Beyond the murkiness of the service transaction itself, this also made it hard to move your data between services, because "your data" wasn't clearly defined anywhere, and different services offered unique import/export options. This was a decent moat for vendors, but bad for competition and overall user experience.

# It's MY data

Before I get to the reason for resurrecting this idea now, another of the earlier benefits I conceived of is a way to fight deepfakes by making it common to trace the source of an image to person. We can have a convention for signing media, and build client side tools for identifying the signature. We can't prove that unsigned media is fake, but we can help distinguish it from media that I'm specifically claiming.

# It's your agents data!

Ok, so while I think this is a good idea anyway, I think it has particular legs right now because of AI and Agents. All the big AI companies want us to delegate stuff to agents, which are generally defined as long-running programs that use LLMs to write and run code to complete tasks you assign to them. On the one hand, this is really cool, because most people have complicated lives that an Agent could help organize. However, most people don't know how to give an agent specific information, and will either opt to avoid it, or will open themselves up to significant risk.

On the other hand, coders like myself know how to expose specific data, and we know what kind of things might be possible. But with few exceptions, experienced software developers have been trained not to give our data to these types of systems without extreme safeguards, which are rarely worth implementing for our own use, since we can still achieve the same results without involving an agent, it just takes more work (but less than the safeguards.) We also generally warn average users about this kind of privacy risk, and would be unlikely to encourage folk to hand over their google keys to OpenAI.

Well, if users BYOD to an Agent, the agent doesn't need credentials, and the user can omit data they don't want the agent to have access to.

# The work.

The biggest piece of work required for success is a robust data syncing system, so BYOD users aren't second guessing where their data is, because they will stop using it if that happens. We need to support a lot of different service providers, which will have varying methods for synching data, which may be more or less stable over time, and possibly even hostile to us. Maintaining those integrations will be significant ongoing work.

I can't say I've done much in the way of concrete estimations, but in the past I estimated 10-20 people would be necessary to maintain this at a sufficient level of reliability to be appealing to the average user. LLM-based development is incredibly well suited to this type of maintenance, to the point that I think a single person part-time with $1000 of tokens could cover a year.

# The oppportunity

Middle of last year, Tailscale asked me if I had any ideas for what they could do better. I had been doing some agentic development, and I mentioned it would be nice to constrain agent connectivity. A couple months later, they announced Aperture, which provides some of that functionality, among others, and I started using it. I didn't do all that much, but I appreciated how Aperture appeared as a service in *my* network, but I didn't really have to do any set up or run anything. After a bit of cogitating, I realized that this set up was nearly ideal for BYOD, and that agentic data access provided a somewhat urgent need for it to exist.

Which led me to create...

# Aegis

Aegis is my first piece of software built to address this problem. I've done some earlier drafts on it, but I wanted to lean into the Tailscale connection, so I started from scratch in Go (well, MiMo-v2.6-pro did.) Aegis is built to help you take back control of your data and manage it going forward, while enabling secure agentic access to that data.

Aegis has two very simple pieces. The first is a data library API, providing standard methods for working with your data. The second is a prompt interceptor that watches for agents attempting to access your data, and injects guidance about using the media library API. By default, anyone inside your Tailnet is granted full access to the data library, but you're free to adjust that how you like.

The usage model for Aegis is to start working with your data in agents, and Aegis will learn about it and guide you to establish and maintain canonical stores.
