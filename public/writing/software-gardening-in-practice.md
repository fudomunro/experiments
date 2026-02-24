Title: Software Gardening in practice
Date: 2015-10-17 10:29
Author: Alec Munro
Tags: best.practices, community, development, process, project.management, python, quality, zope
Slug: software-gardening-in-practice

Software gardening, as expressed by <a href="http://www.artima.com/intv/gardenP.html" target="_blank">Hunt/Thomas</a>, <a href="http://www.codinghorror.com/blog/2008/11/tending-your-software-garden.html" target="_blank">Atwood</a>, <a href="http://www.chrisaitchison.com/2011/05/03/you-are-not-a-software-engineer/" target="_blank">etc</a> uses the metaphor to deal with how a software project is alive, and is constantly being changed by factors outside of the control of the developers. You can plant a seed, and water it, but you can’t control the sunlight, the bugs, bees, etc. As it grows, you can weed the garden, removing features that are not used but taking up resources, add fertilizer, change the plants to better reflect your needs (why didn’t someone tell me Joe was allergic to cucumbers!?).  

  

I want to expand on this idea, as I believe there are several valuable insights that can be derived from adopting this view. In this post I will explore this concept from three different perspectives: the project itself, a software developer, and a client that wants to get some software developed.  

  

<h3>

The Unseen Environment

</h3>

As a particular software environment is like a garden, there are many factors that the garden grows out of. There are obvious factors, like the composition of the soil, and the likely availability of water, and sunlight. But there are also more subtle, “living” factors, that are going to be part of the environment of your garden, yet generally operate independently.  

  

One of the most fascinating things I’ve learned recently is the concept of <a href="http://en.wikipedia.org/wiki/Mycorrhizal_networks" target="_blank">mycorrhizal networks</a>. These are fungal layers that exist within the soil that serve to break down waste matter and distribute molecules that plants depend on for nutrition. It is generally unseen, but is a huge factor in the ability of plant ecosystems to thrive. Generally much better known, but still somewhat unseen, are the pollinators. Birds, bees, and butterflies allow plants to reproduce, and thus stimulate genetic diversity.  

  

So, above and below, there is an environment that allows plant life to thrive. A similar role is played in software development by the ecosystem that exists **around** both the software, and the developers.  

All developers and software libraries come to a project with a history that is shaped through the absorption of “byproducts” from previous projects. These can take the form of learned code snippets, software structure conventions, and many other things. I would liken this to the way the mycorrhizal network digests the output from various past biological processes and produces raw nutrients to begin new ones.  

  

In a similar way, open/shared source cultures could be compared to pollinators. Moving from project to project with very few barriers, a developer can distribute efficient techniques rapidly, effecting the projects and other developers. This has resulted in the establishment of numerous best practices, to the point where high-profile open source projects are the gold standards for software quality. Another interesting way in which open source diversity is like genetic diversity is in the trend of multiple competing software projects springing up with different attributes tailored to their environments. These can continue for very long periods, sharing “genes” with each other but still continuing as distinct “species”.  

  

In some large organizations, the software ecosystem is distinct enough to effect the software that is produced there, but at this point, almost everyone is dependent on Open Source. It produces specific codebases that underly most every modern project, such as Linux, Apache, OpenSSL, GCC, Boost, Python, etc. But it also establishes the best practices and standards for software development that are used by individual developers, whatever they are working on. Conversely, bug reports come from commercial projects that make Open Source stronger, and developer experiences there continue to inform and refine the state of the art. There are also cases where it is beneficial for commercial development to open source certain pieces of their software, to expose them to that wider diversity, and encourage contributions that will help meet business goals (though like natural evolution, predicting the future of an open source project is far from a science).  

  

Tying that back together, that means that for a developer, every project you work on contributes to this larger community, even when the code itself is closed. Because it changes you, and it changes the conversations you have with others, and how you work to solve problems in the future. As a former user of the Zope Web Application Server, I have watched other users and contributors define the cutting edge of web software (<a href="https://github.com/tarekziade" target="_blank">Tarek Ziade</a>, <a href="https://github.com/mcdonc" target="_blank">Chris McDonough</a>, <a href="https://github.com/alex" target="_blank">Alex Gaynor</a>, and <a href="https://github.com/faassen" target="_blank">Martijn Faasen</a>, among <a href="http://www.python.org/~guido/" target="_blank">others</a>).  

  

<h3>

Garden Development as a Service

</h3>

As someone who works on software, your value is not the creation and delivery of a product, but rather the cultivation of an environment. Even when you are employed delivering products, there’s no such thing as a final release, just something that is able to meet the needs of the moment. Needs will change, the ecosystem will change, you will change, and new opportunities will arise. How might this change how you approach a single project, and your career?  

  

In terms of approaching a particular project, it means you need to understand the landscape in order to effectively execute on the vision. You need to know what kind of software is already there, and what the state of third party libraries are in that particular domain. You need to plan for the inevitable bugs and maintenance. The actual implementation flows out of these concerns, not the other way around.  

  

From a career standpoint, I should first confess that, well, I’m not a gardener. However the image I have of them is that they don’t get annoyed that all the cool gardens are already cultivated. As long as you have a willingness to work, gardens are going to need cultivation. Likewise, as long as you have a willingness to develop it, there will always be available work developing software. Under this philosophy, nothing ever reaches the point that it cannot be improved or does not require maintenance.  

  

<h3>

Gardening Agency

</h3>

When we have a need for some software, and we attempt to consider the effort that will be required, we usually think about the features that we want the software to have. The gardening metaphor suggests this is a very limited way to view this. If we think of the features of a particular garden as “has Roses and Violets, and produces Tomatoes”, we can quickly understand that a good deal more information is required to get a reasonable estimate of the effort that will be necessary.  

  

Is the garden in Hawaii, Alaska, or the Central Park Zoo? What if there’s already a garden there? What's the condition of the soil, or local animal life?  

  

Translating these questions over to software, we can see that the environment a piece of software needs to "live" in can impact the effort required to develop it as much or more than the features it needs to have. For instance, if you are looking to add accounting features for exporting financial data to your partners, the effort could vary tremendously depending on the existence and maturity of the open source software that exists to work with data in the formats they use.  

  

Just as working with a professional landscaper will produce dramatically different results than simply purchasing plants, establishing a relationship with someone who can look at your situation holistically is key to a successful software project. They know the questions that need to be asked, the process for finding the answers, and they know how to build out a development team that will take that reality into account.
