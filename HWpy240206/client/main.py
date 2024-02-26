from udp_client import UDP_Client

if __name__ == "__main__":
    client = UDP_Client("localhost", 7777)
    client.send("Hello, UDP Server!")
    response = client.receive()
    print(response)
    client.close()