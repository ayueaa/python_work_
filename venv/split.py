#coding=gbk
filename="qwq.text"
try:
    with open(filename)as file_object:
        contents=file_object.read()
except FileNotFoundError:
    msg="sorry,the file "+filename+" does not exist."
    print(msg)
else:
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+"words")