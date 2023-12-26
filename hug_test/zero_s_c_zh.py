from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sqlite3
import csv

model_name = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

# sequence_to_classify = "這堂課老師不輕鬆，作業蠻多的，也挺難的"
# candidate_labels = ['困難','容易','輕鬆','痛苦','甜','硬','負擔重']
# output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
# print(output)

file_path = '../data/teachers_course_2.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

two_dim_list = []
for line in lines:
    words = line.split()
    two_dim_list.append(words)

# print(len(two_dim_list))
# for row in two_dim_list:
    # if len(row) == 2:
        # print(row[0], row[1])

labels_list = ['容易', '困難', '繁重', '輕鬆', '高分', '低分', '有趣', '清楚', '沉悶', '模糊', '甜', '涼', '硬']
connection = sqlite3.connect('../data/20230827.db')
with open('../data/score_new.csv', mode='a', newline='') as file:
    is_empty = file.tell() == 0
    if is_empty:
        writer = csv.writer(file)
        writer.writerow(labels_list)

flag = 1
step = 0
for row in two_dim_list:
    step += 1
    # print(step)
    if flag == 10:
        break

    if len(row) == 2:
        cursor = connection.cursor()
        name = row[0]
        teacher = row[1]
        query = "SELECT RATE.content, RATE.contentEn FROM RATE, COURSE WHERE COURSE.name=? and COURSE.teacher=? and RATE.courseId=COURSE.id;"
        cursor.execute(query, (name, teacher))
        results = cursor.fetchall()
        # print(results)
        # print('==========----------------------================')

        cursor.close()

        sequence_to_classify = ''
        for row in results:
            sequence_to_classify += row[0] + ','

        print(name, teacher)
        print(sequence_to_classify)
        if len(sequence_to_classify) > 0:
            flag += 1
    
        # if len(sequence_to_classify) > 0:
            # flag += 1
            # candidate_labels_1 = ['容易', '困難', '繁重', '輕鬆','高分', '低分']
            # candidate_labels_2 = ['有趣', '清楚', '沉悶', '模糊']
            # candidate_labels_3 = ['甜', '涼', '硬']
            
            # # print(name, teacher, len(sequence_to_classify))
            # insert_data = [name, teacher]
            # ans = classifier(sequence_to_classify, candidate_labels_1, multi_label=False)
            # # print(ans['labels'], ans['scores'])
            # for attribute in candidate_labels_1:
                # insert_data.append(str(ans['scores'][ans['labels'].index(attribute)]))

            # ans = classifier(sequence_to_classify, candidate_labels_2, multi_label=False)
            # # print(ans['labels'], ans['scores'])
            # for attribute in candidate_labels_2:
                # insert_data.append(str(ans['scores'][ans['labels'].index(attribute)]))
            
            # ans = classifier(sequence_to_classify, candidate_labels_3, multi_label=False)
            # # print(ans['labels'], ans['scores'])
            # for attribute in candidate_labels_3:
                # insert_data.append(str(ans['scores'][ans['labels'].index(attribute)]))
            # # print('='*50, end='\n\n')

            # with open('../data/score_new.csv', mode='a', newline='') as file:
                # writer = csv.writer(file)
                # writer.writerow(tuple(insert_data))

        # else:
            # with open('../data/no_rate_course.txt', 'a') as file:
                # file.write(name + ',' + teacher + '\n')

    # else:
        # with open('../data/zerosc_error.txt', 'a') as file:
            # file.write(name + ',' + teacher + '\n')


connection.close()
