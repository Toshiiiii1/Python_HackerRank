if __name__ == "__main__":
    n = int(input())
    lst = []
    for _ in range(1, n+1):
        command, *value = input().split()
        if (command == "print"):
            print(lst)
            lst = []
        
        elif (command == "insert"):
            lst.insert(int(value[0]), value[1])
            
        elif (command == "remove"):
            lst.remove(value[0])
            
        elif (command == "append"):
            lst.append(value[0])
            
        elif (command == "sort"):
            lst.sort()
            
        elif (command == "pop"):
            lst.pop()
            
        elif (command == "reverse"):
            lst.reverse()