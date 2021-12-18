import requests
import json


credentials = 'CdzhuVrsftMAAAAAAAAAAfuWmHbRXwPh4CffqWPP080A6n8qVsUXo8rDRf56ELKy'


url_upload = "https://content.dropboxapi.com/2/files/upload"
payload_upload = "Eliseeva Anastasiia"
headers_upload = {
    'Dropbox-API-Arg': '{"path": "/file.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
    'Content-Type': 'application/octet-stream',
    'Authorization': f'Bearer {credentials}'
}

response_upload = requests.request("POST", url_upload, headers=headers_upload, data=payload_upload)



url_gfm = "https://api.dropboxapi.com/2/files/get_metadata"
payload_gfm = json.dumps({
    "path": "/file.txt"
})
headers_gfm = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {credentials}'
}

response_gfm = requests.request("POST", url_gfm, headers=headers_gfm, data=payload_gfm)




url_delete = "https://api.dropboxapi.com/2/files/delete_v2"
payload_delete = json.dumps({
    "path": "/file.txt"
})
headers_delete = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {credentials}'
}

response_delete = requests.request("POST", url_delete, headers=headers_delete, data=payload_delete)
