''' Convolution Neural Network Conv1D model '''
# Basic CNN structure (Conv1D) binary classifier w/ dropout to prevent overfitting
# metrics - aud for area under the curve, suitable for classification
# loss function - binary cross entry (standard binary classification)
# optimiser - Stochastic Gradient Descent
# sample weighting is added to as target class distribution favours non binding class

# function conv1d_model w/ argument to drop .Dropout 
def conv1d_model(drop_id=True):

    if(drop_id is False):
        model = keras.models.Sequential([
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu", 
                                input_shape=(101,4)),    
            keras.layers.Dropout(0.5),
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu"),
            keras.layers.Dropout(0.5),
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu"),
            keras.layers.Dropout(0.5),  
            keras.layers.Flatten(),
            keras.layers.Dense(1,activation='sigmoid')])
        return model
    
    # For Test without Dropout Layers
    if(drop_id is True):
        model = keras.models.Sequential([
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu", 
                                input_shape=(101,4)),    
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu"),
            keras.layers.Conv1D(15, 
                                kernel_size=10,
                                padding="same", 
                                activation="relu"),
            keras.layers.Flatten(),
            keras.layers.Dense(1,activation='sigmoid')])
        return model
    
test_seq = conv1d_model(drop_id=True)

''' KERAS METRICS '''
# Keras offers quite a few metrics we can call in compile

METRICS = [
    #   keras.metrics.TruePositives(name='tp'),
    #   keras.metrics.FalsePositives(name='fp'),
    #   keras.metrics.TrueNegatives(name='tn'),
    #   keras.metrics.FalseNegatives(name='fn'), 
#       keras.metrics.BinaryAccuracy(name='accuracy'),
#       keras.metrics.Precision(name='precision'),
#       keras.metrics.Recall(name='recall'),
      keras.metrics.AUC(name='auc')
    #   keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
]

# Compile Neural Network
test_seq.compile(
    optimizer='sgd',
    loss='binary_crossentropy',
    metrics=METRICS)

# Example Train Neural Network /w Sample Weighting 
hist = test_seq.fit(x=data.train['X'],              # feature matrix   
                   y=data.train['y'],              # target vector 
                   sample_weight=data.train['w'],  # weight vector
                   validation_data=(data.valid['X'],
                                    data.valid['y']), # validation data
            epochs = cfg.n_epochs,  # number of iterations
            batch_size = 512,      # batch size
            callbacks = [TqdmCallback(verbose=0)], # tqdm for keras
            verbose=0) # turn of training messages
