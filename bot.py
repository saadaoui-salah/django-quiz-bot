import discord 
import requests
import json

client = discord.Client()

def get_answers(data):
    answers = ''
    id = 1
    right_answer = 0
    for answer in data[0]['answers']:
        answers += f'{id}- {answer}\n'
        if answer['is_correct']:
            right_answer = id
        id += 1
    return answers, right_answer

def get_question(data):
    return f'Question: \n{data[0]["title"]}'

def create_message():
    respose = requests.get("")
    json_data = json.loads(respose)
    question = get_question(json_data)
    answers, right_answer = get_answers(json_data)
    message = question + '\nSelect an answer\n' + answers
    return message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$question'):
        message = create_message()
        await message.channel.send(message)

client.run("ODQ1MjkzMTM2MDA4MDUyNzg2.YKe2lA.caecttCMeEtLk2UjZ4qRCd4gfGc")
