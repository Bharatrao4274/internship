
import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the information
table = soup.find('table', {'class': 'wikitable'})

# Initialize lists to store the details
rank_list = []
name_list = []
artist_list = []
upload_date_list = []
views_list = []

# Iterate through the rows of the table
for row in table.find_all('tr')[1:]:  # Start from the second row to skip the header
    columns = row.find_all('td')
    rank = columns[0].get_text(strip=True)
    name = columns[1].get_text(strip=True)
    artist = columns[2].get_text(strip=True)
    upload_date = columns[3].get_text(strip=True)
    views = columns[4].get_text(strip=True)

    rank_list.append(rank)
    name_list.append(name)
    artist_list.append(artist)
    upload_date_list.append(upload_date)
    views_list.append(views)

# Print or use the data as needed
for i in range(len(rank_list)):
    print(f"Rank: {rank_list[i]}\nName: {name_list[i]}\nArtist: {artist_list[i]}\nUpload Date: {upload_date_list[i]}\nViews: {views_list[i]}\n")

# Now, you have the details of the most viewed YouTube videos in the respective lists.

BCCI:-
import requests
from bs4 import BeautifulSoup

# Define the URL of the BCCI homepage
homepage_url = "https://www.bcci.tv/"

# Send an HTTP GET request to the homepage
response = requests.get(homepage_url)

# Parse the HTML content of the homepage using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the international fixtures page
fixtures_link = soup.find('a', text='INTERNATIONAL FIXTURES')
fixtures_url = fixtures_link['href']

# Combine the base URL with the fixtures URL to get the full URL
fixtures_url = f"https://www.bcci.tv{fixtures_url}"

# Send an HTTP GET request to the international fixtures page
fixtures_response = requests.get(fixtures_url)

# Parse the HTML content of the fixtures page
fixtures_soup = BeautifulSoup(fixtures_response.text, 'html.parser')

# Find the elements containing fixture details
fixture_elements = fixtures_soup.find_all('div', class_='fixture')

# Initialize lists to store the details
series_list = []
place_list = []
date_list = []
time_list = []

# Iterate through the fixture elements
for fixture in fixture_elements:
    series = fixture.find('p', class_='fixture__format').text.strip()
    place = fixture.find('p', class_='fixture__info').span.text.strip()
    date = fixture.find('span', class_='fixture__date').text.strip()
    time = fixture.find('span', class_='fixture__time').text.strip()

    series_list.append(series)
    place_list.append(place)
    date_list.append(date)
    time_list.append(time)

# Print or use the data as needed
for i in range(len(series_list)):
    print(f"Series: {series_list[i]}\nPlace: {place_list[i]}\nDate: {date_list[i]}\nTime: {time_list[i]}\n")

3.
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the main page
main_url = "http://statisticstimes.com/"
response = requests.get(main_url)

# Parse the HTML content of the main page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the Economy or Indian States page and get the full URL
economy_link = soup.find('a', text='Economy')  # Adjust this based on the actual link text
economy_url = economy_link['href']  # This might require further adjustments

# Send an HTTP GET request to the Economy or Indian States page
economy_response = requests.get(economy_url)

# Parse the HTML content of the Economy or Indian States page
economy_soup = BeautifulSoup(economy_response.text, 'html.parser')

# Locate the table that contains the State-wise GDP data
# Extract and process the data you need

4
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the GitHub trending page
url = "https://github.com/trending"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the repository cards on the page
repo_cards = soup.find_all('article', class_='Box-row')

# Initialize lists to store the details
repository_titles = []
repository_descriptions = []
contributors_counts = []
languages_used = []

# Iterate through the repository cards and extract the details
for repo_card in repo_cards:
    title = repo_card.find('h1').get_text(strip=True)
    description = repo_card.find('p', class_='col-9').get_text(strip=True)
    contributors_count = repo_card.find('a', href=True, text=True, attrs={'href': '/{}/graphs/contributors'.format(title)}).get_text(strip=True)
    language = repo_card.find('span', itemprop='programmingLanguage').get_text(strip=True)

    repository_titles.append(title)
    repository_descriptions.append(description)
    contributors_counts.append(contributors_count)
    languages_used.append(language)

# Print or use the data as needed
for i in range(len(repository_titles)):
    print(f"Repository Title: {repository_titles[i]}")
    print(f"Repository Description: {repository_descriptions[i]}")
    print(f"Contributors Count: {contributors_counts[i]}")
    print(f"Language Used: {languages_used[i]}")
    print("\n")

    5
    import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the Billboard Hot 100 page
url = "https://www.billboard.com/charts/hot-100"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the chart container that contains the songs
chart_container = soup.find('ol', class_='chart-list')

# Find all the individual song entries
song_entries = chart_container.find_all('li', class_='chart-list-item')

# Initialize lists to store the details
song_names = []
artist_names = []
last_week_ranks = []
peak_ranks = []
weeks_on_board = []

# Iterate through the song entries and extract the details
for entry in song_entries:
    song_name = entry.find('span', class_='chart-list-item-title').text
    artist_name = entry.find('span', class_='chart-list-item-artist').text
    last_week_rank = entry.find('span', class_='text--last').text
    peak_rank = entry.find('span', class_='text--peak').text
    weeks_on_chart = entry.find('span', class_='text--week').text

    song_names.append(song_name)
    artist_names.append(artist_name)
    last_week_ranks.append(last_week_rank)
    peak_ranks.append(peak_rank)
    weeks_on_board.append(weeks_on_chart)

# Print or use the data as needed
for i in range(len(song_names)):
    print(f"Song Name: {song_names[i]}")
    print(f"Artist Name: {artist_names[i]}")
    print(f"Last Week Rank: {last_week_ranks[i]}")
    print(f"Peak Rank: {peak_ranks[i]}")
    print(f"Weeks on Board: {weeks_on_board[i]}")
    print("\n")
    6.
    import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the URL
url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compar"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the section of the page with the highest-selling novels data
# Extract and process the data you need
7
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the IMDb URL
url = "https://www.imdb.com/list/ls095964455/"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the container that holds the TV series information
series_container = soup.find('div', class_='lister-list')

# Find all the individual series entries
series_entries = series_container.find_all('div', class_='lister-item')

# Initialize lists to store the details
names = []
year_spans = []
genres = []
runtimes = []
ratings = []
votes = []

# Iterate through the series entries and extract the details
for series_entry in series_entries:
    name = series_entry.h3.a.text.strip()
    year_span = series_entry.h3.find('span', class_='lister-item-year').text.strip()
    genre = series_entry.find('span', class_='genre').text.strip()
    runtime = series_entry.find('span', class_='runtime').text.strip()
    rating = series_entry.strong.text.strip()
    vote = series_entry.find('span', {'name': 'rk'})['data-value']

    names.append(name)
    year_spans.append(year_span)
    genres.append(genre)
    runtimes.append(runtime)
    ratings.append(rating)
    votes.append(vote)

# Print or use the data as needed
for i in range(len(names)):
    print(f"Name: {names[i]}")
    print(f"Year Span: {year_spans[i]}")
    print(f"Genre: {genres[i]}")
    print(f"Run Time: {runtimes[i]}")
    print(f"Ratings: {ratings[i]}")
    print(f"Votes: {votes[i]}")
    print("\n")

# Now, you have the details of the most-watched TV series on IMDb in the respective lists.
8
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the UCI Machine Learning Repository URL
url = "https://archive.ics.uci.edu/"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the "View ALL Data Sets" page
data_sets_link = soup.find('a', text='View ALL Data Sets')

# Combine the base URL with the link to the data sets page to get the full URL
data_sets_url = url + data_sets_link['href']

# Send an HTTP GET request to the data sets page
response = requests.get(data_sets_url)

# Parse the HTML content of the data sets page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the data table containing the dataset details
data_table = soup.find('table', {'border': '1'})

# Initialize lists to store the details
dataset_names = []
data_types = []
tasks = []
attribute_types = []
no_of_instances = []
no_of_attributes = []
years = []

# Iterate through the data table rows and extract the details
for row in data_table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    dataset_name = columns[0].get_text(strip=True)
    data_type = columns[1].get_text(strip=True)
    task = columns[2].get_text(strip=True)
    attribute_type = columns[3].get_text(strip=True)
    no_instances = columns[4].get_text(strip=True)
    no_attributes = columns[5].get_text(strip=True)
    year = columns[6].get_text(strip=True)

    dataset_names.append(dataset_name)
    data_types.append(data_type)
    tasks.append(task)
    attribute_types.append(attribute_type)
    no_of_instances.append(no_instances)
    no_of_attributes.append(no_attributes)
    years.append(year)

# Print or use the data as needed
for i in range(len(dataset_names)):
    print(f"Dataset Name: {dataset_names[i]}")
    print(f"Data Type: {data_types[i]}")
    print(f"Task: {tasks[i]}")
    print(f"Attribute Type: {attribute_types[i]}")
    print(f"No of Instances: {no_of_instances[i]}")
    print(f"No of Attributes: {no_of_attributes[i]}")
    print(f"Year: {years[i]}")
    print("\n")






