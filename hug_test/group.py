from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sqlite3

# model_name = "facebook/bart-large-mnli"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

# sequence_to_classify = "one day I will see the world"
# candidate_labels = ['travel', 'cooking', 'dancing']


connection = sqlite3.connect('course.db')
# 建立游標
cursor = connection.cursor()
query = 'SELECT DISTINCT name, teacher FROM COURSE;'
cursor.execute(query)
course = cursor.fetchall()
# for row in course:
    # print(row)
cursor.close()

connection.close()
for C in course:
    print(C[0], C[1])
