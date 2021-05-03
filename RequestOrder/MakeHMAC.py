import hmac, hashlib
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

class RequestHeader:
    __accesskey = "*****"
    __secretkey = "*****"
    __vendorId = "A00356115"

    @property
    def accesskey(self):
        return self.__accesskey

    @property
    def vendorID(self):
        return self.__vendorId

    @property
    def secretkey(self):
        return self.__secretkey
