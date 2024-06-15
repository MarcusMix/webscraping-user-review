from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
profile_path = "C:\\Users\\vini6\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

def web_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')  # Descomente se desejar executar em modo headless
    # options.add_argument('--disable-gpu')
    # options.add_argument("--window-size=1920,1200")
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-data-dir={profile_path}")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    return driver
