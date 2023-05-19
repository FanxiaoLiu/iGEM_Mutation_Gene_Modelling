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

# importing library sympy
from sympy import symbols, Eq, solve
  
# defining symbols used in equations
# or unknown variables
alpha1,alpha2,alpha3,beta1,y2,n3,y1,beta2,beta3,n1,n2,y3 = symbols('alpha1,alpha2,alpha3,beta1,y2,n3,y1,beta2,beta3,n1,n2,y3')
  
# defining equations
eq1 = Eq((alpha1 + beta1*0 - y1*0 - n1*0), 8)
eq2 = Eq((alpha2 + y2*0 - beta2*0 - n2*0), 0.5)
eq3 = Eq((alpha3 + n3*0 - beta3*0 - y3*0), 0.5)

eq4 = Eq((alpha1 + beta1*1 - y1*0 - n1*0), 29)
#eq5 = Eq((alpha2 + y2*0 - beta2*1 - n2*0), 0)
#eq6 = Eq((alpha3 + n3*0 - beta3*1 - y3*0), 0)

eq7 = Eq((alpha1 + beta1*0 - y1*1 - n1*0), 2)
eq8 = Eq((alpha2 + y2*1 - beta2*0 - n2*0), 10)
#eq9 = Eq((alpha3 + n3*0 - beta3*0 - y3*0), 1)

eq10 = Eq((alpha1 + beta1*0 - y1*0 - n1*1), 4)
#eq11 = Eq((alpha2 + y2*0 - beta2*0 - n2*0), 0)
eq12 = Eq((alpha3 + n3*1 - beta3*0 - y3*0), 16)

eq13 = Eq((alpha1 + beta1*1 - y1*1 - n1*0), 12)
eq14 = Eq((alpha2 + y2*1 - beta2*1 - n2*0), 5)
#eq15 = Eq((alpha3 + n3*0 - beta3*0 - y3*0), 0)

eq16 = Eq((alpha1 + beta1*1 - y1*0 - n1*1), 28)
#eq17 = Eq((alpha2 + y2*0 - beta2*0 - n2*0), 0)
eq18 = Eq((alpha3 + n3*1 - beta3*1 - y3*0), 11.5)

#eq19 = Eq((alpha1 + beta1*0 - y1*0 - n1*0), 0)
eq20 = Eq((alpha2 + y2*1 - beta2*0 - n2*1), 8)
eq21 = Eq((alpha3 + n3*1 - beta3*0 - y3*1), 11)

eq22 = Eq((alpha1 + beta1*1 - y1*1 - n1*1), 8.5)
eq23 = Eq((alpha2 + y2*1 - beta2*1 - n2*1), 4)
eq24 = Eq((alpha3 + n3*1 - beta3*1 - y3*1), 12)

#a_signal = alpha1 + beta1*x1 - y1*x2 - n1*x3 - 8
#b_signal = alpha2 + y2*x2 - beta2*x1 - n2*x3 - 0.5
#c_signal = alpha3 + n3*x3 - beta3*x1 - y3*x2 - 0.5


big_array[0].insert(0,"A")
big_array[1].insert(0,"B")
big_array[2].insert(0,"C")
big_array[3].insert(0,"AB")
big_array[4].insert(0,"AC")
big_array[5].insert(0,"BC")
big_array[6].insert(0,"ABC")

#Creating graphs

df = pd.DataFrame(big_array,columns=["Test Groups",'Levels of A','Levels of B','Levels of C'])

print(df)

bp = sns.barplot(data=df.melt(id_vars='Test Groups',
                                  value_name='Editing Levels', var_name='Levels of...'),
            x='Test Groups', y='Editing Levels', hue='Levels of...')

plt.show()