import requests
import json

def jprint(obj):
    # display formatted data only if retreval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))

    # if retrieval not success, dsiplay error number
    else:
        print(f"{obj.status_code} error in API call")

# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

jprint(trucks_data)