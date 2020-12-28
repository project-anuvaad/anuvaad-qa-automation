import os.path
from os import path
import json
import requests
import time


def get_auth():
    print("GETTING AUTH TOKEN")
    url =  URL_HOST+AUTH_ENDPOINT
    # print(url)
    payload="{\"userName\":\""+LOGIN_USERNAME+"\",\"password\":\""+LOGIN_PASSWORD+"\"}"
    # print(payload)
    headers = {'content-type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    response_json = response.json()
    if response.status_code ==200:
        print("GOT THE AUTH TOKEN")
        return response_json["data"]["token"]
    else:
        raise Exception("User Login error")

def upload_local_file(full_path_file_to_be_uploaded):
    print("UPLOADING THE LOCAL FILE")
    if path.exists(full_path_file_to_be_uploaded):
        url = URL_HOST+UPLOAD_FILE_ENDPOINT

        files=[ ('file',(file_to_be_uploaded, open( full_path_file_to_be_uploaded,'rb'))) ]
        headers = {'auth-token': AUTH}
        # print(headers)

        response = requests.post(url, headers=headers, files=files)
        # print(json.dumps(response.json(), indent=4))
        response_json = response.json()
        if response.status_code ==200:
            print("FILE UPLOADED")
            return response_json["data"]
        else:
            raise Exception("UPLOAD error")
    else:
        raise Exception("FILE NOT FOUND: ", full_path_file_to_be_uploaded)


#Variables
RUNNING_FOR_ENV = "BOTH" #It can be LOCAL, WEB, BOTH
URL_HOST = "https://auth.anuvaad.org"
UPLOAD_FILE_ENDPOINT = "/anuvaad-api/file-uploader/v0/upload-file"
JOB_INITIATE_ENDPOINT = "/anuvaad-etl/wf-manager/v1/workflow/async/initiate"
AUTH_ENDPOINT= "/anuvaad/user-mgmt/v1/users/login"
BULK_SEARCH_ENDPOINT = "/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk"
SERVE_FILE_ENDPOINT = "/anuvaad-api/file-uploader/v0/serve-file"

LOGIN_USERNAME = "<USERNAME>"
LOGIN_PASSWORD = "<PASSWORD>"
AUTH = ""


file_name = "/home/abhilash/Desktop/anuvaad_test_script/f0996c5d-9c14-4aed-a956-a846476ce441.json"
full_path_file_to_be_uploaded = "/home/abhilash/Desktop/anuvaad_test_script/f0996c5d-9c14-4aed-a956-a846476ce441.pdf" 
file_to_be_uploaded = full_path_file_to_be_uploaded.split("/")[-1]

UPLOADED_FILE_NAME = ""

WORKFLOW_CODE_BLOCKMERGER = "WF_A_FCBM"
WORKFLOW_CODE_TOKENIZER = "WF_A_FCBMTK"

page_details_local = {}
page_details_web = {}




def create_map_for_input_file(file_obj):
    block_map = {}
    page_details = {}
    global page_details_local
    global page_details_web
    

    if RUNNING_FOR_ENV == "WEB":
        root_key = "result"
        page_details = page_details_web
    if RUNNING_FOR_ENV == "LOCAL":
        root_key = "data"
        page_details = page_details_local
    
    # print(type(file_obj[root_key]))
    if file_obj[root_key] is not None and isinstance(file_obj[root_key], list):
        for count_page_no, page_data in enumerate(file_obj[root_key]):
            # print("Page No: ", count_page_no)
            # print(type(page_data["text_blocks"]))
            if page_data["text_blocks"] is not None and isinstance(page_data["text_blocks"], list):
                for count_text_block_no, text_block in enumerate(page_data["text_blocks"]):
                    # print("text_blocks : ", count_text_block_no)
                    if text_block["text"] is not None and isinstance(text_block["text"], str):
                        text_key = "PAGE_NO_"+ str(count_page_no) +"_TEXT_BLOCK_NO_"+ str(count_text_block_no)
                        text_value = text_block["text"]
                        block_map[text_key] = text_value
                        page_details[count_page_no] = count_text_block_no
                    else:
                        raise Exception("text_block[\"text\"]: text field needs to be of String type")
            else:
                raise Exception("page_data[\"text_blocks\"]: text_blocks field needs to be of list type")
    else:
        raise Exception("file_obj[\"data\"]: data field needs to be of list type")
    
    # print(block_map)
    return block_map




def open_local_json_file(file_name):
    if path.exists(file_name):    
        with open(file_name, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    else:
        raise Exception("File Not Found at: ",os.path.join( os.path.dirname(__file__), file_name) )


    


def initiate_workflow(WORKFLOW_CODE):
    print("INITIATED THE JOB")
    #    payload = "{'workflowCode': "+ WORKFLOW_CODE +",'jobName': "+file_to_be_uploaded +",'files': [{'path': "+UPLOADED_FILE_NAME +", 'type': "+ UPLOADED_FILE_NAME.split('.')[-1] +",'locale': 'en','model': {'model_id': 56,'source_language_code': 'en','source_language_name': 'English','status': 'ACTIVE','target_language_code': 'hi','target_language_name': 'Hindi'},'context': 'JUDICIARY'}]}"

    payload = "{\n    \"workflowCode\": \""+ WORKFLOW_CODE +"\",\n    \"jobName\": \""+file_to_be_uploaded+"\",\n    \"files\": [\n        {\n            \"path\": \""+ UPLOADED_FILE_NAME +"\",\n            \"type\": \""+ UPLOADED_FILE_NAME.split('.')[-1] +"\",\n            \"locale\": \"en\",\n            \"model\": {\n                \"model_id\": 56,\n                \"source_language_code\": \"en\",\n                \"source_language_name\": \"English\",\n                \"status\": \"ACTIVE\",\n                \"target_language_code\": \"hi\",\n                \"target_language_name\": \"Hindi\"\n            },\n            \"context\": \"JUDICIARY\"\n        }\n    ]\n}"
    
    headers = {'auth-token': AUTH, "content-type": 'application/json'}

    url = URL_HOST + JOB_INITIATE_ENDPOINT
    
    # print("URL: ", url)
    # print("PAYLOAD: ", payload)
    # print("HEADERS: ", json.dumps(headers, indent=2))

    response = requests.request("POST",url, headers= headers, data=payload)

    print("Got Response From initiate_workflow")
    response_json = response.json()

    if response.status_code in [200, 201, 202]:
        return response_json["jobID"]
    else:
        raise Exception("JOB INITIATE error")



def bulk_search( workflow_code, jobid):
    print("INITIATE BULK SEARCH")
    
    url = URL_HOST + BULK_SEARCH_ENDPOINT
    payload = "{\n    \"offset\": 0,\n    \"limit\": 10,\n    \"jobIDs\": [\n        \""+jobid+"\"\n    ],\n    \"taskDetails\": true,\n    \"workflowCodes\": [\n        \""+workflow_code+"\"\n    ]\n}"
    headers = {'auth-token': AUTH,  'content-type': 'application/json'}

    time.sleep(10.1)
    
    response = requests.request("POST", url, headers=headers, data=payload).json() 
    # print(response)

    staus =  response.get("jobs")[0]["status"]
    output_file = response.get("jobs")[0]["output"][0]["outputFile"]
    print("Current status for the Job : {} and File name : {} ".format(staus,output_file))
     

    while staus != "COMPLETED":
        time.sleep(10.0)
        print("Trying to fetch the status after 10 sec")
        response = requests.request("POST", url, headers=headers, data=payload).json()
        staus =  response["jobs"][0]["status"]
        output_file = response.get("jobs")[0]["output"][0]["outputFile"]

        print("Current status for the Job : {} and File name : {} ".format(staus,output_file))

    return output_file


def serve_file(file_name):
    print("SERVE FILE STARTED")

    url = URL_HOST + SERVE_FILE_ENDPOINT + "?filename=" + file_name
    headers = {  'auth-token': AUTH}

    response = requests.request("GET", url, headers=headers)

    print("Serve File Completed.")

    return response.json()




def flow_for_web():
    global AUTH 
    AUTH = get_auth()
    global UPLOADED_FILE_NAME 
    UPLOADED_FILE_NAME = upload_local_file(full_path_file_to_be_uploaded)
    print("INITIATING A JOB")
    jobid = initiate_workflow(WORKFLOW_CODE_BLOCKMERGER)
    print("JOBID : ", jobid)
    file_name = bulk_search(WORKFLOW_CODE_BLOCKMERGER, jobid)
    response_json = serve_file(file_name)
    return create_map_for_input_file(response_json)

def flow_for_local():
    response_json = open_local_json_file(file_name)
    print("Got the Local json Map")
    return create_map_for_input_file(response_json)
 
def compare_text_block_map(local_file_map, web_file_map):
    mismatch_found = False
    if len(local_file_map) != len(web_file_map):
        print("BOTH MAP HAVE DIFFERENT TEXT BLOCK SIZE, LOCAL FILE HAS: {} AND WEB FILE HAS: {}".format(str(len(local_file_map)), str(len(web_file_map))))
        compare_page_and_text_block_no(page_details_local, page_details_web)

    for key, value in local_file_map.items():
        if value != web_file_map[key]:
            mismatch_found = True
            print("Content mismatch:")
            print("Key: {}".format(key))
            print("\tValue in LOCAL file: {}".format(value))
            print("\tValue in WEB   file: {}".format(web_file_map[key]))
    if mismatch_found == False:
        print("NO MISMATCH FOUND, BOTH FILES ARE IDENTICAL\n\n")

def compare_page_and_text_block_no(page_details_local, page_details_web):
    print("Total no of page in Local: {} \n Total no of page in Web: {}".format(str(len(page_details_local)), str(len(page_details_web))))
    for page_no, text_block_no in page_details_local.items():
        if text_block_no == page_details_web[page_no]:
            print("In both the file Page Number {} has same no of text block which is {}".format(str(text_block_no)))
        else:
            print("Different no of text block in both file in page no{}, in local:{} and in web: {}".format(str(page_no),str(text_block_no), str(page_details_web[page_no])))
        



#FLOW 1: Initiate a job through API
if RUNNING_FOR_ENV == "WEB":
   flow_for_web()



#FLOW 2: 
if RUNNING_FOR_ENV == "LOCAL":
    flow_for_local()

#FLOW 3:
if RUNNING_FOR_ENV == "BOTH":
    RUNNING_FOR_ENV = "LOCAL"
    print("\n\nRunning for Enviroment: ",RUNNING_FOR_ENV)
    text_block_map_from_local = flow_for_local()
    # print("page_details_local", page_details_local)
    RUNNING_FOR_ENV = "WEB"
    print("\n\nRunning for Enviroment: ",RUNNING_FOR_ENV)
    text_block_map_from_web = flow_for_web()
    # print("page_details_web", page_details_web)

    print("\n\n===============================================================================================")
    print("\t\tGOT BOTH THE KEY VALUE MAP FROM LOCAL AND WEB FILE")
    print("===============================================================================================\n\n")
    compare_text_block_map(text_block_map_from_local, text_block_map_from_web)


    
    









