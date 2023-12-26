import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('../data/score_112_av.csv')

    # data = {'course_name':[], 'teacher_name':[], 'labels':[]}
    data = [['course_name','teacher_name','labels']]
    # for i in df:
        # data[i] = []

    column_1 = ['容易','有趣','輕鬆','高分']
    column_2 = ['困難','沉悶','繁重','低分']

    for i in range(df['course_name'].shape[0]):
        insert = []
        
        insert.append(df['course_name'][i])
        insert.append(df['teacher_name'][i])
        
        label = ''
        # for l in column:
        #     if float(df[l][i]) > 0.6:
        #         label += l+','
        for j in range(len(column_1)):
            if float(df[column_1[j]][i]) > float(df[column_2[j]][i]):
                label += column_1[j] + ','
            else:
                label += column_2[j] + ','

        label = label[:-1]
        insert.append(label)
        data.append(insert)

    # print(data)
    new_df = pd.DataFrame(data)
    new_df.to_csv('../data/score_112_labels.csv', index=False, header=False)
    # new_df.to_parquet('../data/score_112_labels.parquet', index=False, header=False)
