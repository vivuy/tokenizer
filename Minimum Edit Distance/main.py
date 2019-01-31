def initialize(source, target):
    source = source.lower()
    target = target.lower()

    d = [[0 for a in range(len(target) + 1)] for b in range(len(source) + 1)]
    for i in range(len(source) + 1):
        for j in range(len(target) + 1):
            d[i][0] = i
            d[0][j] = j

    compute(source, target, d)


def compute(source, target, d):
    for j in range(1, len(target) + 1):
        for i in range(1, len(source) + 1):
            if source[i - 1] == target[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min([d[i][j - 1] + 2, d[i - 1][j] + 1, d[i - 1][j - 1] + 3])
    # print_table(d)
    get_path(source, target, d)


def print_table(d):
    for i in range(len(d)):
        print(d[i])


def get_path(source, target, d):
    path = ""
    i = len(source)
    j = len(target)
    new_source = ""
    new_target = ""

    while not (i == 0 and j == 0):
        if (i > 0 and j > 0) and (source[i - 1] == target[j - 1]):
            path += "M"
            new_source += source[i - 1]
            new_target += target[j - 1]
            i -= 1
            j -= 1
        else:
            if i < 0 or j < 0:
                if i < 0:
                    num1 = 0
                    num2 = d[i][j - 1]
                    num3 = 0
                elif j < 0:
                    num1 = d[i - 1][j]
                    num2 = 0
                    num3 = 0
            else:
                num1 = d[i - 1][j]
                num2 = d[i][j - 1]
                num3 = d[i - 1][j - 1]

            minimum = min(num1, num2, num3)
            if minimum == num1:
                path += "D"
                new_source += source[i - 1]
                new_target += "-"
                i -= 1
            elif minimum == num2:
                path += "I"
                new_source += "-"
                new_target += target[j - 1]
                j -= 1
            elif minimum == num3:
                path += "S"
                new_source += source[i - 1]
                new_target += target[j - 1]
                i -= 1
                j -= 1

    print("Distance: " + str(d[len(source)][len(target)]))
    print("------------")
    print(new_source[::-1])
    print(path[len(path) - 1::-1])
    print(new_target[::-1] + '\n')


print()
initialize("naruto's son", "boruto's dad")
initialize("kumakain", "kumain")
initialize("levinstien", "levenshtein")
initialize("leviathan", "levenshtein")
initialize("ATGCATCCCATGAC", "TCTATATCCGT")
initialize("AGGCTATCACCTGACCTCCAGGCCGATGCCCACCTGG", "TAGCTATCACGACCGCGGTCGATTTGCCCGACGGTCC")

# ==============FOR FULL PTS
# Implement the base version (1-1-2-0 weighting) w/ backtrace discussed in class
# TODO: Include your thoughts in a write up and provide answers to the questions provided
# TODO: Report the answers (distance + alignment) to all test cases
# TODO: Play around with the weights / costs and include observations from experimentation in the write up

# ==============FOR BONUS PTS
# IMPLEMENT LOCAL ALIGNMENT FOR BONUS PTS
