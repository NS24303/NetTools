# intial method to read a file is. If using this method should include
#f.close()

#f = open("show_version.txt")
#output = f.read()

# A better way to do the above which automatically closes the file.
# considered better python
with open("show_version.txt") as f:
    output=f.read()

# write a file, not each time this is run it will overwrite the old file contents
# could change this with the append function mode="a"
f = open("new_file.txt", mode="w")
f.write ("Add some random text to the new_file.txt")
# The flush method will flush (save) the contents to the file.
f.flush()

# print the type of file
print("\n" ,f, "\n\n")
# print the output of the whole file
print(output, "\n\n")
# output the file removing new lines.
print (output.splitlines())

# read saingle line at a time
#line = f.readline()
# read all lines
#lines = f.readlines()

# close the file at the end
#f.close()
# If needed to start the file again use the seek method.
#output2 = f.seek(0)
