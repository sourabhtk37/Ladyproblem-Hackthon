import httplib, urllib, base64 ,json

# Image to analyse (body of the request)

body = '{\'URL\': \'https://raw.githubusercontent.com/Microsoft/ProjectOxford-ClientSDK/master/Face/Windows/Data/detection3.jpg\'}'

# API request for Emotion Detection

headers = {
   'Content-type': 'application/json',
}

params = urllib.urlencode({
   'subscription-key': '363eebb8e86d4eb3b04026785f930401',  # Enter EMOTION API key
   'returnFaceAttributes':'age,gender',
})

try:
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body , headers)
   response = conn.getresponse()
   print("Send request")

   data = response.read()
   #print(json.loads(data))
   conn.close()
except Exception as e:
   print("[Errno {0}] {1}".format(e.errno, e.strerror))

for x in json.loads(data):
    data = json.dumps(x['scores'])
    print(data)
    
