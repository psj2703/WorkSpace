def my_swap(words, x, y):

    words[x], words[y] = words[y], words[x]
    # temp = words[x]
    # words[x] = words[y]
    # words[y] = temp
    pass

def my_sort(words):
    for left in range(len(words) - 1):
        for right in range(left + 1, len(words)):
            if words[left] > words[right]:
                my_swap(words, left, right)

    return words

input_list = ['hello', 'world', 'korea', 'japan', 'america', 'russia', 'china', 'ukrain', 'france', 'germany']

result = my_sort(input_list)

print(result)