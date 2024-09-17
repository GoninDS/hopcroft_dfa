def prepare_initial_state(states, accepting_states):
    new_states = set()
    non_accepting = []
    accepting = frozenset(accepting_states)

    for i in states:
        if i not in accepting:
            non_accepting.append(i)

    new_states.add(frozenset(accepting))
    new_states.add(frozenset(non_accepting))   
    return new_states

def split(current_set, alphabet, transitions):
    hash_table = {}
    result = set()

    for state in current_set:
        key = ''
        for action in alphabet:
            key += str(transitions[state][action])
        if key not in hash_table:
            hash_table[key] = []
        hash_table[key].append(state)
    
    values = hash_table.values()
    for current in values:
        result.add(frozenset(current))

    return result

def hopcroft(states, alphabet, accepting_states, transitions):
    new_states = prepare_initial_state(states, accepting_states)
    current_states = None

    while (current_states != new_states):
        current_states = new_states.copy()
        new_states = set()
        for current_set in current_states:
            new_states = new_states | split(current_set, alphabet, transitions)

    return new_states


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

hopcroft(states, alphabet, accepting_states, transitions)