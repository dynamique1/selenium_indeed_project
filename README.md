# Indeed Job Scraper

This project is a Python script that scrapes data analyst job postings from Indeed using Selenium. The script extracts job titles, company names, and the dates the jobs were posted, and saves this information to a CSV file.

## Features

- Scrapes job titles, company names, and posting dates from Indeed
- Uses Selenium for web scraping
- Saves the scraped data to a CSV file

## Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver
- Selenium
- pandas
- webdriver_manager

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/indeed-job-scraper.git
    cd indeed-job-scraper
    ```

2. **Create a virtual environment and activate it**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have ChromeDriver installed**

    The script uses `webdriver_manager` to automatically handle ChromeDriver installation. If you encounter issues, you can manually download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage

1. **Run the script**

    ```bash
    python indeed_scraper_demo.py
    ```

    The script will open a Chrome browser window, navigate to Indeed, and start scraping job postings. The data will be saved to a file named `indeed_data_analyst_jobs.csv` in the current directory.

## Script Details

### indeed_scraper_demo.py

This script contains the following functions:

- `scrape_indeed_jobs()`: Main function that handles the scraping process. It navigates to the Indeed job search page, extracts job information, and saves it to a CSV file.

### Example Output

The output CSV file will have the following columns:

- `Job Title`: The title of the job posting
- `Company Name`: The name of the company posting the job
- `Date Posted`: The date the job was posted

## Contributing

1. **Fork the repository**
2. **Create a new branch**

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Commit your changes**

    ```bash
    git commit -m "Add your feature"
    ```

4. **Push to the branch**

    ```bash
    git push origin feature/your-feature
    ```

5. **Open a pull request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Selenium and BeautifulSoup communities for their great libraries and documentation.

## Additional Steps
Create a requirements.txt file with the following contents:

selenium
pandas
webdriver_manager

Ensure the script file indeed_scraper_demo.py is included in the repository.

Customize the repository URL in the git clone command in the README if you have a specific URL.

Optionally, add more details about contributing guidelines and code of conduct if needed.
