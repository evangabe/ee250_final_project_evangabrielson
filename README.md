# ee250_final_project_evangabrielson -- email questions to "ejgabrie@usc.edu" I would love to respond and help
-----------------------------------------------------------------------------------------------------------------------------
iNTRoDUCtION:

Image Classification of Clothing Articles Neural Network using tf.keras, sent to AWS EC2 Server Instance for matplotlib visualization via TCP. I created a viable driver for an old, but functional Playstation Console Webcam based on several articles for creating drivers in Linux. This project can be recreated without the use of the PS Console Webcam (PS Eye), see "WANT TO TAKE YOUR OWN PICTURE?".

-----------------------------------------------------------------------------------------------------------------------------

COMPILE/RUN INSTRUCTIONS:

1. Download files from repository {tcp_server.py / tcp_client.py / fashionista.py}
1a. Make your own directory "test_images" to store "new_img.jpg" or any other images you wish to use
2. Open two terminals and move into the directory with above files
3. Run "python3 tcp_server.py" in one terminal (in your EC2 instance, I ssh'd into mine)
4a. Make sure your EC2 instance is running and that the host ip in "tcp_client.py" is changed to your EC2 instance
4. Run "python3 tcp_client.py" in the other
5. Watch server-side in a browser (type in your IP into the url) for matplotlib.pyplot figure showing the Neural Network's prediction of the article of clothing in the image "new_img.jpg". (a sample image is shown in the repository)
5a. "index.html" is a file I used to format and refresh the "prediction_plot.png" in browser!

Hope you enjoy! Thought it was inventive that the NN classified my sneaker as a bag, maybe the fashion trend will ensue this discovery! :^)

-----------------------------------------------------------------------------------------------------------------------------

Demo Video(s): https://drive.google.com/open?id=1olObl75n8KX2xpdQ1kQJbZRLaxw6GLGd

-----------------------------------------------------------------------------------------------------------------------------
Dependencies: (there are quite a lot of them, I understand this is not ideal, I'll be free to respond to questions to help)
1. Tensorflow
2. OpenCV
3. Matplotlib (pip3)
4. Numpy (pip3)
5. pickle
6. socket
7. os
8. io
9. warnings
10. json
11. random
Pandas (Optional)
Add your Webcam (Optional)


-----------------------------------------------------------------------------------------------------------------------------
WANT TO TAKE YOUR OWN PICTURE?:

It's important to use take_pic.py if you want to add images. If you want to use your webcam to use a different image than "new_img.jpg" (found in my repo), check that your webcam is activated in your VM or whatever desktop you're running the files on and run "python3 take_pic.py". It will take a second to capture an image, and then will save that file in your test_images directory granted it exists!

Once again totally free to answer questions, thought this project was fun and helped me learn a lot, so I want to help you understand how to use it if you don't fully get my instructions!!

--ejgabrie@usc.edu--
