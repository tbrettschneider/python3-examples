class HttpRequest:
    """Represents HTTP request"""

    (RQHEADER_HOST, RQHEADER_CONNECTION) = ("Host", "Connection")

    def getheaders(self):
        return {"Host": "localhost"}

    def getheader(self, requestheader):
        return HttpRequest.getheaders(self).get(requestheader)
