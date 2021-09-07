import requests


def store(attributeValues, deviceId, auth):
    url = "http://iot-api.pod.ir/device-twins/" + deviceId
    headers = {"Content-Type": "application/json", "Authorization": auth, "timeStamp": "1242"}
    data = {
        "deviceTwinDocument": {
            "attributes": {
                "desired": {
                }
            }
        }
    }
    for attr in attributeValues:
        data["deviceTwinDocument"]["attributes"]["desired"][attr] = attributeValues[attr]
    response = requests.put(url=url, json=data, headers=headers)
    print(response.content)
    pass

