from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sqlite3

model_name = "facebook/bart-large-mnli"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)
# sequence_to_classify = "one day I will see the world"
# candidate_labels = ['travel', 'cooking', 'dancing']

file_path = 'teachers_course.txt'  # 將 'your_file.txt' 替換為實際的檔案路徑
with open(file_path, 'r') as file:
    lines = file.readlines()  # 讀取每一行的內容

two_dim_list = []
for line in lines:
    words = line.split()
    two_dim_list.append(words)

# for row in two_dim_list:
    # if len(row) == 2:
        # print(row[0], row[1])

connection = sqlite3.connect('course.db')
# cursor = connection.cursor()
# query = 'SELECT DISTINCT name, teacher FROM COURSE;'
# cursor.execute(query)
# course = cursor.fetchall()
# cursor.close()


# teacher_id = 117695
# query = f"SELECT contentEn FROM RATE WHERE teacherId={teacher_id};"
# cursor.execute(query)
for row in two_dim_list:
    if len(row) == 2:
        cursor = connection.cursor()
        name = row[0]
        teacher = row[1]
        query = "SELECT contentEn FROM RATE WHERE courseId in( SELECT id FROM COURSE WHERE name=? and teacher=?);"
        cursor.execute(query, (name, teacher))
        results = cursor.fetchall()
        # print(results)
        # print('==========----------------------================')

        cursor.close()

        sequence_to_classify = ''
        for row in results:
            # print(row[0])
            # if len(sequence_to_classify) > 10000:
                # break
            sequence_to_classify += row[0]

        # print(len(sequence_to_classify))
    
        if len(sequence_to_classify) > 0:
            candidate_labels_1 = ['easy', 'difficult', 'busy', 'high score', 'low score']
            candidate_labels_2 = ['interesting', 'clear', 'boring', 'heavy', 'implicit']
            candidate_labels_3 = ['sweet', 'cold', 'hard', 'thoughtful']
            print(name, teacher, len(sequence_to_classify))
            ans = classifier(sequence_to_classify, candidate_labels_1, multi_label=True)
            print(ans['labels'], ans['scores'])
            ans = classifier(sequence_to_classify, candidate_labels_2, multi_label=True)
            print(ans['labels'], ans['scores'])
            ans = classifier(sequence_to_classify, candidate_labels_3, multi_label=True)
            print(ans['labels'], ans['scores'])
            print('=====================================================', end='\n\n')

connection.close()
