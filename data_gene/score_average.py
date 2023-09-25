import pandas as pd

original_df = pd.read_csv('data/score_112.csv')

original_df['easy_av'] = original_df['easy'] - original_df['difficult']
original_df['interesting_av'] = original_df['interesting'] - original_df['boring']
original_df['cold_av'] = (original_df['cold']+original_df['easy'])/2 - (original_df['hard']+original_df['heavy']+original_df['busy'])/3
original_df['high_av'] = (original_df['high']+original_df['sweet'])/2 - original_df['low']

result_df = original_df[['course_name','teacher_name','easy_av','interesting_av','cold_av','high_av','clear','implicit','thoughtful','kind','lmtKind','unit']]

result_df.to_csv('data/score_112_av.csv', index=False)

