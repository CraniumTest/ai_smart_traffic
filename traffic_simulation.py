import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

def simulate_traffic_data(days=30, intersections=5):
    np.random.seed(42)
    data = []
    
    for day in range(days):
        for intersection in range(intersections):
            for hour in range(24):
                # Simulate traffic volume (vehicles/hour)
                traffic_volume = np.random.poisson(lam=(hour * 10 + np.random.normal(0, 50)), size=1)[0]
                data.append([day, intersection, hour, max(0, traffic_volume)])  # traffic volume can't be negative
    
    df = pd.DataFrame(data, columns=['Day', 'Intersection', 'Hour', 'TrafficVolume'])
    return df

def plot_traffic(df):
    plt.figure(figsize=(10, 6))
    for intersection in df['Intersection'].unique():
        hourly_traffic = df[df['Intersection'] == intersection].groupby('Hour')['TrafficVolume'].mean()
        plt.plot(hourly_traffic, label=f'Intersection {intersection}')
    
    plt.title('Simulated Traffic Patterns')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Traffic Volume')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    traffic_data = simulate_traffic_data()
    plot_traffic(traffic_data)
    traffic_data.to_csv('traffic_data.csv', index=False)
