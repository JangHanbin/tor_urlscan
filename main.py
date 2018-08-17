from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize
from bs4 import BeautifulSoup
from dbconnect import insertdata

# def parseurl(url):

if __name__ == "__main__":



    # load tor-browser for load url
    with TorBrowserDriver("/home/d0rk94/Downloads/tor-browser_ko") as driver:
        # load url & wait for complete body loaded
        driver.load_url('http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page', wait_for_page_body=True)

        # load page source and save at soup obj for use BeutifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # find all href tag
        for url in soup.find_all('a',href=True):

            # if there is .onion url and start with http(there is irc protocol)
            if str(url['href']).find('.onion') != -1 and str(url['href']).find('http') != -1:
                print("Found URL : " + url['href'])
                page_img = join(dirname(realpath(__file__)), "_page.png")
                driver.load_url(url['href'], wait_for_page_body=True)

                insertdata(url['href'], str(driver.page_source), driver.get_screenshot_as_png())
                driver.get_screenshot_as_file(page_img)
                print("Screenshot is saved as %s (%s bytes)" % (page_img, getsize(page_img)))

