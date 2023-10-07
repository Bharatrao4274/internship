#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup

# Function to scrape hostel data
def scrape_hostel_data():
    url = "https://www.hostelworld.com/s?q=London&country=England"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the hostel listings
        hostel_listings = soup.find_all('div', class_='property-card')

        for hostel in hostel_listings:
            hostel_name = hostel.find('h2', class_='title').text.strip()
            distance = hostel.find('span', class_='distance').text.strip()
            ratings = hostel.find('div', class_='score orange').text.strip()
            total_reviews = hostel.find('div', class_='reviews').text.strip()
            overall_reviews = hostel.find('div', class_='description').text.strip()
            privates_price = hostel.find('div', class_='price-col private-price').text.strip()
            dorms_price = hostel.find('div', class_='price-col dorm-price').text.strip()
            facilities = ', '.join([item.text.strip() for item in hostel.find_all('li', class_='facility-badge')])
            property_description = hostel.find('div', class_='description').text.strip()

            print("Hostel Name:", hostel_name)
            print("Distance from City Centre:", distance)
            print("Ratings:", ratings)
            print("Total Reviews:", total_reviews)
            print("Overall Reviews:", overall_reviews)
            print("Privates from Price:", privates_price)
            print("Dorms from Price:", dorms_price)
            print("Facilities:", facilities)
            print("Property Description:", property_description)
            print("\n")
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

if __name__ == "__main__":
    scrape_hostel_data()


# In[ ]:


import requests
from bs4 import BeautifulSoup

def search_amazon_product(product_name):
    base_url = "https://www.amazon.in/"
    
    # Create a search URL based on the user's input
    search_url = base_url + "s?k=" + product_name
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all product listings on the page
        product_listings = soup.find_all('div', class_='s-result-item')
        
        if not product_listings:
            print("No products found.")
            return
        
        for product in product_listings:
            product_title = product.find('span', {'class': 'a-text-normal'}).text
            product_price = product.find('span', {'class': 'a-price-whole'})
            if product_price:
                product_price = product_price.text
            else:
                product_price = "Not available"
            
            print("Product Title:", product_title)
            print("Product Price:", product_price)
            print("\n")
    else:
        print("Failed to retrieve the search results. Status code:", response.status_code)

if __name__ == "__main__":
    product_name = input("Enter the product you want to search for on Amazon.in: ")
    search_amazon_product(product_name)


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_product_details(product_name, num_pages):
    base_url = "https://www.amazon.in/"
    data = []

    for page in range(1, num_pages + 1):
        # Create a search URL for the current page
        search_url = base_url + f"s?k={product_name}&page={page}"
        
        # Send a GET request to the search URL
        response = requests.get(search_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all product listings on the page
            product_listings = soup.find_all('div', class_='s-result-item')
            
            if not product_listings:
                print(f"No products found on page {page}.")
                break
            
            for product in product_listings:
                product_data = {}
                product_data["Brand Name"] = product.find('span', class_='a-size-base-plus a-color-base').text.strip()
                product_data["Name of the Product"] = product.find('span', class_='a-text-normal').text.strip()
                product_data["Price"] = product.find('span', class_='a-price-whole')
                if product_data["Price"]:
                    product_data["Price"] = product_data["Price"].text
                else:
                    product_data["Price"] = "-"
                product_data["Return/Exchange"] = product.find('div', class_='a-row s-align-children-center').text.strip()
                product_data["Expected Delivery"] = product.find('span', class_='a-text-bold').text.strip()
                product_data["Availability"] = product.find('div', class_='a-row s-align-children-center').text.strip()
                product_url = product.find('a', class_='a-link-normal')['href']
                product_data["Product URL"] = base_url + product_url if product_url.startswith('/') else product_url

                data.append(product_data)
        else:
            print(f"Failed to retrieve the search results on page {page}. Status code:", response.status_code)
    
    return data

if __name__ == "__main__":
    product_name = input("Enter the product you want to search for on Amazon.in: ")
    num_pages = 3  # Number of pages to scrape (change as needed)
    
    product_details = scrape_amazon_product_details(product_name, num_pages)
    
    # Create a DataFrame
    df = pd.DataFrame(product_details)
    
    # Save the data to a CSV file
    df.to_csv(f"{product_name}_amazon_products.csv", index=False)
    
    print("Data saved to CSV file.")


# In[ ]:


import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# Create a directory to save the downloaded images
if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

# Function to search and scrape images
def scrape_images(search_terms, num_images_per_term):
    driver = webdriver.Chrome()  # Change this to your WebDriver path if necessary
    driver.get("https://www.google.com/imghp")

    for search_term in search_terms:
        search_box = driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # Scroll down to load more images
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Get the page source
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Find image elements
        img_elements = soup.find_all("img")

        # Download the images
        for i, img_element in enumerate(img_elements[:num_images_per_term]):
            img_url = img_element.get("src")
            if img_url:
                response = requests.get(img_url)
                if response.status_code == 200:
                    with open(f"downloaded_images/{search_term}_{i+1}.jpg", "wb") as f:
                        f.write(response.content)
            if i >= num_images_per_term - 1:
                break

    driver.quit()

if __name__ == "__main__":
    search_terms = ["fruits", "cars", "Machine Learning", "Guitar", "Cakes"]
    num_images_per_term = 10
    
    scrape_images(search_terms, num_images_per_term)
This code opens a Chrome browser, navigates to Google Images, searches for the specified keywords, scrolls down to load more images, and then downloads the first 10 images for each keyword into a directory named "downloaded_images" with filenames like "fruits_1.jpg", "fruits_2.jpg", and so on.

Make sure to adjust the webdriver.Chrome() line to use the correct WebDriver path if necessary. Additionally, consider using a delay between actions to avoid overloading the website.







# In[ ]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_flipkart_smartphones(search_query):
    base_url = f"https://www.flipkart.com/search?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('div', class_='_1AtVbE')

        data = []

        for product in products:
            details = {}

            product_url = "https://www.flipkart.com" + product.find('a', class_='_1fQZEK')['href']
            details['Product URL'] = product_url

            title = product.find('div', class_='_4rR01T')
            details['Smartphone Name'] = title.text if title else '-'

            price = product.find('div', class_='_30jeq3')
            details['Price'] = price.text if price else '-'

            features = product.find_all('li', class_='rgWa7D')
            for feature in features:
                text = feature.text
                if 'Brand' in text:
                    details['Brand Name'] = text.split(':')[-1].strip()
                elif 'Color' in text:
                    details['Colour'] = text.split(':')[-1].strip()
                elif 'RAM' in text:
                    details['RAM'] = text.split(':')[-1].strip()
                elif 'ROM' in text:
                    details['Storage(ROM)'] = text.split(':')[-1].strip()
                elif 'Primary Camera' in text:
                    details['Primary Camera'] = text.split(':')[-1].strip()
                elif 'Secondary Camera' in text:
                    details['Secondary Camera'] = text.split(':')[-1].strip()
                elif 'Display Size' in text:
                    details['Display Size'] = text.split(':')[-1].strip()
                elif 'Battery Capacity' in text:
                    details['Battery Capacity'] = text.split(':')[-1].strip()

            data.append(details)

        df = pd.DataFrame(data)
        df.fillna('-', inplace=True)

        # Save data to CSV
        df.to_csv(f"{search_query}_smartphones_flipkart.csv", index=False)

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

if __name__ == "__main__":
    search_query = input("Enter the smartphone you want to search for on Flipkart: ")
    scrape_flipkart_smartphones(search_query)


# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_google_maps_coordinates(city_name):
    # URL to perform a Google Maps search
    search_url = f"https://www.google.com/maps/search/{city_name}"
    
    # Send a GET request to the search URL
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the div containing the coordinates
        coords_div = soup.find('div', class_='action-menu-entry-text')
        
        if coords_div:
            # Extract the coordinates from the text
            coords_text = coords_div.text
            coords_parts = coords_text.split(',')
            
            if len(coords_parts) >= 2:
                latitude = coords_parts[0].strip()
                longitude = coords_parts[1].strip()
                print(f"City: {city_name}")
                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")
            else:
                print(f"Coordinates not found for {city_name}.")
        else:
            print(f"Coordinates not found for {city_name}.")
    else:
        print("Failed to retrieve the search results. Status code:", response.status_code)

if __name__ == "__main__":
    city_name = input("Enter the city name to search on Google Maps: ")
    scrape_google_maps_coordinates(city_name)


# In[ ]:




