from keras.models import Sequential
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers import BatchNormalization
from keras.layers import MaxPooling2D, AveragePooling2D
from keras.layers import Concatenate
from keras.layers import Lambda, Flatten, Dense
from keras.initializers import glorot_uniform
from keras.layers import Layer
from keras import backend as K
K.set_image_data_format('channels_first')


def facialRecognitionModel(input_shape):

    """ Model architecture """

    # Create a Sequential model

    model = Sequential()


    # Define the model architecture here


    # Compile the model

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    return model


# Load your training data and labels here


# Train the model

model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))


# Save the trained model

model.save('face_recognition_model.h5')
