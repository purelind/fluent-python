import sys
import re
import collections

WORD_RE = re.compile("\w+")

index = collections.defaultdict(list)
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)

#: 1. Calls list() to create a new list.
#: 2. Inserts the list into dd using "new-key" as key.
#: 3. Return a reference to that list.

#: dd[k] will call the defatul_factory to create a default value.
#: dd.get(k) still returns None.



for word in sorted(index, key=str.upper):
    print(word, index[word])
