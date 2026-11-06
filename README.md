# Shoe Size Prediction Using Linear Regression

**Group Assignment 2 – Project-Based Learning (PBL) | Machine Learning**

A Machine Learning project that implements **Linear Regression** to predict shoe size based on a person's height. This project explores the relationship between height and shoe size through data analysis, model training, prediction, and performance evaluation.

---

## 1. Project Overview

This project aims to develop a predictive model using the Linear Regression algorithm to estimate shoe size based on height.

The model learns the relationship between two variables from a dataset containing height and shoe size observations. After training, the model can generate predictions for new height inputs.

The implementation is developed using Python and Scikit-learn, with Google Colab as the development environment.

## 2. Project Objectives

The main objectives of this project are:

- Understand the fundamentals of supervised Machine Learning.
- Implement the Linear Regression algorithm for a regression problem.
- Perform Exploratory Data Analysis (EDA) to understand the dataset.
- Identify the relationship and correlation between height and shoe size.
- Train and test a predictive model using a dataset.
- Evaluate model performance using regression evaluation metrics.
- Generate shoe size predictions based on new input data.

## 3. Technology Stack

The project utilizes the following technologies and Python libraries:

| Technology | Description |
|---|---|
| Python | Primary programming language |
| Google Colab | Cloud-based development environment |
| NumPy | Numerical computing and array manipulation |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| Scikit-learn | Machine Learning model development and evaluation |
| SciPy | Scientific and statistical computing |

## 4. Dataset Description

The dataset is provided in CSV format and contains two primary variables used for model development.

| Variable | Type | Description |
|---|---|---|
| X | Independent Variable | Height |
| Y | Dependent Variable | Shoe Size |

**Dataset Source:** [Google Drive – Shoe Size Dataset](https://drive.google.com/uc?id=12y4yjLottmCkwRcky7uH_3lneQluY5tC)

The dataset is loaded into the Python environment using Pandas and subsequently processed for exploratory analysis and model training.

## 5. Methodology

This project follows a structured Machine Learning workflow consisting of the following stages:

### 5.1 Data Loading and Preparation

- Import the required Python libraries.
- Connect Google Colab to Google Drive.
- Load the CSV dataset using Pandas.
- Define the independent and dependent variables.

### 5.2 Exploratory Data Analysis (EDA)

EDA is performed to understand the characteristics, distribution, and relationships within the dataset.

The analysis includes:

- **Kernel Density Estimation (KDE):** Examines the distribution of height and shoe size.
- **Boxplot:** Identifies data distribution and potential outliers.
- **Scatter Plot:** Visualizes the relationship between height and shoe size.
- **Correlation Analysis:** Measures the correlation between the independent and dependent variables.

### 5.3 Data Splitting

The dataset is divided into training and testing subsets using Scikit-learn's `train_test_split()` function.

| Dataset | Proportion |
|---|---:|
| Training Data | 65% |
| Testing Data | 35% |

The training dataset is used to build the model, while the testing dataset is used to evaluate its predictive performance.

### 5.4 Model Development

The project uses the **Linear Regression** algorithm implemented through Scikit-learn.

The model is initialized using:

```python
regressor = linear_model.LinearRegression()
```

### 5.5 Model Training

The model is trained using the training dataset through the `fit()` method.

During this process, the algorithm learns the linear relationship between height and shoe size by determining the optimal regression coefficients.

### 5.6 Regression Equation

After training, the model produces two important parameters:

- **Coefficient (M):** Represents the slope of the regression line.
- **Intercept (b):** Represents the constant value of the regression equation.

The resulting prediction equation is:

\[
Y = M X + b
\]

Where:

- Y = Predicted shoe size.
- X = Height.
- M = Regression coefficient.
- b = Intercept.

### 5.7 Model Evaluation

Model performance is evaluated using the testing dataset and the following regression metrics:

| Evaluation Metric | Description |
|---|---|
| MAE (Mean Absolute Error) | Measures the average absolute difference between actual and predicted values. |
| MSE (Mean Squared Error) | Measures the average squared difference between actual and predicted values. |
| Median Absolute Error | Measures the median absolute difference between actual and predicted values. |
| R² Score | Measures how well the model explains the variance in the target variable. |

These metrics provide insights into the accuracy and predictive performance of the developed model.

### 5.8 Prediction and Visualization

After the training and evaluation stages, the model is used to predict shoe size based on new height data.

Example input:

```python
tinggi_badan = 164.5
```

The model generates a predicted shoe size using the trained regression parameters.

A scatter plot is also generated to compare actual testing values with the regression line.

### 5.9 Actual vs. Predicted Comparison

The final stage generates a comparison table containing:

- Height.
- Actual Shoe Size.
- Predicted Shoe Size.

This comparison helps assess the difference between actual observations and the model's predictions.

## 6. Project Workflow

The overall Machine Learning workflow is illustrated below:

```text
Dataset (CSV)
      |
      v
Data Loading & Preparation
      |
      v
Exploratory Data Analysis
      |
      v
Feature & Target Selection
      |
      v
Train-Test Split (65:35)
      |
      v
Linear Regression Model
      |
      v
Model Training
      |
      v
Model Evaluation
      |
      v
New Data Prediction
      |
      v
Actual vs. Predicted Comparison
```

## 7. Repository Structure

```text
shoe-size-prediction/
│
├── README.md
│
└── Prediksi_Ukuran_Sepatu.ipynb
```

| File | Description |
|---|---|
| `README.md` | Project documentation. |
| `Prediksi_Ukuran_Sepatu.ipynb` | Jupyter Notebook containing the complete Machine Learning implementation. |

## 8. Installation and Execution

This project can be executed directly using Google Colab without requiring a local Python environment.

**Execution Steps:**

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload or open the project notebook.
3. Ensure the dataset is accessible through the provided Google Drive link.
4. Run the notebook cells sequentially.
5. Review the EDA visualizations, regression equation, evaluation metrics, and prediction results.

**Dependencies:**

```bash
pip install numpy pandas matplotlib scikit-learn scipy
```

## 9. Expected Outcomes

Upon successful execution, the project produces the following outputs:

1. Statistical and visual analysis of the dataset.
2. Correlation analysis between height and shoe size.
3. A trained Linear Regression model.
4. A linear regression equation based on the training data.
5. Model evaluation results using MAE, MSE, Median Absolute Error, and R² Score.
6. Shoe size predictions based on new height inputs.
7. A comparison between actual and predicted values.

## 10. Limitations

This project uses a simple Linear Regression model with height as the only independent variable.

Therefore, the prediction results depend on the quality, quantity, and distribution of the available dataset. Other factors that may influence shoe size are not included in the model.

The model is intended for educational purposes and demonstrates the fundamental application of regression in Machine Learning.

---

## Project Information

| Attribute | Details |
|---|---|
| Project | Shoe Size Prediction |
| Category | Machine Learning |
| Algorithm | Linear Regression |
| Learning Type | Supervised Learning |
| Problem Type | Regression |
| Development Environment | Google Colab |
| Programming Language | Python |
| Assignment | Group 2 – Project-Based Learning |

**Developed as part of the Group 2 Project-Based Learning (PBL) assignment.**
