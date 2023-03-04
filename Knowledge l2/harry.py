from logic import *

rain = Symbol("rain") # It is raining.
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),  # If it is not raining then Harry visited Hagrid
    Or(hagrid, dumbledore), # Harry visited Hagrid or Dumbledore
    Not(And(hagrid, dumbledore)), # Harry didn't visit both Hagrid and Dumbledore
    dumbledore # Harry visited Dumbledore
)

print(model_check(knowledge, rain)) # Do i know for sure it is raining
