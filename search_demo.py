"""Open python.org, search for a keyword, and open the first result.

Selenium 4 downloads a matching ChromeDriver automatically (Selenium Manager),
so no driver binary needs to be committed or configured.
"""

import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

START_URL = "https://www.python.org/"
SEARCH_BOX = (By.ID, "id-search-field")
FIRST_RESULT = (By.CSS_SELECTOR, "ul.list-recent-events li h3 a")


def build_driver(headless: bool) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    return webdriver.Chrome(options=options)


def run(query: str, headless: bool) -> str:
    driver = build_driver(headless)
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(START_URL)

        search = wait.until(EC.element_to_be_clickable(SEARCH_BOX))
        search.clear()
        search.send_keys(query, Keys.ENTER)

        first = wait.until(EC.element_to_be_clickable(FIRST_RESULT))
        title = first.text
        first.click()
        wait.until(EC.title_contains(""))

        print(f"Opened first result: {title!r} -> {driver.current_url}")
        return driver.current_url
    finally:
        driver.quit()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="selenium")
    parser.add_argument("--headless", action="store_true", help="run without a browser window")
    args = parser.parse_args()
    run(args.query, args.headless)


if __name__ == "__main__":
    main()
