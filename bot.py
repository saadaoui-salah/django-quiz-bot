import discord 
import requests
import json
import asyncio
import os

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
    respose = requests.get("https://discrod-quiz-bot.herokuapp.com/api/random/?format=json")
    print(respose.text)
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
            guess = await client.wait_for('message', check=check, timeout=2)
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry, you took too long")
        
        if int(guess.content) == right_answer:
            await message.channel.send('Right answer')
        else:
            await message.channel.send("Oops, that's not right")


TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
