file = open("data.txt", "r")  # open data source
data = []  # data

# import file to data list
for line in file:
    data.append(int(line))
file.close()

# add edge values
data = [data[0]] + data + [data[-1]]

resampled_data = []  # averaged out data
for i in range(1, len(data) - 1):  # iterate through data
    # recalc and append to resampled_data
    resampled_data.append((data[i-1] + data[i] + data[i+1])/3)

# print result
print(resampled_data)
