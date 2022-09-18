import os
import json
import configparser
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from airtable_api import *
from generate_cards import *
from dialogflow_api import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv('TOKEN')
directory = os.path.dirname(os.path.realpath(__file__))
client = commands.Bot(command_prefix='!', intents=intents)

config = configparser.ConfigParser()
config.read(f"{directory}/config.ini")
integration_id = int(config.get("server", "ifttt_integration_id"))
member_role_id = int(config.get("server","member_role_id"))
home_guild_id = int(config.get("server","home_guild_id"))
introductions_channel_id = int(config.get("server","introductions_channel_id"))
server_guide_channel_id = int(config.get("server","server_guide_channel_id"))
incoming_channel_id = int(config.get("server","incoming_channel_id"))
bot_name = str(config.get("server","bot_name"))

async def greet_member(member:discord.Member, name:str, channel_id:int):
  try:
    await member.send(f'''Yaay 🎉 you've succesfully onboarded our server as a member
You now have the **member** role and have earned access to the rest of the channels on our server
So where you headed to next? Just make sure you give a brief introduction of yourself in <#{introductions_channel_id}> before moving on!

And if you ever feel lost and need help navigating the server do check out <#{server_guide_channel_id}>''')
  except Exception as e:
    print(f"Error sending DM to {str(member)}")
    return e

  try:
    avatar_url = member.avatar.replace(format='png', size=256)
    card = generate_greeting(avatar_url, name)
    card.seek(0)
    channel = client.get_channel(channel_id)
    await channel.send(file=discord.File(card, filename='greet.png'))
  except Exception as e:
    print(f"Error posting in {channel}")
    return e

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
      return

  if message.author.id == integration_id:
    member_data = json.loads(message.content)
    nickname = member_data['name']
    username = member_data['discord_id']
    guild = client.get_guild(home_guild_id)
    member = guild.get_member_named(username)
    if member:
      member_role = guild.get_role(member_role_id)
      if member_role in member.roles:
        try:
          member_data = get_member_data(username)
        except Exception as e:
          print(f"Error fetching user {username} from airtable")
        if member_data != None:
          if 'snowflake_id' not in member_data['fields'].keys():
            delete_last_record(username)
      else:
        await member.add_roles(member_role)
        await member.edit(nick=f"{nickname} 🎓")
        discord_id = member.id
        record_id = get_record_id(username)
        delete_duplicate_records(username)
        update_discord_id(str(discord_id), record_id)
        await greet_member(member, nickname, incoming_channel_id)
        print(f"{str(member)} has succesfully onboarded")
    else:
      pass
  
  elif bot_name in [u.name for u in message.mentions]:
    content = str(message.content).split(" ", 2)
    res = "hmm something went wrong :("
    if len(content) < 2:
      res = random.choice(["👀","How can I help you?","I'm here..","Yepp"])
    else:
      dialogflow_res = send_message_diagflow(message.content)
      res = dialogflow_res["response"]
    await message.channel.send(res)

@client.event
async def on_member_join(member):
  guild = client.get_guild(home_guild_id)
  member_role = guild.get_role(member_role_id)
  username = str(member)
  try:
    member_data = get_member_data(username)
  except Exception as e:
    print(f"Error fetching user {username} from airtable")
  
  if member_data != None:
    nickname = member_data['fields']['name']
    if 'snowflake_id' in member_data['fields'].keys():
      await member.add_roles(member_role)
      await member.edit(nick=f"{nickname} 🎓")
      print(f"{str(member)} has succesfully rejoined")
    else:
      await member.add_roles(member_role)
      await member.edit(nick=f"{nickname} 🎓")
      discord_id = member.id
      record_id = get_record_id(username)
      delete_duplicate_records(username)
      update_discord_id(str(discord_id), record_id)
      await greet_member(member, nickname, incoming_channel_id)
      print(f"{str(member)} has succesfully onboarded")
  else:
    try:
      embed_colour = 0x2f3136
      embed = discord.Embed(description=f'''**` Step 1 `** Fill and submit the onboarding form: https://tally.so/r/3xX1aE

**` Step 2 `** Accept the rules in the **Steps to complete** dialog box (The blue box you see when you click on the server)

**` Step 3 `** Give a brief intoduction of yourself in <#{introductions_channel_id}> 
''', color=discord.Colour(embed_colour))
      await member.send(f'''Hiya **{member.display_name}**, we're excited to have you here 👀
To gain access to all the channels on our server, you need to complete a few steps 👇

''', embed=embed)
      await member.send(f'And in case you need any assistance, just ping us at <#977854608804307005>')
    except Exception as e:
      print(e)
      print(f"Error sending DM to {str(member)}")

  


client.run(TOKEN)