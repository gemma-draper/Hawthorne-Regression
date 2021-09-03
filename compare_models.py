from sklearn.linear_model import Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd

class RidgeRegression:
    def __init__(self, params, X_train, X_val, y_train, y_val):
        self.params = params
        self.X_train, self.X_val = X_train, X_val
        self.y_train, self.y_val = y_train, y_val
        self.results = []
        for param in self.params:
            self.model = Ridge(alpha=param)
            train_score, val_score = self.fit_model()
            result = {
                'name': 'Ridge',
                'alpha': param,
                'training score': train_score,
                'validation score': val_score,
                }
            self.results.append(result)
    
    def fit_model(self):
        self.model.fit(self.X_train, self.y_train)
        train_score = self.model.score(self.X_train, self.y_train)
        val_score = self.model.score(self.X_val, self.y_val)
        return train_score, val_score
        


class LassoRegression:
    def __init__(self, params, X_train, X_val, y_train, y_val):
        self.params = params
        self.X_train, self.X_val = X_train, X_val
        self.y_train, self.y_val = y_train, y_val
        self.results = []
        for param in self.params:
            self.model = Lasso(alpha=param)
            train_score, val_score = self.fit_model()
            result = {
                'name': 'Lasso',
                'alpha': param,
                'training score': train_score,
                'validation score': val_score,
                }
            self.results.append(result)
    
    def fit_model(self):
        self.model.fit(self.X_train, self.y_train)
        train_score = self.model.score(self.X_train, self.y_train)
        val_score = self.model.score(self.X_val, self.y_val)
        return train_score, val_score
        
class KNNRegression:
    def __init__(self, params, X_train, X_val, y_train, y_val):
        self.params = params
        self.X_train, self.X_val = X_train, X_val
        self.y_train, self.y_val = y_train, y_val
        self.results = []
        for param in self.params:
            self.model = KNeighborsRegressor(n_neighbors=param)
            train_score, val_score = self.fit_model()
            result = {
                'name': 'KNN',
                'n_neighbors': param,
                'training score': train_score,
                'validation score': val_score,
                }
            self.results.append(result)
    
    def fit_model(self):
        self.model.fit(self.X_train, self.y_train)
        train_score = self.model.score(self.X_train, self.y_train)
        val_score = self.model.score(self.X_val, self.y_val)
        return train_score, val_score

def run_models(model, params, X_train, X_val, y_train, y_val):
    """
    Input: list of models, training and validation data.
    Output: list of results containing the details for each model icluding the most successful hyperparams."""
    
    best_results = []

    if model == "RidgeRegression":
        current_model = RidgeRegression(params, X_train, X_val, y_train, y_val)
    elif model == "LassoRegression":
        current_model = LassoRegression(params, X_train, X_val, y_train, y_val)
    elif model == "KNNRegression":
        current_model = KNNRegression(params, X_train, X_val, y_train, y_val)
    else: print("Model unrecognised.")
    return




