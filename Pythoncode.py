# import requests
# import beautifulsoup4 on the terminal
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
a= "https://www.bestbuy.com"
response = requests.get(a, headers=headers)
htmlcode = response.content
soup = BeautifulSoup(htmlcode, "html.parser")

# Get the entire HTML content from the page
htmldata = soup.prettify()
print(htmldata)

# Store text data in a separate file
with open("text data.txt", "w") as file:
    file.write(soup.get_text())

# Get all the links on the page
print("Getting all the Links\n")
anchor = soup.find_all("a")
all_links = set()
for i in anchor:
    if i != "#":
        link_text = "https://www.bestbuy.com" + i.get("href")
        all_links.add(link_text)
# Store links data in a separate file
with open("links data.txt", "w") as file:
    for link in all_links:
        file.write(link + "\n")

# Get Image scraping
print("Getting all the Images\n")
images = soup.find_all("img")
# Store image URLs in a separate file
if images:
    with open("image urls.txt", "w") as file:
        for item in images:
            file.write(item['src'] + "\n")
else:
    with open("image urls.txt", "w") as file:
        file.write("No images found on the webpage.")

# Get Audio scraping
print("Getting all the Audios\n")
aud = soup.find_all("audio")
audio_urls = []
for i in aud:
    audio_url = i.find("a")["href"]
    audio_urls.append(audio_url)
# Store audio URLs in a separate file
if audio_urls:
    with open("audio urls.txt", "w") as file:
        for url in audio_urls:
            file.write(url + "\n")
else:
    with open("audio urls.txt", "w") as file:
        file.write("No audio found on the webpage.")

# Get Video scraping
print("Getting all the Videos\n")
video = soup.find_all("video")
video_urls = []
for i in video:
    video_url = i.find("a")['href']
    video_urls.append(video_url)
# Store video URLs in a separate file
if video_urls:
    with open("video urls.txt", "w") as file:
        for url in video_urls:
            file.write(url + "\n")
else:
    with open("video urls.txt", "w") as file:
        file.write("No videos found on the webpage.")

# Get Headings scraping
print("Getting all the Headings\n")
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# Store headings in a separate file
if headings:
    with open("headings.txt", "w") as file:
        for heading in headings:
            file.write(heading.text + "\n")
else:
    with open("headings.txt", "w") as file:
        file.write("No headings found on the webpage.")
print("Data extraction and storage completed successfully!")
