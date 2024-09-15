import requests

pix_endp = "https://pixe.la/v1/users"


#parameters for pixela user creation
pix_params = {
    "token" : "MySecretToken1",
    "username" : "esseklex",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
 }

headers = {
    "X-USER-TOKEN" : "MySecretToken1"
}


##Create pixela user
# response = requests.post(url= pix_endp, json= pix_params)
#check if response is working
# print(response.text)

##Create a graph

graph_endp = f"{pix_endp}/esseklex/graphs"

#graph requirements
graph_config = {
    "id" : "graph1",
    "name" : "reading log",
    "unit" : "pages read",
    "type" : "int",
    "color" : "shibafu"
}

# response = requests.post(url= graph_endp, json= graph_config, headers= headers)
# print(response.text) #check if request is working

##fill in the graph by posting a pixel

pixel_endp = f"{pix_endp}/esseklex/graphs/graph1"

pixel_config = {
    "date" : "20240901",
    "quantity" : "56"
}

#Add pixels as days progress

# add_days = {"date" : "20240902",
#              "quantity" : "26"}

#input a few days at a time
            
add_multiple = f"{pix_endp}/esseklex/graphs/graph1/pixels"

add_pixels = [{"date" : "20240903",
              "quantity" : "47"},
            {"date" : "20240904",
              "quantity" : "204"},
            {"date" : "20240907",
              "quantity" : "23"},
            {"date" : "20240909",
              "quantity" : "106"}]

response = requests.post(url= add_multiple, json= add_pixels, headers= headers)
print(response.text)
