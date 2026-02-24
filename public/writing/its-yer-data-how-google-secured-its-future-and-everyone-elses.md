Title: It's yer data! - how Google secured its future, and everyone else's
Date: 2014-08-29 23:31
Author: Alec Munro
Tags: data, development, do.no.evil, future, google, process, python, vision, web
Slug: its-yer-data-how-google-secured-its-future-and-everyone-elses

Dear Google,  

  

This is a love letter and a call to action.  

  

I believe we stand at a place where there is a unique opportunity in managing personal data.  

  

There is a limited range of data types in the universe, and practically speaking, the vast majority of software works with a particularly tiny fraction of them.  

  

People, for example. We know things about them.  

  

Names, pictures of, people known, statements made, etc.  

  

Tons of web applications conceive of these objects. Maybe not all, but probably most have some crossover. For many of the most trafficked apps, this personal data represents a very central currency. But unfortunately, up until now we've more or less been content with each app having it's own currency, that is not recognized elsewhere.  

  

You can change that. You can establish a central, independent bank of data, owned by users and lent to applications in exchange for functionality. The format of the data itself will be defined and evolved by an independent agency of some sort.  

  

There are two core things this will accomplish.  

  

1\) It will open up a whole new world of application development free from ties to you, Facebook, Twitter, etc.  

  

2\) It will give people back ownership of their data. They will be able to establish and evolve an online identity that carries forward as they change what applications they use.  

  

Both of these have a dramatic impact on Google, as they allow you to do what you do best, building applications that work with large datasets, while at the same time freeing from you concerns that you are monopolizing people's data.  

  

### A new application world

When developing a new application, you start with an idea, and then you spend a lot of time defining a data model and the logic required to implement that idea on that data model. If you have any success with your application, you will need to invest further in your data model, fleshing it out, and implementing search, caching, and other optimizations.  

  

In this new world, all you would do is include a library and point it at an existing data model. For the small fraction of data that was unique to your application, you could extend the existing model. For example:  

    from new_world import Model, FieldBaseUser = Model("https://new_world.org/users/1.0")class OurUser(BaseUser):    our_field = Field("our_field", type=String)

  

That's it. No persistence (though you could set args somewhere to define how to synchronize), no search, no caching. Now you can get to actually building what makes your application great.  

  

Conceivably, you can do it all in Javascript, other than identifying the application uniquely to the data store.  

  

And you can be guaranteed data interoperability with Facebook, Google, etc. So if you make a photo editing app, you can edit photos uploaded with any of those, and they can display the photos that are edited.  

  

### Securing our future

People have good reason to be suspicious of Google, Facebook, or any other organization that is able to derive value through the "ownership" of their data. Regardless of the intent of the organization today, history has shown that profit is a very powerful motivator for bad behaviour, and these caches of personal data represent a store of potential profit that we all expect will at some point prove too tempting to avoid abusing.  

  

Providing explicit ownership and license of said data via a third-party won't take away the temptation to abuse the data, but will make it more difficult in a number of ways:  

  

<ul>

<li>

Clear ownership will make unfair use claims much more cut-and-dried

</li>

<li>

A common data format will make it much easier to abandon rogue applications

</li>

<li>

Reduced application development overhead will increase the competitive pressure, lowering the chance of a single application monopolizing a market and needing to grow through exploitation of its users data

</li>

</ul>

### A gooder, more-productive, Google

By putting people's data back in their hands, and merely borrowing it from them for specific applications, the opportunities for evil are dramatically reduced.  

  

But what I think is even more compelling for Google here is that it will make you more productive. Internally, I believe you already operate similar to how I've described here, but you constantly bump up against limitations imposed by trying not to be evil. Without having to worry about the perceptions of how you are using people's data, what could you accomplish?  

  

### Conclusion

Google wants to do no evil. Facebook is perhaps less explicit, but from what I know of its culture, I believe it aspires to be competent enough that there's no need to exploit users data. The future will bring new leadership and changes in culture to both companies, but if they act soon, they can secure their moral aspirations and provide a great gift to the world.  

  

(Interesting aside, Amazon's recently announced Cognito appears to be in some ways a relative of this idea, at least as a developer looking to build things. [Check it out](http://aws.amazon.com/cognito/).)
