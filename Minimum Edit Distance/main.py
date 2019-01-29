source = "bugs bunny"
target = "big chungus"

D = [[0 for j in range(len(target)+1)] for i in range(len(source)+1)]


def initialize():
    for i in range(len(source)+1):
        for j in range(len(target)+1):
            D[i][0] = i
            D[0][j] = j


def compute():
    for j in range(1, len(target)+1):
        for i in range(1, len(source)+1):
            if source[i-1] == target[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min([D[i][j-1] + 1, D[i-1][j] + 1, D[i-1][j-1] + 2])


def print_table():
    for i in range(len(D)):
        print(D[i])


def get_path():
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
            minimum = min(D[i-1][j], D[i][j-1], D[i-1][j-1])
            if minimum == D[i-1][j]:
                path += "D"
                new_source += source[i-1]
                new_target += "-"
                i -= 1
            elif minimum == D[i][j-1]:
                path += "I"
                new_source += "-"
                new_target += target[j - 1]
                j -= 1
            elif minimum == D[i-1][j-1]:
                path += "S"
                new_source += source[i-1]
                new_target += target[j - 1]
                i -= 1
                j -= 1
    print("Distance: " + str(D[len(source)][len(target)]))
    print("--------")
    print(new_source[::-1])
    print(path[len(target)::-1])
    print(new_target[::-1])


initialize()
compute()
get_path()
