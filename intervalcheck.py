
def is_interval(interval_1,interval_2) -> bool:
    if interval_1[0] > interval_2[0] and interval_1[1] < interval_2[1]:
        return True
    return False
if __name__ == "__main__":
    interval = [[2, 5], [3, 8], [2, 4], [1, 10]]
    interval_map = [0]*len(interval)
    print(interval_map)
    for i in range(len(interval)):
        for j in range(len(interval)):
            if is_interval(interval[i],interval[j]):
                interval_map[i] = True
                break
            interval_map[i] = False
    print((interval_map))
