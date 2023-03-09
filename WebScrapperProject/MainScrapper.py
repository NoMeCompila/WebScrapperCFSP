import requests

URL: str = 'https://www.scrapethissite.com/pages/'


def get_html_structure(url: str) -> str:
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        return content


def create_html_file(html_structure: str, file_name: str):
    with open(file_name, 'w+') as file:
        file.write(html_structure)


if __name__ == '__main__':

    # print(get_html_structure(URL))
    html_content = get_html_structure(URL)
    # create_html_file(html_content, 'sandboxcopy.html')

