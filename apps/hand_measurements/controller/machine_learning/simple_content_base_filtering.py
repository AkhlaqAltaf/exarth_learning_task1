import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
class SimpleContentBasedRecommendation:
    def __init__(self, file, compare_input, compare_with, no_rows):
        self.file = file
        self.compare_input = compare_input
        self.compare_with = compare_with
        self.rows = no_rows

    def recommendation(self):
        features = self.file[self.compare_with]
        _features = np.array(features)
        _hand = np.array(self.compare_input).reshape(1, -1)
        # print("Gun : ", _features)
        # print("Hand : ", _hand)
        distances = euclidean_distances(_features, _hand)
        self.file['distance_to_provided'] = distances
        df = self.file.sort_values(by='distance_to_provided')
        top_recommendations = df[['Title', 'Trigger_Distance', 'Grip_Length', 'Image_Link']].head(self.rows).to_dict(
            orient='records')  # Use the actual rows names
        # print(top_recommendations)

        return top_recommendations

    def get_data(self):
        return self.recommendation()

