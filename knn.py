X = [[0], [1], [2], [3]]
y = [0, 1, 2, 3]
from sklearn.neighbors import KNeighborsRegressor
neigh = KNeighborsRegressor(n_neighbors=3,weights='distance')
neigh.fit(X, y) 
print(neigh.predict([[1.75]]))
neigh = KNeighborsRegressor(n_neighbors=3,weights='uniform')
neigh.fit(X, y) 
print(neigh.predict([[1.75]]))
