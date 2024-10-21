import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import re

# Define the main function
def main():
    # URL of the university website to scrape
    university_url = 'https://www.harvard.edu/'

    try:
        # Send a GET request to the university page
        response = requests.get(university_url)
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting university general information
        university_name = "Harvard University"
        university_logo = soup.find('img', {'class': re.compile(r'logo')})['src'] if soup.find('img', {'class': re.compile(r'logo')}) else None
        university_header_picture = soup.find('img', {'class': re.compile(r'header')})['src'] if soup.find('img', {'class': re.compile(r'header')}) else None
        country = "USA"
        city = "Cambridge"
        university_full_address = "Massachusetts Hall, Cambridge, MA 02138"
        university_email = None  # Requires more specific scraping, or may need to visit a contact page
        university_contact_number = None  # Similar to email, would require more focused scraping
        university_website_url = university_url

        # Extracting course information
        courses = []
        course_elements = soup.find_all('a', href=True)
        for element in course_elements:
            if '/academics/' in element['href']:
                course_name = element.get_text(strip=True)
                course_url = element['href']
                if not course_url.startswith('http'):
                    course_url = university_url + course_url.lstrip('/')
                # Extract additional course details if available
                course_details = {
                    'University Name': university_name,
                    'Course Name': course_name,
                    'Course URL': course_url,
                    'University Website URL': university_website_url
                }
                courses.append(course_details)

        # Extracting scholarship information
        scholarships = []
        scholarship_elements = soup.find_all('a', href=True)
        for element in scholarship_elements:
            if '/financial-aid/' in element['href']:
                scholarship_name = element.get_text(strip=True)
                scholarship_url = element['href']
                if not scholarship_url.startswith('http'):
                    scholarship_url = university_url + scholarship_url.lstrip('/')
                # Extract additional scholarship details if available
                scholarship_details = {
                    'University Name': university_name,
                    'Scholarship Name': scholarship_name,
                    'Scholarship URL': scholarship_url,
                    'University Website URL': university_website_url
                }
                scholarships.append(scholarship_details)

        # Organize data into DataFrames
        university_data = {
            'University Name': [university_name],
            'University Logo': [university_logo],
            'University Header Picture': [university_header_picture],
            'Country': [country],
            'City': [city],
            'University Full Address': [university_full_address],
            'University Website URL': [university_website_url]
        }
        university_df = pd.DataFrame(university_data)
        course_df = pd.DataFrame(courses)
        scholarship_df = pd.DataFrame(scholarships)

        # Save data to an Excel file
        with pd.ExcelWriter('university_data.xlsx', engine='openpyxl') as writer:
            university_df.to_excel(writer, sheet_name='University Info', index=False)
            if not course_df.empty:
                course_df.to_excel(writer, sheet_name='Courses', index=False)
            if not scholarship_df.empty:
                scholarship_df.to_excel(writer, sheet_name='Scholarships', index=False)
        print("Data successfully saved to university_data.xlsx")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
