# IN last chapter we've seen about some methods for using in files....


# FOr reading a file first we need to open a file....
# After opening the file we need to read it with read keyword 
# file1 = open('16th_sample_text_file.txt') 
# content = file1.read()
# print(content)

# # It is a good practice to close a file after opening it with colse keyword....
# file1.close()




# And the second Argument of OPEN IS The type of opening a file as we've seen some types in last chapter....
# As we also seen that read is default we can change it to + , W, X, B etc...
# file1 = open('16th_sample_text_file.txt','r')
# content = file1.read()
# print(content)
# file1.close()



# Line we can even read a text file with binary.....
# file1 = open('16th_sample_text_file.txt','rb')
# content = file1.read()
# print(content)
# file1.close()




# We can also Access the file content with indexing.....
# file1 = open('16th_sample_text_file.txt','rt')
# # content = file1.read(10)
# # If we try to give a high value even our file don't have , (it will print whole character's persent in the file)
# content = file1.read(10000)
# print(content)
# file1.close()








# If we want to read A file Line by line We can use for loops. For it....
# file1 = open('16th_sample_text_file.txt','r')


# for line in file1:
#     # print(line, end="")
#     print(line, )

# file1.close()






# If we nees to read a line we can use readline.........
# file2 = open('16th_sample_text_file.txt', 'rt')
# # Read line print a single line and if we try to print it again it will print another line
# print(file2.readline())
# print(file2.readline())

# file2.close







# If we want single lines print in a list we can use readlines function it is diffrent to readline...
# file2 = open('16th_sample_text_file.txt', 'rt')
# print(file2.readlines())
# file2.close()












# WRITING AND APPENDING IN A FILE....


# Writing in a file (if we don't have a particaular file name it will also create that name file....)
# NOt just txt file we can even write another typr of files....
# file1 = open('16th_written_file.txt',"w")
# # file1.write("THIS IS A FILE CREATED WITH FILE.WRITE WRITE MODE.... OF 16TH CHAPTER...")
# # And we've already learned that if we write in a file it will remove the data present in it....
# file1.write("This text is written for checking if a file content can be changed after writing in a file...")
# file1.close()









# If we don't want to lose our old content present in the file we can use append.....

# APpending A FILE...
# file1 = open('16th_written_file.txt',"a")
# file1.write("\nTHIS IS APPENDED TEXT")
# file1.close()










# If we want to Get the number of characters written with the newest command we can use below technique....
# file1 = open('16th_written_file.txt',"a")
# a = file1.write("\nTHIS TEXT IS AGAIN APPENDED")
# print(a)
# file1.close()








# REAding And adding......(r+) read and write both....
file1 = open('16th_written_file.txt',"r+")
print(file1.read())
file1.write("\nThank you")

file1.close()