class RequestHeader:
    __accesskey = "********************"
    __secretkey = "*******************"
    __vendorId = "*********"

    @property
    def accesskey(self):
        return self.__accesskey

    @property
    def vendorID(self):
        return self.__vendorId

    @property
    def secretkey(self):
        return self.__secretkey
