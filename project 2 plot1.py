
from cProfile import label
from turtle import width
import pandas as pd

df = pd.read_csv(r'2013-2019_Math_Test_Results_School_-_SWD_Ethnicity_Gender_Economic_Status_ELL_Total_of_All.csv')
print(df)




grades = {'4':0, '5':0, '6':0,'7':0}



for i in df['# Level 2']:
    for key in grades:
        if key==i:
            grades[key] +=1

print("grades=", grades)


terms = grades.keys()
counts = grades.values()




meanscore = {'4':0,'5':0, '6':0,'7':0}

for i in df['# Level 3']:
    for key in meanscore:
        if key==i:
            meanscore[key] +=1

print("meanscore=", meanscore)


terms2 = meanscore.keys()
counts2 = meanscore.values()






import matplotlib.pyplot as plt
import numpy as np
labels = ['score4', 'score5', 'score6', 'socre7']
width= 0.25
x = np.arange(len(labels))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, counts, width, label="Level 2 student")
rects2 = ax.bar(x + width/2, counts2, width,label="Level 3 student")

plt.ylabel("number of students")
ax.set_title('Number of students by level and score')
ax.set_xticks(x, labels)
ax.legend()



plt.show()
