import os
from .simple_content_base_filtering import SimpleContentBasedRecommendation
from .knn_model import KNNRecommendation
from django.conf import settings
import pandas as pd
project_directory = settings.BASE_DIR
static_directory = os.path.join(project_directory, 'static')


class Recommendations:
    def __init__(self,file_name,data_rows,hand_features):
        self.file_name = file_name
        self.file_path = os.path.join(static_directory, self.file_name)
        self.data_rows = data_rows
        self.features = hand_features


# it will return recomendation from Content Based Recomendation

    def simple_content_based(self):
        hand_features = self.features
        gun_features = ['Grip_Length', 'Trigger_Distance']
        df = pd.read_csv(self.file_path)
        recommend = SimpleContentBasedRecommendation(df, hand_features, gun_features, self.data_rows)
        recommendations = recommend.get_data()
        return recommendations


# It will return recomendations from KNN model

    def knn(self):
        hand_features = self.features
        gun_features = ['Grip_Length', 'Trigger_Distance']
        df = pd.read_csv(self.file_path)
        recommend = KNNRecommendation(df, hand_features, gun_features, self.data_rows)

        recommendations = recommend.get_data_knn()
        return recommendations
