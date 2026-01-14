from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Sample dataset (replace with your actual dataset file)
dataset_file = 'dataset.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    # Read the dataset and pass it to the template
    dish_list = read_dataset()
    return render_template('menu.html', dish_list=dish_list)

@app.route('/add_dish', methods=['POST'])
def add_dish():
    # Get dish details from the form
    dish_name = request.form['dishName']
    ingredients = request.form['ingredients']
    nutrients = request.form['nutrients']
    health_info = request.form['healthInfo']
    culture = request.form['culture']

    # Add the new dish to the dataset
    add_to_dataset(dish_name, ingredients, nutrients, health_info, culture)

    # Redirect back to the menu page
    return redirect(url_for('menu'))

def read_dataset():
    # Read the dataset from the CSV file
    try:
        with open(dataset_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def add_to_dataset(dish_name, ingredients, nutrients, health_info, culture):
    # Add a new row to the dataset
    fieldnames = ['DishName', 'Ingredients', 'Nutrients', 'HealthInfo', 'Culture']
    with open(dataset_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'DishName': dish_name,
            'Ingredients': ingredients,
            'Nutrients': nutrients,
            'HealthInfo': health_info,
            'Culture': culture,
        })

if __name__ == '__main__':
    app.run(debug=True)
