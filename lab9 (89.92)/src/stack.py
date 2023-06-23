'''
   Stack module.

   Implements a stack data-structure.
   Function getStack() creates and returns an empty stack. All other
   functions receive a stack as input to perform their operation.
'''

def getStack():
    '''Creates and returns an empty stack'''
    return []

def isEmpty(s):
    '''Returns True if stack empty, otherwise returns False'''
    if s == []:
        return True
    else:
        return False

def top(s):
    '''Returns the top item of stack, item not removed
       Otherwise, returns None'''
    if isEmpty(s):
        return None
    else:
        return s[len(s) - 1]

def push(s,item):
    '''Pushes item on the top of stack'''
    
    s.append(item)


def pop(s):
    '''Removes and returns top item of stack.
       If stack empty, returns None.
    '''
    if isEmpty(s):
        return None
    else:
        item = s[len(s) -1]
        del s[len(s) - 1]
        return item

