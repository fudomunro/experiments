Title: Mocking snakes
Date: 2011-09-13 13:06
Author: Alec Munro
Tags: flexmock, fudge, mock, mocker, mocking, python, tdd, testing
Slug: mocking-snakes

Many years ago, I was tasked with improving the performance of a suite of unit tests. They were taking ever longer to run, and were beyond 20 minutes when I started working with them. Needless to say, this meant people rarely ran them.  

[From Miško Hevery](http://misko.hevery.com/2009/05/07/configure-your-ide-to-run-your-tests-automatically/):  

> 
>
> What I want is for my IDE to run my tests every time I save the code. To do this my tests need to be fast, because my patience after hitting Cntl-S is about two seconds. Anything longer than that and I will get annoyed. If you start running your tests after every save from test zero you will automatically make sure that your test will never become slow, since as soon as your tests start to run slow you will be forced to refactor your tests to make them faster.

The problem was that every test was descended from a common base class, and that class brought up fake versions of most of the application. Well, mostly fake versions. There was still a lot of I/O and network activity involved in bringing up these fakes.

  

The solution turned out to be mock objects, JMock in this particular case. For those unfamiliar, mock objects are objects that can stand in for your dependencies, and can be programmed to respond in the particular manner necessary for whatever it is you are testing. So if your network client is supposed to return "oops" every time the network connection times out, you can use a mock to stand in for the network connection, rather than relying on lady fortune to drop the network for you (or doing something terrible, like having code in your test that disables your network interface).

  

There are a couple of general drawbacks to using mock objects, but the primary one is that a mock object only knows what you tell it. If the interface of your dependencies change, your mock object will not know this, and your tests will continue to pass. This is why it is key to have higher level tests, run less frequently, that exercise the actual interfaces between objects, not just the interfaces you have trained your mocks to have.

  

The other drawbacks have more to do with verbosity and code structure than anything else. In order for a mock to be useful, you need a way to tell your code under test what dependency it is standing in for. In my code, this tends to lead to far more verbose constructors, that detail every dependency of the object. But there are other mechanisms, which I will explore here.

  

For a more verbose comparison of mock libraries in a variety of use cases, check this out:

  

<http://garybernhardt.github.com/python-mock-comparison/>

  

Hopefully this post will be a more opinionated supplement to that.

  

There are a couple of categories of things to mock:

<ul>

<li>

Unreliable dependencies (network, file system)
</li>

<li>

Inconsistent dependencies (time-dependent functionality)
</li>

<li>

Performance-impacting dependencies (pickling, hashing functions, perhaps)
</li>

<li>

Calls to the object under test
</li>

</ul>

The last item is certainly not a necessity to mock, but it does come in handy when testing an object with a bunch of methods that call each other. I'll refer to it as *"partial mocking"* here.

  

For this article, I'm going to focus on 4 mock object libraries, [Mocker](http://labix.org/mocker), [Flexmock](http://has207.github.com/flexmock/index.html), and [Fudge](http://farmdev.com/projects/fudge/), chosen primarily because they are the ones I have experience with. I also added in [Mock](http://www.voidspace.org.uk/python/mock/), but I don't have much experience with it yet. I believe, from my more limited experience with other libraries, that these provide a decent representation of different approaches to mocking challenges.

  

I'm going to go through common use cases, how each library handles them, and my comments on that. One important note is that I generally don't (and won't here) differentiate between mocks, stubs, spies, etc.

<h3>

Getting a mock

</h3>

[Gist: "Getting mock objects from different libraries"](https://gist.github.com/1149878)

  

  

  

  

Dependencies are usually injected in the constructor, in a form like the following:  

[Gist "Verbose dependency specification for mocking"](https://gist.github.com/1149767)

  

  

  

  

This is verbose, especially as we build real objects, which tend to have many dependencies, once you start to consider standard library modules as dependencies. :)

  

NOTE: Not all standard library modules need to be mocked out. Things like os.path.join or date formatting operations are entirely self contained, and shouldn't introduce significant performance penalties. As such, I tend not to mock them out. That does introduce the unfortunate situation where I will have a call to a mocked out os.path on one line, and call to the real os.path on the next:  

[Gist: "Confusion when not everything is mocked"](https://gist.github.com/1149773)

  

  

  

  

This can certainly be a bit confusing at times, but I don't yet have a better solution.

  

However, it is quite explicit, and avoids the need for a dependency injection framework. Not that there's anything wrong with using such a framework, but doing so steepens the learning curve for your code.

  

<h3>

Verifying Expectations

</h3>

  

One key aspect of using mock objects is ensuring that they are called in the ways you expect. Understanding how to use this functionality can make test driven development very straightforward, because by understanding how your object will need to work with it's dependencies, you can be sure that the interface you are implementing on those dependencies reflects the reality of how it will be used. For this and more, read [*Mock Roles Not Objects\>, by Steve Freeman and Nat Pryce*](http://www.mockobjects.com/files/mockrolesnotobjects.pdf).

  

...anyway, verification takes different forms across libraries.  

[Gist: "Verifying mock expectations"](https://gist.github.com/1150664)

  

  

  

<h3>

Partial Mocks

</h3>

Partial mocking is a pretty useful way to ensure your methods are tested independently from each other, and while it is supported by all of the libraries tested here, some make it much easier to work with than others.  

[Gist "Partial mocks"](https://gist.github.com/1198698)

  

<h3>

</h3>

<h3>

Chaining Attributes and Methods

</h3>

I'm of the opinion that chained attributes are generally indicative of poor separation of concerns, so I don't place too much weight on how the different libraries handle them. That said, I've certainly had need of this functionality when dealing with a settings tree, where it can be much easier to just create a mock if you need to access settings.a.b.c.

Chained methods are sometimes useful (especially if you use SQLAlchemy), as long as they don't impair readability.  

[Gist "Chaining methods and attributes"](https://gist.github.com/1203804)

  

  

  

<h3>

Failures

</h3>

An important part of any testing tool is how informative it is when things break down. I'm talking about detail of error messages, tracability, etc. There's a couple of errors I can think of that are pretty common. For brevity, I'm only going to show the actual error message, not the entire traceback.  

  

**Note**: Mock is a bit of an odd duck in these cases, because it lets you do literally anything with a mock. It does have assertions you can use afterwards for most cases, but if an unexpected call is made on your mock, you will not receive any errors. There's probably a way around this.  

  

Arguments don't match expectations, such as when we call time.sleep(4) when our expectation was set up for 6 seconds:  

> 
>
> **Mocker**: MatchError: \[Mocker\] Unexpected expression: m_time.sleep(4)  
>
> **Flexmock**: InvalidMethodSignature: sleep(4)  
>
> **Fudge**: AssertionError: fake:time.sleep(6) was called unexpectedly with args (4)  
>
> **Mock**: AssertionError: Expected call: sleep(6)  
>
> Actual call: sleep(4)

When I first encountered Flexmock's InvalidMethodSignature, it threw me off. I think it could certainly be expanded upon. Otherwise, Mock and Fudge have very nice messages, and as long as you know what was supposed to happen, Mockers is perfectly sufficient.  

  

Unexpected method called, such as when you misspell "sleep":  

> 
>
> **Mocker**: MatchError: \[Mocker\] Unexpected expression: m_time.sloop  
>
> **Flexmock**: AttributeError: 'Mock' object has no attribute 'sloop'  
>
> **Fudge** (patched time.sleep): AttributeError: 'module' object has no attribute 'sloop'  
>
> **Fudge**: AttributeError: fake:unnamed object does not allow call or attribute 'sloop' (maybe you want Fake.is_a_stub() ?)  
>
> **Mock**: AssertionError: Expected call: sleep(6)  
>
> Not called

Mock doesn't tell you that an unexpected method was called. Mocker has what I consider the best implementation here, because it names the mock the call was made on. The second Fudge variant is good, but because you might encounter it or the first variant depending on context, Fudge overall is my least favourite for this. Flexmock simply defers handling this to Python.  

  

Expected method not called:  

> 
>
> **Mocker**: AssertionError: \[Mocker\] Unmet expectations:  
>
> =\> m_time.sleep(6)  
>
>  - Performed fewer times than expected.  
>
> **Flexmock**: MethodNotCalled: sleep(6) expected to be called 1 times, called 0 times  
>
> **Fudge**: AssertionError: fake:time.sleep(6) was not called  
>
> **Mock**: AssertionError: Expected call: sleep(6)  
>
> Not called

I think they all do pretty well for this case, which is good, because it's probably the most fundamental.

<h3>

Roundup

</h3>

So, having spent a bit of time with all of these libraries, how do I feel about them? Let's bullet point it!

<h4>

Mocker

</h4>

<ul>

<li>

Pros
</li>

<ul>

<li>

Very explicit syntax
</li>

<li>

Verbose error messages
</li>

<li>

Very flexible
</li>

</ul>

<li>

Cons
</li>

<ul>

<li>

Doesn't support Python 3 and not under active development
</li>

<li>

Performance sometimes isn't very good, especially with patch()
</li>

<li>

Quite verbose
</li>

</ul>

</ul>

<h4>

Flexmock

</h4>

<ul>

<li>

Pros
</li>

<ul>

<li>

Clean, readable syntax for most operations
</li>

</ul>

<li>

Cons
</li>

<ul>

<li>

Syntax for chained methods can be very complex
</li>

<li>

Error messages could be improved
</li>

</ul>

</ul>

<h4>

Fudge

</h4>

<ul>

<li>

Pros
</li>

<ul>

<li>

Using @patch is really nice, syntactically
</li>

<li>

Examples showing web app testing is nice touch
</li>

</ul>

<li>

Cons
</li>

<ul>

<li>

@patch can interfere with test runner operations (because it affects the entire interpreter?)
</li>

<li>

Partial mocking is difficult
</li>

</ul>

</ul>

<h4>

Mock (preliminary)

</h4>

<ul>

<li>

Pros
</li>

<ul>

<li>

Very flexible
</li>

</ul>

<li>

Cons
</li>

<ul>

<li>

Almost too flexible. All-accepting mocks make it easy to think you have better coverage then you do (so use [coverage.py](http://nedbatchelder.com/code/coverage/)!)
</li>

</ul>

</ul>

<h3>

Acknowledgements

</h3>

Clearly, a lot of work has been put into these mock libraries and others. So I would like extend some thanks:  

<ul>

<li>

Gustavo Niemeyer, for his work on Mocker.
</li>

<li>

Kumar MacMillan, for his work on Fudge, and for helping me in preparing material for this post.
</li>

<li>

Herman Sheremetyev, for his work on Flexmock
</li>

<li>

Michael Foord, for his work on Mock, and for getting me on Planet Python
</li>

</ul>

Additionally, while I didn't work with them for this post, there are a number of other mock libraries worth looking at:

<ul>

<li>

[Dingus](http://pypi.python.org/pypi/dingus)
</li>

<li>

[Mox](http://pypi.python.org/pypi/mox)
</li>

<li>

[MiniMock](http://pypi.python.org/pypi/MiniMock), which I've used quite a bit in the past, and I'm delighted to learn that development is continuing on it!
</li>

</ul>

