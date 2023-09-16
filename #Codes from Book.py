#Codes from Book
values = [1, 2, 3, 'N/A', '-', 4, -1, 0, 'a', '', 2, 6]

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)


mylist = [1,4,-5,10,-7,2,3,-1]
import math
print([math.sqrt(n) for n in mylist if n>0])

clip_neg = [n if n>0 else '-' for n in mylist]
print(clip_neg)

###############################

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import combinations_with_replacement, compress, islice
more5 = [n>5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))

######################################

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

#Make a dictionary of all prices over 200
p1={key:value for key, value in prices.items() if value > 200}

#Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2={key:value for key, value in prices.items() if key in tech_names}

print(p1)
print(p2)

#The above can done simplier in the below
p1=dict((key, value) for key, value in prices.items() if value > 200)
p2={key:prices[key] for key in prices.keys() & tech_names}

################################ page 30

from collections import defaultdict, namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', joined='2012-10-19')
print(sub.joined)

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total=0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s=Stock('ACME', 100, 123.45)
print(s)
s=s._replace(shares=75)
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype=Stock('', 0, 0.0, None, None)
#Func to convert a dictionary to a stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

############################

nums = [1, 2,3,4,5]
s=sum(x*x for x in nums)
print(s)

#Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

########### page 34

a={'x': 1, 'z': 3}
b={'y':2, 'z': 4}

from collections import ChainMap
c=ChainMap(a,b)
c['w']=10
#print(c['x'], len(c), list(c.keys()), list(c.values()))

values=ChainMap()
values = values.new_child()
values['x']=6
print(values)

####################Chapter 2 Strings and Text

line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re
print(line)
print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2]+['']
''.join(v+d for v,d in zip(values, delimiters))
print(values)

##################### page 38

filename ='spam.txt'
print(filename.endswith('.txt'))
filename.startswith('file:')
url = 'http://www.python.org'
url.startswith('http:')

import os
filenames=os.listdir('.')
#print(filenames)
[name for name in filenames if name.endswith(('.c', '.h', '.py'))]
#print([name for name in filenames if name.endswith(('.c', '.h'))])

print(any(name.endswith('.py') for name in filename))


from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

######################################page 40
from fnmatch import fnmatch, fnmatchcase
names=['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
matched= [name for name in names if fnmatch(name, 'Dat*.csv')]
print(matched)

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
matched_addr=[addr for addr in addresses if fnmatchcase(addr, '*ST')]
print(matched_addr)
matched_str =[stre for stre in addresses if fnmatchcase(stre, '2122 N CLARK ST')]
print(matched_str)

################# page 42 text/string search/match
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')  # prints False

text1 = text.startswith('yeah')
print(text1)   #Prints True

text2=text.endswith('no')
print(text2)  #prints False

# Search for the location of the first occurrence
text3 = text.find('no')
print(text3)

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
#simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+', text2):
    print('yes')
else:
    print('no')

#if you are going to perform a lot of matche using the same pattern use the precompile regular expression pattern into a pattern object first
datepat =re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
search_text= datepat.findall(text)
print(search_text)

###################### 2.5 page 45

text = 'yeah, but no, but yeah, but no, but yeah'
text1=text.replace('yeah', 'yep')
print(text1)

#rewrite date in the form of "11/27/2012 as 2012-11-27"
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
text1= re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text1)

######## You need to search for and possibly replace text in a case-insensitive manner

text = 'UPPER PYTHON, lower python, Mixed Python'
text1=re.findall('python', text, flags=re.IGNORECASE)
print(text1)

########### 2.7 Specifying a Regular Expression for the Shortest Match
str_pat=re.compile(r'\"(.*)\"') 
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

#str1_pat=re.compile(r'\"(.*?\)"')
#print(str1_pat.findall(text2))


######### 2.11 Stripping unwanted characters from String
#whitespace stripping
s='  hello wolrd   \n'
print(s)
print(s.strip())
t=s.lstrip()
print(t)
y=s.rstrip()
print(y)

#character stripping

t='---------hello======='
z=t.lstrip('-')
print(z)
w=t.strip('-=')
print(w)

##removing spaces in between strings

s=' hello          world     \n'
a=s.strip()
print(a)

t=s.replace('  ', '')
print(t)

import re
s=re.sub('\s+', ' ', s)
print(s.lstrip())

######### 2.12 Sanitizing and cleaning up Text
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap ={
    ord('\t'): ' ',
    ord('\f'):' ',
    ord('\r'): None #Deleted
}
a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
y=b.translate(cmb_chrs) 
print(y)

a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
c = b.encode('ascii', 'ignore').decode('ascii')
print(c)

#####String concatenation
parts =['Is', 'Chicago', 'Not', 'Chicago']
t=' '.join(parts)
print(t)

a='Is Chicago'
b='Not Chicago'
print('{} {}'.format(a,b))

data=['ACME', 50, 91.1]
t=','.join(str(d) for d in data)
print(t)

#Note
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)
#for part in combine(sample(), 32768):
   # f.write(part)

# Problem 2.15 String substitution
s = '{name} has {n} messages.'
t= s.format(name='Dominic', n=37)
print(t)

name='Guido'
n=37
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name=name
        self.n=n
        pass
a = Info('Guido', 37)
y=s.format_map(vars(a))
print(y)

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
t=s.format_map(safesub(vars()))



######## 2.16 Reformatting Text

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='     '))
print(textwrap.fill(s, 40, subsequent_indent='      '))


### 2.18 Tokenizing text

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
scanner.match()

# cleaner code from the above

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generator_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
for tok in generator_tokens(master_pat, 'foo = 42'):
    print(tok)


NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM,PLUS,MINUS,TIMES,DIVIDE,LPAREN,RPAREN,WS]))

from collections import namedtuple

#Tokenizer
#Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type !='WS':
            yield tok

#Parser
class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok =None
        self.nexttok = None
        self._advance()
        return self.expr()



#Byte strings operations
data = b'Hello world'
t=data[0:5]
print(t)
print(data.startswith(b'Hello'))
print(data.split())
y=data.replace(b'Hello', b'Hello Cruel')
print(y)


data = b'FOO:BAR,SPAM'
import re
t = re.split(b'[:,]', data) #replacing ':' with ','
print(t)

#Numbers, dates & times, performing math ops 3.1
print(round(1.27, 1))
print(round(16247731, -3))

x=1.23456
print(format(x,'0.2f'))
print('value is {:0.3}'.format(x))

#Using Decimal module

from decimal import Decimal
a=Decimal('4.2')
b=Decimal('2.1')
print(a+b)
print((a+b)==Decimal('6.3'))

from decimal import localcontext
a=Decimal('1.3')
b=Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

#formatting numbers with modern formatting technique
x = 1234.56789
x1 = format(x, '0.2f') #Two decimal places
print(x1)
x2 = format(x, '<10.2f') #Left justified 10 Chars
print(x2)
x3 = format(x, ',') #Inclusion of thousands separator
print(x3)

#formatting numbers with old formatting technique
x = 1234.56789
print('%0.1f' % x)

#Converting to Binary, Octal and Hex
x = 1234
x1 = bin(x)
x2 = oct(x)
print(x1, x2)

#Alt you can use the format option
x3 = format(x, 'b') #converting to binary
x4 = format(x, 'o') #converting to Oct
x5 = format(x, 'x') #converting to Hex
print(x3,' ', x4, ' ', x5)

#Converting from Bin, Oct, Hex back to Int
x6 = int('4d2', 16) #Converting to integer
x7= int('10011010010', 2)  #base 2
print(x6, ' ', x7)



#Iterators 4.1
'''
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)   #Emphasis is on using the Next Iterator
            print(line, end='')
    except StopIteration:
        pass

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)   #Emphasis is on using the Next Iterator
        if line is None:
            break
        print(line, end='')'''


def frange(start, stop, increment):
    x =start
    while x < stop:
        yield x
        x += increment
for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
#print(next(c))


class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

#example using the above class Node
if __name__ == '__main__':
    root=Node(0)
    child1=Node(1)
    child2=Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

#Iterating in reverse 
a=[1,2,3,4,5]
for x in reversed(a):
    print(x)

#itertools.islice() function is perfectly suited for taking slices of iterators and
#generators where normal slicing fails 4.7
def count(n):
    while True:
        yield n
        n += 1
c=count(0)
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

#Skipping part of an iterable 4.8
from itertools import islice
items = ['a', 'b', 'c', '1', '2', '4', '10', '15']
for x in islice(items, 3, None):
    print(x)
print('\n')
# Iterating over all possible combinations/permutations 4.9
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)
#Giving an optional length
for y in permutations(items, 2):
    print(y)

from itertools import combinations
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)
for c in combinations_with_replacement(items, 3):
    print(c)

print('\n')

# 4.10 iterate over the index-value pairs 
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
#Can be used as numbering
for idx, val in enumerate(my_list, 1):
    print(idx, val )

print('\n')

word_summary = defaultdict(list)
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

print('\n')

#Iterate over multiple sequences simult 4.11
xpts = [1,5,4,2]
ypts = [3,6,9,11]

for x, y in zip(xpts, ypts):
    print(x, y)
print('\n')

#when the lengths are unequal
from itertools import zip_longest
a = [1,2,3,4]
b = ['a','b','c','d','e','f']
for i in zip_longest(a,b):
    print(i)
for j in zip_longest(a,b, fillvalue=0):
    print(j)

print('\n')
#Using zip to make a dictionary
headers =   ['1', '2', '3']
values = ['abc','efg','hij']
s=dict(zip(headers,values))
print(s)
print('\n')

for name, val in zip(headers, values):
    print(name, '=', val)
y = list(zip(headers, values)) #If you need to store the endproduct of zip
print('The end product of zip stored in y =', y)
print('\n')

#Iterating on items in separate containers 4.12
from itertools import chain
a=[1,2,3,4]
b=['x','y','z']
for x in chain(a,b):
    print(x)
print('\n')
#Flattening a nested sequence 4.14

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1,2,[3,4,[5,6],7],8]
for x in flatten(items):
    print(x)

print('\n')

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)
print('\n')

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

print('\n')

# 4.15 Iterating in sorted order over merged sorted iterables
import heapq
a=[1,2,3,4]
b=[5,6,7,8]

for c in heapq.merge(a,b):
    print(c)

print('\n')

#Printing with different separator or ending 5.3
print('ACME','50',60,9.5)
print('ACME','50',60,9.5, sep=',')
print('ACME','50',60,9.5, sep=',',end='!!\n')

