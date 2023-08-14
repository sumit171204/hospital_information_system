class Hospital:
    """
    A class to represent a hospital.
    Attributes:
      name: The name of the hospital.
      city: The city where the hospital is located.
      symptoms: A list of symptoms that the hospital treats.
    """
    def __init__(self, name, city, symptoms):
        self.name = name
        self.city = city
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

def main():
    hospitals = [
        Hospital("Hospital A", "City X", ["headache", "fever", "cough"]),
        Hospital("Hospital B", "City Y", ["broken arm", "broken leg", "broken ankle"]),
        Hospital("Hospital C", "City X", ["stomachache", "constipation", "diarrhea"])
    ]

    while True:
        # Get the user input for symptom and city.
        symptom = input("What is your symptom? (Type 'exit' to quit): ")

        if symptom.lower() == "exit":
            # Exit the loop if the user inputs 'exit'.
            break

        city = input("In which city are you located? ")

        # Find the hospitals in the city that treat the symptom.
        hospitals_in_city = sequential_search(hospitals, symptom, city)

        if hospitals_in_city:
            # Hospitals found, print their names.
            print(f"The hospitals in {city} that treat your symptom are:")
            for hospital in hospitals_in_city:
                print(hospital.name)
        else:
            # No hospital found, inform the user.
            print(f"No hospital found in {city} that treats your symptom.")

# Call the main function to run the code.
if __name__ == "__main__":
    main()