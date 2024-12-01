file = open("input.txt", "r")
left_list = []
right_list = []
while data := file.readline():
    left = True
    x = data.split(" ")
    for i in x:
        try:
            if left:
                left_list.append(int(i))
                left = False
            else:
                right_list.append(int(i))
                left = True
        except Exception:
            continue

left_list.sort()
right_list.sort()

sum = 0
for i in range(0, left_list.__len__()):
    sum += max(left_list[i], right_list[i]) - min(left_list[i], right_list[i])

print(sum)
