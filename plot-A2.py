import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_excel (r'./A2_G4.xlsx')
frame=df.iloc[16:, 1:4]
frame.columns=['Date','PM2.5','PM10']
# Rows with invalid data are dropped
frame=frame[frame['PM10']!="None"]
frame=frame[frame['PM2.5']!="None"]
# Rows with None values can be replaced with 0 
frame.replace('None', 0, inplace=True)
frame=frame.astype({'PM2.5':float,'PM10':float})
print(frame)

frame.plot(x='Date',y='PM10', kind="line")
plt.show()
frame.plot(x='Date',y='PM2.5', kind="line")
plt.show()
print(frame)
print (PM10)