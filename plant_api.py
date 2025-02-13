import requests
import base64
import json
import config

# API key and endpoint from config
PLANT_ID_API_KEY = config.PLANT_ID_API_KEY
PLANT_ID_URL = "https://plant.id/api/v3/health_assessment"

def encode_image(image_path):
    
    try:
        with open(image_path, "rb") as image_file:
            base64_bytes=image_file.read()
            base64_str = base64.b64encode(base64_bytes).decode("utf-8")
            prefix="data:image/jpg;base64,/"

            return base64_str
        
    except FileNotFoundError:
        print("❌ Error: Image file -not found!")
        return None

def identify_plant(image_path):
    """Sends the image to the Plant.id API and returns the identification result."""
    encoded_image = encode_image(image_path) 

    # Build the payload as per the latest API guidelines.
    payload = json.dumps({
        "images":[encoded_image],
        "latitude": 49.207,
        "longitude": 16.608,
        "health":"only",
        
        
        #"details":["description","treatment"]
        })

    headers = {
        
        'Api-Key': PLANT_ID_API_KEY,
        'Content-Type': 'application/json'
    }
   
    

    response = requests.request("POST",PLANT_ID_URL, headers=headers, data=payload)
    suggestion=response.text
    data = json.loads(suggestion)

# Extract diseases
    diseases = data.get("result", {}).get("disease", {}).get("suggestions", [])

# Format output
    if diseases:
        print("Detected plant diseases:")
        for disease in diseases:
            Formatted=(f"- {disease['name']} (Probability: {disease['probability']:.2%})")
            print(suggestion)
            return Formatted
    else:
        print("No diseases detected.")

    
        #if response.status_code == 201:
            #identification = response.json()
            #print('is plant' if identification['result']['is_plant']['binary'] else 'is not plant')
            #print(suggestion['name'])
                #print(f'probability {suggestion["probability"]:.2%}')
                #print(suggestion['details']['url'], suggestion['details']['common_names'])
                #print()
            #return suggestion
        #else:
            #print(f"❌ API Error {response.status_code}: {response.text}")
            #return {"error": f"API returned {response.status_code}"}
    #except requests.exceptions.RequestException as e:
        #print(f"❌ Network Error: {e}")
        #return {"error": "Network error"}

# For standalone testing of this module:
if __name__ == "__main__":
    image_path = "test.jpg"  # Replace with your actual test image path
    result = identify_plant(image_path)
    print(result)
