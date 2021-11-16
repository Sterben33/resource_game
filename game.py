def get_index_of_worst_proportion(target: list, current: list, tonnage: int) -> int:
    _current = [c/tonnage for c in current]
    if target == _current:
        return -1
        
    ratio = []
    for t, c in zip(target, _current):
        ratio.append(t-c)
    # print(ratio)
    return ratio.index(max(ratio))
    

def get_tonnage_of_resource(resources: list, tonnage: int) -> list:
    s = sum(resources)
    if s <= tonnage:
        return resources

    result = []
    percents = []
    for res in resources:
        percents.append(res/s)
        result.append(int((res/s)*tonnage))

    while sum(result) < tonnage:
        index = get_index_of_worst_proportion(percents, result, tonnage)
        if index == -1:
            result[percents.index(max(percents))] += 1
        else:
            result[index] += 1
    return result


print(get_tonnage_of_resource([100, 300, 200], 120))
print(get_tonnage_of_resource([100, 300, 200], 1))
print(get_tonnage_of_resource([100, 20, 3, 3, 0], 123))
print(get_tonnage_of_resource([1, 2, 3, 4], 0))
print(get_tonnage_of_resource([333, 333, 333], 998))
print(get_tonnage_of_resource([3, 3, 3, 3], 1))