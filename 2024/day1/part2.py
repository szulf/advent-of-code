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

similarity = 0
for i in left_list:
    similarity += i * right_list.count(i)

print(similarity)
