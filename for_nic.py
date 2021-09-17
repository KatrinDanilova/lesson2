my_lists=[
    {"school_class":"4А","scores":[3, 4, 4, 5, 2]},
    {"school_class":"4Б","scores":[5, 4, 5, 4, 4]},
    {"school_class":"4c","scores":[3, 4, 2, 4, 4]}
]

def Average(lst):
    return sum(lst) / len(lst)

school_score=[]

for i in my_lists:
    print(f"Class name: { i['school_class'] } score: {Average(i['scores'])}")
    school_score.append(Average(i['scores']))

print(f'School_score {Average(school_score)}')