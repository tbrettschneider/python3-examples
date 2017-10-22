import sys
import socket
import httprequest
import httpresponse


def create_server(hostname="localhost", port=8080):
    request = httprequest.HttpRequest()
    print(request.getheaders())
    print(request.getheader("Host"))

    print("Creating serversocket awaiting incomming connections on {0}:{1}".format(hostname, port))
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((hostname, port))
    serversocket.listen(5)
    while True:
        (conn, address) = serversocket.accept()
        print("Connection from: " + str(address))

        data = conn.recv(1024).decode()
        if not data:
            break
        print("Receiving from connected user: " + str(data))

        response = httpresponse.HttpResponse()
        data = str(response.ok())
        print("Sending to connected user: " + data)
        conn.send(data.encode())
        conn.close()


def main():
    print(str(sys.argv))
    create_server()


if __name__ == "__main__":
    main()
