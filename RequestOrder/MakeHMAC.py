import hmac, hashlib
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

class RequestHeader:
    gmt_time = datetime.now() - timedelta(hours=9) # 한국 기준
    gmt_time_str = "{:%y%m%d}T{:%H%M%S}Z".format(gmt_time, gmt_time)

    __accesskey = "a857d3f0-8a5a-40f9-a91b-02127275010e"
    __secretkey = "49638c59612cdc92029bfcaf8138cf2439c20770"
    __vendorId = "A00356115"

    __method = "GET"

    # replace with your own vendorId
    __path = "/v2/providers/openapi/apis/api/v4/vendors/"+__vendorId+"/ordersheets"
    __query = urllib.parse.urlencode({"createdAtFrom": "2021-05-02", "createdAtTo": "2021-05-03", "status": "ACCEPT"})

    __message = gmt_time_str + __method + __path + __query

    __signature = hmac.new(__secretkey.encode('utf-8'), __message.encode('utf-8'), hashlib.sha256).hexdigest()

    __authorization = "CEA algorithm=HmacSHA256, access-key=" + __accesskey + ", signed-date=" + gmt_time_str + ", signature=" + __signature

    @property
    def pathgetter(self):
        return self.__path

    @property
    def methodgetter(self):
        return self.__method

    @property
    def querygetter(self):
        return self.__query

    @property
    def messagegetter(self):
        return self.__message

    @property
    def signaturegetter(self):
        return self.__signature

    @property
    def authorizationgetter(self):
        return self.__authorization

    @property
    def secretkeygetter(self):
        return self.__secretkey
