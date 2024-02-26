from udp_server import UDP_Server

if __name__ == "__main__":
    udp_server = UDP_Server(7777)
    udp_server.start()
    udp_server.stop()