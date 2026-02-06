from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Store patient records
patients = []
patient_id = 1


# Home page
@app.route("/")
def home():
    return "Welcome To Hospital Management System"


# Patient Registration HTML page
@app.route("/register")
def register_page():
    return render_template("patient_registration.html")


# Get all patients
@app.route("/api/patients", methods=["GET"])
def get_all_patients():
    if not patients:
        return jsonify({
            "status": "error",
            "message": "No patient records available"
        }), 404

    return jsonify({
        "status": "success",
        "total_records": len(patients),
        "data": patients
    }), 200


# Register a new patient
@app.route("/api/patients", methods=["POST"])
def register_patient():
    global patient_id
    data = request.json

    # Check request body
    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body is missing"
        }), 400

    # Validate patient name
    if "name" not in data or data["name"].strip() == "":
        return jsonify({
            "status": "error",
            "message": "Patient name is mandatory"
        }), 400

    # Validate patient age
    if "age" not in data:
        return jsonify({
            "status": "error",
            "message": "Patient age is mandatory"
        }), 400

    try:
        age = int(data["age"])
        if age <= 0:
            raise ValueError
    except:
        return jsonify({
            "status": "error",
            "message": "Age must be a valid positive number"
        }), 400

    # Validate gender
    if "gender" not in data or data["gender"].strip() == "":
        return jsonify({
            "status": "error",
            "message": "Gender is mandatory"
        }), 400

    # Validate contact number
    if "contact" not in data:
        return jsonify({
            "status": "error",
            "message": "Contact number is mandatory"
        }), 400

    contact = str(data["contact"])
    if not contact.isdigit() or len(contact) != 10:
        return jsonify({
            "status": "error",
            "message": "Contact number must be exactly 10 digits"
        }), 400

    # Create patient record
    patient = {
        "id": patient_id,
        "name": data["name"],
        "age": age,
        "gender": data["gender"],
        "contact": contact,
        "disease": data.get("disease", "Not specified"),
        "doctor": data.get("doctor", "Not assigned")
    }

    patients.append(patient)
    patient_id += 1

    return jsonify({
        "status": "success",
        "message": "Patient registered successfully",
        "data": patient
    }), 201


# Get patient details by ID
@app.route("/api/patients/<int:id>", methods=["GET"])
def get_patient_by_id(id):
    if id <= 0:
        return jsonify({
            "status": "error",
            "message": "Invalid patient ID"
        }), 400

    for patient in patients:
        if patient["id"] == id:
            return jsonify({
                "status": "success",
                "data": patient
            }), 200

    return jsonify({
        "status": "error",
        "message": f"Patient with ID {id} not found"
    }), 404


# Update patient details
@app.route("/api/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    data = request.json

    if id <= 0:
        return jsonify({
            "status": "error",
            "message": "Invalid patient ID"
        }), 400

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body is missing"
        }), 400

    for patient in patients:
        if patient["id"] == id:

            if "age" in data:
                try:
                    age = int(data["age"])
                    if age <= 0:
                        raise ValueError
                    patient["age"] = age
                except:
                    return jsonify({
                        "status": "error",
                        "message": "Age must be a valid positive number"
                    }), 400

            if "contact" in data:
                contact = str(data["contact"])
                if not contact.isdigit() or len(contact) != 10:
                    return jsonify({
                        "status": "error",
                        "message": "Contact number must be exactly 10 digits"
                    }), 400
                patient["contact"] = contact

            if "name" in data:
                patient["name"] = data["name"]

            if "gender" in data:
                patient["gender"] = data["gender"]

            if "disease" in data:
                patient["disease"] = data["disease"]

            if "doctor" in data:
                patient["doctor"] = data["doctor"]

            return jsonify({
                "status": "success",
                "message": "Patient details updated successfully",
                "data": patient
            }), 200

    return jsonify({
        "status": "error",
        "message": f"Patient with ID {id} not found"
    }), 404


# Handle invalid HTTP methods
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "status": "error",
        "message": "HTTP method not allowed for this endpoint"
    }), 405


# Handle server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(debug=True)
