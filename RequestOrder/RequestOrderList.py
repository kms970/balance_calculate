import pprint
import urllib.request
import ssl
import json
import MakeHMAC

hMAC = MakeHMAC.RequestHeader()

# replace with your own vendorId
path = hMAC.pathgetter
query = hMAC.querygetter

message = hMAC.messagegetter

signature = hMAC.signaturegetter

authorization = hMAC.authorizationgetter
# print(authorization)

# ************* SEND THE REQUEST *************
url = "https://api-gateway.coupang.com"+path+"?%s" % query

# print('BEGIN REQUEST++++++++++++++++++++++++++++++++++++')
req = urllib.request.Request(url)
# print(req)

req.add_header("Content-type","application/json;charset=UTF-8")
req.add_header("Authorization",authorization)

req.get_method = lambda: hMAC.methodgetter

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# print(req.get_full_url())
# print(req.get_header("Content-type"))
# print(req.get_header("Authorization"))
# print(req.get_method())
#
# print('RESPONSE++++++++++++++++++++++++++++++++++++')
resp = urllib.request.urlopen(req)

try:
    resp = urllib.request.urlopen(req, context=ctx)
except urllib.request.HTTPError as e:
    if e.code == 404:
        print("404")
    else:
        print("NOT 404")
except urllib.request.URLError as e:
    print(e.errno)
else:
    # 200
    body = resp.read().decode(resp.headers.get_content_charset())
    responseJson = json.loads(body)
    pprint.pprint(responseJson)