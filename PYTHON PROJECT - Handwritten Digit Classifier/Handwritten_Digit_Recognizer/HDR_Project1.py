import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# #Directly loads dataset from TF, rather than importing/downloading
# mnist = tf.keras.datasets.mnist

# #Splitting data into training and testing data
# #X is the data itself, Y is LAbelled data(THe actual identified number)
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# #Now Normalizing the data, that is essentially scalling down everthing b/w 0-1
# x_train = tf.keras.utils.normalize(x_train, 1)
# x_test = tf.keras.utils.normalize(x_test, 1)

# #Creating the actual model
# #Here Sequential stands for the basic ANN
# model = tf.keras.models.Sequential()

# #Every ANN has layers
# #The layers.Flatten basically means that we will flatten the input shape into a plain layer, rather than a grid
# #So here its a layer of 28*28 = 784 pixels.
# model.add(tf.keras.layers.Flatten(input_shape = (28, 28)))


# #Adding 2 dense layer that has each neuron connects each neuron to all the othher neurons in the next hidden layer
# #Relu is quite comman it stands for rectified linear unit, its activation function is either 0 or it goes linearlly positively
# model.add(tf.keras.layers.Dense(128, activation ='relu'))
# model.add(tf.keras.layers.Dense(128, activation ='relu'))


# #The final dense layer is the output layer which will represent each digit, i.e., 0-9
# #Softmax makes sure that all the neurons add up to 1, used for accuracy purposes
# model.add(tf.keras.layers.Dense(10, activation = 'softmax'))

# #Compiling the model
# model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# #Fitting the data to train the model on the data
# #Epochs is the no of iterration
# model.fit(x_train, y_train, epochs = 3)

# model.save('Handwritten.model')

model = tf.keras.models.load_model('Handwritten.model')

# #Checking the loss and accuracy rate
# #No model is perfect in accuracy
# loss, accuracy = model.evaluate(x_test, y_test)
# print(loss) #0.08
# print(accuracy)#0.97

#Weve used invert, as the cv2 module reads white over black, thus it wont read the black pixels.
image_number = 1
while os.path.isfile(f"DATA/d{image_number}.png"):
    try:
        img = cv2.imread(f"DATA/d{image_number}.png")[:,:,0]
        #Sending the image as a list in the ANN as an array
        img = np.invert(np.array(img))
        prediction = model.predict(img)
        print(f"The number predicted is : {np.argmax(prediction)}")
        #argmax(prediction) gives the index of the field that has the highest activation func
        plt.imshow(img[0], cmap = plt.cm.binary)
        plt.show()
    except:
        print("ERROR!")
    finally:
        image_number += 1
