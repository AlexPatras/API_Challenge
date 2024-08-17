import requests

# Initialize the API endpoint and the initial cursor
api_url = " Insert your API here"
headers = {
    "Authorization": "Bearer token",
    "Content-Type": "application/json"
}

# Start with the initial cursor
next_cursor = "value of the initial cursor" 

while True:
    # Prepare the request with the current cursor
    response = requests.post(api_url, json={"cursor": next_cursor}, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        break
    
    # Parse the response JSON
    data = response.json()

    # Print the current response
    print(data)
    
    # Check if the flag is present in the response
    if "flag" in data:
        print(f"Flag found: {data['flag']}")
        break
    
    # Update the cursor for the next request
    next_cursor = data.get("nextCursor")
    
    # If there is no nextCursor, break the loop
    if not next_cursor:
        print("No more cursors found. Exiting loop.")
        break
