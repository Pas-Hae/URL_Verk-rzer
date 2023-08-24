# Importieren der benötigten Bibliotheken
import requests
import json

# Funktion zum Verkürzen eines langen URLs
def shorten_url(long_url, api_token):
    
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }

    # Daten für die Anfrage. In diesem Fall nur die lange URL.
    data = {
        "long_url": long_url
    }

    # Anfrage an die Bitly-API senden, um den URL zu verkürzen
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)

    # anfrage erfolgreich
    if response.status_code == 201:
        
        return json.loads(response.content)['link']
    else:
        # Wenn die Anfrage fehlschlägt, fehler zurück
        return f"Error: {response.content}"

# Hauptprogramm
if __name__ == "__main__":
    # Token von Bitly
    api_token = "8c74d6cad814d10fc94e95f16d03b947c22f08e8"
    
    # Die lange URL
    long_url = "https://www.example.com/sehr/langer/link"

    short_url = shorten_url(long_url, api_token)
    
    # Ausgabe des verkürzten URLs
    print(f"Verkürzter URL: {short_url}")
