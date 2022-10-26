import json
from unicodedata import category
import matplotlib.pyplot as plt

x = open('Desktop/CSCI40/dataset3.json')
dataset3=json.load(x)

categy = {"Industrial":0, "Land Use":0,"Livestock":0,"Electric Power":0}

for i in dataset3['data']:
    for key in categy:
        if key==i[14]:
            categy[key] +=1


print(categy)



# Data for plotting
x = categy.keys()
y = categy.values()

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='category of industires', ylabel='number of industry counted in the survey',
       title='counting the number of industry analyzed in the document')
ax.grid()

fig.savefig("test.png")
plt.show()