from django.http import JsonResponse

def get_info(request):
    #the get query from url
    slack_name = request.GET.get("awal_umar")
    track = request.GET.get("backend")

    #to confirm that the query are provided
    if not slack_name or not track:
        return JsonResponse({"error":"Both slack name and track must be provided"}, status=400)
    
    response_data = { 
        "slack_name": "awal_umar",
        "current_day": "Thursday",
        "utc_time": "2023-09-21T15:04:05Z",
        "track": "backend",
        "github_file_url": "https://github.com/drizla01/hng_1/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/drizla01/hng_1",
        "status_code": 200
  }
    return JsonResponse(response_data)