import csv
import os

csv_files_path = '/Users/oihane/Documents/Pablo/Python/csvfiles/'
csv_file_people = 'people-100.csv'

############################## Reading CSV files with csv ##############################
'''
with open(csv_files_path + csv_file_people, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    # print(type(csv_reader))
    for row in csv_reader: # Each row returned by the reader is a list of String elements containing the data found by removing the delimiters
        # print(type(row))
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    # for row in csv_file:
    #     print(type(row))
'''

############################## Reading CSV files into a Dictionary with csv ##############################

l = ['Index','User Id','First Name','Last Name','Sex','Email','Phone','Date of birth','Job Title']

with open(csv_files_path + csv_file_people, 'r') as csv_file:
    # for line in csv_file:
    #     print(type(line))
    # print(type(csv_file))
    csv_reader = csv.DictReader(csv_file)
    print(type(csv_reader)) # csv.DictReader
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(row)
            # print(f'Column names are {", ".join(row)}') # TEST this on IDLE
            line_count += 1
        # print(f'{row['First Name']}')
        # print(type(row)) # dict
        line_count += 1
    print(f'Processed {line_count} lines.')


############################## Writing CSV files with csv ##############################
'''
with open('output.csv', mode = 'w') as output_file:
    output_writer = csv.writer(output_file, delimiter= ',', quotechar= '"', quoting = csv.QUOTE_MINIMAL)
    # Write headers first
    output_writer.writerow(['Full Name', 'Dept', 'BirthMonth'])
    # Write data rows now
    output_writer.writerow(['Pablo del Arco Rodriguez', 'IT, Software Development', 'June'])
    output_writer.writerow(['Sergio Pelaez Sanchez', 'Accounting', 'December'])
'''

############################## Writing CSV files into a Dictionary with csv ##############################
'''
fieldnames = ['Name', 'Dept', 'BirthMonth']

with open('output_dictwriter.csv', mode = 'w') as output_file:
    output_writer = csv.DictWriter(output_file, fieldnames=fieldnames) # Unlike DictReader, the fieldnames parameter is required when writing a dictionary

    output_writer.writeheader()
    output_writer.writerow({'Name': 'Johnny Lawrence', 'Dept': 'Cobra Kai', 'BirthMonth': 'March'})
    output_writer.writerow({'Name': 'Daniel Larusso', 'Dept': 'Miyagi-Do', 'BirthMonth': 'July'})
'''