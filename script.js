// static/script.js (JavaScript)

function addDish() {
    // Placeholder for adding dish logic
    const dishName = document.getElementById('dishName').value;
    const ingredients = document.getElementById('ingredients').value;

    // You can handle AJAX or fetch request to the server here
    // Example using fetch:
    fetch('/add_dish', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ dishName, ingredients }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server (e.g., update dish list)
        updateDishList(data);
    })
    .catch(error => console.error('Error:', error));
}

function filterDishes(category) {
    // Placeholder for filtering logic
    // You can handle AJAX or fetch request to the server here
    // Example using fetch:
    fetch(`/filter_dishes/${category}`)
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server (e.g., update dish list)
        updateDishList(data);
    })
    .catch(error => console.error('Error:', error));
}

function resetFilters() {
    // Placeholder for resetting filters logic
    // You can handle AJAX or fetch request to the server here
    // Example using fetch:
    fetch('/reset_filters')
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server (e.g., update dish list)
        updateDishList(data);
    })
    .catch(error => console.error('Error:', error));
}

function updateDishList(data) {
    // Placeholder for updating the dish list in the UI
    const dishList = document.getElementById('dishList');
    dishList.innerHTML = '';

    data.forEach(dish => {
        const listItem = document.createElement('li');
        listItem.textContent = dish.name + ' - ' + dish.category;
        dishList.appendChild(listItem);
    });
}
