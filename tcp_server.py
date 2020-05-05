import socket
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt

HOST, PORT = "localhost", 9999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete ' + str(PORT))
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
data += conn.recv(4096)
data = pickle.loads(data)

s.close()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 
            'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']


plt.grid(False)
plt.xticks(range(10))
plt.yticks([])

thisplot = plt.bar(range(10), data, color="#777777")
plt.ylim([0,1])
predicted_label = np.argmax(data)

if predicted_label > 0.5:
    plt.xlabel("{} {:2.0f}% Confident".format(class_names[predicted_label],
        100*np.max(data),
        color='red'))
else:
    plt.xlabel("{} {:2.0f}% (Not Very) Confident".format(class_names[predicted_label],
        100*np.max(data),
        color='red'))


thisplot[predicted_label].set_color('red')
plt.title("Prediction")
plt.show()

# while True:
#     while len(data) < payload_size:
#         print("Recv: {}".format(len(data)))
#         data += connn.recv(4096)

#     print("Done Recv: {}".format(len(data)))
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack(">L", packed_msg_size)[0]
#     print("msg_size: {}".format(msg_size))
#     while len(data) < msg_size:
#         data += conn.recv(4096)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]

#     frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
#     print(frame["predictions"])