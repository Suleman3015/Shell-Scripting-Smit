from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}


@app.get("/data")
def get_data():
    return data  

@app.get("/data/serverlist")
def server_list():
    data = readjson()
    return list(data.keys())


@app.get("/data/servername/{servername}")
def server_data_read(servername: str):
    data = readjson()
    return data.get(servername, "Server not found")

@app.post("/server")
def add_server(server_name:str,server_data: dict):
    data = readjson()
    if server_name in data:
        return {"message":"server already exists"}
    data[server_name] = server_data
    writejson(data)
    return {"message":"server added successfully"}

@app.put("/server/{server_name}/{status}")
def update_server_status(server_name:str,status:str):
    data = readjson()
    if server_name in data:
        data[server_name]['status'] = status
        writejson(data)
        return {"message":f"server {server_name} status updated to {status}"}
    return {"message":"server not found"}     

# to read the json file 
def readjson():
    with open('server.json','r') as file:     
        data = json.load(file)
    return data
# readjson = server_details()

# to write in the json file
def writejson(data):
    with open('server.json','w') as file:
        json.dump(data,file,indent=4)

data = readjson()

data['server1']['status'] = 'stopped'
print(data)
writejson(data)

        
                          