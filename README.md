# Supermicro webcrawler

This Python web crawler is designed to meticulously traverse the Supermicro website by using BFS, systematically indexing and categorizing all PDF and text files it encounters. By leveraging the Selenium library, it navigates through the site, identifying relevant files such as case studies, datasheets, brochures, white papers, guides, and miscellaneous documents. The crawler intelligently organizes these files into logical groupings, ensuring that every valuable resource on the Supermicro website is efficiently cataloged for easy access and reference.

## Installation

### install chrome driver
please use below link to install chrome driver under the project root folder
https://chromedriver.chromium.org/downloads

### create venv
```bash
# create venv
$ python3 -m venv venv
# start venv
$ source ./venv/bin/activate
```

### install requirement
```bash
$ pip install -r requirements.txt
```



## Usage

### initiate supermicro crawler, the file will be saved under ./file/
```bash
$ python3 main.py
```

### initiate file categorizing

```bash
$ python3 categorize.py
```

## Future work
Some datasheets don't have the ".pdf" extension in the URL, as shown in the "datasheet_tag_problem.png" image. We need to identify and handle these special cases to ensure proper file handling and processing.