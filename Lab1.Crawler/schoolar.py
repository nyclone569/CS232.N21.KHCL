import requests
from bs4 import BeautifulSoup

# Tên tác giả cần tìm kiếm
#John Doe"
author_name = input()

# Tạo URL tìm kiếm trên Google Scholar với tên tác giả
url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={author_name}&btnG="

# Gửi request và lấy nội dung HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả các thẻ <h3> chứa tiêu đề bài báo
article_titles = soup.find_all('h3', {'class': 'gs_rt'})

# In ra các tiêu đề bài báo
for title in article_titles:
    print(title.text)