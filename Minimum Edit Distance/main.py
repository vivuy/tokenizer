source = "levinstien"
target = "levenshtein"

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

    while i != 0 and j != 0:
        if D[i][j] == D[i-1][j-1]:
            path += "M"
            i -= 1
            j -= 1
        else:
            if j < 0:
                path += "D"
                i -= 1
            elif i < 0:
                path += "I"
                j -= 1
            else:
                minimum = min(D[i-1][j], D[i][j-1], D[i-1][j-1])
                print(D[i-1][j], D[i][j-1], D[i-1][j-1])
                print(minimum)
                if minimum == D[i-1][j]:
                    path += "D"
                    j -= 1
                elif minimum == D[i][j-1]:
                    path += "I"
                    i -= 1
                elif minimum == D[i-1][j-1]:
                    path += "S"
                    i -= 1
                    j -= 1
    return print(path[::-1]);


initialize()
compute()
print_table()
get_path()
print(D[len(source)][len(target)])