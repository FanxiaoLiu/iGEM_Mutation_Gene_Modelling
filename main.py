import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

a = [29,0,0]
b = [2,10,0]
c = [4,0,16]
ab = [12,5,0]
ac = [28,0,11.5]
bc = [0,8,11]
abc = [8.5,4,12]
big_array = [a,b,c,ab,ac,bc,abc]
error = [8,0.5,0.5]


for x in big_array:
    for y in range(len(x)):
        x[y] -= error[y]
        if x[y] < 0:
            x[y] = 0

big_array[0].insert(0,"A")
big_array[1].insert(0,"B")
big_array[2].insert(0,"C")
big_array[3].insert(0,"AB")
big_array[4].insert(0,"AC")
big_array[5].insert(0,"BC")
big_array[6].insert(0,"ABC")

df = pd.DataFrame(big_array,columns=["Test Groups",'Levels of A','Levels of B','Levels of C'])

print(df)

bp = sns.barplot(data=df.melt(id_vars='Test Groups',
                                  value_name='Editing Levels', var_name='Levels of...'),
            x='Test Groups', y='Editing Levels', hue='Levels of...')

plt.show()