import discord 
import requests
import json

client = discord.Client()

def get_answers(data):
    answers = ''
    id = 1
    right_answer = 0
    for answer in data[0]['answer']:
        answers += f'{id}- {answer["answer"]}\n'
        if answer['is_correct']:
            right_answer = id
        id += 1
    return answers, right_answer

def get_question(data):
    return f'Question: \n{data[0]["title"]}'

def create_message():
    respose = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(respose.text)
    question = get_question(json_data)
    answers, right_answer = get_answers(json_data)
    message = question + '\nSelect an answer\n' + answers
    return message, right_answer
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$question'):
        message_text, right_answer = create_message()
        await message.channel.send(message_text)

    def check(m):
        return m.author == message.author and m.content.isdigit()
    
    try:
        guess = await client.wait_for('message', check=check, timeout=5.0)
    except:
        return await message.channel.send("Sorry, you took too long")
    

client.run("ODQ1MjkzMTM2MDA4MDUyNzg2.YKe2lA.pwMdsZ4PGoFcXI0wNbKwas4wJcE")
