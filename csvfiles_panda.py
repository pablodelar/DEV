import pandas
import os

csv_files_path = '/Users/oihane/Documents/Pablo/Python/csvfiles/'
csv_file_organizations = 'organizations-100.csv'

# print(os.environ['HOME'])
# print(os.path.expandvars(os.environ['HOME']))


############################## Reading CSV files with pandas ##############################

df = pandas.read_csv(csv_files_path + csv_file_organizations, index_col= 'Organization Id')

# print(type(df))
# print(type(df['Number of employees'][0]))

# print(df)


############################## Writing CSV files with pandas ##############################

df = pandas.read_csv(csv_files_path + csv_file_organizations,
                     index_col = 'ID',
                     header = 0,
                     names = ['ID', 'Index', 'Company', 'URL', 'Country', 'Description', 'Year', 'Industry', 'No. of Employees'])
df.to_csv(csv_files_path + 'organizations-100_modified.csv')