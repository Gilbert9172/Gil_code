def solution(scores):

    lst = []
    for j in range(len(scores)):
        new = [i[j] for i in scores]
        lst.append(new)

    for idx,array in enumerate(lst):
        if array[idx] == max(array) and array.count(max(array))==1:
                array.remove(array[idx])
        elif array[idx] == min(array) and array.count(min(array))==1:
                array.remove(array[idx])

    test = []
    for i in lst:
        avg = sum(i)/len(i)
        # test.append(avg)
        if avg >= 90:
            test.append("A")
        if 80<= avg < 90:
            test.append("B")
        if 70 <= avg < 80:
            test.append("C")
        if 50 <= avg < 70:
            test.append("D")
        if avg < 50:
            test.append("F")
    answer = str("".join(test))
    return answer