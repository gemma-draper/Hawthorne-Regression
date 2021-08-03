from nltk import ngrams
from nltk.corpus import stopwords
import nltk
# nltk.download('stopwords')
import pandas as pd
import re
from sqlalchemy import create_engine
import csv
from operator import itemgetter

def get_data():
    """
    Get all from all_recipes table.
    Returns a pandas DataFrame.
    Requires credentials.txt file in the same dir with database credentials.
    """

    # get aws rds credentials from txt file
    credentials = []
    with open('credentials.txt','r') as f:
        credentials = eval(f.read())


    user, password, host, port, database = itemgetter('user', 'password', 'host', 'port', 'database')(credentials)

    # create sqlalchemy engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # get all data
    df = pd.read_sql_query("SELECT * FROM all_recipes", engine)
    
    df.set_index('id', inplace=True)

    return df

class Ingredients_Cleaning:
    def __init__(self) -> None:
        pass

    def get_ingredients_tokens(self, df):
        """
        Input: recipe dataframe.
        Output: list of ingredient tokens.
        Output has not been cleaned.
        """
        # filter df ingredient cols
        ingredient_df = df.filter(like="ingredient", axis=1)

        # add all the ingredients to a list
        ingredients_list = []
        for col in ingredient_df.columns:
            ingredients_list += ingredient_df[col].to_list()

        # remove nulls
        ingredients_list = [ele for ele in ingredients_list if ele]

        tokens = []
        for element in ingredients_list:
            gram = ngrams(element.split(), n=1)  
            tokens.extend(element.split())

        # remove non alpha-numeric characters, like trade marks and hyphens
        tokens = [re.sub("[^a-zA-Z0-9]","",token) for token in tokens]
        return tokens


    def has_numbers(self, input):
        """
        Returns true if input string contains digits.
        """
        return any(char.isdigit() for char in input)

    def remove_numbers_and_make_lower_case(self, tokens):
        """
        Removes tokens containing numbers and returns list of lower case tokens"""
        tokens = [token.lower() for token in tokens if not has_numbers(token)]

    def remove_stopwords(self, tokens):

        # define stopwords
        stop_words = stopwords.words('english')
        more_stop_words = [
            "tablespoons",
            "tablespoon",
            "cubes",
            "cube",
            "chopped",
            "cupful",
            "cupfuls",
            "cupsfull",
            "crushed",
            "needed",
            "ground",
            "sliced",
            "slice",
            "slices",
            "halved",
            "half",
            "halves",
            "single",
            "pinch",
            "pinches",
            "optional",
            "large",
            "small",
            "medium",
            "litre",
            "litres",
            "liter",
            "liters",
            "l",
            "leaves",
            "leaf",
            "fl",
            "oz",
            "ml",
            "g",
            "tin",
            "quality",
            "washed",
            "extract",
            "measure",
            "measures",
            "whole",
            "juiced",
            "powder",
            "cut",
            "chunk",
            "chunks",
            "bottle",
            "",
            "bottles",
            "cold",
            "boiling",
            "warm",
            "hot",
            "piece", 
            "pieces",
            "stick",
            "sticks",
            "juice",
            "teaspoon",
            "teaspoons",
            "peeled",
            "chilled",
            "soft",
            "dash",
            "fruit",
            "ripe",
            "dark",
            "light",
            "shot",
            "shots",
            "removed",
            "sweetened",
            "unsweetened",
            "handful",
            "squeezed",
            "cored",
            "tbsp",
            "tbsps",
            "tsp",
            "tsps",
            "mix",
            "mixture",
            "wedge",
            "broken",
            "splash",
            "roughly",
            "fresh",
            "flavoured",
            "quartered",
            "taste"
        ]
        stop_words.extend(more_stop_words)       

        # remove common stopwords from tokens 
        tokens = [token for token in tokens if not token in stop_words]
        return tokens

    def get_word_frequencies(self, tokens):
        """
        Counts tokens, returning dictionary of words and their frequencies.
        """
        word_freq = {}
        for token in tokens:
            if token not in word_freq.keys():
                word_freq[token] = 1
            else:
                word_freq[token] += 1
        return word_freq

    def display_word_freq(self, word_freq):
        """
        Dislays the sorted word frequency dictionary.
        """
        word_freq = sorted(word_freq.items(), key=lambda x: x[1])
        print(word_freq)
        

    def ingredient_user_input(self, word_freq):
        """
        Input: word_freq dictionary (Bag of Words) containing words and their frequency.
        Requests user input to separate ingredients from stopwords.
        Output: list of ingredients.
        """
        ingredients = []
        for k in word_freq:
            user_input = input(f"Is this an ingredient? N or leave blank for Y. {k}")
            if not len(user_input):
                ingredients.append(k)

    def ingredients_to_csv(self, ingredients):
        """
        Write ingredients list to csv
        """
        with open('ingredients.csv', 'w') as f:
            writer = csv.writer(f)
            for item in ingredients:
                writer.writerow([item])
