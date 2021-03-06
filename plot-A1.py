import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_excel (r'./A1_G4.xlsx')
df=df.iloc[16:, 2:6]
print (df)