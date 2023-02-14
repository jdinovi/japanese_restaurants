import json
import requests

def lambda_handler(event, context):
    
    # Business Search URL, max limit of 50 responses per request
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=50"

    # Yelp API Authentication Key
    key = 'key_here'
    
    # Header to pass key into request
    headers = {
        'Authorization' : f"bearer {key}",
        'accept' : 'application/json'
    }
    
    # Generate the content to be displayed in the HTML
    content = "<!DOCTYPE html> <html> <body> <table style='border:1px solid black;margin-left:auto;margin-right:auto;'> <tr> <th style='font-size:150%'>Japanese Restaurants in Boston</th> </tr>"
    
    # Iterate through offset values to get more than just 20 restaurants
    for off in range(0, 301, 50):
        
        try:
            
            # Parameters for search
            parameters = {
                'location' : 'Boston',
                'radius' : 40000,
                'term' : 'restaurant,japanese,japan',
                'offset' : off
            }
    
            # Make request to API
            request = requests.get(url=url, headers=headers, params=parameters)
        
            # Iterate through and add formatted values to table in HTML
            for rest in request.json()['businesses']:
                add = '<tr> <td>' + rest['name'] + '</td> </tr> '
                content += add
        except:
            break
        
    content += "</table> </body> </html>"
    
    # Return the HTML content
    response = {
        "statusCode": 200,
        "body": content,
        "headers": {
            'Content-Type': 'text/html',
        }
    }
    return response
