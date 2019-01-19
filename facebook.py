# AUTHOR : WAHYU ARIF PURNOMO
# DATE   : 19 JANUARI 2019 14:05
# CHANGE : 19 JANUARI 2019 15:30

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from random import randint
from six.moves import input



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

email_id=input("Enter your email or phone.no:\n")
password_input=getpass('Enter your Password:\n')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.facebook.com')

email=browser.find_element_by_id("email")
email.send_keys(email_id)

password=browser.find_element_by_id("pass")
password.send_keys(password_input)

password.send_keys(Keys.RETURN)

wishes = [
    'Happy Birthday !!',
    'Happy Birthday! Have a blast.',
    'Many more happy returns of the day',
    'I wish you all the happiness in the world! Happy Birthday.',
    'Just live it out to the fullest and have fun! Happy Birthday',
    'I hope you have the best day ever. Happy Birthday!',
    'Happy Birthday!! May all of your birthday wishes come true.',
    'Happy Birthday! Welcome to the new age.'
    'Best wishes on your birthday .May you have many, many more.'
    'Wishing you the happiest of birthdays.'
    'Happy Birthday! Today is a good day to spend some time with family, and some money on yourself.'
    'I hope you treat yourself to something special on your birthday , you deserve it!'
    'Happy Birthday to one of my favorite people on the planet.'
    'Getting older sucks, but you make it look easy.'
    'You make life more fun for everyone you meet. Thanks for being you.'
    'Congratulations on another year well lived.'
    'You do so much for others, I hope you find time to do something for yourself on your birthday.'
]

current_url=browser.current_url

if current_url!='https://www.facebook.com/login.php?login_attempt=1&lwv=110' :
    suffix='events/birthdays/'
    url=current_url+suffix
    home = current_url

    wishing_page=browser.get(url)
    count=len(browser.find_elements_by_name("message"))

    #list = []
    #i=0
    if count!=0 :

        while(count>0):

            wish=wishes[randint(0,len(wishes)-1)]

            wishing=browser.find_element_by_name("message")
            wishing.click()

            wishing.send_keys(wish)
            wishing.send_keys(Keys.RETURN)

            #div = browser.find_element_by_class_name('_tzn')
            #list.append(div.find_element_by_css_selector('a').text)
            #print list[i]
            #i+=1

            count=count-1
            sleep(20)
            wishing_page=browser.get(url)
        return_home=browser.get(home)
            
        print ("Done! Semua sudah kami ucapkan!.")
    else :
        print ("Maaf, hari ini tidak ada yang ulang tahun, atau semua sudah anda ucapkan.")
else :
    print ("You are high af. Run program again with correct credentials.")

browser.quit()
