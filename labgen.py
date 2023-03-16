import os
current_dir = os.getcwd()

for i in range(3,17):
    os.mkdir(current_dir + f"\\lab{i}")
    os.mkdir(current_dir + f"\\lab{i}\\lab{i}_2023148006")
    for j in range(1, 11):
        with open(current_dir + f"\\lab{i}\\lab{i}_2023148006\\lab{i}_p{j}.py", 'w') as fp:
            pass
