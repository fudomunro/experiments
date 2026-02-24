Title: The Automator's Manifesto, Part Two
Date: 2021-02-23 18:21
Author: Alec Munro
Slug: the-automators-manifesto-part-two

This was written quite a while ago, but I never got around to publishing it. So here you go!  
  
Proactive Transparency  

  

One of the most important things any automator can do is provide confidence to stakeholders in the project. Confidence can only develop if stakeholders understand the project, and see meaningful improvement. As such, it behooves the automator to make it easy to understand the state of the project. This is particularly relevant when it comes to actual test results, as even successful results that have no audience are essentially useless.  

  

The term I came up with for this aspect of an automators role is "proactive transparency", based on the idea that it's not enough to simply run tests and call it a day. It's a good start, but publishing the results of those tests in a way so as to maximize their audience is where real value starts to develop.

  

  

Entropy Factors  

  

The most challenging automation task of my career came at Research in Motion, where I put together a device lab to test over the air OS software updates (RIM was actually the first to have this available, as I understand). This was a hugely complex endeavour, covering a range of devices with different capabilities, moving between OS versions that could vary greatly. But even more significant to our testing were the externalities we were dependent on.  

  

For instance, knowing what builds were available for updating required manual scraping of a development version of an application maintained by a different team, with no formal connection. This application, in turn, was loosely connected to the servers which devices would contact to identify what updates might apply to them. We frequently encountered issues where a test was queued, but when the device navigated to the update screen, the desired build wasn't found.  

  

These, and many others, came to be known as our "entropy factors". I'm probably misusing entropy, but here the phrase means things outside of your control that could impact the results of your tests. Understanding what these are for a given automation project is one of the most important planning exercises you can do.  

  

  

Measuring Everything  

  

At my first GTAC, Patrick Copeland said "measure everything" (he probably said "at Google we measure everything", but that wasn't what I wrote down.) This was an inspiring credo for a then new-to-the-field automator, and I spent many years trying to live up to it. But it's wrong, or at least deceptive.  

  

Assuming you have the resources to make it possible, measuring everything is still going to require implementation time. But what is much more important is that it is going to increase the scale of measuring output, while doing nothing to identify which metrics mean success. It might feel great to have every system metric, API call, user session and what-have-you carefully collected, but it does nothing on it's own to make your project better. That's an oversimplification, as having this all can increase stakeholder confidence initially, but after a couple of scares, that will fade.

  

You need to commit to measurements that correspond to your desired outcomes for the automation project. That doesn't mean you shouldn't collect a ton of other metrics if your tooling can do it for free, but you shouldn't surface them by default. Keep clear what you are measuring and why, and add cases to that as you grow.  

  

