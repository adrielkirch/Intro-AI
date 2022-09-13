from logic import *

a = Symbol("a")
b = Symbol("b")

# NOT
print('Not')
notSentence = Not(a).evaluate({'a':True})
print(f'{Not(a).formula()} ({notSentence})')

notSentence = Not(a).evaluate({'a':False})
print(f'{Not(a).formula()} ({notSentence})')

print('---/---/---')
# AND
print('And')
andSentence = And(a, b).evaluate({'a':False,'b':False})
print(f'{And(a, b).formula()} ({andSentence})')

andSentence = And(a, b).evaluate({'a':False,'b':True})
print(f'{And(a, b).formula()} ({andSentence})')

andSentence = And(a, b).evaluate({'a':True,'b':False})
print(f'{And(a, b).formula()} ({andSentence})')

andSentence = And(a, b).evaluate({'a':True,'b':True})
print(f'{And(a, b).formula()} ({andSentence})')

print('---/---/---')

print('Or')

orSentence = Or(a, b).evaluate({'a':False,'b':False})
print(f'{Or(a, b).formula()} ({orSentence})')

orSentence = Or(a, b).evaluate({'a':False,'b':True})
print(f'{Or(a, b).formula()} ({orSentence})')

orSentence = Or(a, b).evaluate({'a':True,'b':False})
print(f'{Or(a, b).formula()} ({orSentence})')

orSentence = Or(a, b).evaluate({'a':True,'b':True})
print(f'{Or(a, b).formula()} ({orSentence})')

print('---/---/---')
print('Implication')
implication = Implication(a,b).evaluate({'a':False,'b':False})
print(f'{Implication(a,b).formula()} ({implication})')

implication = Implication(a,b).evaluate({'a':True,'b':False})
print(f'{Implication(a,b).formula()} ({implication})')


implication = Implication(a,b).evaluate({'a':False,'b':True})
print(f'{Implication(a,b).formula()} ({implication})')

implication = Implication(a,b).evaluate({'a':True,'b':True})
print(f'{Implication(a,b).formula()} ({implication})')

print('---/---/---')
print('Biconditional')

biconditional = Biconditional(a,b).evaluate({'a':False,'b':False})
print(f'{Biconditional(a,b).formula()} ({biconditional})')

biconditional = Biconditional(a,b).evaluate({'a':True,'b':False})
print(f'{Biconditional(a,b).formula()} ({biconditional})')


biconditional = Biconditional(a,b).evaluate({'a':False,'b':True})
print(f'{Biconditional(a,b).formula()} ({biconditional})')

biconditional = Biconditional(a,b).evaluate({'a':True,'b':True})
print(f'{Biconditional(a,b).formula()} ({biconditional})')
