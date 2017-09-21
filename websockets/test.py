import requests
from websocket import WebSocket, create_connection
class EdWebSocket(ws.WebSocket):
    def recv_frame(self):
        frame = super().recv_frame()
        print(frame)

ws = websocket.Websocket()
