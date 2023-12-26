import librosa
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

def extract_feature(path):
    id = 1  # Song ID
    feature_set = pd.DataFrame()  # Feature Matrix
    
    # Individual Feature Vectors
    songname_vector = pd.Series()
    harm_mean = pd.Series()
    harm_std = pd.Series()
    harm_var = pd.Series()
    perc_mean = pd.Series()
    perc_std = pd.Series()
    perc_var = pd.Series()

    # Traversing over each file in path
    file_data = [f for f in listdir(path) if isfile (join(path, f))]
    for line in file_data:
        if ( line[-1:] == '\n' ):
            line = line[:-1]

        # Reading Song
        songname = path + line
        y, sr = librosa.load(songname, duration=60)
        S = np.abs(librosa.stft(y))
        
        # Extracting Features
        harmonic = librosa.effects.harmonic(y)
        percussive = librosa.effects.percussive(y)
        
        # Transforming Features
        songname_vector._set_value(id, line)  # song name
        harm_mean._set_value(id, np.mean(harmonic))  # harmonic
        harm_std._set_value(id, np.std(harmonic))
        harm_var._set_value(id, np.var(harmonic))
        perc_mean._set_value(id, np.mean(percussive))  # percussive
        perc_std._set_value(id, np.std(percussive))
        perc_var._set_value(id, np.var(percussive))
        
        print(songname)
        id = id+1
    print(".", end="")
    # Concatenating Features into one csv and json format
    feature_set['song_name'] = songname_vector  # song name
    feature_set['harm_mean'] = harm_mean  # harmonic
    feature_set['harm_std'] = harm_std
    feature_set['harm_var'] = harm_var
    feature_set['perc_mean'] = perc_mean  # percussive
    feature_set['perc_std'] = perc_std
    feature_set['perc_var'] = perc_var
    # Converting Dataframe into CSV Excel and JSON file
    feature_set.to_csv('Emotion_features.csv')
    feature_set.to_json('Emotion_features.json')
    
# Extracting Feature Function Call
extract_feature('Dataset/')