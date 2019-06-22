# Day 16 Cloud Class
ELB Elastic Load Balancer is our today's topic.
*   ```Load Balancer``` is a system which distributes traffic of a single website to multiple machines or instances.
*   ```Elastic Load Balancer``` It is similar to Load Balancer but it can add new servers on demand by cloning a copy of an existing server.

# Machine Learning Class
*   To draw a scatter chart we use ```plt.scatter()``` 
*   To draw a pie chart we use ```plt.pie()```
```py
plt.pie(runs,labels=player,explode=exp,shadow=True,autopct='%1.1%')
plt.grid(color='green')
plt.show()
```
*   CSV (Comma Seperated Values)
*   Pandas is a liberary used for data processing.
*   To read a csv file in pandas
*   Here data readed by pandas is called as dataframe.
*   Data Frame is a structure developed by pandas it converts any type of data to pandas data frame using read_csv.
```py
import pandas as pd
df = pd.read_csv('com.csv')
df1 = pd.read_csv('http://13.234.66.67/summer19/datasets/com.csv')
```
*   Now if I need to see the structure of use the function df.info()
```
df.info()
```
*   Now If I need to print all the data
```
print(df)
```
*   Now If I say I just need top 3 rows then use head function
```
df.head(3)
```
*   Now If I say I just need bottom 3 rows then use tail function
```
df.tail(3)
```
*   Now if we need a specific column or such you can specify  the column name in df
```py
df['Name']
```
*   For selecting rows and columns  we have a function called
```
df.iloc[0:,0]
```
*   To get max min avg mean value from a column
```py
df['Salary'].max()
df['Salary'].min()
df['Salary'].mean()
df['Salary'].avg()
```
## Machine Learning Categories
*   Supervised Learning
*   Unsupervised Learning
*   Reinforcement Learning
    *   This is for Game Automation, Self Driving Cars

