from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from Gereate.GereateManager import GereateManager
from Gereate.HMP4040 import HMP4040
# Create your views here.

def index(request):
    return render(request, 'pages/index.html',{'ahmad': [1,2,3,4,5]})

def gereate(request):
    AngeschlosseneGereate = GereateManager.getAngeschlosseneGereate()
    return render(request, 'pages/gereate.html',{'AG':AngeschlosseneGereate})

def hmp4040(request,ip):
    try:
        hmp4040 = HMP4040(ip)
    except requests.exceptions.ConnectionError as e:
        return render( request,'pages/notfound.html')
    print("test")
        
    if request.method == 'POST':
        try:
            unit = request.POST.get("custom-radio-group")
            value = request.POST.get("value")
            try :
                value = float(value)
            except:
                return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status(),"error" : "Du hast keinen gültigen Wert eingegeben"})    

            selected_channels = []
            for i in range(1,5):
                selected_channels.append((i,request.POST.get(f'sel_ch{i}')))
            for i in range(0,4):
                if selected_channels[i][1] == 'on':
                    break
                if (i == 3 ):
                    return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status(),"error" : "Du hast keinen Kanal ausgewählt"})    
            

            if value:
                for ch in selected_channels:
                    if ch[1]:
                        if (unit == "V"):
                            hmp4040.set_volt(ch[0],float(value))
                        elif (unit == "A"):
                            hmp4040.set_curr(ch[0],float(value))
                        elif (unit == "W"):
                            hmp4040.set_power(ch[0],float(value))
                        else :
                            return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status(),"error" : "Du hast keine Einheit ausgewählt"})


            return redirect( f'/HMP4040/{ip}')
        except ZeroDivisionError:
            return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status(),"error" : "Du hast entweder einen ungültigen Wert eingegeben oder der ausgewählte Kanal ist nicht aktiv."})
        except Exception as e:
            return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status(),"error" : str(e)})    

    return render(request, 'pages/hmp4040.html',{'ip': ip,'channels_status' : hmp4040.get_channels_satus(),'out' : hmp4040.get_output_status()})