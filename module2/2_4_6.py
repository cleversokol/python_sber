import os
import os.path
import shutil

## Print current directory
#print(os.getcwd())
## List all files in current directory
#print(os.listdir())
#
## Check if dir/file exists in FS
## Return True/False respectively
#print(os.path.exists("some/destination/here"))
#
## Check if path if a file/directory
#print(os.path.isfile("some/destination/here"))
#print(os.path.isdir("some/destination/here"))
#
## Change directory
#os.chdir("new/destination/path")
#
## Walk through all sub-directories recursively
## os.walk returns current dir path, list of directories inside, list of files inside
#for current_dirs, dirs, files in os.walk("."):
#    print(current_dirs, dirs, files)
#
## Copy file
#shutil.copy("source/destination", "target/destination")
#
## Copy entire directory
#shutil.copytree("source/destination", "target/destination")

#print(current_dirs[2:])

target = "main"
filename = "my_ans.txt"
#os.chdir(target)
with open(filename, "w") as w:
    for current_dirs, dirs, files in os.walk(target):
        #print(current_dirs, dirs, files)
        for file in files:
            if file.endswith('.py'):
                #path = current_dirs+"\\"+file
                print(current_dirs)
                w.write(current_dirs+"\n")
                break
                #print(path)
