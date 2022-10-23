import os
import json
import configparser
import discord
import random
import feedparser
import xmltodict
import requests
import pytz
import logging
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime
from airtable_api import *
from generate_cards import *
from dialogflow_api import *

config = configparser.ConfigParser()
config.read(f"{directory}/config.ini")
integration_id = int(config.get("server", "ifttt_integration_id"))
member_role_id = int(config.get("server","member_role_id"))
home_guild_id = int(config.get("server","home_guild_id"))
introductions_channel_id = int(config.get("server","introductions_channel_id"))
server_guide_channel_id = int(config.get("server","server_guide_channel_id"))
incoming_channel_id = int(config.get("server","incoming_channel_id"))
bot_name = str(config.get("server","bot_name"))
guild_name = str(config.get("server","guild_name"))
user_dms_channel_id = int(config.get("server","user_dms_channel_id"))
tech_news_channel_id = int(config.get("server","tech_news_channel_id"))
hn_daily_channel_id = int(config.get("server","hn_daily_channel_id"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv('TOKEN')
directory = os.path.dirname(os.path.realpath(__file__))
client = commands.Bot(command_prefix='!', intents=intents)

# setup logging
log_format = logging.Formatter('%(asctime)s %(levelname)s   %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

discord_handler = logging.FileHandler(filename='baymax.log')
discord.utils.setup_logging(handler=discord_handler, formatter=log_format, root=False)

baymax_handler = logging.FileHandler(filename='baymax.log')
baymax_stream_handler = logging.StreamHandler()
baymax_handler.setFormatter(log_format)
baymax_stream_handler.setFormatter(log_format)
baymax_logger = logging.getLogger(__name__)
baymax_logger.addHandler(baymax_handler)
baymax_logger.addHandler(baymax_stream_handler)
baymax_logger.setLevel(logging.INFO)

local_tz = pytz.timezone('Asia/Calcutta')

def utc_to_local(utc_dt:datetime):
  local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
  return local_tz.normalize(local_dt)

def loggable_dt(dt:datetime):
  format_string = "%d-%m-%Y | %I:%M:%S %p"
  lg_dt = dt.strftime(format_string)
  return lg_dt

@tasks.loop(minutes=60.0, reconnect=True)
async def post_hn_daily():
  now = datetime.utcnow()
  now = utc_to_local(now)
  hn_daily_channel = client.get_channel(hn_daily_channel_id)
  history = [m async for m in hn_daily_channel.history(limit = 1)]
  last_posted_at = history[0].created_at
  last_posted_at = utc_to_local(last_posted_at)
  if now.hour == 7:
    if last_posted_at.date() != now.date():
      NewsFeed = feedparser.parse("https://www.daemonology.net/hn-daily/index.rss")
      xmldata = '<root>' + str(NewsFeed.entries) + '</root>'
      data = xmltodict.parse(xmldata)
      
      for m in history:
          try:
              await m.delete()
          except:
              pass

      embed_text = ""
      for i in range(10):
        url = data['root']['ul'][0]['li'][i]['span'][0]['a']['@href']
        text = data['root']['ul'][0]['li'][i]['span'][0]['a']['#text'].replace("\\","")
        embed_text += f"***[{i+1}. {text}]({url})***\n\n"

      time_stamp = now.strftime("%b %d %Y")
      embed_color = 0x5865F2
      embed = discord.Embed(title=f"Top 10 HackerNews | {time_stamp}", description=embed_text, color=discord.Color(embed_color))
      await hn_daily_channel.send(embed=embed)
      baymax_logger.info(f"Posted hn-daily at {loggable_dt(now)}")

@tasks.loop(minutes=60.0, reconnect=True)
async def post_tech_news():
  now = datetime.utcnow()
  now = utc_to_local(now)
  tech_news_channel = client.get_channel(tech_news_channel_id)
  history = [m async for m in tech_news_channel.history(limit = 1)]
  last_posted_at = history[0].created_at
  last_posted_at = utc_to_local(last_posted_at)
  if now.weekday() == 0 and now.hour == 7:
    if last_posted_at.date() != now.date():
      r = requests.get("https://dev.to/api/articles?page=1&per_page=3&top=7%22")

      for post in r.json():
          title = post['title']
          excerpt = post['description']
          author = post['user']['username']
          tags = post['tags']
          url = post['url']
          cover = post['cover_image']
          reactions = post['public_reactions_count']
          published_date_string = post['published_at']
          published_date_object = datetime.strptime(published_date_string, "%Y-%m-%dT%H:%M:%SZ")
          published_date = published_date_object.strftime("%b %d %Y")
          embed_color = 0x5865F2
          embed = discord.Embed(title=title, url=url, color=discord.Color(embed_color))
          embed.set_image(url=cover)
          embed.add_field(name="__Excerpt__", value=f"```{excerpt}```", inline=False)
          embed.add_field(name="__Author__", value=author, inline=False)
          embed.add_field(name="__Tags__", value=tags, inline=False)
          embed.set_footer(text=f"❤️ {reactions} Reactions · Published on {published_date}")
          await tech_news_channel.send(embed=embed)
          baymax_logger.info(f"Posted tech-news at {loggable_dt(now)}")

def get_config(category:str, key:str):
  value = int(config.get(category, key))
  return value

college_roles = {
                  "NSS College of Engineering": get_config("college_roles","nsscian"),
                  "Other": get_config("college_roles","non_nsscian")
                }

gender_roles = {
                  "He/Him": get_config("gender_roles","male"),
                  "She/Her": get_config("gender_roles","female"),
                  "They/Them": get_config("gender_roles","non_binary")
                }

year_roles = {
                "2016": get_config("year_roles","2k16"),
                "2015": get_config("year_roles","2k15"),
                "2017": get_config("year_roles","2k17"),
                "2018": get_config("year_roles","2k18"),
                "2019": get_config("year_roles","2k19"),
                "2020": get_config("year_roles","2k20"),
                "2021": get_config("year_roles","2k21"),
                "2022": get_config("year_roles","2k22"),
                "2023": get_config("year_roles","2k23"),
                "2024": get_config("year_roles","2k24"),
                "2025": get_config("year_roles","2k25"),
                "2026": get_config("year_roles","2k26"),
                "2027": get_config("year_roles","2k27")
              }

async def greet_member(member:discord.Member, name:str, channel_id:int):
  try:
    await member.send(f'''Yaay 🎉 you've succesfully onboarded our server as a member
You now have the **member** role and have earned access to the rest of the channels on our server
So where you headed to next? Just make sure you give a brief introduction of yourself in <#{introductions_channel_id}> before moving on!

And if you ever feel lost and need help navigating the server do check out <#{server_guide_channel_id}>''')
  except Exception as e:
    baymax_logger.error(f"Error sending DM to {str(member)}")
    return e

  try:
    avatar_url = member.display_avatar.replace(format='png', size=256).url
    card = generate_greeting(avatar_url, name)
    card.seek(0)
    channel = client.get_channel(channel_id)
    await channel.send(file=discord.File(card, filename='greet.png'))
  except Exception as e:
    channel = client.get_channel(channel_id)
    baymax_logger.error(f"Error posting welcome card in {channel}")
    return e

@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == guild_name:
      break

  baymax_logger.info(f"{client.user} is online and connected to {guild.name}(id: {guild.id})")
  post_hn_daily.start()
  post_tech_news.start()

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for new members'))

@client.event
async def on_resumed():
  post_hn_daily.restart()
  post_tech_news.restart()

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
      return

  if message.author.id == integration_id:
    member_data = json.loads(message.content)
    nickname = member_data['name']
    username = member_data['discord_id']
    college = member_data['college']
    gender = member_data['gender']
    year = member_data['year']
    guild = client.get_guild(home_guild_id)
    member = guild.get_member_named(username)
    if member:
      member_role = guild.get_role(member_role_id)
      if member_role in member.roles:
        try:
          member_data = get_member_data(username)
        except Exception as e:
          baymax_logger.error(f"Error fetching user {username} from airtable")
        if member_data != None:
          if 'snowflake_id' not in member_data['fields'].keys():
            delete_last_record(username)
      else:
        college_role = guild.get_role(college_roles[college])
        gender_role = guild.get_role(gender_roles[gender])
        year_role = guild.get_role(year_roles[year])
        await member.add_roles(member_role, college_role, gender_role, year_role)
        await member.edit(nick=f"{nickname} 🎓")
        discord_id = member.id
        record_id = get_record_id(username)
        delete_duplicate_records(username)
        update_discord_id(str(discord_id), record_id)
        await greet_member(member, nickname, incoming_channel_id)
        baymax_logger.info(f"{str(member)} has succesfully onboarded")
    else:
      pass
  
  elif bot_name in [u.name for u in message.mentions]:
    content = str(message.content).split(" ", 2)
    res = "hmm something went wrong :("
    if len(content) < 2:
      res = random.choice(["👀","How can I help you?","I'm here..","Yepp"])
    else:
      dialogflow_res = send_message_dialogflow(message.content)
      res = dialogflow_res["response"]
    await message.channel.send(res)

  elif message.channel.type is discord.ChannelType.private:
    author_id = message.author.id
    author_name = message.author.display_name
    icon_url = message.author.display_avatar.replace(format='png', size=256).url
    msg_content = message.content
    now = datetime.utcnow()
    now = utc_to_local(now)
    time_stamp = (now.strftime("%a %b %d %Y"), now.strftime("%I:%M:%S %p"))
    embed_color = 0x5865F2
    embed = discord.Embed(description=f'''**Discord ID:**  <@{author_id}>
**Message:**  {msg_content}''', color=discord.Colour(embed_color))
    embed.set_author(name=author_name, icon_url=icon_url)
    embed.set_footer(text=f"{time_stamp[0]} · {time_stamp[1]}")
    user_dms_channel = client.get_channel(user_dms_channel_id)
    await message.author.send("My programming limits me from having conversations in a private channel. However I've forwaded your message to the server admins so that they can give you a swift response!")
    await user_dms_channel.send(embed=embed)

@client.event
async def on_member_join(member):
  guild = client.get_guild(home_guild_id)
  member_role = guild.get_role(member_role_id)
  username = str(member)
  try:
    member_data = get_member_data(username)
  except Exception as e:
    baymax_logger.error(f"Error fetching user {username} from airtable")
  
  if member_data != None:
    nickname = member_data['fields']['name']
    college = str(member_data['fields']['college'])
    gender = str(member_data['fields']['pronouns'])
    year = str(member_data['fields']['graduation_year'])
    college_role = guild.get_role(college_roles[college])
    gender_role = guild.get_role(gender_roles[gender])
    year_role = guild.get_role(year_roles[year])
    if 'snowflake_id' in member_data['fields'].keys():
      await member.add_roles(member_role, college_role, gender_role, year_role)
      await member.edit(nick=f"{nickname} 🎓")
      baymax_logger.info(f"{str(member)} has succesfully rejoined")
    else:
      await member.add_roles(member_role, college_role, gender_role, year_role)
      await member.edit(nick=f"{nickname} 🎓")
      discord_id = member.id
      record_id = get_record_id(username)
      delete_duplicate_records(username)
      update_discord_id(str(discord_id), record_id)
      await greet_member(member, nickname, incoming_channel_id)
      baymax_logger.info(f"{str(member)} has succesfully onboarded")
  else:
    try:
      embed_colour = 0x2f3136
      embed = discord.Embed(description=f'''**` Step 1 `** Fill and submit the onboarding form: https://bit.ly/Join-THNSSCE

**` Step 2 `** Accept the rules in the **Steps to complete** dialog box (The blue box you see when you click on the server)

**` Step 3 `** Give a brief introduction of yourself in <#{introductions_channel_id}> 
''', color=discord.Colour(embed_colour))
      await member.send(f'''Hiya **{member.display_name}**, we're excited to have you here 👀
To gain access to all the channels on our server, you need to complete a few steps 👇

''', embed=embed)
      await member.send(f'And in case you need any assistance, just ping us at <#977854608804307005>')
    except Exception as e:
      baymax_logger.error(f"Error sending DM to {str(member)}")

@client.command()
@commands.has_any_role("admin")
async def send_message(ctx, text:str, channel_id:int):
  '''Send a custom message to a specific channel'''
  destination_channel = client.get_channel(channel_id)
  try:
    await destination_channel.send(text)
  except Exception as e:
    baymax_logger.error("Error sending custom message")

@send_message.error
async def send_message_error(ctx, error):
  if isinstance(error, commands.MissingAnyRole):
    await ctx.send("Welp.. seems like you don't have the right permission to do that.", delete_after=10)

client.run(TOKEN)