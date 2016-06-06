# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def double_elements(list):
    try:
        for i in range(len(list)):
            list[i] *= 2
    except:
        return 'Parameter is not a list'
    return list

print(double_elements([1, 2, 3, 'sdg']))
print(double_elements(23))
