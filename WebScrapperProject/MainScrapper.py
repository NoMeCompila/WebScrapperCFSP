import requests
import re

URL: str = 'https://www.scrapethissite.com/pages/'


def get_html_structure(url: str) -> str:
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        return content


def create_html_file(html_structure: str, file_name: str):
    with open(file_name, 'w+') as file:
        file.write(html_structure)


def get_titles(url: str, regex: str) -> list:
    titles = []
    content = get_html_structure(url)
    for title in re.findall(regex, content):
        titles.append(title[1])
    return titles


if __name__ == '__main__':
    #regex = '<a href="(.+?)">(.+?)</a>'
    tag = '<a href="(.+?)">(.+?)</a>'
    print(get_titles(URL, tag))