#source = open("test.txt")
#contents = source.readlines()
#source.close()
#contents.reverse()
#
#with open("test_copy.txt", "w") as w:
#    for line in contents:
#         w.write(line.rstrip() + "\n")

# Without last unnecessary '\n' symbol
# Original internet-version
#filename = "test.txt"
#filename2 = "test_copy.txt"
#file = open(filename,'r')
#lines = file.read().split("\n")
#file.close()
#file = open(filename2, "w")
#file.write("\n".join(lines[::-1]))
#file.close()

filename = "dataset_20659_4.txt"
filename2 = "output.txt"
with open(filename,'r') as file:
    lines = file.read().split("\n")

with open(filename2, "w") as file:
    file.write("\n".join(lines[::-1]))
