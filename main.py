# -*- coding: utf-8 -*-
'''
Created on 2 nov. 2017

@author: Daniel López Ávila
'''
from selenium import webdriver

# paht to chromedriver
path_to_chromedriver = '../scrapingTwitter/chromedriver_2.33.exe'  # change path as needed
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

flag=True
while(flag):
    print("Enter a user")
    name = input()
    # looking for the url with the username
    url = 'https://twitter.com/'+name+'?lang=es'
    browser.get(url)
    #creatong a list of users and tweets
    # finding every users of the tweet with the class
    users=browser.find_elements_by_class_name('show-popup-with-id')
    # finding every tweet of the tweet with the class
    tweet =browser.find_elements_by_css_selector('.TweetTextSize.TweetTextSize--normal')
    list_tweets=''
    total_=len(users)
    if(total_!=0):
        print('Pinned Tweet:')
        # iterate the length
        for i in range(total_):
            list_tweets += 'User: '+users[int(i)].text+"\n"+'Tweet: '+tweet[int(i)].text+"\n\n"
            
        print(list_tweets)
        print("You want to look again? \nY(yes) N(no)")
        search = input()
        if('y'!=search.lower()):
            print('Bye!')
            flag=False
            browser.close() 
    else:
        if(browser.find_elements_by_class_name('errorpage-body-content')):
            print('This user doesn´t exist \n')
            
        else:
            print('There are no tweets in this account \n')
            
