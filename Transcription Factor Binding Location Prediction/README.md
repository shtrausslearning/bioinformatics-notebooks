## Transcription Factor Binding Location Prediction 
- [Kaggle Notebook](https://www.kaggle.com/shtrausslearning/transcription-factor-binding-location-prediction)

### Binding Site Location Prediction Model
- Binary classification problem, aiming to predict transcription factor binding sides in the DNA

### Tested CNN Models
- <code>baseline model</code> - DNA sequence model uses feature matrix constructed from OHE of the four bases in each segment sequence
- <code>accessibility model</code> - Accessibility of each dna segment added to the baseline feature matrix

### File Listings 
- <code>dnaseq_ohe.py</code> - One-Hot-Encoding of DNA sequences for ML applications
- <code>plot_keras_history.py</code> - Function to plot Keras History, uses Plotly
- <code>keras_classifier.py</code> - Keras Binary CNN Classifier Model
- <code>transcription-factor-binding-location-prediction.ipynb</code> - Storage of latest version
