with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        line = line.rstrip()
        print(line)
        w.write(line)
