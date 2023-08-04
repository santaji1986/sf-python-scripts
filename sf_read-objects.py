from simple_salesforce import Salesforce
import pandas as pd

def update_sf_object(isProduction, username, password_token):
    if(isProduction.lower() == 'y') :
        print(f"Signing-in to production with {username}")
        sf = Salesforce(username=username, password=password_token,security_token='')
    else :
        print(f"Signing-in to sandbox with {username}")
        sf = Salesforce(username=username, password=password_token,security_token='',domain='test')
    response = sf.query_all("""SELECT Id, Name FROM Profile where Name in ('System Administrator','System Administrator Interface')""")
    printResponse(response)
    
def printResponse(response):
    records = response["records"]
    print("Print records.")
    for record in records:
        print(f"Id : {record['Id']}, Name : {record['Name']}")
    
    print("Print using pandas")
    pdRecords = [dict(Id=rec['Id'], Name=rec['Name']) for rec in records]
    df=pd.DataFrame(pdRecords) 
    for index in df.index:
        print(f"Id : {df['Id'][index]}, Name : {df['Name'][index]}")

def get_credentials():
    isProduction = input("Login production (y/n)?")
    username = input("Enter your username: ")
    password_token = input("Enter your password+token: ")
    return isProduction, username, password_token

# Main function
def main():
    isProduction, username, password_token = get_credentials()
    print(f"isProduction : {isProduction}, Username : {username}, password_token : {password_token}")
    update_sf_object(isProduction, username, password_token)

if __name__ == "__main__":
    main()
