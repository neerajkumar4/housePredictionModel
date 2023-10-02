import json
import pickle
import numpy as np

__locations = None
__dataColumns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__dataColumns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__dataColumns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_name():
    return __locations

def load_artifacts():
    print("Loading artifacts--->start")

    global __locations
    global __dataColumns
    global __model 

    with open("./artifacts/columns.json",'r') as f:
        __dataColumns=json.load(f)['data_columns']
        __locations= __dataColumns[3:]
    with open("./artifacts/bangloreHousePriceModel.pickle",'rb') as f:
        __model = pickle.load(f)

    print("Loading artifacts--->done!")

if __name__ == '__main__':
    load_artifacts()
    print(get_location_name())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('Rajaji Nagar',1000,2,2))  #other location
    print(get_estimated_price('Ejipura',1000,2,2))     #ther location
    