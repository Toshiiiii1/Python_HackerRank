if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)

    temp = max(arr)
    while (arr.count(temp) != 0):
        arr.remove(temp)
        
    print(max(arr))