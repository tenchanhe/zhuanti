import pandas as pd

df = pd.read_csv('score.csv')

column = ['difficult','busy','low','high','easy','interesting','clear','implicit','heavy','boring','thoughtful','sweet','hard','cold']

for label in column:
    df[label] = df[label] * 100
    df[label] = df[label].round(2)

df.to_csv('score_realscore.csv', index=False)

