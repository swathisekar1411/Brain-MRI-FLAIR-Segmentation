# Brain MRI FLAIR Segmentation (MLOps Project)

## Overview
This project focuses on **segmenting FLAIR (Fluid-Attenuated Inversion Recovery) abnormalities** in **brain MRI images**. The model utilizes **MobileNet v3** for lightweight yet effective segmentation, ensuring minimal memory footprint while maintaining high accuracy. The dataset used is the **LGG (Lower-Grade Glioma) MRI Segmentation dataset** from Kaggle.

This project follows **MLOps principles**, integrating tools like **DVC (Data Version Control)**, automated training pipelines, and model versioning.

## Features
- **Brain MRI FLAIR segmentation using deep learning**
- **Implementation of MLOps practices**, including DVC for dataset management
- **Model training using a MobileNet v3-based segmentation model**
- **Evaluation using Dice Coefficient and IoU metrics**
- **Streamlit-based web application** for inference
- **Automatic model checkpointing and versioning**
- **Inference pipeline for predicting segmentation masks on new MRI images**

## Dataset
The dataset used in this project comes from [Kaggle's Brain MRI Segmentation Dataset](https://www.kaggle.com/mateuszbuda/lgg-mri-segmentation). It includes:
- **MRI slices** (as images)
- **Ground truth masks** (to indicate abnormal regions)

## Project Structure
```plaintext
├── LICENSE
├── README.md               <- Documentation providing an overview of the project.
│
├── data
│   ├── processed           <- Final, structured datasets ready for modeling.
│   └── raw                 <- Original, unprocessed data for reference.
│
├── saved_models            <- Directory to store trained and serialized models.
│
├── inference               <- Scripts for running inference on new data.
│
├── report                  <- Logs and performance metrics from training.
│
├── images                  <- Visualizations, plots, and generated figures for analysis.
│
├── full-requirements.txt   <- Dependencies for reproducing the full development environment.
│
├── requirements.txt        <- Dependencies for the production/deployment environment.
│
├── dvc.yaml                <- DVC pipeline configuration file.
│
├── config.yaml             <- Configuration file with all training parameters.
│
├── src                     <- Main source code directory for this project.
│   ├── __init__.py         <- Marks `src` as a Python package.
│   ├── utils.py            <- Utility functions for common tasks.
│   ├── early_stopping.py   <- Implementation of early stopping to prevent overfitting.
│   │
│   ├── data                <- Scripts for data processing and loading.
│   │   ├── preprocess_data.py  <- Data preprocessing scripts.
│   │   └── dataset.py       <- Dataset class and loaders.
│   │
│   ├── models              <- Scripts for model training and optimization.
│   │   ├── train.py         <- Training script for the model.
│   │   └── optimize_graph.py <- Optimization techniques for performance improvements.
│
├── tests                   <- Unit and integration tests for project components.
│   ├── __init__.py         <- Marks `tests` as a Python package.
│   ├── config_test.py      <- Unit tests for validating `config.yaml`.
│
├── deployment              <- Files and scripts for deployment.
│   ├── Procfile            <- Deployment configuration for Heroku.
│   ├── setup.sh            <- Shell script for Heroku deployment setup.
│   ├── runtime.txt         <- Specifies the Python runtime version for Heroku.
│
└── tox.ini                 <- Configuration for running tests using Tox.