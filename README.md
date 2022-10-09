# Baymax

<p align="center">
  <img src="https://user-images.githubusercontent.com/78845005/191757987-a1c2d3ef-e38d-47e7-9aad-601fdf0023a1.png" width=200>
</p>

<p align="center">
  The bot you were looking for for your discord server
  <br />
  <a href="https://github.com/Tinkerhub-NSSCE/baymax"><strong>Explore the documents »</strong></a>
  <br />
  <br />
  <a href="https://github.com/Tinkerhub-NSSCE/baymax">See demo</a>
    ·
  <a href="https://github.com/Tinkerhub-NSSCE/baymax/issues/new?assignees=&labels=feature&template=bug_report.md&title=">Report a Bug</a>
    ·
  <a href="https://github.com/Tinkerhub-NSSCE/baymax/issues/new?assignees=&labels=feature&template=feature_request.md&title=">Request feature</a>
</p>

<p align="center">
  <a href="https://discordpy.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/Code-Discord.py-informational?style=plastic&logo=python&logoColor=white&color=5865F2"></a>
  <a href="https://discordpy.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/NLP-Dialogflow-informational?style=plastic&logo=dialogflow&logoColor=white&color=5865F2"></a>
  <a href="https://github.com/Tinkerhub-NSSCE/baymax/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Source-Download-informational?style=flat&logo=download&logoColor=white&color=5865F2"></a>
  <a href="#"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTinkerhub-NSSCE%2Fbaymax&count_bg=%235865F2&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com"></a>
</p>

**Baymax** is the official Discord bot of TinkerHub NSSCE, designed to manage the server effectively and efficiently while also keeping it lively by engaging in natural conversations with users.

## Overview
Baymax was developed in an effort to automate and streamline the onboarding process to TinkerHub NSSCE's discord server providing the members an easier and quicker way to get themselves verified and gain complete access to the server. But it doesn't stop there, Baymax is capable of much more🔮

Here's what Baymax can do :-
- He can send you a greeting message on joining the server with steps to onboard the server
- He can detect once you've succesfully onboarded and assign appropriate roles and a nickname
- He sends out a beautiful image with your discord avatar and nickname once onboarded
- He can answer your common queries regarding onboarding
- He has answers to common questions regarding TinkerHub
- He is self-aware and can provide answers to questions about himself
- He can do a lot of small talk, try asking him for jokes
- He can lighten you up with inspiring quotes if you're feeling down
- He can find the latest hot news in tech and deliver them directly to the server

Well there certainly is a lot more he can do, if you're curious then you can find out for yourself by joining our server here 👉 https://discord.gg/2bBPbdRud6

## How to configure?
You can host the bot locally by configuring all necessary values in the `config.ini` file

- Copy `config.ini.sample` to a new file `config.ini` and replace all placeholders with appropriate values
- Copy `.env.sample` to a new file `.env` and replace the placeholder with your bot token
- Download a private key file for dialogflow in json format from your google cloud console. To learn more click [here](https://cloud.google.com/dialogflow/es/docs/quick/setup)
- Rename the downloaded file to `dialogflow_api.json` and place it in the root directory
- Install all the requirements
```bash
$ pip install -r requirements.txt
```
- Run the bot
```bash
$ python main.py
```

## How does it work?
Here's a few example screenshots of how the bot actually works

- Welcome message sent to user on joining 

![Screenshot 2022-09-21 093503](https://user-images.githubusercontent.com/78845005/191782427-0be65f3c-643a-4c22-bd25-82f6b969e7a4.png)

- Welcome card sent to a channel on succesful onboard

![Screenshot 2022-09-21 095523](https://user-images.githubusercontent.com/78845005/191783039-38d59be2-cf12-4249-b6c4-80852b31b805.png)

- Questions about himself

![Screenshot 2022-09-21 095004](https://user-images.githubusercontent.com/78845005/191783458-fc91ff80-d0cb-4392-a494-77bc94dfff96.png)

- Questions about TinkerHub

![Screenshot 2022-09-21 095055](https://user-images.githubusercontent.com/78845005/191784135-dedf6788-1b93-4818-96d7-9725c27e4c50.png)

- Small talk, jokes and uplifitng quotes

![Screenshot 2022-09-21 095232](https://user-images.githubusercontent.com/78845005/191783831-c8840b6b-6564-4a71-a928-ae92614d10bf.png)

![Screenshot 2022-09-21 095311](https://user-images.githubusercontent.com/78845005/191783851-afc34de9-8daf-40d6-acc5-fd74e88921f3.png)

- Daily top HackerNews and weekly top rated dev.to articles

![Screenshot 2022-09-21 094809](https://user-images.githubusercontent.com/78845005/191784473-1498e91b-37df-4c24-8ff2-e4147be1687a.png)

![Screenshot 2022-09-21 094851](https://user-images.githubusercontent.com/78845005/191784486-b692c836-9691-480d-a08d-cc7694f2ee92.png)

- Private message handling and forwarding them to a private channel

![Screenshot 2022-09-21 104348](https://user-images.githubusercontent.com/78845005/191784860-b68b9f87-96c9-4d80-a16b-137103e9543c.png)

## What's under the hood?
You can find all the required dependencies in the `requirements.txt` file. However here's an overview of the major libraries/tools we've used to create Baymax :-
- [discordpy](https://discordpy.readthedocs.io/en/stable/)
- [dialogflow](https://cloud.google.com/dialogflow/es/docs)
- [google-cloud-dialogflow](https://googleapis.dev/python/dialogflow/latest/index.html)
- [pyairtable](https://pyairtable.readthedocs.io/en/latest/)
- [pillow](https://pillow.readthedocs.io/en/stable/)

## Contributing
Do you have any thoughts on improving the bot? Ideas, design changes, code cleaning or even major codebase revamps, any and all such contributions are always welcome. Baymax just keeps getting better with each contribution, no matter how big or small 💪. If you'd like to get involved, you can start with the issues listed [here](https://github.com/Tinkerhub-NSSCE/baymax/issues) or you can create your own issue [here](https://github.com/Tinkerhub-NSSCE/baymax/issues/new/choose) 

