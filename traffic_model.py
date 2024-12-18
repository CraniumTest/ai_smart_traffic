from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_traffic_model(data_path='traffic_data.csv'):
    df = pd.read_csv(data_path)
    
    X = df[['Day', 'Intersection', 'Hour']]
    y = df['TrafficVolume']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print(f'Model Score: {model.score(X_test, y_test):.2f}')
    return model

if __name__ == "__main__":
    model = train_traffic_model()
