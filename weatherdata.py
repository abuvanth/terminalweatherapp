import requests as rt
var=True
while var:

      city=raw_input("enter the city name : ")
      url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=APIKEY"
      data=rt.get(url)
      read=data.json()
      print "Cityname : {} ".format(read['name'])
      print "Temperature : {} ".format(read['main']['temp'])
      print "Humidity : {}".format(read['main']['humidity'])
      print "pressure : {} ".format(read['main']['pressure'])
      print "Wind Speed : {} ".format(read['wind']['speed'])
      print "details : {} ".format(read['weather'][0]['description'])
      ask=raw_input("Do you want to know another city info(y/n)?")
      if ask=="y":
      	var=True
      else:
      	var=False
