import requests
from bs4 import BeautifulSoup

# Jenkins URL and login credentials
jenkins_url = 'http://127.0.0.1:5000'
username = 'jenkins'
password = 'matt@123'

# Session setup
session = requests.Session()

# Get login page to retrieve CSRF token
response = session.get(jenkins_url + '/login')
csrf_token = response.cookies['crumb']

# Login data
login_data = {
    'j_username': username,
    'j_password': password,
    'Submit': 'Log In',
    'jenkins-crumbs': csrf_token
}

# Log in to Jenkins
login_response = session.post(jenkins_url + '/j_security_check', data=login_data)

# Check if login was successful
if 'dashboard' in login_response.url:
    print("Login successful!")
else:
    print("Login failed.")
    exit()

# Fetch project details
projects_response = session.get(jenkins_url + '/view/All/')
projects_soup = BeautifulSoup(projects_response.content, 'html.parser')

# Find and print project details
project_links = projects_soup.find_all('a', class_='model-link inside')
if project_links:
    print("Project details:")
    for link in project_links:
        project_name = link.text.strip()
        project_url = jenkins_url + link['href']
        print(f"Project Name: {project_name}")
        print(f"Project URL: {project_url}")
        print("-" * 30)
else:
    print("No projects found.")

# You can further customize and enhance this script to extract and display more project details.
