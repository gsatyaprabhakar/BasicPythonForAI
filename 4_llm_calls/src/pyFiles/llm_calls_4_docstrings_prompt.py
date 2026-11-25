from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def generate_recipe(ingradients, cuisine, diet):
    '''
    Generate a recipe using ingradients provided. 
    Cuisine can be "Italian", "Mexican", "Indian", "Any" etc.
    diet can be "Vegan", "Vegeterian", "Jain", "Any" etc.
    '''
    
    prompt = f'''
    Generate one food receipe using these ingradients: {','.join(ingradients)}
    Receipe should not be more than 100 words
    Cuisine: {cuisine}
    Diet: {diet}
    '''
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text 

recipe = generate_recipe(["Tomatoes", "lentils", "onion", "jeera", "salt"],"Indian","Vegan")
print(recipe)
