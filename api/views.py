from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from Gereate.GereateManager import GereateManager
from Gereate.HMP4040 import HMP4040

@api_view(['GET'])
def getAngeschlosseneGereate(request):
    return Response(GereateManager.getAngeschlosseneGereate())

@api_view(['GET'])
def hmp4040_measure(request):
    try:
        
        hmp4040 = HMP4040(request.GET.get('ip', None))
            # Process the data as needed
        response_data = {'1' : [hmp4040.read_volt(1),hmp4040.read_curr(1),hmp4040.read_power(1)],
                         '2' : [hmp4040.read_volt(2),hmp4040.read_curr(2),hmp4040.read_power(2)],
                         '3' : [hmp4040.read_volt(3),hmp4040.read_curr(3),hmp4040.read_power(3)],
                         '4' : [hmp4040.read_volt(4),hmp4040.read_curr(4),hmp4040.read_power(4)]}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@api_view(['POST'])
def hmp4040_auto_corrector(request):
    try:
        # Parse the JSON data from the request body
        data = json.loads(request.body.decode("utf-8"))

        ip = data.get('ip')
        hmp4040 = HMP4040(ip)
        ch = float(data.get('ch'))
        print("sollwert : ",float(data.get('sollwert')))
        sollwert = float(data.get('sollwert'))
        hmp4040.power_correcter(ch, sollwert)
        
        # Process the data as needed
        
        response_data = {}
        return JsonResponse(response_data, status=200)
    except ZeroDivisionError:
        hmp4040.set_power(ch, sollwert)
        response_data = {}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@api_view(['POST'])
def channel_aktivieren(request):
    try:
        data = json.loads(request.body.decode("utf-8"))

        hmp4040 = HMP4040(data.get('ip'))
                # Process the data as needed
        hmp4040.enable_Channel(int(data.get('ch')))   
        response_data = {}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)    
    
@api_view(['POST'])
def channel_deaktivieren(request):
    try:
        data = json.loads(request.body.decode("utf-8"))

        hmp4040 = HMP4040(data.get('ip'))
                # Process the data as needed
        hmp4040.disable_Channel(int(data.get('ch')))   
        response_data = {}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)    
    
@api_view(['POST'])
def out_aktivieren(request):
    try:
        data = json.loads(request.body.decode("utf-8"))

        hmp4040 = HMP4040(data.get('ip'))
                # Process the data as needed
        hmp4040.enable_output()   
        response_data = {}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)   
@api_view(['POST'])
def out_deaktivieren(request):
    try:
        data = json.loads(request.body.decode("utf-8"))

        hmp4040 = HMP4040(data.get('ip'))
                # Process the data as needed
        hmp4040.disable_output()   
        response_data = {}
        return JsonResponse(response_data, status=200)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)  