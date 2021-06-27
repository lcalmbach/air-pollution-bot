# Air Pollution Bot
## Introduction

Hourly concentrations for the air pollutants PM10, PM2.5 and ozone are published in real time on [opendata.bs](https://data.bs.ch/explore/dataset/100049/table/?sort=datum_zeit). This application scans this dataset and sends a tweet, if thresholds are exceeded. In Switzerland, guidelines for the air pollutants monitored by this application are defined as follows:

| pollutant  | threshold  |description   |
|---|---|---|
| PM2.5 |10µg/m3 | yearly average |
| PM10 |20µg/m3 | yearly average |
| PM10 |50µg/m3 | 24h average, may be exceeded only 3 times per year |
| Ozone |100µg/m3 | 98% of half hour averages <100µg/m3 |
| Ozone |120µg/m3 | 1h average may be exceeded one time per year |

The app uses the most stringent thresholds for PM 10 (50µg/m3) and ozone (120) and 2.5 times the yearly average threshold (25µg/m3) for PM2.5.
[More infos can be found here](https://www.bafu.admin.ch/bafu/de/home/themen/luft/fachinformationen/luftqualitaet-in-der-schweiz/grenzwerte-fuer-die-luftbelastung/immissionsgrenzwerte-der-luftreinhalte-verordnung--lrv-.html).

## Creating Your Own Bot-App
In order to run this or a similar application, you require a twitter developer account. This app was implemented following instructions from [Real Python: How to Make a Twitter Bot in Python With Tweepy](https://data.bs.ch/explore/dataset/100049/table/?sort=datum_zeit).

After cloning the repo, the file named const.py must be created and filled with your Twitter Authentification info, provided once your developer account is set up. Make sure that this file is kept secret.

const.py:
```
CONSUMER_KEY = <CONSUMER_KEY>
CONSUMER_SECRET = <CONSUMER_SECRET>
ACCESS_TOKEN= <CONSUMER_SECRET>
ACCESS_TOKEN_SECRET= <ACCESS_TOKEN_SECRET>
BEARER_TOKEN = <BEARER_TOKEN>
```

When playing around, make sure that you comment out the command to send the tweet ans switch on the print command, so you do not generate any unintended tweets. Once the program works as expected, don't forget to switch the comment off again.

During testing:
```
print(text)
#api.update_status(text)
```
During production:
```
#print(text)
api.update_status(text)
```