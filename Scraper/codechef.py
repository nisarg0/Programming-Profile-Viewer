# import json
# import requests


# from bs4 import BeautifulSoup


# class UsernameError(Exception):
#     pass

# def codechef_api(id):
#         url = 'https://www.codechef.com/users/{}'.format(id)
#         page = requests.get(url)

#         soup = BeautifulSoup(page.text, 'html.parser')

#         def get_ratings():
#             # print(soup)
#             try:
#                 rating = soup.find('div', class_='rating-number').text
#             except AttributeError:
#                 raise UsernameError('User not Found')

#             stars = soup.find('span', class_='rating')
#             if stars:
#                 stars = stars.text

#             highest_rating_container = soup.find('div', class_='rating-header')
#             highest_rating = highest_rating_container.find_next('small').text.split()[-1].rstrip(')')

#             rating_ranks_container = soup.find('div', class_='rating-ranks')
#             rating_ranks = rating_ranks_container.find_all('a')

#             global_rank = rating_ranks[0].strong.text
#             country_rank = rating_ranks[1].strong.text

#             if global_rank != 'NA':
#                 global_rank = int(global_rank)
#                 country_rank = int(country_rank)
            
#             return {
#                 'Rating': rating,
#                 'Starts': stars,
#                 'Highest Rating':highest_rating,
#                 'Global Rank':global_rank,
#                 'Country Rank':country_rank
#             }

#         def get_user_details():
#             header_containers = soup.find_all('header')
#             name = header_containers[1].find('h1', class_="h2-style").text

#             user_details_section = soup.find('section', class_='user-details')
#             user_details_list = user_details_section.find_all('li')

#             return {
#                 'name': name, 
#                 'username': user_details_list[0].text.split('★')[-1].rstrip('\n'),
#                 'country': user_details_list[1].text.split(':')[-1].strip(),
#                 'state': user_details_list[2].text.split(':')[-1].strip(),
#                 'city': user_details_list[3].text.split(':')[-1].strip(),
#                 'student/professional': user_details_list[4].text.split(':')[-1].strip(),
#                 'institution': user_details_list[5].text.split(':')[-1].strip()
#             }
#         ratings = get_ratings()
#         userDetails = get_user_details()
#         result = userDetails
#         result.update(ratings)
#         print(result)
#         return result

# # json.dumps(codechef_api('nisarg_0'))
# codechef_api('nisarg_0')

print({'name': 'Nisarg Gogate', 'username': 'nisarg_0', 'country': 'India', 'state': 'Maharashtra', 'city': 'Nagpur', 'student/professional': 'Student', 'institution': 'Visvesvaraya National Institute of Technology, Nagpur Maharashtra, India', 'Rating': '1974', 'Starts': '4★', 'Highest Rating': '1974', 'Global Rank': 6798, 'Country Rank': 4719})
