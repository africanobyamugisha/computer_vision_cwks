# 🚦 Traffic Monitoring System using Traditional Machine Learning

## Overview

This project aims to develop a traffic monitoring system using traditional machine learning techniques. The system detects motorcycles and trucks in a video feed and utilizes various machine learning models for classification.


## Introduction

The project involves designing and formulating a traffic monitoring tool based on traditional machine learning techniques such as KNN, SVM, Decision Trees, Random Forest, and Logistic Regression. The system analyzes video footage to identify motorcycles and trucks for traffic monitoring purposes.

## Dataset Acquisition

### 📹 Video Source

The video source for the project is `data/traffic_output.avi`.

## Data Preprocessing and Annotation

### ✍️ Image Annotation

Frames from the video are extracted and annotated to label motorcycles and trucks for training purposes. CVAT, a self-hosted annotation tool, was used in a Docker environment on Linux (WSL).

## Feature Extraction

### 📊 Identified Features

- Color histograms
- Edges
- SIFT (Scale-Invariant Feature Transform)
- SURF (Speeded-Up Robust Features)
- Pixel values

## Model Training

### 🤖 Traditional Machine Learning Models

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Trees
- Random Forest
- Logistic Regression

## Model Evaluation

Performance metrics such as confusion matrices, AUC, Precision, Recall, and F1 score are used to evaluate the trained models.

## Ensemble Model Building

The top three performing models are selected to build an ensemble model using techniques like voting or averaging.

## Results Comparison

The performance of the ensemble model is compared with individual models to assess improvement.

## Future Work

Suggestions for future work include enhancements to the system, such as incorporating deep learning techniques for improved accuracy and efficiency.

