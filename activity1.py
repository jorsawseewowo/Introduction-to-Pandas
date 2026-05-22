import pandas as pd
import numpy as np

family_members = {'name': ['Nathan', 'Leonn', 'Baim', 'Zia', 'Sovann', 'Chris', 'Gabby', 'Sunny', 'Cathleen', 'James'],
                  'family members':[5, 6, 12, 29, 47, 15, 12, 9, 10, 19],
                  'siblings': [1, 1, 2, 2, 2, 2, 0, 0, 1, 0],
                  'gender': ['boy', 'boy', 'boy', 'girl', 'boy', 'boy', 'girl', 'boy', 'girl', 'boy']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(family_members , index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())