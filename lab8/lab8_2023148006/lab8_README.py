##############################################################################
# CCO1100-01 Lab 8                                                           #
# answers to questions                                                       #
##############################################################################
#
# Q1: please replace the empty strings and lists by your answer
# Replace the empty strings by what the programs of Q1 print.
# Replace the empty lists with the list of occurrences in the programs of Q1.
# Note: Add all occurrences to the list if the number of occurences is more
# than one.
# Occurrences should be in the form of (line, variable, frame).
# * line: type int, line number
# * variable: type str, name of variables
# * frame: type str
# * frame: function names for function scopes,"global" for global frame
# E.g., Line 2, variable n, frame x in (a): [(2, "n", "x")]
# E.g., q1_1_occurrences = [(2, "n", "x"), (5, "n", "y")...]
#
q1_a_answer = "11 20"
q1_a_occurrences = [(2, "n", "global"),
                    (5, "n", "foo1"),
                    (6, "n", "foo1"),
                    (8, "n", "global"),
                    (9, "x", "global"),
                    (9, "n", "global"),
                    (10, "y", "global"),
                    (11, "x", "global"),
                    (11, "y", "global")]
q1_b_answer = "2"
q1_b_occurrences = [(3, "y", "bar"),
                    (3, "x", "foo"),
                    (5, "x", "foo"),
                    (8, "x", "global")]
q1_c_answer = "1"
q1_c_occurrences = [(3, "y", "bar"),
                    (3, "x", "global"),
                    (8, "x", "global")]

##############################################################################
# Grading code. Please do not touch any code below this line:                #
##############################################################################
SEP = '-' * 79
print(SEP)
print('CCO1100-01 Lab 8')
print('Answers to questions')
print(SEP)
# Q1 grading code
print('Answer Q1a:\n'+q1_a_answer)
for (l, n, x) in q1_a_occurrences:
    if type(l) == int and type(n) == str and type(n) == str:
        print('Line '+str(l)+', variable '+n+': '+x)
    else:
        print('ERROR answer must be list of one integer and two strings')
print('\nAnswer Q1b:\n'+q1_b_answer)
for (l, n, x) in q1_b_occurrences:
    if type(l) == int and type(n) == str and type(n) == str:
        print('Line '+str(l)+', variable '+n+': '+x)
    else:
        print('ERROR answer must be list of one integer and two strings')
print('\nAnswer Q1c:\n'+q1_c_answer)
for (l, n, x) in q1_c_occurrences:
    if type(l) == int and type(n) == str and type(n) == str:
        print('Line '+str(l)+', variable '+n+': '+x)
    else:
        print('ERROR answer must be list of one integer and two strings')
print(SEP)
