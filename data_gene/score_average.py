import pandas as pd

original_df = pd.read_csv('../data/score_112_haverate.csv')

original_df['容易'] = original_df['容易'] - original_df['困難']
original_df['有趣'] = original_df['有趣'] - original_df['沉悶']
original_df['輕鬆'] = (original_df['輕鬆']+original_df['涼'])/2 - (original_df['繁重']+original_df['硬'])/2
original_df['高分'] = (original_df['高分']+original_df['甜'])/2 - original_df['低分']

original_df['困難'] = original_df['困難'] - original_df['容易']
original_df['沉悶'] = original_df['沉悶'] - original_df['有趣']
original_df['繁重'] = (original_df['繁重']+original_df['硬'])/2 - (original_df['輕鬆']+original_df['涼'])/2
original_df['低分'] = original_df['低分'] - (original_df['高分']+original_df['甜'])/2

result_df = original_df[['course_name','teacher_name','容易','有趣','輕鬆','高分', '困難', '沉悶', '繁重', '低分', 'kind','lmtKind','unit']]

result_df.to_csv('../data/score_112_av.csv', index=False)

