##
# Gets the latest tokens
##

import sys, urllib.request, json

longLatArray = []
nowHere = True

def getList(offSet):
    print("Load with offset: " + str(offSet))
    token = sys.argv[1]
    with urllib.request.urlopen("https://api.foursquare.com/v2/users/23018068/checkins?sort=newestfirst&offset=" + str(offSet) + "&limit=250&oauth_token=" + token + "&v=20170908") as url:
        mainData = json.loads(url.read().decode())
        for data in mainData['response']['checkins']['items']:
            if "venue" in data:
                if len(data["venue"]["categories"]) != 0:
                    if data["venue"]["categories"][0]["name"] != "Home (private)":
                        global nowHere
                        longLatArray.append({
                            "name": data["venue"]["name"],
                            "lng": data["venue"]["location"]["lng"],
                            "lat": data["venue"]["location"]["lat"],
                            "type": data["venue"]["categories"][0]["name"],
                            "now": nowHere
                        })
                        nowHere = False

    if mainData["response"]["checkins"]["count"] - offSet > 0:
        getList(offSet + 250)

getList(0)

with open('whereWasBob.json', 'w') as outfile:
    json.dump(longLatArray, outfile)