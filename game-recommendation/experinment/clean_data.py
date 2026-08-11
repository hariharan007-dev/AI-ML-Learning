import pandas as pd

data = pd.read_csv('data/games.csv')

data.drop(columns=['Release Date','Rating','Times Listed',
       'Number of Reviews', 'Reviews', 'Plays', 'Playing',
       'Backlogs', 'Wishlist','Unnamed: 0'],inplace=True)
#combine Summary and Genres columns into a new column called features
data['features'] = data['Summary']+" "+data['Genres']+" "+data['Team']
#drop null values in features column
data.dropna(subset="features",inplace=True)
#remove duplicates based on Title column
data.drop_duplicates(subset="Title", inplace=True)

print(data.head())
