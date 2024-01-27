# everest_broker/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ReceivedData

MAX_RECORDED_DATA = 10

# everest_broker/views.py
# everest_broker/views.py

# everest_broker/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ReceivedData

MAX_RECORDED_DATA = 10

@csrf_exempt
def receive_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Convert data to text format (stringify) for storage
            data_text = json.dumps(data)

            # Save received data to the database
            ReceivedData.objects.create(data=data_text)

            # Keep only the latest 10 rows in the database
            # oldest_records = ReceivedData.objects.order_by('timestamp')[:MAX_RECORDED_DATA]
            # oldest_record_pks = oldest_records.values_list('pk', flat=True)
            # ReceivedData.objects.filter(pk__in=oldest_record_pks).delete()

            # Send a confirmation response
            response_data = {'status': 'connected'}
            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            response_data = {'error': 'Invalid JSON'}
            return JsonResponse(response_data, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def live_data(request):
    # Retrieve the latest 10 rows from the database
    latest_data = ReceivedData.objects.order_by('-timestamp')[:MAX_RECORDED_DATA]
    serialized_data = [json.loads(item.data) for item in latest_data]

    return render(request, 'live_data.html', {'received_data': serialized_data})


@csrf_exempt
def delete_all_data(request):
    if request.method == 'POST':
        try:
            ReceivedData.objects.all().delete()
            response_data = {'status': 'success'}
            return JsonResponse(response_data, status=200)
        except Exception as e:
            print(f"Error deleting all data: {e}")
            response_data = {'error': 'Error deleting data'}
            return JsonResponse(response_data, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)