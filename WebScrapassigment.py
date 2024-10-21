import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

# Function to scrape the university's general information
def scrape_university_info(university_url):
    try:
        response = requests.get(university_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scrape the university name with multiple possible selectors
        university_name_tag = soup.find('h1', {'class': 'university-name'}) or soup.find('title')
        university_name = university_name_tag.text.strip() if university_name_tag else "N/A"

        # Scrape the university email (find the first 'mailto' link)
        email_tag = soup.find('a', href=lambda x: x and 'mailto' in x)
        university_email = email_tag['href'].replace('mailto:', '').strip() if email_tag else "N/A"

        # Scrape the university contact number with multiple possible selectors
        contact_tag = soup.find('span', {'class': 'contact-number'}) or soup.find('a', href=lambda x: x and 'tel' in x)
        university_contact = contact_tag.text.strip() if contact_tag else "N/A"

        # Scrape the university address with broader tag search
        address_tag = soup.find('address') or soup.find('p', {'class': 'address'})
        university_address = address_tag.text.strip() if address_tag else "N/A"

        # Placeholder for additional information
        university_logo = "N/A"
        university_header_picture = "N/A"
        country = "USA"
        city = "Stanford"

        return {
            'University Name': university_name,
            'University automatic code': 'N/A',
            'University Logo': university_logo,
            'University Header Picture': university_header_picture,
            'University Pictures': 'N/A',
            'Country': country,
            'City': city,
            'University Full Address': university_address,
            'University Email': university_email,
            'University contact number': university_contact,
            'US News & World Report Ranking 2024': 'N/A',
            'QS Ranking 2024': 'N/A',
            'THE (Times Higher Education) Ranking 2024': 'N/A',
            'ARWU (Shanghai Ranking) Ranking 2024': 'N/A',
            'Our Ranking': 'N/A',
            'University Type': 'N/A',
            'University Info': 'N/A',
            'Application fee waived': 'N/A',
            'University website URL': university_url
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching university info: {e}")
        return {
            'University Name': "N/A",
            'University automatic code': 'N/A',
            'University Logo': 'N/A',
            'University Header Picture': 'N/A',
            'University Pictures': 'N/A',
            'Country': 'N/A',
            'City': 'N/A',
            'University Full Address': 'N/A',
            'University Email': 'N/A',
            'University contact number': 'N/A',
            'US News & World Report Ranking 2024': 'N/A',
            'QS Ranking 2024': 'N/A',
            'THE (Times Higher Education) Ranking 2024': 'N/A',
            'ARWU (Shanghai Ranking) Ranking 2024': 'N/A',
            'Our Ranking': 'N/A',
            'University Type': 'N/A',
            'University Info': 'N/A',
            'Application fee waived': 'N/A',
            'University website URL': 'N/A'
        }

# Function to scrape courses
def scrape_courses(university_url):
    try:
        response = requests.get(university_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        courses = []
        # Extracting course-related content from potential course-related sections
        course_sections = soup.find_all(['section', 'div'], {'class': lambda x: x and 'course' in x.lower()})
        for section in course_sections:
            course_name_tag = section.find(['h2', 'h3'])
            course_name = course_name_tag.text.strip() if course_name_tag else "N/A"

            if course_name != "N/A":
                courses.append({
                    'Course Name': course_name,
                    'University Name': 'Stanford University',
                    'Course Level': 'N/A',
                    'Study Major': 'N/A',
                    'Discipline': 'N/A',
                    'Specialization': 'N/A',
                    'School / Department': 'N/A',
                    'Course Overview': 'N/A',
                    'Course Taught Language': 'English',
                    'Course open for intake': 'N/A',
                    'Course admission open for the years': 'N/A',
                    'Course attendance type': 'N/A',
                    '1st Year tuition fees': 'N/A',
                    'Total Tuition Fee': 'N/A',
                    'Tuition Fee Currency': 'USD',
                    'Duration in Months': 'N/A',
                    'Course URL': university_url,
                    '12th Grade requirement': 'N/A',
                    'Undergraduate degree requirement': 'N/A',
                    'Minimum IELTS score required': 'N/A',
                    'Minimum TOEFL score required': 'N/A',
                    'Minimum PTE score required': 'N/A',
                    'Minimum Duolingo English Test score required': 'N/A',
                    'Minimum Cambridge English Exams score required': 'N/A',
                    'Other English Language test score accepted': 'N/A',
                    'GRE score required': 'N/A',
                    'GMAT score required': 'N/A',
                    'SAT score required': 'N/A',
                    'ACT score required': 'N/A',
                    'Without GRE': 'N/A',
                    'Without GMAT': 'N/A',
                    'Without English Proficiency Test': 'N/A',
                    'Application Fee amount': 'N/A',
                    'Application Fee currency': 'USD',
                    'Application material or List of documents Required': 'N/A',
                    'FT (Financial Times) Ranking 2024': 'N/A',
                    'Acceptance rate': 'N/A',
                    'Home country / domestic students application deadline': 'N/A',
                    'International Applicant Deadlines': 'N/A'
                })

        return courses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching courses: {e}")
        return []

# Function to save the scraped data into an Excel file
def save_to_excel(university_info, courses, scholarships):
    try:
        # Create a DataFrame for university info
        university_df = pd.DataFrame([university_info])

        # Create DataFrames for courses and scholarships
        courses_df = pd.DataFrame(courses)
        scholarships_df = pd.DataFrame(scholarships)

        # Write all DataFrames to an Excel file with multiple sheets
        with pd.ExcelWriter('university_Detail_data.xlsx', engine='openpyxl') as writer:
            university_df.to_excel(writer, sheet_name='University Info', index=False)
            courses_df.to_excel(writer, sheet_name='Courses', index=False)
            scholarships_df.to_excel(writer, sheet_name='Scholarships', index=False)

        print("Data saved to 'university_Detail_data.xlsx'")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")

# Function to check robots.txt file
def check_robots_txt(website_url):
    robots_url = website_url + '/robots.txt'
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            print("robots.txt found:")
            print(response.text)

            # Basic parsing of robots.txt
            rules = response.text.splitlines()
            disallowed_paths = []
            for rule in rules:
                if rule.startswith('Disallow:') and ': ' in rule:
                    disallowed_paths.append(rule.split(': ', 1)[1].strip())

            return disallowed_paths
        else:
            print("robots.txt not found.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching robots.txt: {e}")
        return []

# Function to check if scraping is allowed
def is_allowed_to_scrape(path, disallowed_paths):
    for disallowed in disallowed_paths:
        if path.startswith(disallowed):
            return False
    return True

# Main script
if __name__ == '__main__':
    university_url = 'https://www.stanford.edu/'

    # Check robots.txt for scraping permissions
    disallowed_paths = check_robots_txt(university_url)

    # Scrape university info, courses, and scholarships if allowed
    if is_allowed_to_scrape('/', disallowed_paths):
        university_info = scrape_university_info(university_url)
        time.sleep(1)  # Rate limiting
        courses = scrape_courses(urljoin(university_url, '/academics'))
        time.sleep(1)  # Rate limiting
        scholarships = []  # No specific scholarships page found, keeping empty list

        # Save data to Excel
        save_to_excel(university_info, courses, scholarships)
    else:
        print("Scraping is not allowed based on robots.txt")
