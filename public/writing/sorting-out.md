Title: Sorting out
Date: 2011-09-18 17:49
Author: Alec Munro
Tags: experiments, learning, python, sorting
Slug: sorting-out

As someone who almost exclusively uses high-level languages, the idea of writing my own sorting algorithm seems a bit silly. However, I can certainly appreciate the algorithms used for sorting, and it's a neat opportunity to try to document and implement these algorithms using methods I am familiar with.  

  

**Preface**  

  

These implementations are likely to be extremely naive. If you went CS school, you probably learned better implementations in your first year. There is absolutely no reason to use these in production code anywhere. The built-in python sorting is 10-50 times faster than anything I've produced (I'm actually surprised it's not more). If you've got tips about how to speed these up just by changing the code around, feel free to comment, or you can try forking [my repository](https://github.com/alecmunro/Experiments-in-Public/tree/master/sorting) and sending a pull? request. I can't promise to spend much time on it, because this is pretty well-trod territory, but it would be a bit entertaining to see how close we can get.  

  

**Quick Sort**

My understanding of quicksort is still developing, but based on what I've read on Wikipedia, it can work something like this:

<ol>

<li>

Grab an item in the list, called the "pivot".
</li>

<li>

Create two lists, representing everything greater than the pivot, and everything less then the pivot.
</li>

<li>

Repeat steps 1 and 2 on the two sub-lists, returning the a list comprised of the smaller list items, then the pivot, then the larger list items.
</li>

</ol>

In this way, the entire list should get sorted. It's my understanding there are various optimizations that can be done, such as swapping elements instead of creating new lists. It seems to be one of the "best" all around algorithms, though for certain cases, it's performance can be beaten by others.

[Gist-it](http://gist-it.appspot.com/) for [quick_sort.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/sorting/src/quick_sort.py)

  

  

This was the second fastest list implementation I created, at about 1/12th the performance of the built-in sorting.  

  

**Merge Sort**  

Merge sort relies on splitting the list recursively until you have an ordered hierarchy of l item item lists. Then you compare each list with it's neighbour, and return a combined list of the two merged together. Now you have 2-item sorted lists, which you work through, comparing the left-most element to its neighbour's left-most element, and moving the lowest one to a new list, eventually creating a 4-item list.  

  

[Gist-it](http://gist-it.appspot.com/) for [merge_sort.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/sorting/src/merge_sort.py)

  

**Heap Sort**

Heap sort relies on understanding what a "heap" is, in this context. So let's do that.  

  

A heap is a data structure that is tree based, and follows the rule that all children of a node will have a value that is lower than or equal to the value of that node (for a max-heap, for a min-heap the rule is reversed). In practice, heaps are usually implemented within arrays, with the first or last item of the array being the root of the tree.  

  

Now, why do we do have a heap? What's the advantage? Apparently sorting things. :)  

  

In a heap sort, we first build the heap from the list we've been given. Once we have our heap, we know the item with the highest value is at the root of the heap, which is position 0 in the list representing the heap. So now we swap the first and last elements in that list, and either move the last element from the list, or simply treat that part of the heap as already sorted (which means our heap needs to know to ignore it somehow). Then we take the first item, and trickle it down through the heap until the heap is proper again. This consists of comparing it's value with it's children, and swapping it with the higher one of these, until one of these is not higher.  

  

[Gist-it](http://gist-it.appspot.com/) for [heap_sort.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/sorting/src/heap_sort.py)

  

Python apparently does have a [built-in heap library](http://docs.python.org/library/heapq.html), which might be worth benchmarking, as heap was my slowest sort implementation.  

  

**Bubble Sort**

Bubble sort is fairly trivial.  

  

Iterate through the items, except the last one, if an item is greater than the next one, swap their positions. When you reach the end of the list, do it again, unless there were zero swaps.  

  

[Gist-it](http://gist-it.appspot.com/) for [bubble_sort.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/sorting/src/bubble_sort.py)

  

**Insertion Sort**

Insertion sort is another trivial sort. I'm really only including it because I think my (unwitting) choice of an insertion sort in an interview may have cost me a job.  

  

[Gist-it](http://gist-it.appspot.com/) for [insertion_sort.py](https://github.com/alecmunro/Experiments-in-Public/blob/master/sorting/src/insertion_sort.py)

  

Interestingly enough, for my stupid example of sorting a small list of characters, insertion sort is the fastest implementation I created.  

  

**Acknowledgements and Conclusion**  

<b>

  

</b>  

Not really much to conclude, except that I now have a better understanding how to write a sorting algorithm, and some of the pros and cons of different algorithms. I certainly can't look at a data set and give you the big O case for a given algorithm.  

  

But one thing I do want to draw special attention to is Wikipedia's pages on this subject. They vary a bit in information density, but they were incredibly informative, and make use of numerous methods to help communicate how each sort works. If you really want to understand this stuff, I would definitely start with these pages:  

  

<ul>

<li>

[Quicksort](http://en.wikipedia.org/wiki/Quicksort)
</li>

<li>

[Merge sort](http://en.wikipedia.org/wiki/Merge_sort)
</li>

<li>

[Heap sort](http://en.wikipedia.org/wiki/Heapsort)
</li>

<li>

[Bubble sort](http://en.wikipedia.org/wiki/Bubble_sort)
</li>

<li>

[Insertion sort](http://en.wikipedia.org/wiki/Insertion_sort)
</li>

</ul>

Also, my thought to do this post was sparked by another post on Planet Python that mentioned Insertion Sort, where I recognized the algorithm. I'm not entirely sure, but [this](http://lionel.textmalaysia.com/insertion-sort.html) may be that post.

