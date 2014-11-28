# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 22:34:52 2014

@author: Michael
"""
from selenium import webdriver
from browsermobproxy import Server
import datetime
import re
import json
import requests

def setupdevices():    
    """
    Description:
        Sets u browser proxy, Selenium driver, and har object

    Usage:
        [driver,proxy]=setupdevices()
        
    Inputs:
        NA
    
    Output:
        Selenium driver
        Browsermob proxy
        Browsermob server        
    """    
    #set up proxy
    server = Server("############/browsermob-proxy-2.0-beta-9/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()
    profile  = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    proxy.new_har("________")
    
    #set up driver
    driver = webdriver.Firefox(firefox_profile=profile)
    
    return (driver,proxy,server)
    
def closedevices(driver,server):
    """
    Description:
        Closes browser server and Selenium driver

    Usage:
        
    Inputs:
        Selenium driver
        Browsermob server
        
    Output:
        NA
        
    """ 

    server.stop()
    driver.quit()

def gotomiddleframe(driver):
    """
    Description:
        Goes to default content, then goes to middle frame
    
    Usage:
    
    Inputs:
        Selenium driver 
    
    Output:
        Selenium driver        
    """  
    driver.switch_to_default_content()    
    middleframe=driver.find_element_by_xpath("//iframe")
    driver.switch_to_frame(middleframe)
    
    return driver

def goto________frame(driver):
    """
    Description:
        Goes to middleframe then goes to ________ frame
    
    Usage:
    
    Inputs:
        Selenium driver 
    
    Output:
        Selenium driver        
    """ 
    driver=gotomiddleframe(driver)
    frames=driver.find_elements_by_xpath("//iframe")
    driver.switch_to_frame(frames[3])
    
    return driver
    
def goto________frame(driver):
    """
    Description:
        Goes to middleframe then goes to ________ frame
    
    Usage:
    
    Inputs:
        Selenium driver 
    
    Output:
        Selenium driver        
    """ 
    
    driver=gotomiddleframe(driver)
    frames=driver.find_elements_by_xpath("//iframe")
    driver.switch_to_frame(frames[4])
    
    return driver
    
def click________(driver):
    """
    Description:
        clicks on ________ tab
    
    Usage:
    
    Inputs:
        Selenium driver 
    
    Output: string:
        Selenium driver        
    """  
    driver=gotomiddleframe(driver)
    
    for counter in range(100):
        ________=driver.find_element_by_xpath("//a[text()='________']")
        ________.click()
        try:
            ________=driver.find_element_by_xpath("//li[contains(@class,'active')]/a[text()='________']")
            break
        except:
            print counter, '________ TAB NOT CLICKED'
            
    return driver
    
def click________(driver):
    """
    Description:
        Clicks on ________ tab
    
    Usage:
    
    Inputs:
        Selenium driver 
    
    Output: string:
        Selenium driver        
    """  
    driver=gotomiddleframe(driver)
    
    for counter in range(100):
        ________=driver.find_element_by_xpath("//a[text()='________']")
        ________.click()
        try:
            ________=driver.find_element_by_xpath("//li[contains(@class,'active')]/a[text()='________']")
            break
        except:
            print counter, '________ TAB NOT CLICKED'
            
    return driver
    
def choose________tabs(driver,index):
    """
    Description:
        Chooses ________ type of data based on index
        index can be 0-4
    Usage:
        
    Inputs:
        Selenium driver 
        integer: index
        
    Output: string:
        Selenium driver        
    """  
    tabnames=["'_______'","'_______'","'_______'","'_______'","'_______'"]
    name=tabnames[index]
    
    driver=goto________frame(driver)  
    
    for counter in range(100):    
        tabelement=driver.find_element_by_xpath("//button[./span[text()=%s]]" %(name,))
        tabelement.click()        
        try:
            tabelement=driver.find_element_by_xpath("//button[contains(@class,'Selected')][./span[text()=%s]]" %(name,))
            break
        except:
            print counter, '________ DATA TAB NOT CLICKED'
            
    return driver
    
def choose________tabs(driver,index):
    """
    Description:
        Chooses ________ type of data based on index
        index can be 1-2
    Usage:
        
    Inputs:
        Selenium driver 
        integer: index
        
    Output: string:
        Selenium driver        
    """  
    driver=goto________frame(driver)
    
    if index==1:
        for counter in range(100):
            try:
                tabelement=driver.find_element_by_xpath("//li[@class='expanded'][./label[text()='________']]/input[@type='checkbox']")
            except:
                tabelement=driver.find_element_by_xpath("//li[@class][./label[text()='________']]/input[@type='checkbox']")
                tabelement.click()
            
            try:
                tabelement=driver.find_element_by_xpath("//li[@class='expanded'][./label[text()='________']]/input[@type='checkbox']")
                break
            except:
                print counter, '________ DATA TAB NOT CLICKED'
    elif index==2:
        for counter in range(100):        
            try:
                tabelement=driver.find_element_by_xpath("//li[@class='expanded'][./label[text()='________']]/input[@type='checkbox']")
            except:
                tabelement=driver.find_element_by_xpath("//li[@class][./label[text()='________']]/input[@type='checkbox']")
                tabelement.click()

            try:
                tabelement=driver.find_element_by_xpath("//li[@class='expanded'][./label[text()='________']]/input[@type='checkbox']")
                break
            except:
                print counter, '________ DATA TAB NOT CLICKED'
    else:
        print 'VALID INDEX NOT GIVEN'
    
    return driver
    
def choosepulldown(driver,index,tab):
    """
    Description:
        With driver, sets both pulldowns to pulldownname denoted by index
        index can be 0-4
        tab denotes whether we are in ________ tab or ________ tab
            1: ________
            2: ________
            
    Usage:
    
    Inputs:
        Selenium driver 
        integer: index
        inger: tab
    Output: string:
        Selenium driver        
    """  
    if tab==1:
        driver=goto________frame(driver)
    elif tab==2:
        print "NO PULLDOWN FOR ________"
        #driver=goto________frame(driver)
    else:
        print '________ FRAME NOT CHOSEN!'
        
    pulldownnames=["'_______'","'_______'","'_______'","'_______'","'_______'"]
    name=pulldownnames[index]  
      
    for counter2 in range(100):
        #click left pulldown tab
        try:
            leftpulldown=driver.find_elements_by_xpath("//button[@aria-haspopup='true']")[0]
            leftpulldown.click()
        except:
            pass
        
        for counter in range(100):
            try:
                leftpulldownitem=driver.find_elements_by_xpath("//li[@class='']/label/span[text()=%s]" %(name,))[0]
                leftpulldownitem.click()
                break
            except:
                print counter, 'Left WebElement Not Visible'
                try:
                    leftpulldown=driver.find_elements_by_xpath("//button[@aria-haspopup='true']")[0]
                    leftpulldown.click()
                except:
                    pass

        #click right pulldowntab
        try:
            rightpulldown=driver.find_elements_by_xpath("//button[@aria-haspopup='true']")[1]
            rightpulldown.click()                                
        except:
            pass
        
        for counter in range(100):
            try:
                rightpulldownitem=driver.find_elements_by_xpath("//li[@class='']/label/span[text()=%s]" %(name,))[1]
                rightpulldownitem.click()
                break
            except:
                print counter, 'Right WebElement Not Visible'
                try:
                    rightpulldown=driver.find_elements_by_xpath("//button[@aria-haspopup='true']")[1]
                    rightpulldown.click()
                except:
                    pass
                
        # test that both pulldowns are correct
        try:
            rightpulldown=driver.find_elements_by_xpath("//button[@aria-haspopup='true'][./span[text()=%s]]" %(name,))[1]
            break
        except:
            print counter2, 'Pulldown Elements not both correct'
            
    return driver
    
def clickprevious(driver,tab):
    """
    Description:
        Clicks on previous button
        tab is 1-2
    Usage:
    
    Inputs:
        Selenium driver
        integer: index
    Output:
        Selenium driver
    """ 
    if tab==1:
        driver=goto________frame(driver)
    elif tab==2:
        driver=goto________frame(driver)
    else:
        print '________ FRAME NOT CHOSEN!'
    
    button=driver.find_element_by_xpath("//span/button[@id='prev']")
    button.click()
    """    
    for counter in range(100):
        try:
            oldchart=driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @class='highcharts-title']/*[name()='tspan' and text()]")
            button=driver.find_element_by_xpath("//span/button[@id='prev']")
            button.click()
            newchart=driver.find_element_by_xpath("//*[name()='svg']/*[name()='text' and @class='highcharts-title']/*[name()='tspan' and text()]")

            if newchart.text!=oldchart.text:
                break                
            else:
                print counter, 'NEW CHART NOT LOADED'
        except:
            print counter, 'PREVIOUS BUTTON ERROR'
    """
    return driver
    
def setupdates(presentdate):
    """
    Description:
        Creates list of date strings from (i.e. first element) ________ to presentdate inclusive  
    
    Usage:
    
    Inputs:
        string: presentdate in form '%Y-%m-%d'
    
    Output:
        list of string dates
        
    """ 
    start = datetime.datetime.strptime("________", "%Y-%m-%d")
    end = datetime.datetime.strptime(presentdate, "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]
    dates=map(lambda x: x.strftime("%Y-%m-%d"),date_generated)    
    
    return dates

def setupdatestest(presentdate):
    """
    Description:
        Creates list of date strings from (i.e. first element) ________ to presentdate inclusive  
        Then only takes first 10 dates for testing purposes
    Usage:
    
    Inputs:
        string: presentdate in form '%Y-%m-%d'
    
    Output:
        list of string dates
        
    """ 
    start = datetime.datetime.strptime("________", "%Y-%m-%d")
    end = datetime.datetime.strptime(presentdate, "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]
    dates=map(lambda x: x.strftime("%Y-%m-%d"),date_generated)    
    dates=dates[len(dates)-10:len(dates)]
    print dates
    return dates
    
def printhartofile(proxy,index,filestring):
    """
    Description:
        Writes textfile with har urls
        index is 1-2
        filestring adds addition info to textfile name
    Usage:
    
    Inputs:
        browsermob proxy
        integer: index
        string: filestring

    Output:
        NA
        
    """
    if index==1:
        matchstring=re.compile('_______')
        filename='________'+'-'+filestring
    elif index==2:
        matchstring=re.compile('_______')
        filename='________'+'-'+filestring
    else:
        print 'VALID INDEX NOT SELECTED'
        
    file=open(filename,'w')

    for index, ent in enumerate(proxy.har['log']['entries']):
        if matchstring.search(ent['request']['url']):
            print index
            print ent['request']['url']
            file.write(ent['request']['url']+'\n')
    
    file.close()
    
def query________(today):
    """
    Description:
        queries all ________ data and creates json blob
        
    Usage:
        
    Inputs:
        string: today 
            in format %Y-%m-%d

    Output:
        jsonblob
    
    """    
    strings=[None]*11
    strings[0]='http:________'
    strings[1]='________'
    strings[2]='________'
    strings[10]='________'
    
    dates=setupdates(today)
    
    datatypes=['_____','_____','_____','_____','_____']
    datatypenames=['_____','_____','_____','_____','_____']    
    dataintervals=['_____','_____','_____','_____','_____']
    
    devices=['_____','_____','_____','_____','_____']
    devicenames=['_____','_____','_____','_____','_____']    
    devicetypes=['_____','_____','_____','_____','_____']
    
    jsonblob=[]    
    for dataindex in range(len(datatypes)):
        for deviceindex in range(len(devices)):
            for dateindex in range(len(dates)-1):
                #dates
                fromdate=dates[dateindex]
                todate=dates[dateindex+1]
                
                strings[3]='_______='+fromdate+'_______'
                strings[4]='_______='+fromdate+'_______'
                strings[5]='_______='+todate+'_______'
                
                #data type
                datatype=datatypes[dataindex]
                datainterval=dataintervals[dataindex]
                
                strings[6]='_______='+datainterval+'&'
                strings[8]='_______='+datatype+'&'
                
                #devices
                device=devices[deviceindex]
                devicetype=devicetypes[deviceindex]
                
                strings[7]='_______='+device+';'+device+'&'    
                strings[9]='_______='+devicetype+';'+devicetype
                
                #get query
                url="".join(strings)
                response = requests.get(url)
                responsedata = response.json()
                
                jsondata=dict()
                jsondata['time']=responsedata['categories']
                jsondata['value']=responsedata['dataset']
                jsondata['date']=fromdate             
                jsondata['datatype']=datatypenames[dataindex]
                jsondata['device']=devicenames[deviceindex]
                
                jsonblob.append(jsondata)
                
    return json.dumps(jsonblob)
    
def query________(today):
    """
    Description:
        queries all ________ data and creates json blob
        
    Usage:
        
    Inputs:
        string: today 
            in format %Y-%m-%d

    Output:
        jsonblob
    
    """ 
    strings=[None]*9
    strings[0]='http:________'
    strings[1]='_______'
    strings[2]='_______'
    strings[4]='_______'
    strings[8]='_______'

    devices=['_______','_______']
    devicenames=['_____','_____']
    dates=setupdates(today)
    
    jsonblob=[]    
    for deviceindex in range(len(devices)):    
        for dateindex in range(len(dates)-1): 

            #dates
            fromdate=dates[dateindex]
            todate=dates[dateindex+1]
            
            strings[5]='_______='+fromdate+'_______'
            strings[6]='_______='+fromdate+'_______'
            strings[7]='_______='+todate+'_______'
            
            #devices               
            device=devices[deviceindex]
                            
            strings[3]='_______='+device+'&'
            
            #get query
            url="".join(strings)
            response = requests.get(url)
            responsedata = response.json()
                
            jsondata=dict()
            jsondata['time']=responsedata['categories']
            jsondata['value']=responsedata['dataset']
            jsondata['date']=fromdate 
            jsondata['device']=devicenames[deviceindex]            
            
            jsonblob.append(jsondata)
    
    return json.dumps(jsonblob)

