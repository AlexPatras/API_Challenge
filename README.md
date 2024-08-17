# API_Challenge

 # Here you can find the solution to the initial challenge:
 
1. Fetch Initial Data: The script starts by sending a POST request to the API to retrieve initial data.

2. Follow the Cursor: The API response includes a 'nextCursor value'. The script uses this cursor to send following POST requests.

3. Loop Through Responses: The script continuously loops through the API responses, updating the cursor each time, until it discovers the hidden flag.

4. Error Handling: It checks for and handles errors, such as unexpected status codes, to ensure proper execution 

# Technologies Used

- Postman
- Python
