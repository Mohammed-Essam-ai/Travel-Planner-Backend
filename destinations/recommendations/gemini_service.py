import os
import json

from google import genai
from google.genai import types


client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

user_data={
  "trip_type": "Couple",
  "transportation": "plane",
  "interests": ["nature","beaches"],
  "budget_level": "medium",
  "country":'Egypt'	
}
available_places=[
  {
    "rank": 1,
    "id": "dest_sharm",
    "place_id": "ChIJ0a0x3q9uWBQRW7B9KXvXvJ0",
    "name": "Sharm El Sheikh",
    "rating": 4.8,
    "reviews_count": 12000,
    "tags": ["beaches", "nature"]
  },
  {
    "rank": 2,
    "id": "dest_cairo",
    "place_id": "ChIJD7fiBh9uWBQR2xg4b9WZK1Q",
    "name": "Cairo",
    "rating": 4.7,
    "reviews_count": 24000,
    "tags": ["history", "culture"]
  },
  {
    "rank": 3,
    "id": "dest_luxor",
    "place_id": "ChIJf3F5V7lqVhQRv5F5Y9Q",
    "name": "Luxor",
    "rating": 4.9,
    "reviews_count": 8500,
    "tags": ["history", "culture", "nature"]
  }
]

def generate_trip(user_data, available_places):

    prompt = f"""
    You are an expert travel planner.

    Create a complete travel itinerary based on the
    user's preferences.

    User preferences:
    {json.dumps(user_data)}

    Available places:
    {json.dumps(available_places)}

    Instructions:

    1. Select exactly 3 places from Available places.
    2. Never invent places or their IDs.
    3. Arrange the places in a logical geographical order.
    4. Create a realistic daily itinerary.
    5. Include morning, afternoon and evening activities.
    6. Consider the user's interests and budget.
    7. Estimate the total trip cost in currency of the state or country.
    8. Estimate the appropriate number of days.
    9. give me an image url for every place .
    11. Make sure every selected place appears in
        at least one itinerary day.
    12. Return the complete itinerary.
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )    
    return json.loads(response.text)
