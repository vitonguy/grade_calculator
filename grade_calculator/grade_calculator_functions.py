def percentage():
    e = int(input("Percentage: "))
    e = e/100
    return e


def calc_portion(work):
    d = 0
    howmany = 0
    print("When finished, type 0")
    b = float(input("Grades: "))
    # while there are assignments to put in
    for n in range(work):
        d += b
        b = float(input())
        
    b = d/work #gets the average of the assignment
    return b
