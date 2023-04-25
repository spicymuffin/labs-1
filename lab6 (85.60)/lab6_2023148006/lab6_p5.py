import sys

# outer list
f = []
# accept input
while True:
    f_i = input("Enter a fruit type (q to quit): ")
    if f_i == 'q':
        break # break if 'q'
    w_i = int(input("Enter the weight in kg: "))
    f.append([f_i, w_i])  # append [fruit, mass] to outer list

if len(f) == 0:  # if no data exit
    print("No data received, exiting.")
    sys.exit(0)

f.sort()  # sort
# since the list is sorted, we can add to mass counter until fruit changes
curr_fr = f[0][0]
curr_fr_mass = 0
for i in range(len(f)):
    if f[i][0] == curr_fr:  # if prev and curr fruit match
        curr_fr_mass += f[i][1]  # add to curr mass
    else:
        print(f"{curr_fr}, {curr_fr_mass}kg.")  # else print vals
        # sent new (previous in the next iteration) current fruit
        curr_fr = f[i][0]
        # add to mass 0 current mass e.g. set mass to current mass
        curr_fr_mass = f[i][1]

# since last fruit's change isnt detected we have to print the current fruit and its mass
# before ending the program
print(f"{curr_fr}, {curr_fr_mass}kg.")
