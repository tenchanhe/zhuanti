import pandas as pd

csv_filename = '../data/score_new.csv'
df = pd.read_csv(csv_filename)

excel_filename = '/mnt/c/Users/user/OneDrive/Desktop/data'

df.to_excel(excel_filename, index=False)

