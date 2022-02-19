#NFA simple impl
import sys

trans = {
    'q1,0':['q1'],
    'q1,1':['q1','q2'],
    'q2,0':['q3'],
    'q2,~':['q3'],
    'q3,1':['q4'],
    'q4,0':['q4'],
    'q4,1':['q4']
}

tape ='001001'

machine = {
    'input':tape,
    'start':'q1',
    'accept':['q4'],
    'transition':trans,
}


def get_input(index):
    return machine['input'][index]

def is_last_char(index):
    return index == (len(machine['input'])-1)

def is_accept(states):
    for s in states:  
        c = machine['accept'].count(s)
        if(c > 0):
            return True

    return False

def get_tab():
    return machine['transition']

def add_items(lt,item):
    sett = set()
    if(type(item) is list):
        for it in item:
            sett.add(it)
    else:
        sett.add(item)

    result =[]
    for s in sett:
        result.append(s)
    return result

def transition(ch,cur_state):
    tab = get_tab()
    states = []
    key = cur_state + ',' + ch
    if(key in tab):
        states = add_items(states,tab.get(key))
    # add enlarged non-determin transition
    key = cur_state + ',' + '~'
    if(key in tab):
        states = add_items(states,tab.get(key))
    
    return states

def nfa(ch_index,stat):
    ch = get_input(ch_index)
    next_states = transition(ch,stat)
    print(ch + stat)
    print(next_states)
    if(is_last_char(ch_index)):
        if(is_accept(next_states)):
            print('recgnize input')
            sys.exit('stopped')
        else:
            print('reject input')
        #sys.exit('stopped')
    else:
        if(len(next_states) == 0):
            print('dead')
            return
        for s in next_states:
            nfa(ch_index + 1,s)


def start():
    start_state = machine['start']
    nfa(0,start_state)
    
    
start()    
    
