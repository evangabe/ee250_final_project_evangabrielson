# ee250_final_project_evangabrielson
-----------------------------------------------------------------------------------------------------------------------------
iNTRoDUCtION:

Image Classification of Clothing Articles Neural Network using tf.keras, sent to AWS EC2 Server Instance for matplotlib visualization via TCP. I created a viable driver for an old, but functional Playstation Console Webcam based on several articles for creating drivers in Linux. This project can be recreated without the use of the PS Console Webcam (PS Eye), see "WANT TO TAKE YOUR OWN PICTURE?".
-----------------------------------------------------------------------------------------------------------------------------

COMPILE/RUN INSTRUCTIONS:

1. Download files from repository {tcp_server.py/tcp_client.py/new_img.jpg/fashionista.py}
2. Open two terminals and move into the directory with above files
3. Run "python3 tcp_server.py" in one terminal
4. Run "python3 tcp_client.py" in the other
5. Watch server-side for matplotlib.pyplot figure showing the Neural Network's prediction of the article of clothing in the image "new_img.jpg".

Hope you enjoy! Thought it was inventive that the NN classified my sneaker as a bag, maybe the fashion trend will ensue this discovery! :)

-----------------------------------------------------------------------------------------------------------------------------
PUT IN LINK TO DEMO VIDEO
-----------------------------------------------------------------------------------------------------------------------------
Dependencies:
1. Tensorflow
2. OpenCV
3. Pandas (Optional)

Webcam (Optional)
-----------------------------------------------------------------------------------------------------------------------------
WANT TO TAKE YOUR OWN PICTURE?:

It's important to check/uncomment the cv2.VideoCapture(0) line in tcp_client.py based on how you want to run the code. If you want to use your webcam to use a different image than "new_img.jpg" (found in my repo), check that your webcam is activated in your VM or whatever desktop you're running the files on and uncomment that line.
