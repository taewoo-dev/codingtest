def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]-1
        j = command[1]
        k = command[2]-1
        array_1 = array[i:j]
        array_1.sort()
        answer.append(array_1[k])
    return answer