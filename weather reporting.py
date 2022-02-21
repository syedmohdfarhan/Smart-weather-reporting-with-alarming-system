import requests
from boltiot import Sms,Bolt
import time
import conf
import json
url='https://openweathermap.org/find?utf8=%E2%9C%93&q=lucknow,IN&appid=9605590f270856874a260f44a5fb9918' 
json_data=requests.get(url).json()
weather = json_data['weather'][0]['id']
mybolt=Bolt(conf.API_KEY,conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

while True:
   print("Reading the weather report...")
   response1=mybolt.isOnline()
   c=json.loads(response1)
   cc=c['success']
   #print(weather)
   try:
       if cc!=1:
          print ("Error in retrieving information")
          break
       if weather==200:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '200') and mybolt.analogWrite('0', '220')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("There is Light rain with Thunderstorm outside, sir" + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==202:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '255') and mybolt.analogWrite('0', '250')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("There is heavy rain with Thunderstorm outside, sir" + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==500 or weather==501 or weather==502 or weather==503 or weather==504 or weather==511 or weather==520 or weather==521 or weather==52$
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '255') and mybolt.analogWrite('0', '250')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("It is raining outside please keep a umbrella while going outside, sir" + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==801 or weather==802 or weather==804:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '255') and mybolt.analogWrite('0', '250')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("The sky is cloudy now, sir " + str(weather))
          trigger_integromat_webhook1()
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==800:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '150') and mybolt.analogWrite('0', '100')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("There is a clear sky for you outside sir " + str(weather))
          trigger_integromat_webhook()
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==300 or weather==301 or weather==302 or weather==310 or weather==311 or weather==312 or weather==313 or weather==314 or weather==32$
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '170') and mybolt.analogWrite('0', '150')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("There is a drizzlerain outside, sir " + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==803:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '110') and mybolt.analogWrite('0', '120')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("There are broken clouds in the sky, sir " + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==600 or weather==601 or weather==602 or weather==611 or weather==612 or weather==615 or weather==616 or weather==620 or weather==62$
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '85') and mybolt.analogWrite('0', '75')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("It's a snowy weather outside sir,please wear coats while getting outside " + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==701 or weather==711 or weather==721 or weather==731 or weather==740 or weather==751 or weather==761 or weather==762 or weather==77$
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '45') and mybolt.analogWrite('0', '60')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("Sir, there is a smoky and dusty weather outside, please use  mask and glouses outside " + str(weather))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
       if weather==201 or weather==210 or weather==211 or weather==212 or weather==221 or weather==230 or weather==231 or weather==2323:
          print("Turning the Alert ON!")
          mybolt.analogWrite('1', '255') and mybolt.analogWrite('0', '255')
          print("Making request to Twilio to send a SMS")
          response = sms.send_sms("Sir, It is heavy thuderstorm outside, please do not go outside " + str(weather))
          print("Response received from Twilio is: " + str(response))
          print("Status of SMS at Twilio is :" + str(response.status))
          time.sleep(5)
          mybolt.analogWrite('1', '0') and mybolt.analogWrite('0', '0')
   except Exception as e:
          print ("Error",e)
   time.sleep(10)
