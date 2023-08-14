from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

class Hospital:
    """
    A class to represent a hospital.
    Attributes:
      name: The name of the hospital.
      city: The city where the hospital is located.
      symptoms: A list of symptoms that the hospital treats.
    """
    def __init__(self, name, city, address, symptoms):
        self.name = name
        self.city = city
        self.address = address  # Add address attribute
        self.symptoms = symptoms

    def treats(self, symptom):
        """
        Checks if the hospital treats the given symptom.
        Args:
          symptom: The symptom to check.
        Returns:
          True if the hospital treats the symptom, False otherwise.
        """
        return symptom in self.symptoms
    
def sequential_search(hospitals, symptom, city):
    """
    This function implements a sequential search algorithm for finding a hospital that treats a given symptom in the specified city.
    Args:
      hospitals: A list of hospitals.
      symptom: A symptom.
      city: The city where the user is located.
    Returns:
      The list of hospitals in the city that treat the symptom, or an empty list if no hospital in the city treats the symptom.
    """
    hospitals_in_city = []
    # Iterate over the list of hospitals, one by one.
    for hospital in hospitals:
        if hospital.city.lower() == city.lower() and hospital.treats(symptom):
            # The hospital is in the specified city and treats the symptom, add it to the list.
            hospitals_in_city.append(hospital)

    return hospitals_in_city
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    hospitals = [
        Hospital("Santram Hospital", "Nadiad", "Santram road, Nadiad.", ["headache", "fever", "cough","stomachache", "constipation", "diarrhea"]),
        Hospital("Navjyot Hospital", "Nadiad", "Paras road, Nadiad.", ["fever","facture","broken arm", "broken leg", "broken ankle"]),

        # Add more hospitals with addresses
    ]

    symptom = request.form.get("symptom")
    city = request.form.get("city")

    hospitals_in_city = sequential_search(hospitals, symptom, city)

    if hospitals_in_city:
        result = []
        for hospital in hospitals_in_city:
            result.append({
                "name": hospital.name,
                "city": hospital.city,
                "address": hospital.address,
                "symptoms": hospital.symptoms
            })
        return jsonify(result)
    else:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)