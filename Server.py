#flask is module which allow us write python service which serve http requests
#here we are using Anaconda as the interpreter(Anaconda comes with the flask)
#if we are not using anaconda then we have do "pip install flask"

from flask import Flask, request, jsonify
import util

app=Flask(__name__)
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft =float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft, bath, bhk)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting python flask server for home price prediction")
    util.load_saved_artifacts()
    app.run(debug=True)

#All of our code is written and now it is the time to do testing now,for this we can use "Postman Application",we can download it for free.
#The post man application is used to test your http calls
