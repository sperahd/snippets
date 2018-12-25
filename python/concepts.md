# Python special concepts

## Iterators

An iterator is an object that can be iterated (looped) upon. It is used to abstract a container of data to make it behave like an iterable object. You probably already use a few iterable objects every day: strings, lists, and dictionaries to name a few. 

An iterator is defined by a class that implements the Iterator Protocol. This protocol looks for two methods within the class: __iter__ and __next__.

### Why to use iterators

Iterators don’t compute the value of each item when instantiated. They only compute it when you ask for it. This is known as lazy evaluation.

### When to use iterators

Lazy evaluation is useful when you have a very large data set to compute. It allows you to start using the data immediately, while the whole data set is being computed.


## Generators

Generators introduce the yield statement to Python. It works a bit like return because it returns a value. The difference is that it saves the state of the function. The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding.

### Why to use generators

Much more pythonic than iterators, very few lines of code to achieve what we could be defining a class in iterator.
