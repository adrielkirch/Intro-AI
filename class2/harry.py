from logic import *

rain = Symbol("rain") # It's rainning
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited dumbledore

#print the sentence logical formula
sentence = And(rain,hagrid)
print(sentence.formula())
print('---/---/---/')
#print logic value of a sentence

#Implication
print(Implication(Not(rain), hagrid).formula())
print('---/---/---/')

#Knowledge
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
print(knowledge.formula())
print(model_check(knowledge, rain))
