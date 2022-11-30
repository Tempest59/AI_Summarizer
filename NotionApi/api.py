import requests, json

token = 'secret_t1cuxyZwo1IVPGgtfNvDXEu6LaXvgpZRYvq4txBkrhe'

databaseId = '4d008ab360dd4678b6b5a5e37230ce3c' 

headers = {
    "Authorization": "Bearer " + token,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json"

}

def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}"
    
    res = requests.request("GET", readUrl, headers=headers)
    print(res.status_code)
    print(res.text)


def createPageData(titre, emoji, cover_url, content):
    data = {
    "parent": { "database_id": databaseId },
    "icon": {
  	"emoji": emoji
    },
    "cover": {
		"external": {
			"url": cover_url
		}
	},
    "properties": {
        "title": {
      "title": [{ "type": "text", "text": { "content": titre } }]
        }
    },
    "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "type": "text", "text": { "content": content } }]
      }
    }
  ]
}
    return data


def createPage(pageData):

    createUrl = "https://api.notion.com/v1/pages/"


    data = json.dumps(pageData)


    response = requests.request("POST", createUrl, headers=headers, data=data)
    print(response.status_code)
    print(response.text)
    

def updatePage():
    pass

