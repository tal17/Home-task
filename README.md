# Home-task - File generator
File generator home task - a python file called file_generator.py.
## Description
Here I will give a short explenation about the way I solved the given problem. First, I wanted to generate all possible sections. In order to do that, I ran over all the possible tags (numbers between 0-255, which a single byte can represent). For each tag, I ran over all possible value lengths, and for each length I generated a list with all possible sets of values that match that length. It is important to say that I saved all the sections in a list, where each item in this list is a string, that stores numbers between 0-255 in a string format, separated by the seperator '+', Each number is meant to represent a byte.
After generating a list of all possible sections, I needed to make all possible section combinations according to the number of sections. So, I ran over all numbers between 0-255 which here represent the number of sections, and saved in a list all possible section combinations according to the number of sections.
Finally, all I had to do is to iterate over the list with all the file options, seperate each item in it by the seperator '~', convert each string in the separated list into the integer it represented, then convert it to a binary value, and then write it into a file. Of course, at the beginning of each file the first thing that was written to it was the constant magic in little endian.
