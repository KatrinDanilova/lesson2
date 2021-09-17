#student_scores = [15, 21, 4, 10, 40]
#for i in student_scores:
#    print(i)

# task 1
#integers = [10,9,8,7,6,5,4,3,2,1]
#for i in integers:
#    print(i+1)

# task 2
#str = input("Inter string: ")
#for i in str:
#    print(i)

# task 3

school = []

school_scores = {
    'school_class': '4A',
    'scores': [3,4,4,5,2]
}
school.append(school_scores)

school_scores = {
    'school_class': '4Б',
    'scores': [5, 4, 5, 4, 4]
}
school.append(school_scores)

school_scores = {
    'school_class': '4В',
    'scores': [3, 4, 2, 4, 4]
}
school.append(school_scores)


for i in school:
    print(f"{i.get('school_class')}: {round(sum(i.get('scores')) / len(i.get('scores')))}")
    
ls = []   
leng = 0 
for i in school:    
    ls = ls + i.get('scores')
    leng = leng + len(i.get('scores'))

print(f"Средний балл по школе составляет: {round(sum(ls) / leng)}")

