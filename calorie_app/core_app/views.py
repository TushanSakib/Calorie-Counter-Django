from django.shortcuts import render

# Create your views here.
# GAQmDgkcjcvfhvkY7uxv1w==KMIkvCgfoSdXq1gl
def home(request):
    import json
    import requests
    if request.method == "POST":
        q = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url+q, headers={'X-Api-Key': 'GAQmDgkcjcvfhvkY7uxv1w==KMIkvCgfoSdXq1gl'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Opps! There wae an error"
            print(e)
        return render(request,'home.html',{'api':api})

    else:
        return render(request,'home.html',{'q':'Enter a valid query'})