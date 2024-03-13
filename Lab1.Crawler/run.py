from vnexpress import *
from ggimage_crawl import *


def option1():
    title_news_links = []
    getLinks(title_news_links)
    i = 0
    skip = 0
    getInformation(title_news_links, i, skip)


def option2():
    # input
    name = input("Image title: ")
    limit = int(input("Number of images you want to crawl: "))
    num_of_pages = int(
        input("Number of pages you want to scroll (1 page ~ 200 images): "))

    # create file to save images
    if not os.path.isdir('image/' + str(name)):
        os.mkdir('image/' + str(name))

    # browser generate
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.google.com/imghp?hl=en")  # Link gg images
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    scrollPages(num_of_pages, driver)
    imageCrawl(name, limit, driver, num_of_pages)


print('1. vnexpress crawler')
print('2. image crawler')
k = int(input("Choose a number  "))
if k == 1:
    option1()
elif k == 2:
    option2()
else:
    k = int(input("Choose a number  "))
