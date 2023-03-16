class Flight:
    """A class that represents Flight.
    
    Attributes:
        number (int): Flight number.
        origin (str): Departure destination.
        destination (str): Final destination.
        num_passengers (int): Number of passengers.
        total_weight (float): Total weight of flight.
        pilot (str): Pilot name.
        crew (dict): Flight crew members.
    
    Methods:
        display_flight_data(self):
            Print flight number, number of passengers, flight weight, pilot 
            name and crew members.
    """
       
    def __init__(self, number, origin, destination, num_passengers, 
                 total_weight, pilot, crew):
        """Initialize an instance of Flight.

        Arguments:
            number (int): Flight number.
            origin (str): Departure destination.
            destination (str): Final destination.
            num_passengers (int): Number of passengers.
            total_weight (float): Total weight of flight.
            pilot (str): Pilot name.
            crew (dict): Flight crew members.
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot 
        self._crew = crew
 
    @property
    def total_weight(self):
        """Return the total weight of the flight.

        This is a float that represents the total weight of flight.
        """
        return self._total_weight
 
    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight	
 
    @property
    def pilot(self):
        """Return pilot name.

        This is a string that represents the pilot name.
        """
        return self._pilot
 
    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot
 
    @property
    def crew(self):
        """Return the crew members.

        This is a dictionary that contains crew positions as keys and crew 
        member names as values.
        """
        return self._crew
	
    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew
 
    def display_flight_data(self):
        """Print flight number, number of passengers, flight weight, pilot name
            and crew members.
        """
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self._total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)
