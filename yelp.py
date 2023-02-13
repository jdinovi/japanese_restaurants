import json
import requests

def lambda_handler(event, context):
    
    # Business Search URL
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=50"

    # Yelp API Authentication Key
    key = 'LxvXmOaNEwhHOcObouKMKmHG_grsIlTv3WbQjNeF5wUAr7Bpehay0f-TJe_Qu3GbP7Q6QYNKL_VoaCBx6uCAE8_4jMDoy_VvN2uDroftwkQzLqQdu3qijVqA16LkY3Yx'
    
    # Header to pass key into request
    headers = {
        'Authorization' : f"bearer {key}",
        'accept' : 'application/json'
    }
    
    # Generate the content to be displayed in the HTML
    content = "<!DOCTYPE html> <html> <body> <table style='border:1px solid black;margin-left:auto;margin-right:auto;'> <tr> <th style='font-size:150%'>Japanese Restaurants in Boston</th> </tr>"
    
    # Iterate through the offset values to get more than just 20 restaurants (timeout at 150 restaurants)
    for off in [0, 50, 100]:
        
        # Parameters for search
        parameters = {
            'location' : 'Boston',
            'radius' : 40000,
            'term' : 'restaurant,japanese,japan',
            'offset' : off
        }

        # Make request to API
        request = requests.get(url=url, headers=headers, params=parameters)
    
        # Iterate through and add formatted values to HTML table
        for rest in request.json()['businesses']:
            add = '<tr> <td>' + rest['name'] + '</td> </tr>'
            content += add
    
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