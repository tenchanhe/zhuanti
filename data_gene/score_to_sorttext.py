import pandas as pd
column = ['容易','困難','輕鬆','繁重','高分','低分','有趣','沉悶']

def get_data_kind1():
    df = pd.read_csv('../data/score_112_av.csv')
    df = df[df['kind']==1]

    grouped = df.groupby('course_name')
    course_groups = {}

    for course, group in grouped:
        # print(course, group)
        course_groups[course] = group

    return course_groups


def get_data_kind2_3():
    df = pd.read_csv('../data/score_112_av.csv')
    # df = df[df['kind']==2]
    df = df[df['kind']==3]

    grouped = df.groupby('unit')

    course_groups = {}

    for course, group in grouped:
        # print(course, group)
        course_groups[course] = group

    return course_groups


def get_data_kind4():
    df = pd.read_csv('../data/score_112_av.csv')
    df = df[df['kind']==4]

    grouped = df.groupby('lmtKind')

    course_groups = {}

    for course, group in grouped:
        # print(course, group)
        course_groups[course] = group

    return course_groups


def get_data_norate():
    df = pd.read_csv('../data/score_112_norate.csv')

    return df


def get_data_len():
    # df = pd.read_csv('../data/course_len_112_all.csv')
    # df = pd.read_csv('../data/course_len_112_kind2.csv')
    # df = pd.read_csv('../data/course_len_112_kind3.csv')
    # df = pd.read_csv('../data/course_len_112_kind4.csv')

    return df


def gene_kind_1(course_groups, course_len):
    data = {'text':[]}
    for course in course_groups.keys():

        if course_groups[course].shape[0] >= 3:
            
            for i in range(len(column)):

                for l in range(course_len['course_name'].shape[0]):
                    if course_len['course_name'][l]==course:
                        num = course_len['num'][l]
                        break

                df_sort = course_groups[course].sort_values(by=column[i], ascending=False)
                ans = f"這學期總共開了{num}堂{course}, {df_sort['teacher_name'].iloc[0]}老師, {df_sort['teacher_name'].iloc[1]}老師, {df_sort['teacher_name'].iloc[2]}老師的課{column[i]}度排名前三."
                data['text'].append("<s>[INST] " + ans + " [/INST]</s>")

    print(data)
    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_text_kind1.parquet', index=False)


def gene_kind_2(course_groups, course_len):
    data = {'text':[]}
    for unit in course_groups.keys():

        if course_groups[unit].shape[0] >= 3:
            
            for i in range(len(column)):
                
                for l in range(course_len['unit'].shape[0]):
                    if course_len['unit'][l]==unit:
                        num = course_len['num'][l]
                        break
                
                df_sort = course_groups[unit].sort_values(by=column[i], ascending=False)
                ans = f"這學期總共開了{num}堂{unit}的選修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的的{df_sort['course_name'].iloc[2]}, {column[i]}度排名前三."
                data['text'].append("<s>[INST] " + ans + " [/INST]</s>")
            

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_text_kind2.parquet', index=False)


def gene_kind_3(course_groups, course_len):
    data = {'text':[]}
    for unit in course_groups.keys():

        if course_groups[unit].shape[0] >= 3:
            
            for i in range(len(column)):
                
                for l in range(course_len['unit'].shape[0]):
                    if course_len['unit'][l]==unit:
                        num = course_len['num'][l]
                        break
                
                df_sort = course_groups[unit].sort_values(by=column[i], ascending=False)
                ans = f"這學期總共開了{num}堂{unit}的群修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {column[i]}度排名前三."
                data['text'].append("<s>[INST] " + ans + " [/INST]</s>")

    print(data)
    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_text_kind3.parquet', index=False)


def gene_kind_4(course_groups, course_len):
    data = {'text':[]}
    for lmtKind in course_groups.keys():

        if course_groups[lmtKind].shape[0] >= 5:
            
            for i in range(len(column)):
                
                for l in range(course_len['lmtKind'].shape[0]):
                    if course_len['lmtKind'][l]==lmtKind:
                        num = course_len['num'][l]
                        break
                
                df_sort = course_groups[lmtKind].sort_values(by=column[i], ascending=False)
                ans = f"這學期總共開了{num}堂的{lmtKind}, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {df_sort['teacher_name'].iloc[3]}老師的{df_sort['course_name'].iloc[3]}, {df_sort['teacher_name'].iloc[4]}老師的{df_sort['course_name'].iloc[4]}, {column[i]}度排名前五."
                data['text'].append("<s>[INST] " + ans + " [/INST]</s>")

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_text_kind4.parquet', index=False)


def gene_norate(df):
    data = {'text':[]}
    for i in range(df.shape[0]):
        ans = f"資料庫內沒有對於{df['teacher_name'][i]}老師的{df['course_name'][i]}課程的評價，請同學參考課程大綱哦~"
        data['text'].append("<s>[INST] " + ans + " [/INST]</s>")
        # print(ques)
        # print(ans)
    
    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_text_norate.parquet', index=False)


if __name__ == "__main__":

    # gene_kind_1(get_data_kind1(), get_data_len())
    # gene_kind_2(get_data_kind2_3(), get_data_len())
    # gene_kind_3(get_data_kind2_3(), get_data_len())
    # gene_kind_4(get_data_kind4(), get_data_len())
    gene_norate(get_data_norate())
