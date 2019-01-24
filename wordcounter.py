import re
from collections import Counter


def main():
    lines = [line.rstrip('\n') for line in open('S17 Text File.txt')]
    lines.pop(0)
    items = []

    for line in lines:
        result = re.findall(r'([\w+’()-]*)', line)
        for i in result:
            if len(i.strip()) > 0:
                items.append(i.strip())

    items = [re.sub(r'[()]', '', x) if '(' in x else x for x in items]
    items = [re.sub(r'’', '', x) if re.fullmatch(r'(.*?)’', x) is not None else x for x in items]
    items = [x.lower() for x in items]
    word_count_dict = Counter(items)

    print("Total words: " + str(len(word_count_dict)))
    print(word_count_dict)


main()
