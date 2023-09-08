from django.http import JsonResponse
import datetime
from django.http import HttpResponseBadRequest

def get_info(request):
    #the get query from url
    slack_name = request.GET.get("awal_umar")
    track = request.GET.get("backend")

    #to confirm that the query are provided
    if not slack_name or not track:
        error_message ="Both slack name and track must be provided"
        return HttpResponseBadRequest(error_message)
    
    github_repo = "https://github.com/drizla01/hng_1"
    github_file = "https://github.com/drizla01/hng_1/blob/master/endpoint/api/views.py"
    cur_day = datetime.datetime.utcnow().strftime('%A')
    utctime = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    response_data = { 
        "slack_name": slack_name,
        "current_day": cur_day,
        "utc_time": utctime,
        "track": track,
        "github_file_url": github_file,
        "github_repo_url": github_repo,
        "status_code": 200
  }
    return JsonResponse(response_data)