from sklearn model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston

df=pd.read_csv('data.csv')
df.head()
df.info()
df.isnull().sum()
df.fillna(df.mean(), inplace=True)
df.describe()
