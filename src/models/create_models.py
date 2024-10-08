import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D




def create_cnn_model(
    input_shape,
    num_classes,
    metrics =['accuracy'],
    kernel_size =(3,3),
    loss_func = "categorical_crossentropy",
    optimizer = "adadelta",
    polling = True
):
    
    model = Sequential()
    model.add(Conv2D(32, kernel_size=kernel_size,
                    activation='relu',
                    input_shape=input_shape))
    model.add(Conv2D(64, kernel_size, activation='relu'))
    if polling:
        model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=loss_func,
                optimizer=optimizer,
                metrics=metrics)
    
    return model

def create_fcnn_model(
    input_shape,
    num_classes,
    metrics=['accuracy', 'f1_score'],
    loss_func="categorical_crossentropy",
    optimizer="adadelta"
):
    model = Sequential()
    model.add(Flatten(input_shape=input_shape))  # Camada Flatten para transformar a entrada em 1D
    model.add(Dense(1024, activation='relu'))    # Primeira camada densa com mais neurônios
    model.add(Dropout(0.25))                     # Dropout para evitar overfitting
    model.add(Dense(512, activation='relu'))     # Segunda camada densa
    model.add(Dropout(0.5))                      # Outro Dropout
    model.add(Dense(num_classes, activation='softmax'))  # Camada de saída

    model.compile(loss=loss_func,
                  optimizer=optimizer,
                  metrics=metrics)
    
    return model
