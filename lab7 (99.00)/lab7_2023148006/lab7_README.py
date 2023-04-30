##############################################################################
# CCO1100-01 Lab 7                                                           #
# answers to questions                                                       #
##############################################################################

#
# Q1: please replace 'None' by your answer (bool: True or False)
# * True: valid function call
# * False: invalid function call
#
q1_a_answer = False
q1_b_answer = True
q1_c_answer = True
q1_d_answer = True
q1_e_answer = True

#
# Q2: please replace 'None' by your answer (answer = [n, req1, req2])
# Requirement 1: n1 must be less than or equal to n2
# Requirement 2: n1 and n2 must be integer values (type int)
# * n: type int, total number of gcd function calls
# * req1: type int, number of gcd function calls that satisfy requirement 1
# * req2: type int, number of gcd function calls that satisfy requirement 2
#
q2_a_answer = [1, 1, 1]
q2_b_answer = [1, 1, 0]
q2_c_answer = [1, 1, 1]
q2_d_answer = [2, 2, 2]
q2_e_answer = [2, 0, 1]

#
# Q3: please replace the empty strings by your answer (string)
# * Complete the following answer:
# The output of the program is '(a)' because l2[0] and l1[2] are (b) of (c)
# (a) True or False
# (b) a plural noun
# (c) a variable name
#
q3_a_answer = "True"
q3_b_answer = "aliases"
q3_c_answer = "l3"

##############################################################################
# Grading code. Please do not touch any code below this line:                #
##############################################################################
SEP = '-' * 79
print(SEP)
print('CCO1100-01 Lab 7')
print('Answers to questions')
print(SEP)
# Q1 grading code
q1_subq_answer_list = [
    ('a', q1_a_answer),
    ('b', q1_b_answer),
    ('c', q1_c_answer),
    ('d', q1_d_answer),
    ('e', q1_e_answer),
]
for (subq, answer) in q1_subq_answer_list:
    if type(answer) == bool:
        print('Answer Q1'+subq+':', answer)
    else:
        print('Answer Q1'+subq+': ERROR answer must be bool (True or False')
print(SEP)
# Q2 grading code
q2_subq_answer_list = [
    ('a', q2_a_answer),
    ('b', q2_b_answer),
    ('c', q2_c_answer),
    ('d', q2_d_answer),
    ('e', q2_e_answer),
]
for (subq, answer) in q2_subq_answer_list:
    if (type(answer) == list and len(answer) == 3 and
        len([x for x in answer if type(x) != int]) == 0):
        print('Answer Q2'+subq+':', answer)
    else:
        print('Answer Q2'+subq+': ERROR answer must be list of three integers')
print(SEP)
# Q3 grading code
print('Answer Q3a:', q3_a_answer)
print('Answer Q3b:', q3_b_answer)
print('Answer Q3c:', q3_c_answer)
print('Answer Q3 (complete answer):')
print('The output of the program is \''+q3_a_answer+'\'')
print('because l2[0] and l1[2] are '+q3_b_answer+' of '+q3_c_answer)
print(SEP)
