Title: Design patterns
Date: 2011-09-13 18:17
Author: Alec Munro
Tags: adapter, best.practices, communication, design.patterns, learning, mediator, python, strategy, template.method
Slug: design-patterns

Design patterns are a very broad subject, but as far as I can tell, they are primarily common conventions for structuring software. I've never been taught them, and as far as I can tell, I've used nearly all of them, repeatedly. So for an experienced software developer, I don't believe studying design patterns is likely to improve your coding skills much, if at all. However, it could certainly improve your collaboration skills.  

  

**Words Matter**  

If there's one downside to being self-taught in the field of computer programming (there are several), it would be the difficulty of communicating your ideas with those who have a "standard" education. However good my code may be doesn't matter if I spend all my time trying to explain how I'm going to implement something. Formal computer science comes with a whole boatload of terminology, design patterns among them. Being able to say "use the template method pattern to defer processing to subclasses" is much more concise than "in the superclass method, call methods that are overridden in the subclass, but have only stub implementations in the superclass". Even that verbose description is concise compared to what usually comes up with discussing actual project code.  

  

**Template Method**  

The template method pattern is something that eventually comes in handy to anyone who does a fair amount of object oriented design. It's a response to the problem of how to mix specialized behaviour of subclasses with general behaviour of superclasses. The basic idea is that the superclass implementation of a method will contain mostly calls to other methods of the object, which will be mostly abstract in the superclass, and implemented in the subclasses, which won't implement the method being called.  

I recently used this on an email reporting system, which used either HTML or text email depending on the job being reported on. There was a fair amount of commonality between both types, in that they dealt with collecting data from the environment and stuffing it into some kind of template (the use of the word template here is unrelated), then formatting that template into an email and sending it along.  

The actual email sending was almost the same for both HTML and text, so with just a condition or two we could handle that entirely in the superclass. However, the data that was sent out varied a bit between the two types, as did the emails themselves.  

  

[Gist: "Template Method example"](https://gist.github.com/1214125)

  

Note that the implementation above is not ideal, because the subclasses do need a certain awareness of the superclass implementation in order to behave properly.  

  

**Mediator**

The mediator pattern, in my understanding, mostly deals with managing the flow of communication between objects. It puts a layer between your object and it's intended communication target. I use this pattern frequently for building UIs, most of which I build in JQuery, so that's where I use it.

The way I build UIs in JQuery has been a constantly evolving pattern, so this may change, but right now it gives me the flexibility I need. What I usually do is create an object representing the page itself, as well as objects to represent each of the distinct interface areas, which I am going to call widgets (thought that might be too specific of a term in this context). Each of the widgets takes zero or more callback functions, depending on what they do, and the page object is responsible for seeing that these point to the same things. In some cases, they are methods of other widgets (though in typical javascript fashion, they are anonymous functions that call those methods), but more often they are methods of the page object, which accept the communication and see it dispatched to any other widget(s) that are interested. The page object is almost never more than wiring between the widgets.  

  

The following is probably not syntactically correct. It frequently takes a bit of trial and error before I get into the swing of JavaScript OOP.  

  

[Gist: "Mediator Pattern example"](https://gist.github.com/1214446)

  

**Strategy**

The strategy pattern deals with abstracting away algorithms. In situations where a different context might require a different algorithm to achieve the desired results, you apply the strategy pattern. This might sounds complex, but in practice, it is as simple as using different validation functions on different data types, as long as you have a common interface to those functions.  

  

[Gist: "Strategy Pattern example"](https://gist.github.com/1214513)

  

**Adapter**  

The adapter pattern is one that, thanks to Zope 3, I've been familiar with for a long time. An adapter is an object that "wraps" another object to provide a desired interface. Designing a system based on the adapter pattern requires using capital-I Interfaces for establishing object communication. Then, as necessary, adapters are created to allow the available objects to satisfy those interfaces.  

To a certain degree, the adapter pattern takes the concept of polymorphism, traditionally understood as being able to use a superclass' interface to interact with instances of subclasses, and expands it. So you can use the specification of an Interface to interact with any objects that are adaptable to that Interface. To use the traditional Bicycle example, Bicycle might extend Vehicle, and have traditional vehicular methods. However, maybe we want to check what color the bike is, or paint it. Vehicle may not have methods for this, but IPaintable might. Then, with a BicyclePainter adapter, we can adapter our Bicycle instance to this interface. (For the record, I've never found the Bicycle example very useful, and I'm not sure if I'm doing you any favours by using it here).  

  

[Gist: "Adapter Pattern example"](https://gist.github.com/1214536)

  

**Conclusion**

So there's some design patterns, and their usage. It's by no means comprehensive, and I'm sure many of you will have encountered these in other contexts where my definitions aren't entirely accurate. That's just fine, because the value of these is not in having rigid development patterns, it's having useful ways to elevate the discussion of your development. I've almost never encountered clearly recognizable design patterns in code I inherited, because patterns are theory, and when applied, the real world makes things start to get messy.  

  

**References**  

  

<ul>

<li>

[Wikipedia](http://en.wikipedia.org/wiki/Design_pattern_(computer_science)): I relied on this for design patterns and their basic descriptions.
</li>

<li>

["Adapters" chapter from Grok tutorial](http://grok.zope.org/documentation/tutorial/grok-poller-tutorial/adapters)
</li>

</ul>

