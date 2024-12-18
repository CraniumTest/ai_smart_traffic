from traffic_model import train_traffic_model

def adaptive_signal_control(hour):
    # This function simulates signal control based on predicted traffic volume
    model = train_traffic_model()
    decision_threshold = 50  # Threshold to decide traffic signal duration adjustment

    predicted_volumes = []
    for intersection in range(5):  # Assuming 5 intersections
        predicted_volume = model.predict([[0, intersection, hour]])[0]
        predicted_volumes.append(predicted_volume)
        
        if predicted_volume > decision_threshold:
            print(f"Intersection {intersection}: Increase green light duration")
        else:
            print(f"Intersection {intersection}: Normal traffic flow duration")
    
    return predicted_volumes

if __name__ == "__main__":
    current_hour = 15
    print(f"Signal control decisions for hour: {current_hour}:")
    adaptive_signal_control(current_hour)
