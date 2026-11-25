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

print(generate_recipe("tomatoes, lentils, onion", "Indian", "Vegan"))
