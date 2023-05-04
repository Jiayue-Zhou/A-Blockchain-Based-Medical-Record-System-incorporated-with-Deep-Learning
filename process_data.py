import pandas as pd
from people import People

df = pd.read_csv('C:/Users/Jiayue/Desktop/Final_dataset_Copy.csv')

num_features = [
        'Age',
        'Gender',
        'Air Pollution',
        'Alcohol use',
        'Dust Allergy',
        'OccuPational Hazards',
        'Genetic Risk',
        'chronic Lung Disease',
        'Balanced Diet',
        'Obesity',
        'Smoking',
        'Passive Smoker',
        'Chest Pain',
        'Coughing of Blood',
        'Fatigue',
        'Weight Loss',
        'Shortness of Breath',
        'Wheezing',
        'Swallowing Difficulty',
        'Clubbing of Finger Nails',
        'Frequent Cold',
        'Dry Cough',
        'Snoring',
        'Level'
      ]

def make_people(sl):
    return People(sl[-1], sl[:-1])


def processing_data():
    ll = df.values.tolist()
    result = []
    for i in range(df.shape[0]):
        pp = make_people(ll[i])
        result.append(pp)
    return result


def pre_process_for_model(ll):
    df = pd.DataFrame(ll, columns=num_features)
    return df
