from enum import Enum


class HttpResponse:
    """Represents HTTP response"""

    class Status(Enum):
        OK = (200, "OK")
        BAD_REQUEST = (400, "Bad Request")
        NOT_FOUND = (404, "Not Found")

    headers = {}
    statusline = ""

    def addheader(self, resheader):
        self.headers.update(resheader)
        return self

    def setstatus(self, status):
        if not isinstance(status, self.Status):
            raise TypeError('status must be an instance of Status Enum')
        self.setstatus(self, status[0], status[1])
        return self

    def setstatus(self, status_code, reason_phrase, http_version="HTTP/1.1"):
        self.statusline = "{0} {1} {2}\n\r".format(http_version, status_code, reason_phrase)
        return self

    def ok(self):
        self.setstatus(self, self.Status.OK)
        return self

    def error(self, status):
        self.setstatus(status.code, status.reason)
        return self

    def __str__(self) -> str:
        return self.statusline

