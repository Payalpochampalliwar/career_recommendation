import requests

url = "http://127.0.0.1:8000/api/careers/"  # Replace with your actual API endpoint
headers = {
    "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczOTI3NjcwMiwiaWF0IjoxNzM5MTkwMzAyLCJqdGkiOiIwOWY2YWI0NDVlZWU0MmFkOTc2ZjY5Yzk2YTUyOWFkNSIsInVzZXJfaWQiOjF9.qLVi9laZvcSoIdKLDm9JMPxuEvlG1P5OcH8wBSavaR4', 'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5MTkwNjAyLCJpYXQiOjE3MzkxOTAzMDIsImp0aSI6IjU4MWRhZmZlNGUyZjRkOTE4MjFmOTlkY2VlZjUyNTQ5IiwidXNlcl9pZCI6MX0.IHRA-8BDF6yg34_CC-A5gkoMmNHCBkjzWn-WOQL5pR4"
}

response = requests.get(url, headers=headers)
print(response.json())
#token vale topic pe dyn dena hai 