def is_anagramm(str_1,str_2) -> bool:
    char_size = 256
    count_1 = [0]*char_size
    count_2 = [0]*char_size

    for char in str_1:
        count_1[ord(char)] += 1
    for char in str_2:
        count_2[ord(char)] += 1

    if(len(str_1) != len(str_2)):
        return False
    else:
        for i in range(len(count_1)):
            if count_1[i] != count_2[i]:
                return False
    return True

print(is_anagramm("thang","gthan"))

def agram(str1,str2):
    arr1 = []
    arr2 = []
    if len(str1) != len(str2):
        return False
    else:
        for char in range(len(str1)):
            arr1.append(ord(str1[char]))
            arr2.append(ord(str2[char]))
        if sum(arr1) == sum(arr2):
            return True
        else:
            return False

print(agram("thang","gthanaaa"))
