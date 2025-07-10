import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up undetected ChromeDriver
driver = uc.Chrome()

# URL of the WeSIS login page
login_url = 'https://wesis.org/login'

# Open the login page
driver.get(login_url)

# Find the username and password fields and enter your credentials
username = driver.find_element(By.NAME, 'username')  # Adjust the selector as needed
password = driver.find_element(By.NAME, 'password')  # Adjust the selector as needed

username.send_keys('your_username')  # Replace with your username
password.send_keys('your_password')  # Replace with your password

# Submit the login form
password.send_keys(Keys.RETURN)

# Wait for the login to complete and the next page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'main-category')))  # Adjust the selector as needed

# URL of the WeSIS webpage to scrape
url = 'https://wesis.org/indicators'

# Make a GET request to the target page
driver.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Initialize a list to store the data
data = []

# Example: Find the main categories (adjust selectors as needed)
categories = soup.find_all('div', class_='main-category')

# Loop through each category
for category in categories:
    category_name = category.find('h2').text

    # Find the subcategories within each category
    subcategories = category.find_all('div', class_='subcategory')
    
    for subcategory in subcategories:
        subcategory_name = subcategory.find('h3').text

        # Find the "Attainment" section within each subcategory
        attainment_sections = subcategory.find_all('div', class_='attainment')
        
        for attainment in attainment_sections:
            # Find the "Tertiary" section within each attainment section
            tertiary_sections = attainment.find_all('div', class_='tertiary')
            
            for tertiary in tertiary_sections:
                # Find the links within each tertiary section
                links = tertiary.find_all('a', href=True)

                for link in links:
                    link_url = link['href']
                    driver.get(link_url)

                    # Wait for the page to load
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

                    # Parse the HTML content of the new page
                    soup = BeautifulSoup(driver.page_source, 'html.parser')

                    # Extract the data you need (adjust selectors as needed)
                    technical_name = soup.find('span', class_='technical-name').text
                    scale = soup.find('span', class_='scale').text
                    description = soup.find('span', class_='description').text

                    # Append the data to the list
                    data.append([category_name, subcategory_name, link_url, technical_name, scale, description])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Category', 'Subcategory', 'Link URL', 'Technical Name', 'Scale', 'Description'])

# Save the DataFrame to a CSV file
df.to_csv('indicators_data.csv', index=False)

print('Data saved to indicators_data.csv')

# Close the browser
driver.quit()
