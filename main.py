from datetime import datetime
import  random
import openai
import pymysql

conn = pymysql.connect(host='sudosoft-1.cpf9r06qfgdc.us-east-2.rds.amazonaws.com', user='user', password='chocho0804', db='crontab_ex1', charset='utf8') #DB open
cur = conn.cursor() #커서

openai.api_key = "[api-key]"

def get_chat_response(messages):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = response.choices[-1].message.content.strip()
    return answer


a= ["지진","홍수","화재","산사태"]
b=random.choice(a)+' 메뉴얼 알려줘'
user_input = b

messages = [
    {"role": "system", "content": "You are a Disaster manual assistant, name is C-DGM"},
    {"role": "user", "content": "What is C-DGM?"},
    {"role": "assistant", "content": "That is my name, Chat bot - Disaster Guide Manual"},
    {"role": "user", "content": user_input}
]

chat_response = get_chat_response(messages)

now = datetime.now()
vals = (chat_response, now)
sql = "INSERT INTO ct_times (qst, ans) VALUES (%s, %s)"
cur.execute(sql, vals)
conn.commit()

print("C-DGM:", chat_response)

cur.close()
conn.close()