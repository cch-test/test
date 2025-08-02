from playwright.sync_api import sync_playwright

def run():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://humanbenchmark.com/")
    page.wait_for_load_state("networkidle")
    page.click("text=Get Started")
    browser.close()

if __name__ == "__main__":
  run()
