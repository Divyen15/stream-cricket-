import cv2
import socket
import threading
import tkinter as tk

def start_stream(host, port):
    # Create a socket and bind it to the specified host and port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    # Start the stream.
    conn, addr = sock.accept()
    threading.Thread(target=stream_video, args=(conn,)).start()

def stream_video(conn):
    # Open the webcam.
    capture = cv2.VideoCapture(0)

    # Start streaming the video to the client.
    while True:
        # Capture a frame from the webcam.
        ret, frame = capture.read()

        # Encode the frame and send it to the client.
        conn.sendall(frame.tostring())

def main():
    # Start the stream on port 8080.
    start_stream("localhost", 8080)

if __name__ == "__main__":
    main()
