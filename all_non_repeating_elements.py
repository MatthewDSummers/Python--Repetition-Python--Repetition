# A function which eliminates every occurance of an item in a list if it is repeated
def all_non_repeating_elements(lst):
    if not lst:
        return None
    count = {}
    unique = []
    for x in lst:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    for k,v in count.items():
        if v == 1:
            unique.append(k)

    return unique
print (all_non_repeating_elements([1, 2, 3, 3, 3, "Repeated", "Repeated", "Not Repeated"]))
# output: [1, 2, 'Not Repeated']