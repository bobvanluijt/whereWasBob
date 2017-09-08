##
# Gets the latest tokens
##

import sys, urllib.request, json

longLatArray = []

def getList(offSet):
    print("Load with offset: " + str(offSet))
    token = sys.argv[1]
    with urllib.request.urlopen("https://api.foursquare.com/v2/users/23018068/checkins?offset=" + str(offSet) + "&limit=250&oauth_token=" + token + "&v=20170908") as url:
        mainData = json.loads(url.read().decode())
        for data in mainData['response']['checkins']['items']:
            if "venue" in data:
                if len(data["venue"]["categories"]) != 0:
                    longLatArray.append({
                        "name": data["venue"]["name"],
                        "lng": data["venue"]["location"]["lng"],
                        "lat": data["venue"]["location"]["lat"],
                        "type": data["venue"]["categories"][0]["name"]
                    })
    if mainData["response"]["checkins"]["count"] - offSet > 0:
        getList(offSet + 250)

getList(0)

with open('whereWasBob.json', 'w') as outfile:
    json.dump(longLatArray, outfile)