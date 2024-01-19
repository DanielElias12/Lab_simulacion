import requests
from firebase_admin import db
from firebase_admin import credentials, firestore
import firebase_admin
import pyrebase
firebase_sdk = credentials.Certificate('C:\\Users\\daeli\\Desktop\\lab-simulacion-firebase-adminsdk-rj5w1-75b9f2edce.json')
firebase_admin.initialize_app(firebase_sdk, {'databaseURL':'https://lab-simulacion-default-rtdb.firebaseio.com/'})

random_api_url = "http://www.randomnumberapi.com/api/v1.0/random"

def get_random_number():
    response = requests.get(random_api_url)
    data = response.json()
    number = data[0] if isinstance(data, list) and len(data) > 0 else None
    
    return number


def main():
    random_number = str(get_random_number())
    ref= db.reference(random_number)
    ref.push({'carnet': '1247020', 'nombre' : 'Daniel Elias'})
    print(f'Se ha generado el número aleatorio {random_number} y se ha guardado en Firebase.')

if __name__ == "__main__":
    main()