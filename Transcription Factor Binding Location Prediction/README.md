## Transcription Factor Binding Location Prediction 

### [Kaggle Notebook](https://www.kaggle.com/shtrausslearning/transcription-factor-binding-location-prediction)
![](https://camo.githubusercontent.com/d38e6cc39779250a2835bf8ed3a72d10dbe3b05fa6527baa3f6f1e8e8bd056bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652d507974686f6e2d696e666f726d6174696f6e616c3f7374796c653d666c6174266c6f676f3d707974686f6e266c6f676f436f6c6f723d776869746526636f6c6f723d326262633861) ![](https://badgen.net/badge/status/WIP/orange) 

### Binding Site Location Prediction Model
- Binary classification problem, aiming to predict transcription factor binding sides in the DNA

### Problem Relevance
- Transcription Factor Binding affects Protein production 

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
