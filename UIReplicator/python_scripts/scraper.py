
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
 
    session = requests.Session()
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.google.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'
    }
    
   
    response = session.get(url, headers=headers)
    
   
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        print(f'Title: {title}')
        
        with open('cloned_website.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        print('Website scraped and saved as cloned_website.html')
    else:
        print(f'Failed to retrieve the website. Status code: {response.status_code}')

if __name__ == '__main__':
    target_url = input('Enter the URL of the website to clone: ')
    scrape_website(target_url)