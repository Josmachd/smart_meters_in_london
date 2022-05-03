from sklearn.ensemble import IsolationForest

class Iso:
    def __init__(self, contam): # Create model
        self.model =  IsolationForest(contamination = contam)
        
    def fit(self, data): # Fit model
        self.model.fit(data.to_numpy())

    def predict(self, data): # Return data prediction
        return self.model.predict(data.to_numpy())
