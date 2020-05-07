from __future__ import print_function
from fashionista import fashion_nn, proc_new_img
import socket
import struct
import time
import pickle
import cv2
import io
import os
import warnings
import tkinter as tk
import cv2
import numpy as np

HOST, PORT = "18.222.120.186", 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# img = proc_new_img("new_img.jpg")

serial_tx = fashion_nn()

try:
    s.connect((HOST, PORT))
    s.sendall(serial_tx)

finally:

    s.close()

print("Sent:    {}".format(serial_tx))
# def capture_image():
    
#     cam = cv2.VideoCapture(0)
#     cam.set(3,28)
#     cam.set(4,28)

#     result = True

#     while (result):
#         ret, frame = cam.read()
#         #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         cv2.imwrite("new_img.jpg", frame)

#         result = False

#     cam.release()
#     cv2.destroyAllWindows()

#     return ret, frame


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.hi_there = tk.Button(self, fg="green")
#         self.hi_there["text"] = "\nTake Picture\n"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

#         self.QUIT.pack(side="bottom")

#     def send_picture(self):

#         encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
#         ret, frame = capture_image()
#         result, frame = cv2.imencode('.jpg', frame, encode_param)
#         data = pickle.dumps(frame, 0)
#         size = len(data)

#         s.sendall(struct.pack(">L", size) + data)
#         print("New image in 'new_img.jpg'")


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


