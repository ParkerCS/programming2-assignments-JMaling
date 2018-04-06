from bs4 import BeautifulSoup
import requests

# PROBLEM 1 (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.
url = "https://twitter.com/jack?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print("Jack Dorsey's Tweets:")
tweets = soup.findAll("p", class_="TweetTextSize")
for i in range(5):
    print("Tweet #", (i + 1), "-", tweets[i].text)
print("\n")

# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

url1 = "https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US"
page = requests.get(url1)
soup = BeautifulSoup(page.text, "html.parser")

dates = soup.findAll("span", class_="day-detail")
date_list = [date.text for date in dates]

days = soup.findAll("span", class_="date-time")
day_list = [day.text for day in days]

weathers = soup.findAll("td", class_="description")
weather_list = [weather.text for weather in weathers]

temps = soup.findAll("td", class_="temp")
temps_list = [temp.text for temp in temps]

precips = soup.findAll("td", class_="precip")
precips_list = [precip.text for precip in precips]

winds = soup.findAll("td", class_="wind")
winds_list = [wind.text for wind in winds]

humids = soup.findAll("td", class_="humidity")
humids_list = [humid.text for humid in humids]

print("Ten Day Weather Forecast:", "\n")
for i in range(len(day_list)):
    if weather_list[i] == "Rain" or weather_list[i] == "AM Showers" or weather_list[i] == "Light Rain/Wind" or weather_list[    i] == "Rain/Snow Showers" or weather_list[i] == "PM Showers" or weather_list[i] == "Showers":
        print(day_list[i] + ",", date_list[i], "will have", weather_list[i], "with winds traveling",
              winds_list[i].strip() + ".", "Temperatures could reach highs and lows of", temps_list[i],
              "respectively, with percent humidity reaching a potential high of", humids_list[i],
              "and percent precipitation reaching a potential high of", precips_list[i], "\n")
    else:
        print(day_list[i] + ",", date_list[i], "will be", weather_list[i], "with winds traveling", winds_list[i].strip() +          ".", "Temperatures could reach highs and lows of", temps_list[i], "respectively, with percent humidity reaching a           potential high of", humids_list[i], "and percent precipitation reaching a potential high of", precips_list[i], "\n")
