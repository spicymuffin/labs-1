# get input
m1 = int(input("Person 1: Enter month born (1-12): "))
d1 = int(input("Person 1: Enter day born (1-31): "))
y1 = int(input("Person 1: Enter year born (4-digit): "))
m2 = int(input("Person 2: Enter month born (1-12): "))
d2 = int(input("Person 2: Enter day born (1-31): "))
y2 = int(input("Person 2: Enter year born (4-digit): "))

# define constants
H_P_D = 24
M_P_H = 60
S_P_M = 60
D_P_Y = 365

# calcuate seconds
secsperday = H_P_D * M_P_H * S_P_M
secsperyear = D_P_Y * secsperday

avg_secsperyear = ((4 * secsperyear) + secsperday) // 4
avg_secspermonth = avg_secsperyear // 12

# calculate seconds to 1900 for both people
p1_secs = ((y1-1900) * avg_secsperyear) + \
          ((m1-1) * avg_secspermonth) + \
          (d1 * secsperday)

p2_secs = ((y2-1900) * avg_secsperyear) + \
          ((m2-1) * avg_secspermonth) + \
          (d2 * secsperday)

# abs bc we dont know who is older
print("Age difference in seconds:", (abs(p2_secs-p1_secs)))
