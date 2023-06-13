from datetime import datetime

import openai
import pymysql

openai.api_key = "api"
conn = pymysql.connect(host='sudosoft-1.cpf9r06qfgdc.us-east-2.rds.amazonaws.com', user='user', password='chocho0804', db='loc', charset='utf8') #DB open
cur = conn.cursor() #커서1

def get_chat_response(messages):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = response.choices[-1].message.content.strip()
    return answer



user_input = input("USER: ")

messages = [
    {"role": "system", "content": "You are a Disaster manual assistant, name is C-DGM"},
    {"role": "user", "content": "What is C-DGM?"},
    {"role": "assistant", "content": "That is my name, Chat bot - Disaster Guide Manual"},
    {"role": "user", "content": user_input}
]

chat_response = get_chat_response(messages)
now = datetime.now()
a=2
vals = (a,chat_response)
sql = "INSERT INTO chatting (uid, chatting_log) VALUES (%s, %s)"
cur.execute(sql, (a,chat_response))
conn.commit()
cur.close()
conn.close()
print("C-DGM:", chat_response)
