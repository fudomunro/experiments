Title: Python Web Client 0.1.dev1
Date: 2011-09-27 03:24
Author: Alec Munro
Tags: best.practices, experiments, mock, mocking, project.management, python, selenium, testing, web
Slug: python-web-client-01dev1

**tl;dr**  

I built a preliminary version of the [Socal Piggies](https://bitbucket.org/socal.piggies/pwc/wiki/Home) Python Web Client. Take a look at the code and methodology, suggest features/fixes, and otherwise enjoy! There's no live demo because of a gaping security hole.  

  

**Intro**  

First off, I would just like to express my sincere appreciation for everyone who responded to my [request for ideas](http://alecmunro.blogspot.com/2011/09/let-me-build-you-web-appservice.html). There were a number of interesting options, but for now, I've decided to build an implementation of the Python Web Client described on the [Socal Piggies](https://bitbucket.org/socal.piggies/pwc/wiki/Home) site. I made this choice because it's a comfortable area for me to work in, it's a tool I can see using, and probably most important, I think I can build a simple version fairly quickly. :)  

  

**Design**  

The first thing I usually do with a new project is retreat to a quiet corner with a notebook and a writing implement. It would be nice to find an electronic way to do this, but so far nothing has come close to what I need in terms of offering a combination or structured and free-form input, along with instant availability.  

  

In this case, I was trying to strip the concept down to the bare essentials. In this case that means:  

<ul>

<li>

One page, with two widgets:

</li>

<ul>

<li>

Create request (Enter a URL)

</li>

<li>

Display response (Status Code + Headers)

</li>

</ul>

<li>

Startup script that launches a browser to the service

</li>

</ul>

That last one may seem non-essential, but speaks to my philosophy that "delivery is as important as development". In practice, that means that how a client is introduced to functionality is just as important as how well that functionality works. Make it really easy to start using.  

  

Because this is somewhat of a showcase project, there's a couple of other things I pinned on my design list:  

<ul>

<li>

Testing (unit, functional, system, jsunit)

</li>

<li>

Docs (UI + API, published in Sphinx)

</li>

</ul>

While I was putting this together, I also wrote down a whole lot of nice-to-have features for later. You can check them out on the [Rally site](https://community.rallydev.com/slm/rally.sp?) I am (kind of) using to manage this project. You will need to log in:  

alecmunro+public@gmail.com:Experiments  

  

**Testing**  

Because I'm a TDD advocate, let's do that. So first I need to decide what tests I want to have. Since I don't know my code structure at all yet, I'm going to start with system level tests, which I usually define as something that tests the system at the UI level, running very close to how it will run in production:  

<ul>

<li>

Visit site, enter URL, press submit, verify results.

</li>

</ul>

[Gist-It for test_ui.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/tests/test_ui.py)  

  

That pretty much does it, and can be done with something like [Selenium](http://seleniumhq.org/), unless I also wanted to test the startup script. Doing so would involve using something like [Sikuli](http://sikuli.org/)(which I do love), to observe the state of the desktop, but that might balloon the scope of this project a bit too much. So we are on to functional testing, in this case defined as testing the API of the web service, in as isolated an environment as we can create. So what are we looking at there?

<ul>

<li>

Submit URL, verify response
</li>

<ul>

<li>

Probably some variants of this, to test error handling or redirect responses (we are handling those, right?).
</li>

<li>

What happens if the URL to retrieve is the URL of the webservice itself? Could we experience some nastiness there?
</li>

</ul>

</ul>

So both of the test types we have addressed so far require an actual connection to another server. We could use something that's always going to be available, like www.google.com, but we aren't really guaranteed a network connection. So for this, I'll write a small web server that can be set to return whatever you want it to.  

[Gist-It for echo_server.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/tests/echo_server.py)  

  

This was actually a bit trickier than I anticipated, due to the need to run the server in a separate thread/process, and [this bug](http://bugs.python.org/issue11969). Anyway, here's the API tests:

[Gist-It for test_apis.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/tests/test_apis.py)  

  

  

Ok, so unit tests now. From our earlier tests, it's become pretty clear that the API will have one view, which accepts the details to construct a request (just a URL to start), submits that request, and returns the status code and headers from the response.  

Well, that was all really boring. Maybe the jsunit tests will be more interesting? In practice, I probably won't write these before the code, because it still takes me a while to get into the rhythm of writing tests for javascript. I need a bit of trial-and-error.

<ul>

<li>

Create Request Widget:
</li>

<ul>

<li>

Enter text and press submit. A call should be made to create the request, and the deferred for that call should be passed to the page.
</li>

</ul>

</ul>

[Gist-It for test_create_request.js](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/static/script/tests/test_create_request.js)  

  

<ul>

<li>

Display Response Widget:
</li>

<ul>

<li>

Supply it with various responses, and confirm that they display properly. Probably the most interesting bit of testing of the whole lot.
</li>

</ul>

</ul>

[Gist-It for test_display_response.js](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/static/script/tests/test_display_response.js)  

  

**Implementation**

Ok, so we have our tests, perhaps. Now, on to the implementation. This part is actually really simple.  

  

There's the Python view:  

[Gist-It for views.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/views.py)  

  

and the two Javascript widgets:  

[Gist-It for create_request.js](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/static/script/create_request.js)  

  

[Gist-It for display_response.js](https://github.com/alecmunro/Experiments-in-Public/blob/master/python_web_client/pwc/static/script/display_response.js)  

  

  

Feel free to [take a look at the GitHub repository](https://github.com/alecmunro/Experiments-in-Public/tree/master/python_web_client/pwc) for more details (or check it out to run it). 

  

**Documentation**  

I've left off the documentation for now, both because I wanted to get this up soon, and it's been a while since I started anything with Sphinx, and also because it really doesn't do much yet. I'm also still missing the launch script.  

  

**Conclusion**  

There's lots more work to be done here to make something useful, so I'm taking suggestions. But hopefully this gives you an idea of how you can build a simple and somewhat tested web-app using Pyramid and JQuery. You will notice that it is very testing heavy, probably significantly more than real-world deadlines would allow for. But once you get these tests in place (and a system to run them), they are fairly easy to build on, and can provide a safe container in which to experiment.  

For the moment, I'm planning two distinct iterations:  

  

<ul>

<li>

Add docs and launch script, as well as displaying the response body. That will be 0.1

</li>

<li>

Flesh out the request creation ability, to allow settings headers and parameters. Along with hopefully some fixes/refinements, that will be 0.2

</li>

</ul>

Beyond that, development will depend on whether this is interesting to anyone, so let me know.

