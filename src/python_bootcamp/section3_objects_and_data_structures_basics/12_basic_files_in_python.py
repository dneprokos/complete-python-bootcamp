my_file = open('sample.txt')

'''
Hello this is a text file
this is the second line
this is the third line
'''
print(my_file.read())

my_file.seek(0)  # Reset cursor
all_file_content = my_file.read()
print(all_file_content)
my_file.seek(0)  # Reset cursor

# Read by lines
each_line = my_file.readlines()
my_file.seek(0)  # Reset cursor
print(each_line)  # ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line\n']
my_file.close()

# Read file and close automatically. Preferred
with open('sample.txt') as readme_file:
    contents = readme_file.read()

# Append mode - cursor always in the end
with open('sample2.txt', mode='a') as my_file2:
    my_file2.write('\nThis command was written from code')

# Write file - write new file or overrides old one
with open('new_file.txt', mode='w') as new_file:
    new_file.write('This file was created or override')
