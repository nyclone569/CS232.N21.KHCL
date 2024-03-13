from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
# Khởi tạo trình duyệt
driver = webdriver.Chrome('chromedriver.exe')

# Mở trang Facebook
driver.get('https://mbasic.facebook.com')

# Tìm đến các trường input để đăng nhập
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")

# Nhập thông tin đăng nhập
email_input.send_keys('lptrungc10.c3nvtroi@gmail.com')
password_input.send_keys('Lelouch512')

# Submit form để đăng nhập
login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
login_button.click()
sleep(random.randint(3, 6))


# Đi đến trang Facebook
page_url = 'https://mbasic.facebook.com/UITconfess?v=timeline&lst=100011667640148%3A100088809545601%3A1683116795&eav=AfaejFry8oEAkEKfUC2Pvjt9ovs0B6EU9rbuibdatKU8hROVfADm0hDMAswExg57ikw&paipv=0'
driver.get(page_url)
sleep(random.randint(3, 6))
xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/ul"

# Lấy các bài viết trên trang Facebook
comment_list = driver.find_elements(By.XPATH, xpath + '/li')
print(len(comment_list))


# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
for i in range(1, len(comment_list) + 1):

    name = driver.find_elements(By.XPATH, xpath + "/li[" + str(
        i) + "]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/span/a/span/span")

    cmt = driver.find_elements(By.XPATH, xpath + "/li[" + str(
        i) + "]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/span/div")
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    # poster = comment.find_element(By.CLASS_NAME, "x3nfvp2")

    # print("*", poster.text,":")
    print(name[0].text, ': ', cmt[0].text)
# In ra các bài viết
