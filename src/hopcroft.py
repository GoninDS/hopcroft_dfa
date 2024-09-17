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
            if action in transitions[state]:
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