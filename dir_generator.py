import os

# ATTENTION:
# RUNNING THIS SCRIPT WILL OVERWRITE ANY FILES THAT WERE
# INSTRUCTED REQUESTED TO BE GENERATED!!

# paste this code into a python file and run it 😊

# region config


# init docstring
# your name (duh)
NAME = "Luigi Cussigh"
# your student id (duh)
STUDENT_ID = "2023148006"
# write the initial docstring or not
INCLUDE_INIT_DOCSTRING = True

# general config
# represents lab numbers
FOLDERS_TO_GENERATE = range(12, 15 + 1)
# problem files to generate per lab
PROBLEMS_PER_LAB = 10
# generate readme.py or not
GENEARTE_README = False
# directory which will contain the folders
# ex: PATH = "C:\\Users\\YOUR USERNAME\\Desktop\\aaa"
# be sure to use '\\' instead of '\' when writing paths in python
# because of escape sequences

# leave PATH equal to "" to generate folders
# in THIS script's folder (where this script is located)
PATH = ""


# endregion


# generate target path if blank
if PATH == "":
    PATH = os.path.dirname(os.path.abspath(__file__))


# prompt
cnt = len(FOLDERS_TO_GENERATE)  # i hate flake8
print(f"this will generate {cnt} folders in the folder: {PATH}")
confirm = input("enter 'y' to confirm action: ")

if confirm != "y":
    print("aborted.")
    exit(0)

# iterate through range
for lab_number in FOLDERS_TO_GENERATE:
    # create outer directory for lab
    if not os.path.exists(PATH + f"/lab{lab_number}"):
        os.mkdir(PATH + f"/lab{lab_number}")

    # path to folder that is to be submitted on LearnUs
    zip_folder_path = PATH + f"/lab{lab_number}/lab{lab_number}_{STUDENT_ID}"

    # create the folder if it doesnt exist
    if not os.path.exists(zip_folder_path):
        os.mkdir(zip_folder_path)

    # create p1, p2, pn
    for i in range(1, PROBLEMS_PER_LAB + 1):
        with open(zip_folder_path + f"/lab{lab_number}_p{i}.py", "w") as file:
            if INCLUDE_INIT_DOCSTRING:  # write docstring
                file.write('"""\n')
                file.write(f"Name: {NAME}\n")
                file.write(f"Student ID: {STUDENT_ID}\n")
                file.write(f"Lab problem: lab{lab_number}_p{i}.py\n")
                file.write('"""\n')

    # generate readme
    if GENEARTE_README:
        with open(
            zip_folder_path + f"/lab{lab_number}_README.py", "w"
        ) as file:
            pass

print("done!")
