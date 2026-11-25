'''
## 🏋️ Exercise: Customer review analyzer

Companies drown in free-text reviews. Let's turn one into structured data your code can sort and chart.

Given this review:
```
"I ordered the wireless earbuds last week. Sound quality is amazing and battery
lasts all day, but the case feels cheap and it arrived two days late. Probably
won't buy from this brand again."
```

1. Create a Pydantic model `ReviewAnalysis` with these fields:
   - `sentiment`: `str`  (should come back as "positive", "negative", or "neutral")
   - `rating`: `int`  (the model's guess, 1 to 5)
   - `pros`: `list[str]`
   - `cons`: `list[str]`
2. Send the review with `response_schema=ReviewAnalysis`.
3. Print the sentiment and rating, then loop over `pros` and `cons` and print each one.

**Bonus 1:** make a list of 3 different reviews, loop over them, and print a one-line summary for each (`sentiment` + `rating`). Now you've got the core of a review-dashboard. 📊

**Bonus 2:** add a field `recommended_action: str` and watch the model suggest what the company should do.

Hint: the structure is identical to the `Recipe` example — only the fields change. 😉
'''

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

# This class IS the shape we want back. Note the types: str, int, list of str.
class ReviewAnalysis(BaseModel):
    sentiment: str      # Should come back as positive, negative, or neutral
    rating: int         # The model's guess, 1 to 5
    pros: list[str]
    cons: list[str]

   
load_dotenv()
client = genai.Client()

def sentiment_analysis(review):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=review,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",    # "reply in JSON"
            response_schema=ReviewAnalysis,           # "...in exactly THIS shape"
        ),
    )

    return response

reviews_list = []

review1 = '''
I ordered the smart phone this week. Overall product is amazing and battery
lasts for 3 day, but the packing box feels cheap and it delivers on time. 
I would recommended this brand.
'''
reviews_list.append(review1)

review2 = '''
I ordered the wireless charger month week. Charging speed is good and model is 
compatible with different brands and it arrived in time. One of the best wireless 
charger to consider.
'''
reviews_list.append(review2)

review3 = '''
I ordered the wireless earbuds last week. Sound quality is amazing and battery
lasts all day, but the case feels cheap and it arrived two days late. Probably
won't buy from this brand again.
'''
reviews_list.append(review3)

for review in reviews_list:
    response = sentiment_analysis(review)
    details = response.parsed
    print(details.sentiment, details.rating)
