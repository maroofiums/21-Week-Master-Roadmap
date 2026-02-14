# **21-Week Complete Master Roadmap**

---

## **Week 1: Python & Data Foundations**

**Goal:** Master Python & data handling.
**Topics:**

* Python OOP, functions, decorators, lambda, map/filter, list comprehension
* NumPy, Pandas
* Data visualization: Matplotlib, Seaborn
* Statistics: mean, median, variance, correlation

**Practice/Projects:**

* Titanic dataset EDA
* Correlation heatmaps & distribution plots

**Tip:** Write **reusable preprocessing functions**; they’ll help in ML pipelines.

---

## **Week 2: Math & Stats for ML**

**Goal:** Build math foundation.
**Topics:**

* Linear algebra: vectors, matrices, dot product
* Probability basics & Bayes theorem
* Calculus: derivatives & gradients
* Statistical distributions: normal, uniform, binomial

**Practice/Projects:**

* Linear regression from scratch
* Probability simulations in Python

---

## **Week 3: Machine Learning Basics**

**Goal:** Supervised learning & metrics.
**Topics:**

* Linear & Logistic Regression
* KNN, Decision Trees
* Train/test split, evaluation metrics (accuracy, precision, recall, F1)
* Feature scaling & encoding

**Practice/Projects:**

* House price prediction
* Titanic survival prediction

---

## **Week 4: Advanced ML**

**Goal:** Ensemble methods & evaluation.
**Topics:**

* Random Forest, Gradient Boosting (XGBoost, LightGBM)
* SVM
* Cross-validation, hyperparameter tuning
* Confusion matrix, ROC-AUC

**Practice/Projects:**

* Credit approval model
* Customer segmentation

---

## **Week 5: ML Pipelines**

**Goal:** Production-ready pipelines.
**Topics:**

* Pipeline concept: preprocessing → modeling → evaluation
* `sklearn.pipeline` & `ColumnTransformer`
* Feature selection in pipelines
* Hyperparameter tuning & cross-validation
* Saving/loading pipelines (joblib)

**Practice/Projects:**

* Loan approval ML pipeline
* Titanic full ML pipeline

**Tip:** Treat preprocessing + model as **one unit** for production.

---

## **Week 6: Deep Learning Foundations (PyTorch)**

**Goal:** Neural networks basics.
**Topics:**

* Perceptron, activation functions (ReLU, Sigmoid, Tanh)
* Forward/backward propagation
* Loss functions & gradient descent
* PyTorch: tensors, autograd, optimizers, DataLoader

**Practice/Projects:**

* MNIST digit classification (MLP)

---

## **Week 7: CNN Basics**

**Goal:** Image modeling with CNNs.
**Topics:**

* Convolution, pooling, flatten, fully connected
* CNN architecture basics
* PyTorch training workflow

**Practice/Projects:**

* CIFAR-10 classification

---

## **Week 8: Advanced CNN & Pretrained Models**

**Goal:** Transfer learning & advanced architectures.
**Topics:**

* Pretrained CNNs: ResNet, VGG, EfficientNet, MobileNet
* Fine-tuning pretrained models
* Data augmentation
* PyTorch best practices: training loops, checkpoints

**Practice/Projects:**

* Flower classification with transfer learning
* Visualize intermediate CNN layers

---

## **Week 9: Computer Vision Basics (OpenCV)**

**Goal:** Image preprocessing & feature extraction.
**Topics:**

* OpenCV: read/write images, resize, crop
* Filters, thresholding, edge detection
* Contours, ORB/SIFT features
* Color space conversions

**Practice/Projects:**

* Preprocess images for CNN
* Edge & feature detection

---

## **Week 10: Computer Vision Advanced**

**Goal:** Object detection & video analytics.
**Topics:**

* Object detection: Haar cascades, YOLO-tiny
* Video capture & frame processing
* Object tracking (Centroid, OpenCV trackers)
* Real-time detection

**Practice/Projects:**

* Face mask detection (video)
* Real-time object tracker

---

## **Week 11: NLP Fundamentals**

**Goal:** Classic NLP preprocessing & text classification.
**Topics:**

* Tokenization, stopwords, stemming, lemmatization
* Bag-of-Words, TF-IDF
* Text classification (spam/ham)
* Sentiment analysis

**Practice/Projects:**

* Spam classifier
* Twitter sentiment analysis

---

## **Week 12: NLP Advanced**

**Goal:** Transformers & embeddings.
**Topics:**

* Word embeddings: Word2Vec, GloVe
* Transformers: BERT, DistilBERT, HuggingFace
* Sequence-to-sequence: summarization, translation
* Fine-tuning small pretrained models

**Practice/Projects:**

* Text summarizer (BERT)
* Basic chatbot using HuggingFace

---

## **Week 13: Time Series Forecasting (Classical)**

**Goal:** ARIMA/SARIMA & basics.
**Topics:**

* Decomposition: trend, seasonality
* Stationarity & differencing
* AR, MA, ARMA, ARIMA, SARIMA
* Evaluation metrics: MAE, MSE, RMSE

**Practice/Projects:**

* Stock price forecasting
* Sales forecasting with classical models

---

## **Week 14: Time Series Forecasting (ML/DL)**

**Goal:** LSTM & GRU networks.
**Topics:**

* LSTM & GRU architecture
* Multi-step forecasting
* Feature engineering for sequences
* PyTorch implementation

**Practice/Projects:**

* Weather forecasting using LSTM
* Compare ARIMA vs LSTM

---

## **Week 15: Databases & Integration**

**Goal:** Store, query, and connect ML/DL pipelines.
**Topics:**

* SQL: MySQL/PostgreSQL (joins, group by, indexing)
* NoSQL: MongoDB (JSON storage, queries)
* Python integration: SQLAlchemy, PyMongo
* Deploy ML pipelines with DB

**Practice/Projects:**

* CRUD API for ML predictions
* Store historical time series

---

## **Week 16: Generative AI Basics**

**Goal:** HuggingFace text generation.
**Topics:**

* GenAI concepts: text generation, tokenization
* HuggingFace GPT2/T5 pipelines
* Fine-tuning small models

**Practice/Projects:**

* Text generation chatbot
* Poetry/story generation

---

## **Week 17: Generative AI Advanced**

**Goal:** Multi-modal generation.
**Topics:**

* Image generation: HuggingFace Stable Diffusion, DALL·E
* Prompt engineering & pipelines
* Fine-tuning & dataset prep

**Practice/Projects:**

* AI art generation
* Multi-modal story creation

---

## **Week 18: Deep Learning Advanced Topics**

**Goal:** Modern DL architectures.
**Topics:**

* Attention mechanisms & transformers for CV & sequences
* UNet for segmentation
* Faster-RCNN for object detection
* PyTorch Lightning basics

**Practice/Projects:**

* Image segmentation (UNet)
* Custom object detection (Faster-RCNN)

---

## **Week 19: End-to-End ML/DL Capstone**

**Goal:** Full workflow projects.
**Project Ideas:**

* Loan Approval API (ML + DB + FastAPI)
* Face Mask Detection (CV + DL)
* Sentiment Dashboard (NLP + Streamlit)
* Stock/Sales Forecasting (Time series + DB)

---

## **Week 20: Generative AI Capstone**

**Goal:** Showcase GenAI skills.
**Project Ideas:**

* Chatbot with HF GPT + DB
* AI-generated art gallery + text descriptions
* Multi-modal story app

---

## **Week 21: Portfolio & Deployment**

**Goal:** Polish projects & deploy.
**Topics:**

* Deployment: FastAPI/Flask + Docker
* Model saving/loading
* GitHub portfolio preparation
* Streamlit/Dash dashboards
* Optional cloud hosting (AWS/GCP)

---

### ✅ **General Advice**

* Master **PyTorch for DL** and **pretrained models**.
* ML pipelines = production-readiness; don’t skip them.
* CV = preprocessing + DL combination.
* GenAI = pipelines + prompt engineering.
* Document every project; GitHub clarity = key for jobs.
* One **small polished project per domain** is better than many unfinished ones.
