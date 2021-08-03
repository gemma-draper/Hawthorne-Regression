# Regression Project

## Introduction
This project is a continuation of Project Hawthorne, for which I wrote a Python web-scraper to collect drink recipes from user submitted recipe sites. The ultimate aim of Project Hawthorne is to create a recipe-generator bot which will invent, and then publish cocktail recipes to user-submitted websites.

For this regression project I applied supervised learning to solve a regression problem based on my own data. Several regression models were evaluated. The full evaluation process, including regularisation and hyperparameter tuning, is documented in the Jupyter notebooks in this repo. Results are displayed below.

## Project Brief & Deliverables

The project brief was to:
* Identify an industry relevant prediction problem.
* Develop a solution to this problem.
* Present the results.

Deliverables were:
* A GitHub repo containing all code.
* A presentation in two parts:
    1. **Non-technical presentation** highlighting the problem and the solution at a high level. This part explained the results that were attained and how they will drive business value.
    2. **Technical presentation** giving details of the techniques applied during data processing and modelling.

## Planning
### Identifying the Problem

The key criteria for excellence in cocktail making have been widely discussed by professional bartenders and mixologists. Among these criteria are:
- An eye catching or descriptive name.
- Quality ingredients in a unique formulation.
- A memorable story or interesting inspiration.
- The look.
- The purpose.

However, in the world of user-submitted recipe sites the criteria may be quite different. I hypothesize that:
- The simplest recipes are the most popular.
- Drinks containing familiar ingredients are more popular than those with unusual ingredients.
- Alcoholic drinks are more popular than non-alcoholic drinks.

### Stakeholders

Stakeholders for this project include:
- **Myself.** I plan to create a recipe-generator bot which will invent and publish cocktail recipes. The insights generated in this regression analysis will be vital in creating popular recipes.
- **Drinks manufacturers.** Many drinks manufacturers provide recipes to inspire and encourage the customer to buy their products. Understanding the driving forces behind recipe popularity will aid their recipe writing and may boost sales.

### Defining Success

This project investigates the hypotheses:
- The simplest recipes are the most popular.
- Drinks containing familiar ingredients are more popular than those with unusual ingredients.
- Alcoholic drinks are more popular than non-alcoholic drinks.

Using regression analysis, I will investigate recipe complexity, degree of familiarity, and alcohol content, and the impact these criteria have on the recipe popularity as shown in star rating. 

Success will be measured by :
- Identifying the most powerful of these influences on star rating.
- Selecting a model which can generalise well to unseen data.
- Being able to predict star rating of unseen data using recipe complexity, degree of familiarity, and alcohol content.

## Data
### Data Cleaning

Some data cleaning was performed in part one of [Project Hawthorne](https://github.com/gemma-draper/Project-Hawthorne). 

#### Ingredients & Method
For easy manipulation in Python, each recipe occupies a single row of a pandas DataFrame. The DataFrame contains 15 ingredients columns (`ingredient_0` to `ingredient_14`); recipes which have fewer than 15 ingredients contain null values in the unused ingredient columns. 

The same approach was used for the method; the DataFrame contains 11 method columns (`step_0` to `step_10`) and recipes with fewer steps contain null values in unused columns.

#### Star rating
Star rating did not always appear in integer or string format in recipes from allrecipes.co.uk. However, there was always a pictoral representation of star rating, and a class attribute description such as "rating4" or "rating45" for a star rating of 4 or 4.5, respectively. 

The following code was used to clean the class attribute:

```python
def clean_star_rating(messy):
    """
    Takes a string containing star rating.
    Removes all non-numeric chars.
    Returns star rating as float.
    """
    messy = re.sub('[^0-9]', "", messy)
    if len(messy) == 2:
        clean = float(messy[0] + "." + messy[1])
    else:
        clean = float(messy)
    return clean

star_rating_box = d.find_element('//span[contains(@class, "mediumStar")]')
messy_star_rating = star_rating_box.get_attribute('class')

clean_rating = clean_star_rating(messy_star_rating)
```

#### Ingredients
Each ingredient occupies an individual 

A random seed was applied at the start of the Jupyter notebook for the purposes of reproducibility.
## Modelling

## Presentation

## Code



