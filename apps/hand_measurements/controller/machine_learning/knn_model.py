import numpy as np
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


# TODO: waiting for requirement clearence
class KNNRecommendation:
    def __init__(self, file, hand_features, gun_features, rows):
        self.file = file
        self.hand_features = hand_features
        self.gun_features = gun_features
        self.rows = rows

    def recommendknn(self):
        df = self.file

        # Extract features (grip length, grip width, trigger distance) and target variable (gun title)
        X = df[self.gun_features]
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(df['Title'])

        new_data = pd.DataFrame(
            {'Grip_Length': [float(self.hand_features[0])], 'Trigger_Distance': [float(self.hand_features[1])], })
        print(new_data)
        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        new_data_scaled = scaler.transform(new_data)

        # Train the KNN model
        knn_model = KNeighborsRegressor(n_neighbors=5)
        knn_model.fit(X_scaled, y_encoded)

        print(new_data_scaled)
        predictions = knn_model.predict(new_data_scaled)
        distances = knn_model.kneighbors(new_data_scaled)[0]

        threshold = 2
        max_predictions = 5

        filtered_predictions = []
        for prediction, distance in zip(predictions, distances):
            if np.all(distance < threshold):
                filtered_predictions.append((prediction, distance))

        filtered_predictions.sort(key=lambda x: x[1])
        filtered_predictions = filtered_predictions[:max_predictions]

        recommended_guns = [gun_title for gun_title, _ in filtered_predictions]

        print("Recommended Guns:", recommended_guns)

        return recommended_guns

    def get_data_knn(self):
        return self.recommendknn()
