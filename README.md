# linkedin-detail-scrapper-from-jobs-page

This tool is used for educational purpose only. Scrapping is against LinkedIn's terms of condition.

Please use at your own risk! 

The python script 'scrapper.py' takes input of a simple csv file with only one column containing 
links to linked in job pages. 

Important: Links must be in the following format: https://www.linkedin.com/jobs/view/2698109989

If your link is in any other format, please take the job code out and replace the last string
https://www.linkedin.com/jobs/view/*


Following are required for this script to work:
- Pip dependencies mentioned in the code: BeautifulSoub, selenium, csv
- CSV file with the above-mentioned requirements
- Chrome web driver for your version


This script will take jobs links in put and export them in a CSV file with following colums
- Title
- URL
- Location
