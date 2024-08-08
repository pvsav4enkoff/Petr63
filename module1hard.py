grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
journal1=[]
journal1 = sorted(students)

journal = {}
i=0
while i<len(journal1):
    journal[journal1[i]]=sum(grades[i])/len(grades[i])
    i+=1


print(journal)

