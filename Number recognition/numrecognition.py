import keras
from keras import Sequential
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
import matplotlib.pyplot as plt

# parameters
batch_size = 128
epochs = 1
num_classes = 10
img_rows, img_cols = 28, 28
input_shape = (img_rows, img_cols, 1)   # shape input

# get data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# generalization
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# reshape
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# print sample
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# to one-hot
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# CNN model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.2))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(num_classes, activation='softmax'))
model.summary()     # print parameter
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# train
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

# prediction
n = 5   # the number of the figures
predicted_number = model.predict(x_test[:n], n)

# plot
plt.figure(figsize=(10, 3))
for i in range(n):
    plt.subplot(1, n, i + 1)
    t = x_test[i].reshape(28, 28)  
    plt.imshow(t, cmap='gray')      
    plt.subplots_adjust(wspace=2)   
    if y_test[i].argmax() == predicted_number[i].argmax():
        plt.title('%d,%d' % (y_test[i].argmax(), predicted_number[i].argmax()), color='green')
    else:
        plt.title('%d,%d' % (y_test[i].argmax(), predicted_number[i].argmax()), color='red')
    plt.xticks([])  
    plt.yticks([])
plt.show()