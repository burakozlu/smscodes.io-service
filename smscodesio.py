from time import sleep
import requests

apiKey = "your_api_key_is_here"

def getBalance():
    url = f"https://code.smscodes.io/api/sms/GetBalance?key={apiKey}"
    response = requests.get(url).json()
    return response["Balance"]

def services():
    url = f"https://code.smscodes.io/api/sms/GetServiceCodes?key={apiKey}"
    response = requests.get(url).json()
    return {str(x["ServiceName"]) : x["ServiceID"] for x in response["Services"]}

def getPrices(serviceID):
    url = f"https://code.smscodes.io/api/sms/GetServicePrices?serviceId={serviceID}&key={apiKey}"
    response = requests.get(url).json()
    return response["Prices"]

def getNumber(country,serviceID):
    url = f"https://code.smscodes.io/api/sms/GetServiceNumber?key={apiKey}&iso={country}&serv={serviceID}"
    response = requests.get(url).json()
    return response

def getSMSCode(securityID, number):
    url = f"https://code.smscodes.io/api/sms/GetSMSCode?key={apiKey}&sid={securityID}&number={number}"
    while True:
        response = requests.get(url).json()
        if(response["SMS"] != "Message not received yet"):
            break
        sleep(10)
        print(response)
    return response


print("Your balance is : " + str(getBalance()))
service = services()
for x in service:
    print(x)
serviceID = service[input("Chosen Service Name: ")]
print(serviceID)
country = input("Enter ISO Country Code: ")
numberSession = getNumber(country,serviceID)
print("Use this number: ", numberSession["Number"])
getSMSCode(numberSession["SecurityId"],numberSession["Number"])