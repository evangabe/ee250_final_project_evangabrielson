import cv2
import json
import os
import warnings
import pickle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt



def proc_new_img(img):

    WIDTH = 28
    HEIGHT = 28
    dim = (WIDTH, HEIGHT)
    # read and resize new image
    full_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    new_img = cv2.resize(full_img, dim, interpolation=cv2.INTER_LINEAR)
    new_img = new_img / 255.0

    return new_img

def fashion_nn():


	# Print version
	print("TensorFlow " + str(tf.__version__))


	## Initialize Model ##
	# Gather training and test datasets for classifying articles of clothing
	data = keras.datasets.fashion_mnist
	(train_imgs, train_labels), (test_imgs, test_labels) = data.load_data()

	# Map labeled data to correct article name
	class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 
			'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']


	## Preprocessing Data ##
	# Condense data into range of 0 to 1
	train_imgs = train_imgs / 255.0


	## Building the Model ##
	# Setting up the layers
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(28,28)), # input layer corresponding to 1D array of 28*28 pixels
		keras.layers.Dense(128, activation='relu'), # hidden layer running RELU
		keras.layers.Dense(10, activation='softmax') # output layer
		# 'Dense' corresponds to fully connected neural layers
	])


	# Compile the model, set up parameters for model (optimization, loss, metrics)
	model.compile(optimizer='adam', 
		loss="sparse_categorical_crossentropy",
		metrics=['accuracy'])


	# Train the model with 3 epochs
	model.fit(train_imgs, train_labels, epochs=5)


	# Evaluate and print metrics
	#model_loss, 


	old_img = proc_new_img("new_img.jpg")
	print(old_img.shape)
	img_file = np.expand_dims(old_img,0)


	# Make Predictions
	probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
	prediction_single = probability_model.predict(img_file)

	# Make JSON dictionary

	predictionary = {
		'probabilities': prediction_single[0],
		'img': old_img,
		'recall': 0,
		'precision': 0
	}

	serial_probs = pickle.dumps(predictionary['probabilities'])
	serial_img = pickle.dumps(predictionary['img'])
	return serial_probs, serial_img
