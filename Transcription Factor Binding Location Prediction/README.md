## Transcription Factor Binding Location Prediction 

### Main Editing Location
- [Kaggle Notebook](https://www.kaggle.com/shtrausslearning/transcription-factor-binding-location-prediction)
- Status: Work in Progress

### Binding Site Location Prediction Model
- Binary classification problem, aiming to predict transcription factor binding sides in the DNA

### Tested CNN Models
- <code>baseline model (BL)</code> - DNA sequence model uses feature matrix constructed from OHE of the four bases in each segment sequence
- <code>BL(no sample weighting)</code> - investigation into whether class imbalance affects the model & was our assumption to weight samples correct
- <code>BL(no dropout)</code> - investigation into whether removing dropout will cause the cnn model to overfit in this problem
- <code>accessibility model</code> - Accessibility of each dna segment added to the baseline feature matrix

### File Listings 
Some parts of the notebook for reusability
- <code>dnaseq_ohe.py</code> - One-Hot-Encoding of DNA sequences for ML applications
- <code>plot_keras_history.py</code> - Function to plot Keras History, uses Plotly
- <code>keras_classifier.py</code> - Keras Binary CNN Classifier Model
- <code>transcription-factor-binding-location-prediction.ipynb</code> - Storage of latest version (<code>v8</code>)
