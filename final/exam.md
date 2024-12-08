# Problem 1:
a. In the statement L = [1,2,3], L is a class.
False

b. The orders of growth of bubble sort and merge sort are both polynomial.
False

c. A bisection search algorithm always returns the correct answer when searching for an element in a sorted list.
True

d. Performing binary search on an unsorted list will always return the correct answer in O(log(n)) time where L is the length of the list.
False

# Problem 2:
a. You have the following class hierarchy:
```python
class A(object):
    def foo(self):
        print("hi")

class B(A):
    def foo(self):
        print("bye")
```

b. Which is correct?
- When a = A() we say that a is an instance of A <--- Correct
- When b = B() we say that b is a subclass of A
- Both of the above 
- Neither of the above

c. Consider the function f below. What is its Big O complexity? <--- WRONG, m is set to 0 in the g(m) func
```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)
```
Ans: O(n^2)

d. A dictionary is an immutable object because its keys are immutable.
Ans: False because a dictionary is mutable

e. Consider the following two functions and select the correct choice below:
```python
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1:
        return 1.0
    else:
        return n*foo_two(n-1)
```
- The worst case Big Oh time complexity of foo_one is worse than the worst case Big Oh time complexity of foo_two.
- The worst case Big Oh time complexity of foo_two is worse than the worst case Big Oh time complexity of foo_one.
- The worst case Big Oh time complexity of foo_one and foo_two are the same. <---- Correct
- Impossible to compare the worst case Big Oh time complexities of the two functions.

f. The complexity of 1^n + n^4 + 4n + 4 is
Ans: polynomial

# Problem 3 - Implement a function that meets the specifications below
```python
def sum_digits(s):
""" assumes s a string
Returns an int that is the sum of all of the digits in s.
If there are no digits in s it raises a ValueError exception. """
    dig = False
    sum = 0
    for c in s:
        try:
            sum += int(c)
            dig = True
        except:
            continue
    if not dig:
        raise ValueError("No digits in string!")
    return sum
```
For example, sum_digits("a;35d4") returns 12.

# Problem 4 - Implement a function that meets the specifications below
```python
def max_val(t):
    """ t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t """
    comp = -696969
    if type(t) is int:
        return t
    else:
        for ele in t:
            comp = max(comp, max_val(ele))
    return comp
```
Examples:
    max_val((5, (1,2), [[1],[2]])) returns 5.
    max_val((5, (1,2), [[1],[9]])) returns 9.
better:
```python
def max_val(t):
    if type(t) is int:
        return t
    else:
        for ele in t:
            return max(max_val(ele) for ele in t)
```

# Problem 5 - Implement a function that meets the specifications below.
```python
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain N unique lowercase letters.
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where each key is a letter in map_from at index i and the corresponding value is the letter in map_to at index i.
    decoded is a string that contains the decoded version of code using the key_code mapping. """
    key_code = {}
    decoded = []
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for c in code:
        decoded.append(key_code[c])

    return(key_code, ''.join(decoded))
```
For example:
cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) ({'a':'d','b': 'c', 'd': 'a', 'c': 'b'}, 'adc') Paste your entire function, including the definition, in the box below.

# Problem 6 - Write a class that implements the specifications below
Superclass:
```python
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
        occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
        Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
```
Ans: 
```python
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
        If e occurs in self, reduces the number of
        times it occurs in self by 1. Otherwise does nothing. """
        if self.vals.get(e, 0) > 0:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
        Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)
    
    def __add__(self, bag2):
        assert isinstance(bag2, Bag), "Type is not bag"
        new_bag = Bag()
        for key in self.vals:
            new_bag.vals[key] = self.vals.get(key, 0)
        for key in bag2.vals:
            new_bag.vals[key] = new_bag.vals.get(key, 0) + bag2.vals.get(key, 0)
        return new_bag
```
For example:
    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    print(d1)
    d1.remove(2)
    print(d1)
Prints:
    4:2
    4:2

For example:
    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    d1.insert(4)
    print(d1.count(2))
    print(d1.count(4))
Prints:
    0
    3

For example,
    a = Bag()
    a.insert(4)
    a.insert(3)
    b = Bag()
    b.insert(4)
    print(a+b)
Prints:
    3:1 and 4:2

b. Write a class that implements the specifications below.
```python
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
        removes e from self"""
        del self.vals[e]
    def is_in(self, e):
        """assumes e is hashable
        returns True if e has been inserted in self and
        not subsequently removed, and False otherwise."""
        return e in self.vals
```

# Problem 7 - Implement a class that meets the specifications <-- Wrong kinda, small mistakes overall logic good
Superclasses:
```python
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
```
Ans:
```python
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        super().__init__(center_loc)
        self.tents = [tent_loc]
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        
        for loc in self.tents:
            if loc.dist_from(new_tent_loc) <= 0.5:
                return False
        self.tents.append(new_tent_loc)
        return True
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc in self.tents:
            self.tents.remove(tent_loc)
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        return [str(tent) for tent in sorted(self.tents, key = lambda tent: tent.getX())]
```
Example:
c = MITCampus(Location(1,2))
c.add_tent(Location(2,3)) should return True
c.add_tent(Location(1,2)) should return True
c.add_tent(Location(0,0)) should return False
c.add_tent(Location(2,3)) should return False
c.get_tents() should return ['<0,0>', '<1,2>', '<2,3>']