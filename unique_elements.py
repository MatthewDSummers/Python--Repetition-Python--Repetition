# A function which eliminates only repeated occurances of an item in a list
def unique_elements(lst):
    if not lst:
        return None
    unique = []
    for x in lst:
        if x not in unique:
            unique.append(x)
    return unique
print (unique_elements([1, 2, 3, 3, 3, "Repeated", "Repeated", "Not Repeated"]))
# output: [1, 2, 3, 'Repeated', 'Not Repeated']