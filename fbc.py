import requests
import json 
import MySQLdb

conn = MySQLdb.connect(host= "edx.devstack.mysql",
                  port=3506,
                  user="root",
                  passwd="",
                  db="fbc")
c = conn.cursor()

url = "https://online.fa.ru/oauth2/access_token/"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\nclient_credentials\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token_type\"\r\n\r\njwt\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\necommerce-key\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_secret\"\r\n\r\necommerce-secret\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'grant_type': "client_credentials",
    'token_type': "JWT",
    'client_id': "***",
    'client_secret': "***",
    'cache-control': "no-cache",
    'postman-token': "801a50dc-f49d-70de-6ca6-bf7fdd373482"
    }

   
response = requests.request("POST", url, data=payload, headers=headers)
response_native = json.loads(response.text)
access_token=(response_native.get('access_token'))
token_type=(response_native.get('token_type'))
expires_in=(response_native.get('expires_in'))
scope=response_native.get('scope')
id=headers.get('client_id')


try:
    c.execute('CREATE TABLE IF NOT EXISTS clients (id TEXT, access_token TEXT, token_type TINYTEXT, expires_in BLOB, scope TEXT)') 
    c.execute("INSERT INTO clients (id, access_token, token_type, expires_in, scope) VALUES(%s,%s,%s,%s,%s)", (id,access_token, token_type, expires_in, scope)) 
    conn.commit()
except:
    conn.rollback()

c.close() 
conn.close() 
