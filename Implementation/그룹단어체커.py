N = int(input())
count = 0

for _ in range(N):
    char = list(input().strip())
    char_list = []
    lastest_char = ""
    check = 0

    for i in char:
        if i not in char_list:
            char_list.append(i)
            lastest_char = i
            continue

        if i == lastest_char:
            continue

        if i in char_list:
            check = 1
            break

    if check == 0:
        count += 1
print(count)