# Smoking/Cancer Correlation Program

import math


def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (smoking_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    smoking_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4

    # prompt for file names and attempt to open files
    while ((not smoking_datafile_opened) or
           (not cancer_datafile_opened)) \
            and (num_attempts > 0):
        try:
            if not smoking_datafile_opened:
                file_name = input('Enter smoking data file name: ')
                smoking_datafile = open(file_name, 'r')
                smoking_datafile_opened = True

            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data file name: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

        except OSError:
            print('File not found:', file_name + '.', 'Please reenter\n')
            num_attempts = num_attempts - 1

    # if one or more files not opened, raise OSError exception
    if not smoking_datafile_opened or not cancer_datafile_opened:
        raise OSError('Too many attempts of reading input files')

    # return file objects if successfully opened
    else:
        return (smoking_datafile, cancer_datafile)


def readFiles(smoking_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects smoking_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (smoking_datafile, cancer_datafile).
    '''

    # init
    smoking_data = []
    cancer_data = []
    empty_str = ''

    # read past file headers
    smoking_datafile.readline()
    cancer_datafile.readline()

    # read data files
    eof = False

    while not eof:

        # read line of data from each file
        s_line = smoking_datafile.readline()
        c_line = cancer_datafile.readline()

        # check if at end-of-file of both files
        if s_line == empty_str and c_line == empty_str:
            eof = True

        # check if end of smoking data file only
        elif s_line == empty_str:
            raise OSError('Unexpected end-of-file for smoking data file')

        # check if at end of cancer data file only
        elif c_line == empty_str:
            raise OSError('Unexpected end-of-file for cancer data file')

        # append line of data to each list
        else:
            smoking_data.append(s_line.strip().split(','))
            cancer_data.append(c_line.strip().split(','))

    # return list of data from each file
    return (smoking_data, cancer_data)


def calculateCorrelation(smoking_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists smoking_data and cancer_data
    '''

    # init
    sum_smoking_vals = sum_cancer_vals = 0
    sum_smoking_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    # calculate intermediate correlation values
    num_values = len(smoking_data)

    for k in range(0, num_values):

        sum_smoking_vals = sum_smoking_vals + float(smoking_data[k][1])
        sum_cancer_vals = sum_cancer_vals + float(cancer_data[k][1])

        sum_smoking_sqrd = sum_smoking_sqrd +  \
            float(smoking_data[k][1]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd +  \
            float(cancer_data[k][1]) ** 2

        sum_products = sum_products + float(smoking_data[k][1]) *  \
            float(cancer_data[k][1])

    # calculate and display correlation value
    numer = (num_values * sum_products) - \
            (sum_smoking_vals * sum_cancer_vals)

    denom = math.sqrt(abs(
        ((num_values * sum_smoking_sqrd) - (sum_smoking_vals ** 2)) *
        ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2))
    ))

    return numer / denom


# ---- main

# program greeting
print('This program will determine the correlation (-1 to 1) between')
print('data on cigarette smoking and incidences of lung cancer\n')

try:
    # open data files
    smoking_datafile, cancer_datafile = openFiles()

    # read data
    smoking_data, cancer_data = readFiles(smoking_datafile, cancer_datafile)

    # calculate correlation value
    correlation = calculateCorrelation(smoking_data, cancer_data)

    # display correlation value
    print('r_value = ', correlation)

except OSError as e:
    print(e)
    print('Program terminated ...')
