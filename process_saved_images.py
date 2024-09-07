import requests
import json

def generate_text(prompt, model="llava"):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
prompt = ''''Use less than 10 words to describe any aircraft or unusual phenomena present in the sky in these photos. The photos are of the same scene 10 seconds apart so you can tell how things are moving. Describe ONLY things in the sky and nothing else. "C:\\Users\\natha\\Documents\\GitHub\\SkySearch\\output-1.png" "C:\\Users\\natha\\Documents\\GitHub\\SkySearch\\output-2.png"'''


print("Waiting for llava result")
result = generate_text(prompt)
print(result)
