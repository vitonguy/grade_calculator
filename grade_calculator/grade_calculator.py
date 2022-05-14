grades = [0, 0, 0, 0, 0]
classes = ['calculus', 'psychology', 'embedsys', 'chemistry', 'teaching']
ReportCard = [grades, classes]

from grade_calculator_functions import calc_portion, percentage

# calculus = 0, psychology = 1, embedsys = 2, chemistry = 3, teaching = 4
def check():
    c = int(input("What class grades do you want to see? ")) # get input for what class we're doing
    print(ReportCard[1][c], ": ", ReportCard[0][c])
    main()

# grade get's calculated into here
def calculate():
   a = int(input("What class are we calculating for? "))
   print(ReportCard[1][a])
   z = 0
   x = 0
   while z != 1:
       s = int(input("How many assignments are we working we with for this portion?"))
       b = calc_portion(s) #will get us that portion's grade
       e = percentage()
       z += e
       x += b*e
   ReportCard[0][a] = x # put into the report card
   main() # when finished calculating, return back to main to see the grade


def reportcard():
    print("All the grades are posted here: ")
    l = 0
    k = 0
    while k < 5:
        print(ReportCard[l][k])
        l = l +1
        print(ReportCard[l][k])
        if(l == 1):
            l = 0
        k = k + 1
        print("\n")
    main()
            
    
        
def main():
    b= int(input("""What do you want to do?
        1 - calculate my grade
        2 - see my grade for one class
        3 - see my entire report card
    """))
    if b == 1:
           calculate()
    if b == 2:
           check()
    if b == 3:
           reportcard()








        
