from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_indeed_jobs():
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Set an explicit wait
    wait = WebDriverWait(driver, 20)
    
    try:
        # Navigate to the job search page
        driver.get("https://www.indeed.com/q-data-analyst-jobs.html")

        # Wait for the page to load
        time.sleep(5)

        # Initialize lists to store scraped data
        job_titles = []
        company_names = []
        post_dates = []

        # Scrape 20 data analyst roles
        while len(job_titles) < 20:  # Ensure we scrape at least 20 roles
            job_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result")))

            for card in job_cards:
                if len(job_titles) >= 20:
                    break
                try:
                    title = card.find_element(By.CSS_SELECTOR, 'span[title]').text
                    company = card.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]').text
                    date_posted = card.find_element(By.CSS_SELECTOR, 'span[data-testid="myJobsStateDate"]').text

                    job_titles.append(title)
                    company_names.append(company)
                    post_dates.append(date_posted)
                except Exception as e:
                    print(f"Error occurred: {e}")

            # Click the "Next" button to go to the next page of results
            try:
                next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Next"]')))
                next_button.click()
                time.sleep(5)  # Wait for the next page to load
            except:
                break

        # Save the data to a CSV file
        df = pd.DataFrame({
            'Job Title': job_titles,
            'Company Name': company_names,
            'Date Posted': post_dates
        })
        df.to_csv('indeed_data_analyst_jobs.csv', index=False)
        print("Data saved to indeed_data_analyst_jobs.csv")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    scrape_indeed_jobs()