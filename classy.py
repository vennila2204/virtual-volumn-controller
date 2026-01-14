# Import necessary libraries
from flask import Flask, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

app = Flask(__name__)

# Load your existing dataset from the CSV file
dataset_path = 'your_dataset.csv'  # Replace with the actual path to your dataset
df = pd.read_csv(dataset_path)

# Assume you have a 'DishName' and 'Ingredients' columns in your dataset

# Preprocess the data and train a simple classifier
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Ingredients'])
y = df['Category']  # Replace 'Category' with the actual column containing categories

classifier = MultinomialNB()
classifier.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html', dishes=df['DishName'])

@app.route('/classify/<dish_name>')
def classify_dish_page(dish_name):
    # Get the ingredients for the selected dish
    ingredients = df[df['DishName'] == dish_name]['Ingredients'].values[0]

    # Vectorize the ingredients
    ingredients_vectorized = vectorizer.transform([ingredients])

    # Predict the category
    category = classifier.predict(ingredients_vectorized)[0]

    return render_template('classify.html', dish_name=dish_name, ingredients=ingredients, category=category)

if __name__ == '__main__':
    app.run(debug=True)
