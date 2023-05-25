from datetime import datetime

import openai
import pymysql

conn = pymysql.connect(host='sudosoft-1.cpf9r06qfgdc.us-east-2.rds.amazonaws.com', user='user', password='chocho0804', db='crontab_ex1', charset='utf8') #DB open
cur = conn.cursor() #커서

openai.api_key = "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"

def get_chat_response(messages):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = response.choices[-1].message.content.strip()
    return answer




user_input = "서울은 지금 몇시야?"

messages = [
    {"role": "system", "content": "Disaster manual supporter"},
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