from datetime import datetime, timedelta
import time
import tweepy
import requests
import const as cn

__version__ = '0.0.1' 
__author__ = 'Lukas Calmbach'
__author_email__ = 'lcalmbach@gmail.com'
app_name = 'air-pol-twitter-bot'
version_date = '2021-06-27'

INTERVAL = 3600

today = datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
url_ogdbs_today = f"https://data.bs.ch/explore/dataset/100049/table/?sort=datum_zeit&rows=24&q.timerange.datum_zeit=datum_zeit:%5B{yesterday}T22:00:00Z+TO+{today}T21:59:59Z%5D"
url_values = f"https://data.bs.ch/api/records/1.0/search/?dataset=100049&q=datum_zeit%3A%5B{yesterday}T22%3A00%3A00Z+TO+{today}T21%3A59%3A59Z%5D&rows=24&sort=datum_zeit&facet=datum_zeit"

params = {}
params['pm2_5_stundenmittelwerte_ug_m3'] = {'guideline':10, 'text': "⚠️ Hohe Feinstaub 2.5μm Konzentration in Basel: {} μg/m3. Grenzw. jährliches Mittel=10μg/m3. Alle Daten unter @OpenDataBS: {}",'last_tweet':(datetime.now() - timedelta(1))}
params['pm10_stundenmittelwerte_ug_m3'] = {'guideline':20, 'text': "⚠️ Hohe Feinstaub 10μm Konzentration in Basel: {} μg/m3. Grenzw. jährliches Mittel=25μg/m3. Alle Daten unter @OpenDataBS: {}",'last_tweet':(datetime.now() - timedelta(1))}
params['o3_stundenmittelwerte_ug_m3'] = {'guideline':120, 'text': "⚠️ Hohe Ozon Konzentration in Basel: {} μg/m3. Grenzw. jährliches Mittel=120μg/m3. Alle Daten unter @OpenDataBS: {}",'last_tweet':(datetime.now() - timedelta(1))}

auth = tweepy.OAuthHandler(cn.CONSUMER_KEY, cn.CONSUMER_SECRET)
auth.set_access_token(cn.ACCESS_TOKEN, cn.ACCESS_TOKEN_SECRET)

def get_data():
    """
    Retrieves the data in json format from opendata.bs and converts it to a list of records.

    """
    data = []
    try:
        data = requests.get(url_values).json()
        data = [row['fields'] for row in data['records'] if 'pm2_5_stundenmittelwerte_ug_m3' in row['fields'].keys()]
    except:
        print(f"{datetime.now()} no data returned")

    return data

def has_exceeding_parameters(row, param):
    """
    Verifies if the value for the given parameter  is higher than the guideline
    """
    result = row[param] >= params[param]['guideline'] 
    return result

def main():
    """
    the app checks the last hourly values for 3 air pollutants and sends a tweet, if an exceedance is found and has not been
    tweeted previously today.
    """
    api = tweepy.API(auth)
    start_message = f"Started {app_name} version {__version__} ({version_date}) at {datetime.now()}"
    print(start_message)
    while True:
        #get must recent data record from opendata.bs
        data = get_data()
        for param in params.keys():
            # if value is high and there was no tweet today
            if has_exceeding_parameters(data[0], param) & ((params[param]['last_tweet']).strftime('%Y-%m-%d') != datetime.now().strftime('%Y-%m-%d')):
                text = params[param]['text'].format("{:0.1f}".format(data[0][param]), url_ogdbs_today)                
                try:
                    print(text)
                    params[param]['last_tweet'] = datetime.now()
                    api.update_status(text) #comment for testing
                    print(f"{datetime.now()} Tweet has been sent") # uncomment for testing
                    # linux server is 2 hours ahead
                except Exception as ex:
                    print(f"{datetime.now()} {ex}")
            else:
                print(f"{datetime.now()} no exceedances found for {param}")    
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()