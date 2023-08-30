from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import random
def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

class TinderBot:
    def __init__(self):
        self.driver = setup_driver()
        self.wait = WebDriverWait(self.driver, 10)
        
    def like(self):
        like_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u-1535117240 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button')))
        like_btn.click()
        time.sleep(0.5)

  
    def dislike(self):
        dislike_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u-1535117240 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-nope-default\) > button')))
        dislike_btn.click()
        time.sleep(0.5)
    def close_popup(self):
        popup_3 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u1031468980 > main > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\)--ml.Px\(24px\) > button.c1p6lbu0.D\(b\).Mx\(a\)')))
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    def close_superlike(self):
        superlike_popup=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u1031468980 > main > div > button.c1p6lbu0.D\(b\).My\(20px\).Mx\(a\)')))
        superlike_popup.click()
    def main(self):
        self.driver.get(r'https://tinder.com/')
        time.sleep(3)
        # Call the like or dislike methods here as needed
        # Example:
        # self.like()
    
    def auto_swipe(self):
        from random import random
        left_count,right_count= 0, 0 
        while True:
            time.sleep(0.5)
            try:
                rand=random()
                if rand <0.73 :
                   self.like()
                   
                   right_count=right_count+1
                   print('{} th right swipe'.format(right_count))
                  
                else :
                   self.dislike()
                   
                   left_count=left_count+1
                   print('{} th left swipe'.format(left_count))
                    
                    
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    
                    self.close_superlike()
                    print("nothing")
if __name__ == "__main__":
    bot = TinderBot()
    bot.main()
    bot.auto_swipe()
