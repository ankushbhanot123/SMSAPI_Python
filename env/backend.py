from flask import Flask,request,jsonify,Response;
import json;
import requests;
import pyodbc;
app = Flask(__name__)

@app.route('/',methods=['POST'])
def baseAPI():
   data=request.data
   URL = "https://apisms.bongolive.africa/v1/send"
   user = "<USER_NAME>"
   passw = "<USER_PASSWORD>"
   requests.post(url=URL,data=data,auth=(user,passw),verify=False)
   return Response(
        json.dumps(request.data),
        status=200,
    )

@app.route('/submit',methods=['POST'])
def dataEntry():
    server="tcp:truckapp.database.windows.net,1433";
    database="dbTruckApp";
    username="truckuser";
    password="Amit@slinfyy";
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    data=request.get_json()
    print(type(data))
    request_id1=data['request_id']
    recipient_id1=data['recipient_id']
    dest_addr1=data['dest_addr']
    status1=data['Status']
    query_str="INSERT INTO dbo.SMSCallback (request_id,recipient_id,dest_addr,Status) VALUES("+"'"+request_id1+"','"+recipient_id1+"','"+dest_addr1+"','"+status1+"')"
    cursor.execute(query_str)
    cnxn.commit()
    return Response(
        json.dumps(data),
        status=200,
    )
@app.errorhandler(500)
def server_error(e):
    errorName="Server Error"
    return Response(
        json.dumps(errorName),
        status=500,
    )


if __name__ == '__main__':
    app.run(debug=True)
