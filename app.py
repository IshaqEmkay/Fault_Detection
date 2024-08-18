from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np
import random

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load the trained model
model = joblib.load('vehicle_fault_model.pkl')

# List of possible fault descriptions
fault_descriptions = {
    1: "Squeaky engine noise due to loose reams rod bearings. Tighten reams or bearings.",
    2: "Blocked fuel filter. Replace fuel filter.",
    3: "Loose clutch due to weak clutch plates. Replace clutch plate.",
    4: "Clutch not responding due to leaking dance sleeve. Close the leak.",
    5: "Black exhaust emissions due to bad rings. Adjust pistons.",
    6: "Faulty links and metals. Adjust/replace links.",
    7: "Thin white exhaust emissions due to fouled injector. Change fuel injector.",
    8: "Exhaust system leak. Fix the leak.",
    9: "Thick white exhaust emissions due to fuel mixture being too rich. Adjust/replace carburetor.",
    10: "Bluish exhaust emissions due to greasy engine oil. Change lubrication oil.",
    11: "Non-starting cold engine due to a flat battery. Change/replace battery.",
    12: "Broken timing chain. Replace timing chain.",
    13: "Clogged air filter. Flush air filter.",
    14: "Faulty spark plugs. Replace spark plugs.",
    15: "Non-starting hot engine due to clogged air filter. Flush air filter.",
    16: "Leaking fuel injector. Replace/fix injector.",
    17: "Fuel mixture too rich. Adjust/replace carburetor.",
    18: "Lack of power due to bad timing belt. Adjust timing belt.",
    19: "Low fuel pressure. Replace pressure regulator.",
    20: "Incorrect grade of oil. Change lubrication oil.",
    21: "Hesitation or uneven running due to fuel injection system fault. Replace injector.",
    22: "Engine stalling or cutting out due to inductor vacuum leak. Seal leak.",
    23: "Idle speed issue due to injector mechanical leak. Seal injector leak.",
    24: "Engine knock due to worn spark plugs. Change spark plugs.",
    25: "Cooling fault. Check cooling fans.",
    26: "Build-up of carbon deposits in cylinders. Clean out cylinders.",
    27: "Fuel of low octane. Flush tank and change fuel.",
    28: "Engine backfires through exhaust valve due to injector mechanical fault. Clean injector/seal injector leaks.",
    29: "Leaking or burnt exhaust valve. Replace exhaust valve.",
    30: "Overheating due to burnt gasket. Replace gasket.",
    31: "Leaking radiator. Seal leak with sealant.",
    32: "Radiator choked up. Flush radiator/change coolant.",
    33: "Alternator belt not well tensioned. Adjust alternator belt.",
    34: "Screeching sound from engine due to bad adjustment of fan belt. Adjust/change fan belt.",
    35: "Car jerking due to bad plug adjustment. Change spark plugs.",
    36: "Water in fuel tank. Flush fuel tank.",
    37: "Choked fuel filter. Flush/replace filter."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    # Simulate the diagnosis process
    fault_code = random.randint(1, len(fault_descriptions))  # Randomly select a fault code
    fault_description = fault_descriptions[fault_code]  # Get the fault description based on the fault code
    
    return jsonify({'fault': fault_description})


    # Extract features from input data
    features = np.array([[data['engine_temp'], data['rpm'], data['speed'], data['error_code']]])

    # Predict the fault
    prediction = model.predict(features)

    # Generate a random fault description based on the prediction
    if prediction[0] == 0:
        fault_description = fault_descriptions[0]
    else:
        fault_description = random.choice(fault_descriptions[1:])

    return jsonify({'fault': fault_description})

if __name__ == '__main__':
    app.run(debug=True)
