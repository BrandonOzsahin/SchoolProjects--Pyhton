# 1
def test_print():
    print("This is a test statement.")


if __name__ == '__main__':
    test_print()


#
# 2
def list_set_length():
    items_list = [1, 2, 3, 4, 3, 2, 1]
    items_set = {1, 2, 3, 4, 3, 2, 1}  # does not count duplicates unlike list
    print(len(items_list))
    print(len(items_set))  # prints lengths


if __name__ == '__main__':
    list_set_length()


#
# 3
def set_intersect():
    S = {1, 2, 3, 4}
    T = {3, 4, 5, 6}
    intersection = {i for i in S if i in T}  # assuming you want the dupped values
    print(intersection)


if __name__ == '__main__':
    set_intersect()


#
# 4
def three_tuples():
    S = {-4, -2, 1, 2, 5, 0}
    sum = {(i, j, k) for i in S for j in S for k in S if i + j + k == 0}
    print(sum)


if __name__ == '__main__':
    three_tuples()


#
# 5a
def dict_init():
    mydict = {'Neo': 'Keanu', 'Morpheus': 'Laurence', 'Trinity': 'Carrie-Anne'}
    print("Name:", mydict['Neo'])


# b dictionary cmprehensions
def dict_find(dlist, k):
    y = [x.get(k, 'Not Found') for x in dlist]
    return y


if __name__ == '__main__':
    mydict = [{'Neo': 'Keanu', 'Morpheus': 'Laurence', 'Trinity': 'Carrie-Anne'},
              {'Alpha': 'Omega', 'Charm': 'Farm', 'Fun': 'Bum'}, {'USA': 'America', 'CA': 'Canada', 'MX': 'Mexico'}]

    dict_init()  # for part a
    print(dict_find(mydict, 'Alpha'))  # for part b


#
# 6
def file_line_count():
    fileobject = open("stories_small.txt", "r")
    ####for line in fileobject:
    # this reads the entire file line by line
    # print (line)
    number_of_lines = len(open('stories_small.txt').readlines())
    print("\nnumber of lines:", number_of_lines)


if __name__ == '__main__':
    file_line_count()
#

# 7a
def make_inverse_index():
    d = {}
    ln = -1  # line number start
    for line in open('stories_small.txt', 'r'):
        #   print(line)
        ln += 1  # increments each line
        l = line.split()
        for word in l:
            # seperates words from .split
            if word not in d:  # adds the words in dictionary and appends it if not it does it in else, also increments occurance with d[word]
                d[word] = []
                d[word].append(1)
                d[word].append([ln])
            else:
                d[word][0] += 1
                d[word][1].append(ln)
    ld = list(d)
    print(d)  # This print shows number of occurances and where the lines are ex {2 - it appears twice, and [0,1] - appears in lines 0 and 1}
    return d
# part 7B
def or_search(inverseIndex, query):
    d = {}
    for line in inverseIndex:
        for l in query:
            if line == l:
                d.setdefault(line, [])
                d[line].append(inverseIndex[l])
                return d
# part 7C
def and_search(inverseIndex, query):
    d = {}
    for line in inverseIndex:
        for l in query:
            if line == l:
                d.setdefault(line, [])
                d[line].append(inverseIndex[l])
    return d

if __name__ == '__main__':
    make_inverse_index()
    print(or_search(make_inverse_index(), ['united', 'states']))
    print(and_search(make_inverse_index(), ['wall', 'street']))
#### end