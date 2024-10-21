# University Scraper

This script scrapes general information, course details, and scholarship data from a university website and saves the collected information into an Excel file.

## Prerequisites

Ensure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

You can install these dependencies using the following command:

```sh
pip install requests beautifulsoup4 pandas openpyxl
```

## How to Run the Script

1. **Clone or download the repository** containing this script.
2. **Navigate** to the folder containing the script.
3. **Run the script** using Python:

   ```sh
   python university_scraper.py
   ```

## Script Overview

The script performs the following actions:

1. **Checks the `robots.txt` file** of the university website to determine if scraping is allowed.
2. **Scrapes university general information**, such as name, email, contact number, and address.
3. **Scrapes course details**, including course name, language, and tuition fees.
4. **Saves the scraped data** into an Excel file (`university_data.xlsx`) with three sheets:
   - University Info
   - Courses
   - Scholarships (currently left empty)

## Important Notes

- The script is set to scrape data from **Stanford University** (`https://www.stanford.edu/`).
- Ensure that scraping is in compliance with the website's **terms of service**.
- The script uses **rate limiting** with `time.sleep(1)` to avoid overwhelming the server.

## Modifying the Target University

To scrape a different university, update the `university_url` variable in the script:

```python
university_url = 'https://www.new-university.edu/'
```

## Output

The script generates an Excel file named **`university_data.xlsx`** containing three sheets:

- **University Info**: Contains general information about the university.
- **Courses**: Contains details about the courses offered by the university.
- **Scholarships**: Currently left empty, but can be modified to include scholarship information.

## License

This project is licensed under the MIT License.

