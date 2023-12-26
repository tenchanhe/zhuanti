import pandas as pd
column_pos = ['easy_av','interesting_av','cold_av','high_av']
column_word_pos = ['容易','有趣','輕鬆','高分']
column_neg = ['easy_av','interesting_av','cold_av']
column_word_neg = ['難','無聊','負擔重']


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
    df = df[df['kind']==2]

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


def gene_kind_1(course_groups):

    data = {'question':[], 'answer':[], 'text':[]}
    for course in course_groups.keys():

        if course_groups[course].shape[0] >= 3:
            
            for i in range(len(column_pos)):
                df_sort = course_groups[course].sort_values(by=column_pos[i], ascending=False)
                ques = f"哪些{course}會比較{column_word_pos[i]}?"
                ans = f"這學期總共開了{course_groups[course].shape[0]}堂{course}, {df_sort['teacher_name'].iloc[0]}老師, {df_sort['teacher_name'].iloc[1]}老師, {df_sort['teacher_name'].iloc[2]}老師的課{column_word_pos[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")
            
            for i in range(len(column_neg)):
                df_sort = course_groups[course].sort_values(by=column_neg[i], ascending=True)
                ques = f"哪些{course}會比較{column_word_neg[i]}?"
                ans = f"這學期總共開了{course_groups[course].shape[0]}堂{course}, {df_sort['teacher_name'].iloc[0]}老師, {df_sort['teacher_name'].iloc[1]}老師, {df_sort['teacher_name'].iloc[2]}老師的課{column_word_neg[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_qa_kind1.parquet', index=False)


def gene_kind_2(course_groups):
    data = {'question':[], 'answer':[], 'text':[]}
    for unit in course_groups.keys():

        if course_groups[unit].shape[0] >= 3:
            
            for i in range(len(column_pos)):
                df_sort = course_groups[unit].sort_values(by=column_pos[i], ascending=False)
                ques = f"哪些{unit}的選修會比較{column_word_pos[i]}?"
                ans = f"這學期總共開了{course_groups[unit].shape[0]}堂{unit}的選修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的的{df_sort['course_name'].iloc[2]}, {column_word_pos[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")
            
            for i in range(len(column_neg)):
                df_sort = course_groups[unit].sort_values(by=column_neg[i], ascending=True)
                ques = f"哪些{unit}的選修會比較{column_word_neg[i]}?"
                ans = f"這學期總共開了{course_groups[unit].shape[0]}堂{unit}的選修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的的{df_sort['course_name'].iloc[2]}, {column_word_neg[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_qa_kind2.parquet', index=False)


def gene_kind_3(course_groups):
    data = {'question':[], 'answer':[], 'text':[]}
    for unit in course_groups.keys():

        if course_groups[unit].shape[0] >= 3:
            
            for i in range(len(column_pos)):
                df_sort = course_groups[unit].sort_values(by=column_pos[i], ascending=False)
                ques = f"哪些{unit}的群修會比較{column_word_pos[i]}?"
                ans = f"這學期總共開了{course_groups[unit].shape[0]}堂{unit}的群修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {column_word_pos[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")
            
            for i in range(len(column_neg)):
                df_sort = course_groups[unit].sort_values(by=column_neg[i], ascending=True)
                ques = f"哪些{unit}的群修會比較{column_word_neg[i]}?"
                ans = f"這學期總共開了{course_groups[unit].shape[0]}堂{unit}的群修, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {column_word_neg[i]}度排名前三."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_qa_kind3.parquet', index=False)


def gene_kind_4(course_groups):
    data = {'question':[], 'answer':[], 'text':[]}
    for lmtKind in course_groups.keys():

        if course_groups[lmtKind].shape[0] >= 5:
            
            for i in range(len(column_pos)):
                df_sort = course_groups[lmtKind].sort_values(by=column_pos[i], ascending=False)
                ques = f"哪些{lmtKind}比較{column_word_pos[i]}?"
                ans = f"這學期總共開了{course_groups[lmtKind].shape[0]}堂的{lmtKind}, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {df_sort['teacher_name'].iloc[3]}老師的{df_sort['course_name'].iloc[3]}, {df_sort['teacher_name'].iloc[4]}老師的{df_sort['course_name'].iloc[4]}, {column_word_pos[i]}度排名前五."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")
            
            for i in range(len(column_neg)):
                df_sort = course_groups[lmtKind].sort_values(by=column_neg[i], ascending=True)
                ques = f"哪些{lmtKind}比較{column_word_neg[i]}?"
                ans = f"這學期總共開了{course_groups[lmtKind].shape[0]}堂的{lmtKind}, {df_sort['teacher_name'].iloc[0]}老師的{df_sort['course_name'].iloc[0]}, {df_sort['teacher_name'].iloc[1]}老師的{df_sort['course_name'].iloc[1]}, {df_sort['teacher_name'].iloc[2]}老師的{df_sort['course_name'].iloc[2]}, {df_sort['teacher_name'].iloc[3]}老師的{df_sort['course_name'].iloc[3]}, {df_sort['teacher_name'].iloc[4]}老師的{df_sort['course_name'].iloc[4]}, {column_word_neg[i]}度排名前五."
                data['question'].append(ques)
                data['answer'].append(ans)
                data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")

    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_qa_kind4.parquet', index=False)


def gene_norate(df):
    data = {'question':[], 'answer':[], 'text':[]}
    for i in range(df.shape[0]):
        ques = f"請問{df['teacher_name'][i]}老師的{df['course_name'][i]}課程評價如何？"
        ans = f"資料庫內沒有對於{df['teacher_name'][i]}老師的{df['course_name'][i]}課程的評價，請同學參考課程大綱哦~"
        data['question'].append(ques)
        data['answer'].append(ans)
        data['text'].append("<s>[INST] " + ques + " [/INST]" + ans + " </s>")
        # print(ques)
        # print(ans)
    
    new_df = pd.DataFrame(data)
    new_df.to_parquet('../data/score_112_qa_norate.parquet', index=False)


if __name__ == "__main__":

    # gene_kind_1(get_data_kind1())
    # gene_kind_2(get_data_kind2_3())
    # gene_kind_3(get_data_kind2_3())
    # gene_kind_4(get_data_kind4())
    gene_norate(get_data_norate())
