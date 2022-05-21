from logic import *

A = Symbol("A")
B = Symbol("B")

# NOT

notSentence = Not(A)
valueNotSentence = model_check(notSentence, Not(A))

print(notSentence.formula() + f" ({valueNotSentence})")

notSentence = Not(A)
valueNotSentence = model_check(notSentence, A)

print(notSentence.formula() + f" ({valueNotSentence})")
print('---/---/---/')

# AND

andSentence = And(A, B)
valueAndSentence = model_check(andSentence, A)
print(andSentence.formula() + f" ({valueAndSentence})")
valueAndSentence = model_check(andSentence,  Not(B))
print(andSentence.formula() + f" ({valueAndSentence})")
print('---/---/---/')

# OR

orSentence = Or(A, B)
valueOrSentence = model_check(orSentence, A)
print(orSentence.formula() + f" ({valueOrSentence})")
