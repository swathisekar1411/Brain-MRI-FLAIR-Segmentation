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
│   ├── raw                 <- Original, unprocessed data.
│   ├── lgg-mri-segmentation.dvc <- DVC tracking file for dataset versioning.
│
├── images                  <- Visualizations, plots, and generated figures.
│   ├── logs.png
│   ├── predictions.png
│   ├── sample-1.png
│
├── inference               <- Scripts for running inference on new data.
│   ├── engine.py           <- Inference pipeline script.
│   ├── result.png          <- Sample inference output.
│   ├── ui.py               <- UI integration for visualization.
│
├── report                  <- Logs and performance metrics from training.
│   ├── metrics.json        <- Model evaluation metrics.
│
├── saved_models            <- Directory to store trained and serialized models.
│   ├── flair-segmentation.pt <- Saved model checkpoint.
│
├── src                     <- Main source code directory for this project.
│   ├── __init__.py         <- Marks `src` as a Python package.
│   ├── dataset.py          <- Dataset class and loaders.
│   ├── early_stopping.py   <- Implementation of early stopping to prevent overfitting.
│   ├── optimize_graph.py   <- Optimization techniques for performance improvements.
│   ├── preprocess_data.py  <- Data preprocessing scripts.
│   ├── train.py            <- Training script for the model.
│   ├── utils.py            <- Utility functions for common tasks.
│
├── tests                   <- Unit and integration tests for project components.
│   ├── __init__.py         <- Marks `tests` as a Python package.
│   ├── config_test.py      <- Unit tests for validating `config.yaml`.
│
├── config.yaml             <- Configuration file with all training parameters.
├── dvc.lock                <- Lock file for DVC.
├── dvc.yaml                <- DVC pipeline configuration file.
├── full-requirements.txt   <- Dependencies for reproducing the full development environment.
├── requirements.txt        <- Dependencies for the production/deployment environment.
├── setup.sh                <- Shell script for deployment setup.
├── template.py             <- Placeholder template for additional scripts.
├── tox.ini                 <- Configuration for running tests using Tox.