"""
File WordCount.py

Program to count the number of occurrences of a word
in a textfile.
"""


def getFile():
    """
    Returns the file name and associated file object for reading the
    file  as tuple of the form (file_name, input_file).
    """
    input_file_opened = False
    while not input_file_opened:
        try:
            #file_name = input('Enter input file name (with extension): ')
            file_name = "1984.txt"
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print('Unable to open input file, please reenter')
    return (file_name, input_file)


def countWords(input_file, search_word):
    """
    Returns the number of occurrences
    of search_word in the provided input_file object.
    """
    num_occurrences = 0
    word_delimiters = (' ', ',', ';', ':', '.', '\n',
                       '"', "'", '(', ')')
    search_word_len = len(search_word)
    for line in input_file:
        line = line.lower()  # convert to lower case characters.
        end_of_line = False
        begin_of_line = True  # the begin of line counts as a word_delimiter
        while not end_of_line:
            # print('>' + line.strip() + '<')
            try:
                found_search_word = False
                # throws ValueError if not found
                index = line.index(search_word)
                if index == 0:
                    # Only valid case for 'index == 0' is at begin of line.
                    # In the middle of a line, line[index-1] must be a delimiter. If not,
                    # the word lacks a LEFT delimiter and we're in the middle of a
                    # word, for example at the second 'foo' in 'foofoo' when counting
                    # 'foo'. Thus, index==0 is not possible in the middle of a line.
                    if begin_of_line and line[search_word_len] in word_delimiters:
                        found_search_word = True
                elif index > 0:
                    # All matching cases in middle of line must have 'index > 0',
                    # because line[index - 1] must be a delimiter! (So index=0 is
                    # invalid, because the LEFT delimiter is missing.)
                    if line[index - 1] in word_delimiters and \
                            line[index + search_word_len] in word_delimiters:
                        found_search_word = True
                if found_search_word:
                    # print('Pos:', index)
                    num_occurrences = num_occurrences + 1
                begin_of_line = False  # we moved past the begin of line
                line = line[index + search_word_len:]
            except ValueError:
                end_of_line = True
    return num_occurrences


file_name, input_file = getFile()
output_file = open(file_name[:-3] + 'wc', 'w')

word_delimiters = (' ', ',', ';', ':', '.', '\n',
                   '"', "'", '(', ')')

word_list = []
for l in input_file:
    bgn = 0
    end = 0
    while end < len(l):
        while end < len(l) and l[end] not in word_delimiters:
            end += 1
        word = l[bgn:end]
        if word != '' and word.lower() not in word_list:
            word_list.append(word.lower())
        end += 1
        bgn = end

input_file.seek(0)

word_list.sort()

for w in word_list:
    cnt = countWords(input_file, w)
    print(cnt)
    output_file.write(w + ": " + str(cnt) + '\n')
    input_file.seek(0)

output_file.close()
