from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

# function which is true i.e. an assertion
sentence = And(
    Implication(Not(rain), hagrid), 
    Or(hagrid, dumbledore), 
    Not(And(hagrid, dumbledore)), 
dumbledore)

print(sentence.formula())
print(model_check(sentence, rain)) # model check algorithm
print(model_check(sentence, Not(hagrid)))

print(model_check(sentence, hagrid)) # KB |= alpha
print(model_check(And(rain, hagrid), Or(rain, hagrid)))  # KB |= alpha
print(model_check(Or(rain, hagrid), And(rain, hagrid))) # KB |= alpha




