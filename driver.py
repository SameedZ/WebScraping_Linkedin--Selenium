from selenium import webdriver
import time

#### Add your path to the chrome driver here.
## Download link to chrome driver for diff OS here.
# Navigate to Browsers section @ https://www.selenium.dev/downloads/
driver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")

#### Navigating to Sign In Page Linkedin
urltoSignInPage = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
driver.get(urltoSignInPage)
time.sleep(2)

## Targetting the Email & Password page on the web
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")


## Enter your credentials here.
username.send_keys('youremailhere')
password.send_keys('yourpasswordhere')
time.sleep(2)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
# Login Process Complete.


#### Searching people on linkedin. Place the link of your prefence. in urllink
for i in range(5):
    urllink = ""
    urllink = "https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&page="+str(i+5)+"&sid=aiC"
    
    ### Visiting the Link placed.
    driver.get(urllink)
    time.sleep(2)


    ### Finding all the connect button on the page.  
    ## This will ignore Following Option that might appear next to some people.

    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    ## Iterating over all the buttons. 

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
    # Added Cause some people only prefer connection if you have their official email.
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(2)
    time.sleep(2)
    print("Page No. = ",str(i+5)," | Connection Invitation Send = ", len(connect_buttons) )