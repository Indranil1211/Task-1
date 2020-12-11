a=str(input("Input the filename: "))
if a[-5:]==".java":
    print("The extension of the file is: 'Java' ")
elif a[-2:]==".c":
    print("The extension of the file is: 'C' ")
elif a[-3:]==".cc" or a[-4:]==".cpp" or a[-4:]==".cxx" :
    print("The extension of the file is: 'C++' ")
elif a[-3:]==".py":
    print("The extension of the file is: 'Python' ")
else:
    print("The extension of the file does not exist.")
