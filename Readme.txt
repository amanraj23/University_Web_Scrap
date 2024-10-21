NOTE: There are two python file which perform two different task.

University Information Scraper

This project scrapes general information, courses, and scholarships (if available) from a university website and saves the data in an Excel file.

Features:

Scrapes university info like name, email, contact number, and address.
Scrapes course details like course name, taught language, and fees.
Saves data in an Excel file with separate sheets for university info, courses, and scholarships.
Checks the website's robots.txt file to follow scraping rules.
Requirements:


Required libraries: Install by running:

pip install requests beautifulsoup4 pandas openpyxl
How to Use:

Download this project.
In the script, change the university_url to the website you want to scrape.
Run the script:
python university_info_scraper.py
The script checks the website’s robots.txt file to make sure scraping is allowed.
If allowed, the script scrapes the data and saves it in university_Detail_data.xlsx.
Main Files:

university_info_scraper.py: Main script to scrape information.
university_Detail_data.xlsx: The output file (created after running the script).
Functions:

scrape_university_info(university_url): Scrapes university info.
scrape_courses(university_url): Scrapes course details.
save_to_excel(university_info, courses, scholarships): Saves data into an Excel file.
check_robots_txt(website_url): Checks if scraping is allowed by reading robots.txt.
is_allowed_to_scrape(path, disallowed_paths): Verifies if scraping a specific path is allowed.
Note:

Always follow the rules in the website's robots.txt.
Adjust the scraping functions for different websites, as the structure may vary.
