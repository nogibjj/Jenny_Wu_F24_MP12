from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Your API Key for Spoonacular (or chosen API)
API_KEY = 'your_api_key_here'
API_URL = 'https://api.spoonacular.com/recipes/findByIngredients'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    ingredients = request.form.get('ingredients')
    if not ingredients:
        return redirect(url_for('index'))
    
    # Call the Recipe API
    response = requests.get(API_URL, params={
        'ingredients': ingredients,
        'number': 5,  # Number of recipes to fetch
        'apiKey': API_KEY
    })
    recipes = response.json() if response.status_code == 200 else []
    
    return render_template('recommendations.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
