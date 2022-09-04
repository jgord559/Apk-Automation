from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap = {
# Set your access credentials
"browserstack.user" : "jamesgordon_63HSTY",
"browserstack.key" : "pabj8EMYhcrBMh1LmerG",
# Use the unique URL to specify the app to be downloaded
"app_url" : "bs://dc331ab8ef10b1cade9594bd6a137b4d9247bd87",
# Provide device specifications
"device" : "Google Pixel 3",
"os_version" : "9.0",
# grant permissions automatically and accept any pop up alerts
"autoGrantPermissions":"true",
"autoAcceptAlerts":"true",
#Specify the project, build, and name
"project" : "Test Python project", 
"build" : "BrowserStack-build-1",
"name" : "notes_app_test"
}


driver = webdriver.Remote(command_executor="http://hub-cloud.BrowserStack.com/wd/hub", desired_capabilities=desired_cap)

time.sleep(5)
el_createnote = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Tap to create a text note. Press and hold to create a voice note. Release the button to stop recording and create the note, or slide up to cancel.')
el_createnote.click()
el_notetitle = driver.find_element(AppiumBy.ID,'com.miui.notes:id/note_title')
el_notetitle.click()
el_notetitle.send_keys("Watch Later")
el_note = driver.find_element(AppiumBy.ID,'com.miui.notes:id/rich_editor')
el_note.click()
el_note.send_keys("Naruto"+"\n"+"WandaVision"+"\n"+"The Little Mermaid")
back=driver.find_element(AppiumBy.ID,'com.miui.notes:id/home')
back.click()
driver.quit()