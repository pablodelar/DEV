import pandas
import os

csv_files_path = '/Users/oihane/Documents/Pablo/Python/csvfiles/'
csv_file_organizations = 'organizations-100.csv'

# print(os.environ['HOME'])
# print(os.path.expandvars(os.environ['HOME']))


############################## Reading CSV files with pandas ##############################

# df = pandas.read_csv(csv_files_path + csv_file_organizations, index_col= 'Organization Id')
df = pandas.read_csv(csv_files_path + csv_file_organizations)

# print(type(df))
# print(type(df['Number of employees'][0]))

# print(df.head(10)) # To print the first 'n' lines of the data frame
# print(df.tail(10)) # To print the last 'n' lines of the data frame
# print(df.columns) # If the input file does NOT include column names -> Define a list 'headers' with the column names and run df.colums = headers
# print(df.dtypes) # To check data types
# print(df.describe(include='all')) # Returns a statistical summary
print(df.info())

# index = (df['Index'])
# for i in index:
#     print(type(i))


############################## Writing CSV files with pandas ##############################
'''
df = pandas.read_csv(csv_files_path + csv_file_organizations,
                     index_col = 'ID',
                     header = 0,
                     names = ['ID', 'Index', 'Company', 'URL', 'Country', 'Description', 'Year', 'Industry', 'No. of Employees'])
df.to_csv(csv_files_path + 'organizations-100_modified.csv')
'''