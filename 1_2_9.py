objects = [1, 2, 1, 2, 3, 3]

ans = 0
result=[]
for obj in objects: # доступная переменная objects
    print("------------------")
    print("obj = ",obj)
    if len(result) == 0:
        print("if")
        ans += 1
        result.append(obj)
    else:
        print("else")
        for i in result:
            print("i = ",i)
            print("obj = ", obj)
            if not(obj is i):
                ans += 1
                result.append(obj)
                break
    print("objects = ", objects)
    print("result = ", result)
print(ans)