# import extract
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# extract.extract_feature('dataset/')

song_name = {1: "A.Dvorak - Symphony_no_9", 2: "C.Saint-Saens - Symphony_no_3", 3: "F.Schubert - Symphony_no_8", 4: "F.Schubert - Symphony_no_9", 5: "J.Brahms - Symphony_no_3", 6: "J.Brahms - Symphony_no_4", 7: "J.Haydn - Symphony_no_100", 8: "J.Sibelius - Symphony_no_7", 9: "L.V.Beethoven - Symphony_no_1", 10: "L.V.Beethoven - Symphony_no_3", 11: "L.V.Beethoven - Symphony_no_3", 12: "L.V.Beethoven - Symphony_no_5", 13: "L.V.Beethoven - Symphony_no_6", 14: "L.V.Beethoven - Symphony_no_7", 15: "L.V.Beethoven - Symphony_no_8", 16: "L.V.Beethoven - Symphony_no_9", 17: "W.A.Mozart - Symphony_no_40", 18: "W.A.Mozart - Symphony_no_25", 19: "W.A.Mozart - Symphony_no_35", 20: "W.A.Mozart - Symphony_no_36", 21: "W.A.Mozart - Symphony_no_41", 22: "J.Haydn - TrumpetConcerto", 23: "W.A.Mozart - ClarinetConcerto", 24: "P.I.Tchaikovsky - ViolinConcerto", 25: "P.I.Tchaikovsky - PianoConcerto"}
harmonics = []
percussion = []

csv = pd.read_csv('Emotion_features.csv')
value = csv.iloc[0, 1]
for x in range(98):
    harmonics.append(round(((1 if csv.iloc[x, 6] >= 0 else -1) * abs(csv.iloc[x, 6] / 100)**0.5) * 100, 2))
    percussion.append(round(((1 if csv.iloc[x, 7] >= 0 else -1) * abs(csv.iloc[x, 7] / 100)**0.5) * 100, 2))
    print(csv.iloc[x, 1], harmonics[-1], percussion[-1])
plt.plot([-100, 100], [-57, 57], color='lightgray', linestyle='--', linewidth=2)
plt.plot([-57, 57], [-100, 100], color='lightgray', linestyle='--', linewidth=2)
plt.plot([100, -100], [-57, 57], color='lightgray', linestyle='--', linewidth=2)
plt.plot([57, -57], [-100, 100], color='lightgray', linestyle='--', linewidth=2)
plt.axhline(0, 0, 1, color='lightgray', linestyle='--', linewidth=2)
plt.axvline(0, 0, 1, color='lightgray', linestyle='--', linewidth=2)
plt.plot(harmonics, percussion, 'ro')
plt.xlabel('Valence')
plt.ylabel('Arousal')
plt.show()

print(len(percussion))