from bs4 import BeautifulSoup
import requests


def get_food(section):
    result = requests.get("http://www.ruled.me/keto-recipes/{}".format(section))
    soup = BeautifulSoup(result.text, 'html.parser')

    navigation = soup.find('div', {'class': 'navigation'})
    total_pages = int(navigation.find_all('a')[-2].text)
    print(repr(total_pages))

    for page in range(1, total_pages+1):
        result = requests.get("http://www.ruled.me/keto-recipes/{}/page/{}".format(section, page))
        soup = BeautifulSoup(result.text, 'html.parser')
        posts = soup.find_all("div", {'class': 'post'})

        for post in posts:
            try:
                title = post.find('h2', {'class': 'entry-title'}).text
                post_link = post.find('a')['href']
                post_details = BeautifulSoup(requests.get(post_link).text, 'html.parser')
                table = post_details.find('table')

                # Find the last row in the table
                last_row = table.find_all('tr')[-1].find_all('td')

                # Get details
                servings = last_row[0].text.split('/')[1].replace(')', '')
                calories = last_row[1].text
                carbs = last_row[3].text

                print(title)
                print("Servings: {} | Calories: {} | Carbs: {}".format(servings, calories, carbs))

            except:
                print(post_link)
