# Multiple Linear Regression

Multiple linear regression (MLR) is a statistical technique that helps determine the relationship between a single dependent variable and multiple independent variables.

    ->The model plots a straight line after being trained on a training set and its performance is evaluated for a testing set. 
    ->It is different from Simple Linear Regression in terms of the number of input features. 
    ->It consists of multiple input features whereas the Simple Linear Regression takes only a single input feature.

Required python libraries: 1) numpy 2) matplotlib 3) pandas 4) sklearn

The python implementation uses the sklearn library to build a regression model which is trained with the training set.
## MLR

![App Screenshot](https://media.licdn.com/dms/image/D4D12AQFIJ_41MpAq2w/article-cover_image-shrink_720_1280/0/1692450132499?e=2147483647&v=beta&t=UWu2peXzF4N2Ki16pSOKDAe4lG1AjoMkylC0-_dePTU)

### used data : car_purchasing_data

we import the required libraries.And the data should be pre-processed before training the model.

    ->Every column should contain only numerical data.
    ->should not contain null values.
    ->Unnecessary columns should be removed.

we divide the data into two parts.

    1.independent columns
    2.dependent column

## splitting the data into training and test parts

    # from sklearn.model_selection import train_test_split 

By importing above function we split the entire data into four parts 

    1.independent training data
    2.independent test data
    3.dependent training data
    4.dependent test data 

## Introducing algorithm

An algorithm is a set of rules or procedures applied to data

    # from sklearn.linear_model import LinearRegression
An object is assigned for the LinearRegression class.

## Training the algorithm to get model

    ->fit() is used to train the algorithm and get the model as an outcome.

     Then the model is
     y = m1(x1) + m2x2 +....+ c
where,
        m = slope
        c = intercept

    
           
