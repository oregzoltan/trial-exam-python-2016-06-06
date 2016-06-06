# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def count_a(name):
    try:
        f = open(name)
        text = f.read()
    except:
        return 0
    f.close()
    counter = 0
    for i in text:
        if i == 'a':
            counter += 1
    return counter

print(count_a('test.txt'))
