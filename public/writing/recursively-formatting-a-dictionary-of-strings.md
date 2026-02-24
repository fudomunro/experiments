Title: Recursively formatting a dictionary of strings
Date: 2012-03-09 14:52
Author: Alec Munro
Tags: python, utility
Slug: recursively-formatting-a-dictionary-of-strings

I have a use-case where I'm using a dictionary as a basis for generating a configuration file, and many of the values in the file share pieces, such as URL bases or credentials. I will also be generating configuration files for several different instances from the same dictionary.  

I wanted a simple way to define replaceable parts of the dictionary. I made a couple of Google searches, didn't find anything on the first page, so I wrote this:

  

[gist for dict_format.py](https://gist.github.com/2006829)  

I hope it's useful to someone else, or that I find it next time I have this use-case. :)

