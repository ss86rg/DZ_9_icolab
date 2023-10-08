# задание выполнено в googl.icolab 
Здравствуйте.
Отлично выполненная работа, молодец!
Можно еще заранее задать датафрейм с нулями, а потом где нужно поставить 1
А ещё можно просто два условия оставить:
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.fillna(0, inplace=True)
или так
data.loc[data['whoAmI'] == 'robot', ['robot', 'human']] = (1, 0)
data.loc[data['whoAmI'] == 'human', ['robot', 'human']] = (0, 1)