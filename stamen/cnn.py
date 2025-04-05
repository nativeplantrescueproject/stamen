"""
CNN = Convolutional neural network
"""
from keras.src.layers import (
    Activation,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D
)
from keras.src.models import Sequential
from sklearn.model_selection import train_test_split


class CNN:
    DESIRED_ACCURACY = 0.90
    NUM_EPOCHS = 15
    IMAGE_SIZE_PX = 64

    @classmethod
    def build_model_a(cls) -> Sequential:
        """Builds out Model A"""
        layers = [
            # Input shape is the desired size of the image 150x150 with 3 bytes of color

            # First convolution
            Conv2D(16, (3, 3), activation='relu',
                   input_shape=(cls.IMAGE_SIZE_PX, cls.IMAGE_SIZE_PX, 4)),
            MaxPooling2D(2, 2),

            # Second
            Conv2D(32, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),

            # Third
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),

            # Fourth
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),

            # Fifth
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D(2, 2),

            # Flatten results to feed into a DNN
            # Flatten (i.e., unroll) the 3D output to 1D, then add one or more dense layers on top
            Flatten(),

            # 2048-neuron hidden layer
            Dense(2048, activation='relu'),

            # 3 output neurons
            Dense(3, activation='softmax')
        ]

        return Sequential(layers)

    @classmethod
    def build_model_b(cls) -> Sequential:
        """Builds out Model B"""
        layers = [
            # Input shape is the desired size of the image 150x150 with 3 bytes of color

            # First convolution
            Conv2D(32, (2, 2), input_shape=(cls.IMAGE_SIZE_PX, cls.IMAGE_SIZE_PX, 3)),
            Activation('relu'),
            MaxPooling2D(pool_size=(2, 2)),

            # Second
            Conv2D(32, (2, 2)),
            Activation('relu'),
            MaxPooling2D(pool_size=(2, 2)),

            # Flatten results to feed into a DNN
            # Flatten (i.e., unroll) the 3D output to 1D, then add one or more dense layers on top
            Flatten(),
            Dense(64),
            Activation('relu'),
            Dropout(0.5),

            # 21 output neurons
            Dense(21),
            Activation('softmax'),
        ]

        return Sequential(layers)

    @classmethod
    def compile_and_train_model(cls, model: Sequential, data, labels, test_size: float = 0.2,
                                random_state: int = 42) -> Sequential:
        model.summary()

        model.compile(
            loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

        x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=test_size, random_state=random_state)

        # Train the model
        model.fit(x_train, y_train, epochs=cls.NUM_EPOCHS, validation_data=(x_test, y_test), batch_size=64)

        return model
