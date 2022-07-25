from urllib import response
from django.shortcuts import render,HttpResponse
import requests
# Create your views here.





def index(request):
   return render(request,"index.html")
 
def Aries(request):

    

 url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

 querystring = {"sign":"aries","day":"today"}

 headers = {
	"X-RapidAPI-Key": "1a57489368msh305d203ec7ccac3p18b25fjsn652439095b69",
	"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
 }

 response = requests.request("POST",url=url,params=querystring,headers=headers)
 users=response.json()
 print(response.text)

 return render(request,"Aries.html",{'users': users})

def Taurus(request):

 return render(request,"Taurus.html")




def Gemini(request):

 return render(request,"Gemini.html")


def Cancer(request):

 return render(request,"Cancer.html")






def Leo(request):

 return render(request,"Leo.html")





def Virgo(request):

 return render(request,"Virgo.html")



def Libra(request):

 return render(request,"Libra.html")





def Scorpio(request):

 return render(request,"Scorpio.html")



def Sagitarius(request):

 return render(request,"Sagitarius.html")




def Capricorn(request):

 return render(request,"Capricorn.html")





def Aquarius(request):

 return render(request,"Aquarius.html")




def Pisces(request):

 return render(request,"Pisces.html")





















