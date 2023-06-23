# Sparse Text Program

def createModifiedFile(input_file, output_file):
    '''
        For text file input_file, creates a new version in file output_file
        in which all instances of the letter 'e' are removed.
    '''

    num_total_chars = 0
    num_removals = 0

    for line in input_file:
        # save original line length
        if line[-1] == '\n':  # if the line ends with \n
            orig_line_length = len(line) - 1
        else:  # if the line doenst end with \n
            orig_line_length = len(line)

        num_total_chars += orig_line_length

        # remove all duplicate whitespaces
        s = []
        i = 0
        spflag = False
        while i < len(line):
            if line[i] == ' ' and not spflag:
                spflag = True
                s.append(line[i])

            if line[i] != ' ' and spflag:
                spflag = False

            if not spflag:
                s.append(line[i])

            i += 1

        modified_line = ''.join(s)

        if line[-1] == '\n':  # if the line ends with \n
            num_removals = num_removals + \
                (orig_line_length - (len(modified_line) - 1))
        else:  # if the line doenst end with \n
            num_removals = num_removals + \
                (orig_line_length - len(modified_line))

        # simulataneouly output line to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)

    return (num_total_chars, num_removals)


# --- main

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name, 'r')
new_file_name = 'r_' + file_name
output_file = open(new_file_name, 'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, "whitespace characters removed")
print(num_removals, "out of", num_total_chars, "characters removed")
print('Percentage of data lost:',
      int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file', new_file_name)
