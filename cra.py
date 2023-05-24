from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

# 크롬 드라이버 경로 설정 ( 폴더까지만 )
driver_path = 'C:\workspace_kkwo\python'

# 웹 드라이버 생성
driver = webdriver.Chrome(executable_path=driver_path)

wait = WebDriverWait(driver, 10)

# 웹 페이지 열기 
driver.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%9D%84%EC%99%95%EB%A6%AC+%ED%95%B4%EC%88%98%EC%9A%95%EC%9E%A5')

# 이미지 요소 선택
image_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'html ._image._listImage')))

# 이미지 다운로드
for i, image_element in enumerate(image_elements):

    if i >= 4:
        break

    # 이미지 URL 가져오기
    image_url = image_element.get_attribute('src')

    # 이미지 다운로드 및 저장
    filename = f'image_{i}.jpg'
    urllib.request.urlretrieve(image_url, filename)

# 드라이버 종료
driver.quit()
