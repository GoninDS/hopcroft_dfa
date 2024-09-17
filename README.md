# **Hopcroft DFA Algorithm**

A simple implementation of Hopcroft's DFA minimization algorithm done in Python

## Instruction manual

To use the algorithm you can view the following example

``` python
from hopcroft import hopcroft

states = {0, 1, 2, 3, 4, 5}
alphabet = {'a', 'b'}
initial_state = {0}
accepting_states = {1, 3, 5}
transitions = {
    0:{'a': 1, 'b': 2},
    1:{'a':0, 'b':3},
    2:{'a':4, 'b':5},
    3:{'a':4, 'b':5},
    4:{'a':4, 'b':5},
    5:{'a':5, 'b':5},
}

result = hopcroft(states, alphabet, accepting_states, transitions)
```

## Credits

+ Luis David Solano Santamaría


