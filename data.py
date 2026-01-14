import csv
import os

def create_or_update_dataset():
    dataset_file = 'homekitchen_dataset.csv'

    # Check if the dataset file already exists
    dataset_exists = os.path.exists(dataset_file)

    # Get dish information from the user
    dish_name = input("Enter Dish Name: ")
    ingredients_1 = input("Enter Ingredients Set 1 (comma-separated): ")
    ingredients_2 = input("Enter Ingredients Set 2 (comma-separated): ")
    ingredients_3 = input("Enter Ingredients Set 3 (comma-separated): ")
    nutrients = input("Enter Nutrients: ")
    health_info = input("Enter Health Info: ")
    culture = input("Enter Culture: ")

    # Create or update the dataset
    with open(dataset_file, 'a', newline='') as file:
        fieldnames = ['DishName', 'Ingredients1', 'Ingredients2', 'Ingredients3', 'Nutrients', 'HealthInfo', 'Culture']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the dataset is created for the first time
        if not dataset_exists:
            writer.writeheader()

        # Write the new dish information
        writer.writerow({
            'DishName': dish_name,
            'Ingredients1': ingredients_1,
            'Ingredients2': ingredients_2,
            'Ingredients3': ingredients_3,
            'Nutrients': nutrients,
            'HealthInfo': health_info,
            'Culture': culture,
        })

    print(f"The dish '{dish_name}' has been added to the dataset.")

if __name__ == "__main__":
    create_or_update_dataset()
