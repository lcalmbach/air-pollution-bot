# Air Pollution Bot
Hourly concentrations for the air pollutants PM10, PM2.5 and ozone are published in real time on [opendata.bs](https://data.bs.ch/explore/dataset/100049/table/?sort=datum_zeit). This application scans this dataset and sends a tweet, if thresholds are exceeded. Guidelines for air pollutants are typically defined for average yearly values (10µg/m3 for PM2.5 (24h average), 20µg/m3 for PM10 (yearly average) and 120µg/m3 for ozone in Switzerland (98% of the 50% average of the month <=100 µg/m3>)) [More infos here](https://www.bafu.admin.ch/bafu/de/home/themen/luft/fachinformationen/luftqualitaet-in-der-schweiz/grenzwerte-fuer-die-luftbelastung/immissionsgrenzwerte-der-luftreinhalte-verordnung--lrv-.html). Therefore the exceedance of such a guideline by an hourly average does not necessarily represent an exceedance, it does however indicate an elevated value since if the concentration stayed at this level throughout the year, the guideline would be violated. Separate tweets are sent for each pollutant. 

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