import bisect

#: bisect_right returns an insertion point after the existing item, and
bisect_left returns the position of the existing item
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

def main():
    pass

if __name__ == '__main__':
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
