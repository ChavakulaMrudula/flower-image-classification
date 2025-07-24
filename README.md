# 🌸 Flower Classification using CNN

## 📌 Introduction
Flower classification involves identifying the species of a flower from its image. This is a challenging task due to:
- Wide diversity of flower species
- Varying lighting and background conditions
- Different angles and image quality

**Convolutional Neural Networks (CNNs)** are well-suited for this task due to their powerful feature extraction capabilities.

---

## 🔑 Keywords
- Flower Recognition  
- Convolutional Neural Networks (CNNs)  
- TensorFlow  
- Image Classification  

---

## 📂 Dataset
- Publicly available flower dataset (e.g., IRIS dataset from Kaggle)
- Multiple classes with sufficient images per class

### 🧹 Data Preprocessing
- Resize all images to 128×128 pixels
- Normalize pixel values to [0, 1] by dividing by 255
- Split dataset into training, validation, and test sets

---

## ❓ Problem Statement
Develop a robust CNN model to classify flower species from digital images based on:
- Color  
- Petal shape  
- Texture  

### 🎯 Target
Achieve at least **90% accuracy** on a diverse test dataset under various conditions like:
- Lighting variation  
- Background noise  
- Angled views

---

## 🏗️ Model Architecture

### Layers Used:
- **Conv2D Layers**: Feature extraction with ReLU activation  
- **MaxPooling2D Layers**: Downsample feature maps  
- **Flatten Layer**: Convert 2D feature maps to 1D  
- **Dense Layers**: Fully connected layers with ReLU and final softmax for classification

---

## 📈 Output
The CNN model using TensorFlow successfully:
- Identified and classified flower species
- Achieved high accuracy on test data
- Proved effective for image recognition tasks

---

## ✅ Conclusion
The integration of CNNs and TensorFlow offers:
- Efficient, scalable, and accurate flower classification
- Applications in agriculture, conservation, and botanical research
