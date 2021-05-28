import urllib.request
import ssl
import json
from datetime import datetime, timedelta
import hmac, hashlib
import urllib.parse
from RequestOrder import MakeHMAC
import pandas as pd

class RequestOrder:
    def RequestOrderVendorId(self, nextToken):
        hMAC = MakeHMAC.RequestHeader()

        gmt_time = datetime.now() - timedelta(hours=9)  # 한국 기준
        gmt_time_str = "{:%y%m%d}T{:%H%M%S}Z".format(gmt_time, gmt_time)

        method = "GET"

        # replace with your own vendorId
        path = "/v2/providers/openapi/apis/api/v4/vendors/" + hMAC.vendorID + "/ordersheets"
        query = urllib.parse.urlencode({"createdAtFrom": "2021-05-27",
                                        "createdAtTo": "2021-05-27",
                                        "status": "FINAL_DELIVERY",
                                        "nextToken": nextToken})

        message = gmt_time_str + method + path + query
        signature = hmac.new(hMAC.secretkey.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
        authorization = "CEA algorithm=HmacSHA256, access-key=" + hMAC.accesskey + ", signed-date=" + gmt_time_str + ", signature=" + signature
        # print(authorization)

        # ************* SEND THE REQUEST *************
        url = "https://api-gateway.coupang.com" + path + "?%s" % query

        # print('BEGIN REQUEST++++++++++++++++++++++++++++++++++++')
        req = urllib.request.Request(url)
        # print(req)

        req.add_header("Content-type", "application/json;charset=UTF-8")
        req.add_header("Authorization", authorization)

        req.get_method = lambda: method

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
            # pprint.pprint(responseJson)
            return responseJson


    def allDatafromAPI(self):
        next_page = 1
        all_dataframe = pd.DataFrame()

        while True:
            df = self.RequestOrderVendorId(next_page)

            dfJson = pd.DataFrame.from_dict(df['data'], orient='columns')
            all_dataframe = pd.concat([dfJson, all_dataframe], ignore_index=True)
            next_page = df['nextToken']

            if next_page == '':
                break

        # print(all_dataframe)
        return all_dataframe
