##############################################################################
# CCO1100-01 Lab 6                                                           #
# answers to questions                                                       #
##############################################################################

#
# Q1: please replace the strings by your answer (type str)
# * a: single line of code printing the 4th character of str1
# * b: single line of code printing the index of the 1st 'o' in str1
#
q1_a_answer = "print(str1[3])"
q1_b_answer = "print(str1.index('o'))"

#
# Q2: please replace the strings by your answer (type str)
# * a, b: single line of code (expression)
# * c: multiple lines of code storing the computed value in 'lstsum'
# * d: single line of code (assignment statement)
# (DO NOT call print function in the answers of Q2.)
#
q2_a_answer = "len(lst)"
q2_b_answer = "len(lst)*3"
q2_c_answer = """
lstsum = 0
for i in range(len(lst)):
    lstsum += sum(lst[i])"""
q2_d_answer = "lst[3][2] = 12"

#
# Q3: please replace each 'None' in lists by your answer (type list [int, int])
# answer = [list1[0], list2[0]]
#
q3_a_answer = [10, 50]
q3_b_answer = [10, 10]
q3_c_answer = [15, 15]
q3_d_answer = [0, 0]

#
# Q4: please replace lists by your answer (type list [type int, ...])
# Note: put all numbers to the list if the number of answers is more than one
# Ex 1), If the equivalent expressions are 1, 3 => q4_a_answer = [1, 3]
# Ex 2), If the equivalent expression is only 2 => q4_a_answer = [3]
# Ex 3), If there are no equivalent expressions => q4_a_answer = []
#
q4_a_answer = [1]
q4_b_answer = [1, 5]

##############################################################################
# Grading code. Please do not touch any code below this line:                #
##############################################################################
SEP = '-' * 79
print(SEP)
print('CCO1100-01 Lab 6')
print('Answers to questions')
print(SEP)
# Q1 grading code
str1 = 'Hello World'
print('Answer Q1a (code):', q1_a_answer)
print('Answer Q1b (code):', q1_b_answer)
print('Answer Q1a (exec):')
exec(q1_a_answer)
print('Answer Q1b (exec):')
exec(q1_b_answer)
print(SEP)
# Q2 grading code
lst = [[0, 1, 2], [5, 4, 3], [0, 0, 0], [3, 2, 1]]
print('Answer Q2a (code):', q2_a_answer)
print('Answer Q2b (code):', q2_b_answer)
print('Answer Q2c (code):', q2_c_answer)
print('Answer Q2d (code):', q2_d_answer)
print('Answer Q2a (eval):', eval(q2_a_answer))
print('Answer Q2b (eval):', eval(q2_b_answer))
exec(q2_c_answer)
print('Answer Q2c (lstsum):', lstsum)
exec(q2_d_answer)
print('Answer Q2d (lst):', lst)
print(SEP)
# Q3 grading code
q3_subq_answer_list = [
    ('a', q3_a_answer),
    ('b', q3_b_answer),
    ('c', q3_c_answer),
    ('d', q3_d_answer),
]
for (subq, answer) in q3_subq_answer_list:
    if (type(answer) == list and len(answer) == 2 and
            type(answer[0]) == int and type(answer[1]) == int):
        print('Answer Q3'+subq+':', answer)
    else:
        print('Answer Q3'+subq+': ERROR answer must be list of two integers')
print(SEP)
# Q4 grading code
q3_subq_answer_list = [
    ('a', q4_a_answer),
    ('b', q4_b_answer),
]
for (subq, answer) in q3_subq_answer_list:
    if len([x for x in answer if type(x) != int]) == 0:
        answer.sort()
        print('Answer Q4'+subq+':', answer)
    else:
        print('Answer Q4'+subq+': ERROR answer must be list of integers')
print(SEP)
