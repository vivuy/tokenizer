def initialize(source, target):
    source = source.lower()
    target = target.lower()

    d = [[0 for a in range(len(target) + 1)] for b in range(len(source) + 1)]
    for i in range(len(source)+1):
        for j in range(len(target)+1):
            d[i][0] = i
            d[0][j] = j

    compute(source, target, d)


def compute(source, target, d):
    for j in range(1, len(target)+1):
        for i in range(1, len(source)+1):
            if source[i-1] == target[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min([d[i][j-1] + 1, d[i-1][j] + 1, d[i-1][j-1] + 2])
    get_path(source, target, d)


# def print_table():
#     for i in range(len(D)):
#         print(D[i])


def get_path(source, target, d):
    path = ""
    i = len(source)
    j = len(target)
    new_source = ""
    new_target = ""

    while not (i == 0 and j == 0):
        if source[i-1] == target[j-1]:
            path += "M"
            new_source += source[i-1]
            new_target += target[j-1]
            i -= 1
            j -= 1
        else:
            minimum = min(d[i-1][j], d[i][j-1], d[i-1][j-1])
            if minimum == d[i-1][j]:
                path += "D"
                new_source += source[i-1]
                new_target += "-"
                i -= 1
            elif minimum == d[i][j-1]:
                path += "I"
                new_source += "-"
                new_target += target[j - 1]
                j -= 1
            elif minimum == d[i-1][j-1]:
                path += "S"
                new_source += source[i-1]
                new_target += target[j - 1]
                i -= 1
                j -= 1

    print("Distance: " + str(d[len(source)][len(target)]))
    print("------------")
    print(new_source[::-1])
    print(path[len(path)-1::-1])
    print(new_target[::-1] + '\n')


print()
initialize("bugs bunny", "big chungus")
initialize("naruto's son", "boruto's dad")
initialize("kumakain", "kumain")
initialize("levinstien", "levenshtein")
initialize("leviathan", "levenshtein")
initialize("ATGCATCCCATGAC", "TCTATATCCGT")
initialize("AGGCTATCACCTGACCTCCAGGCCGATGCCCACCTGG", "TAGCTATCACGACCGCGGTCGATTTGCCCGACGGTCC")
