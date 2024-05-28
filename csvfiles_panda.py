import pandas
import os

csv_files_path = '/Users/oihane/Documents/Pablo/Python/csvfiles/'
csv_file_organizations = 'organizations-100.csv'

# print(os.environ['HOME'])
# print(os.path.expandvars(os.environ['HOME']))

df = pandas.read_csv(csv_files_path + csv_file_organizations)
print(type(df))