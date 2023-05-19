f_correct = open("out1.txt")
f_testing = open("out2.txt")

correct = []
for i in f_correct:
    correct.append(i)

testing = []
for i in f_testing:
    testing.append(i)

print(correct == testing)