import requests 
import json 

URL = "http://127.0.0.1:8000/codeapi/"


def get_coder(id=None):
    data={}
    if id is None:
        data={"id":id}
    json_data=json.dumps(data)
    headers={
        'Content-Type':'application/json'
      }
    r=requests.get(url=URL ,headers=headers, data=json_data)
    data=r.json()
    print(data)

# get_coder()

def post_coder():
    data={
        'name':'samarth',
        'domain':'full stack',
        'company':'microsoft'                                                                                                                                     
    }
    headers={
        'Content-Type':'application/json'
      }
    # convert data into json
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# post_coder()


# update coder 

def update_coder():
    data={
        'id':2,
        'name':'Steve Jobs',
    }
    headers={
        'Content-Type':'application/json'
      }
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

update_coder()

def delete_coder():
    data={
        'id':7,
        }
    headers={
        'Content-type':'application/json'
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# delete_coder()