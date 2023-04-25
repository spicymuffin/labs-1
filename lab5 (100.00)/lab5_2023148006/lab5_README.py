##############################################################################
# CCO1100-01 Lab 5                                                           #
# answers to questions                                                       #
##############################################################################

#
# Q1: please replace each 'None' by your answer (Boolean: True or False):
#
q1_a_answer = True
q1_b_answer = True
q1_c_answer = False
q1_d_answer = False

#
# Q2: please replace each 'None' by your answer (Boolean: True or False):
#
q2_a_answer = False
q2_b_answer = True
q2_c_answer = True
q2_d_answer = False
q2_e_answer = True

#
# Q3: please replace the empty strings by your answer (string):
#
q3_a_answer = "num >= 0 and num < 100"
q3_b_answer = "(num < 100 and num >= 0) or num == 200"
q3_c_answer = "'Thompson' in last_names or 'Wu' in last_names"
q3_d_answer = "'Thomson' in last_names and 'Wu' not in last_names"

#
# Q4: please fill in the blanks (empty string and parameters) by your answer:
# (a: string, b and c: integer)
#
q4_a_answer = "We need to insert " + "int" + "() function"
q4_b_answer = "We need to swap line " + str(4) + " and " + str(5)
q4_c_answer = "We need to fix indentation for line " + str(6)

##############################################################################
# Grading code. Please do not touch any code below this line:                #
##############################################################################
SEP = '-' * 79
print(SEP)
print('CCO1100-01 Lab 5')
print('Answers to questions')
print(SEP)
print('Answer Q1:', q1_a_answer)
print('Answer Q1:', q1_b_answer)
print('Answer Q1:', q1_c_answer)
print('Answer Q1:', q1_d_answer)
print(SEP)
print('Answer Q2:', q2_a_answer)
print('Answer Q2:', q2_b_answer)
print('Answer Q2:', q2_c_answer)
print('Answer Q2:', q2_d_answer)
print('Answer Q2:', q2_e_answer)
print(SEP)
for num in [-1, 0, 67, 99, 100]:
    print('Answer Q3:', eval(q3_a_answer))
for num in [-1, 0, 67, 99, 100, 199, 200]:
    print('Answer Q3:', eval(q3_b_answer))
last_names = ["Peter", "James", "Wu"]
print('Answer Q3:', eval(q3_c_answer))
print('Answer Q3:', eval(q3_d_answer))
print(SEP)
print('Answer Q4:', q4_a_answer)
print('Answer Q4:', q4_b_answer)
print('Answer Q4:', q4_c_answer)
print(SEP)
