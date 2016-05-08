import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#np
arr = np.array([1,2,3,4,5])
print(arr)
#print(np.std(arr))

tab10n5 = np.random.randn(10,5)
#print(tab10n5)

# Series
s = pd.Series([1,3,5,np.nan,6,8])
#print(s)

dates = pd.date_range('20160101', periods=10)
#print(dates)

df = pd.DataFrame(tab10n5, index=dates, columns=['A','B','C','D','E'])
#print(df)

#print(df.head())

#print(df.index)
#print(df.columns)
#print(df.values)

#print(df.describe())

#Selection
#print(df['A'])
#print(df[0:3])

# label location
#print(df.loc[:,['A','B']])
#print(df.loc['20160102':'20160104',['A','B']])

#print(df.iloc[3])
#print(df.iloc[[1,2,4],[0,2]])
#print(df.iloc[1:3,:])

#Cond
#print(df[df.D > 0])


# Operations
print('\n')
s = pd.Series([1,2,3,np.nan,5,6,7,8,9,10], index=dates).shift(2)
#print(s)


#print(df.sub(s, axis='index'))

#Joins

left = pd.DataFrame({'key': ['a', 'b', 'c'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key': ['a', 'c', 'd'], 'rval': [4, 5, 6]})
#print(left)
#print(right)
#print(pd.merge(left, right, on='key'))

#Group
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                      'B' : ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                      'C' : np.random.randn(8),
                      'D' : np.random.randn(8)})

#print(df.groupby('A').sum())
#print(df.groupby(['A','B']).sum())
