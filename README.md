# **Diamond Price Prediction**

## Introduction
This project aims to predict the price of diamonds using regression analysis. The dataset used for this purpose is sourced from Kaggle. The primary objective is to build a predictive model that can accurately estimate the price of a given diamond based on various diamond characteristics. The project utilizes modular coding and a well-structured approach, with automated pipelines for both training and prediction phases.

## About The Data
The dataset includes the following 10 independent variables, including a unique identifier id, and the target variable price:

- id: A unique identifier for each diamond.
- carat: Carat (ct.), which represents the weight of the diamond.
- cut: Quality of the diamond cut.
- color: Color of the diamond.
- clarity: Diamond clarity, graded by visibility of characteristics under 10-power magnification.
- depth: The height of the diamond in millimeters, from culet to table.
- table: The facet visible when the diamond is viewed face up.
- x: Diamond X dimension.
- y: Diamond Y dimension.
- z: Diamond Z dimension.

**Target Variable**
- price: The price of the given diamond.

## Methodology
In this project, we implement modular coding practices to ensure a well-structured and automated workflow. We create two primary pipelines: a training pipeline and a prediction pipeline. The goal is to streamline the entire process from data preparation to model deployment.To enhance code robustness and maintainability, we implement logging and exception handling mechanisms, ensuring a smooth and error-free execution of the project.

## Regression Model
We explore various regression models, including Linear Regression, Lasso Regression, Ridge Regression, Elastic Net, and Decision Tree Regression. After thorough evaluation, the Decision Tree model outperformed the others with an impressive R-squared (R²) score of 0.954266, making it the model of choice for this project.





