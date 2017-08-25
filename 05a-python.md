# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of objects that both maintain order of elements. A key difference is that lists can be changed while tuples cannot. Because of this, tuples can be used as keys in dictionaries and lists cannot.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are sequences of objects. One difference is that lists maintain order, but sets do not. Another difference is that there can be no duplicate objects in a set, where a list can have duplicates. When searching for an element in a list versus a set, performance is faster for sets. This is because when searching for an item in a list, each item in that list needs to be compared for equality, which is done in linear time. A set, however, uses a hash table. A hash table has constant lookup time and is faster than linear time.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` in Python is function created at runtime that does not require a name. It can be useful when sorting or searching through different data structures of objects as a parameter. If we want to sort a list of tuples by last element, we could use a `lambda` function as a parameter. For example:
```python
l = sorted(tuples_list, key=lambda i: i[1]))  
```
>> Another reason to use `lambda` is it can rewrite blocks of statements into a single line expression . If we want to write a function that adds two numbers:
```python
def my_add(x,y):
    return x + y
```
>> This can be written in one line with a `lambda` function.
```python
f = lambda x, y: x+y
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to construct lists in an easy one line way in Python. We can use this to create a list of squaring the numbers between 1 and 10:
```python
l = [i**2 for i in range(1,11)]
```
>> Equivalents `map` and `filter`:
```python
import math

m = map(lambda i: i**2, range(1,11))
f = filter(lambda i: math.sqrt(i) - int(math.sqrt(i)) == 0, range(1,101))
```
>> List comprehension is always preferred in Python, but if the comprehension gets too long/complicated, then using `map` or `filter` would be more appropriate.

>> Set comprehension, same as the list example above:
```python
s = {i**2 for i in range(1,11)}
```
>> Creating a dictionary of numeric keys and empty list values using comprehension:
```python
d = {key:[] for key in range(10)}
``` 

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





