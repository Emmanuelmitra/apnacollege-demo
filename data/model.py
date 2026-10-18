
df=pd.read_csv('data.csv')
df.head()
df.info()
df.isnull().sum()
df.fillna(df.mean(), inplace=True)
df.describe()
