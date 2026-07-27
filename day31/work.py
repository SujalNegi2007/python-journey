import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#Visual Style
sns.set_theme(style = 'whitegrid')

#Loading Dataset
data = pd.read_csv('titanic.csv')

#checking info
print('\n\nData Info')
print(data.info())
print('\n\nData Summary')
print(data.describe(include = 'all'))
print('\n\nMissing Data')
print(data.isnull().sum())

#cleaning data
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data.drop('Cabin', axis = 1, inplace = True)

#feature 1
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand = False)
rare_titles = ['Lady', 'Countess','Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
data['Title'] = data['Title'].replace(rare_titles, 'rare')
data['Title'] = data['Title'].replace(['Mlle', 'Ms'], 'Miss')
data['Title'] = data['Title'].replace('Mme', 'Mrs')

#feature 2
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

#feature 3
data['IsAlone'] = 0
data.loc[data['FamilySize'] == 1, 'IsAlone'] = 1

plt.figure(figsize = (8,5))
sns.barplot(x = 'Sex', y = 'Survived', data = data, palette = 'pastel')
plt.title('1. Survival Rate By Gender')
plt.ylabel('Survival By Probability')
plt.show()

plt.figure(figsize = (8,5))
sns.histplot(x = 'Age', y = 'Survived', data = data, palette = 'muted', multiple='stack', kde=True)
plt.title('2. Age Distribution Of Survivor And Non Survivor')
plt.ylabel('Survival Probability')
plt.show()

plt.figure(figsize = (8,5))
sns.barplot(x = 'Pclass', y = 'Survived', data = data, palette = 'pastel')
plt.title('3. Survival Rate By Pclass')
plt.ylabel('Survival By Probability')
plt.show()

plt.figure(figsize = (8,5))
sns.barplot(x = 'Title', y = 'Survived', data = data, palette = 'pastel')
plt.title('4. Survival Rate By Passenger Title')
plt.ylabel('Survival By Probability')
plt.show()

plt.figure(figsize = (8,5))
sns.barplot(x = 'IsAlone', y = 'Survived', data = data, palette = 'coolwarm')
plt.title('5. Survival Rate: Alone(1) Vs. With Family(0)')
plt.ylabel('Survival By Probability')
plt.xticks(ticks = [0,1], labels = ['With Family', 'Alone'])
plt.show()
