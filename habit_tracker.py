import requests
from datetime import datetime


DATE = datetime(year=2021, month=7, day=25)  # the date that you want to MAKE A CHANGE
# test https://pixe.la/v1/users/abduvali/graphs/tracker1.html

# ################  CONSTANTS  ###################
USERNAME = "put your username here"    # this site 👉 https://pixe.la/ is used to make a habit graph
TOKEN = "write anything for token"
GRAPH_ID = "your graph name"
pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}


# ####################  CREATE A USER  ##############################
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}
response = requests.post(url=pixela_endpoint, json=user_params)


# #####################  CREATE A GRAPH  ############################
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Qur'an reciting tracker graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"}  # it is a green color
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)    #then uncomment this


# ####################  POST ITEM INTO A PIXEL  ######################
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages have you read today?:  ")}
# response = requests.post(url=post_pixel_endpoint, json=pixel_configs, headers=headers)


# #######################  UPDATE ITEM IN THE GRAPH  #######################
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE.strftime('%Y%m%d')}"
update_config = {
    "quantity": "7"}
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)


# ######################  DELETE ITEM FROM GRAPH  ###########################
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)


print(response.text)
