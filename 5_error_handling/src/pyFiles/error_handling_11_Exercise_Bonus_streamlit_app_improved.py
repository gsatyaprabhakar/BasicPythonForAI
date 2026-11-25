import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def generate_recipe(ingredients, cuisine, diet):
    prompt = f'''
    Generate one food recipe using these ingredients: {ingredients}
    Recipe should not be more than 100 words
    Cuisine: {cuisine}
    Diet: {diet}
    '''
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        if not response.text:
            return "The model returned an empty response. Please try again."
        return response.text
    except Exception as e:
        # Network down, bad API key, rate limit, etc.
        return f"Sorry, couldn't generate a recipe right now. ({e})"

st.title("Recipe Generator")

ingredients = st.text_area("Ingredients", placeholder="e.g. tomatoes, lentils, onion, cumin, salt")

diet = st.selectbox("Diet", ["Any", "Vegan", "Jain", "Vegetarian"])

cuisine = st.selectbox("Cuisine", ["Any", "American", "Italian", "Thai", "Mexican", "Indian", "Chinese"])

if st.button("Generate Recipe"):
    if not ingredients.strip():
        st.warning("Please enter some ingredients.")
    else:
        with st.spinner("Generating recipe..."):
            recipe = generate_recipe(ingredients, cuisine, diet)

        if recipe.startswith(("Sorry, couldn't generate a recipe right now.", "The model returned an empty response.")):
            st.error(recipe)
        else:
            st.markdown(recipe)
