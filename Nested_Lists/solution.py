if __name__ == "__main__":
    members = []
    temp = set({})
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(score)
        student.append(name)
        members.append(student)
        temp.add(score)
    members.sort()
    temp.remove(min(temp))
    minValue = min(temp)
    for i in members:
        if (i[0] == minValue):
            print(i[1])