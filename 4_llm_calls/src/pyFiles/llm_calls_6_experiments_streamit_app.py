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
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text


st.title("Recipe Generator")

ingredients = st.text_area("Ingredients", placeholder="e.g. tomatoes, lentils, onion, cumin, salt")

diet = st.selectbox("Diet", ["Any", "Vegan", "Jain", "Vegetarian"])

cuisine = st.selectbox("Cuisine", ["Any", "American", "Italian", "Thai", "Mexican", "Indian", "Chinese"])

if st.button("Generate Recipe"):
    if not ingredients.strip():
        st.warning("Please enter some ingredients.")
## These check not required
##    elif not diet.strip():
##        st.warning("Please select a diet.")
##    elif not cuisine.strip():
##        st.warning("Please select a cuisine.")
    else:
        ## These print statements writes on console
        print("ingredients :", ingredients)
        print("diet :", diet)
        print("cuisine :", cuisine)
        with st.spinner("Generating recipe..."):
            try:
                recipe = generate_recipe(ingredients, cuisine, diet)
                if not recipe:
                    st.error("No recipe was generated. Please try again.")
                else:
                    st.markdown(recipe)
            except Exception as e:
                st.error(f"An error occurred: {e}")
