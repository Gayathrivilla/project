class CarShowroom:
    def __init__(self, cgst, sgst, insurance):
        self.cgst = cgst
        self.sgst = sgst
        self.insurance = insurance
        self.carcompany = None
        self.carmodel = None

    def company(self):
        while True:
            print("Toyota")
            print("Mahindra")
            print("Mercedes")
            self.carcompany = input("Enter a car company: ").strip().lower()
            if self.carcompany == "toyota":
                print("Welcome to Toyota")
                print("Innova")
                print("Fortuner")
                break
            elif self.carcompany == "mahindra":
                print("Welcome to Mahindra")
                print("Scorpio")
                print("Thar")
                break
            elif self.carcompany == "mercedes":
                print("Welcome to Mercedes")
                print("Gwagen")
                print("AMG")
                break
            else:
                print("Enter a valid company")

    def model(self):
        valid_models = {
            "toyota": ["innova", "fortuner"],
            "mahindra": ["scorpio", "thar"],
            "mercedes": ["gwagen", "amg"]
        }
        while True:
            self.carmodel = input("Enter a car model: ").strip().lower()
            if self.carcompany in valid_models and self.carmodel in valid_models[self.carcompany]:
                break
            else:
                print("Enter a valid car model")

    def price(self):
        model_prices = {
            "innova": 3000000,
            "fortuner": 3300000,
            "scorpio": 2450000,
            "thar": 1120000,
            "gwagen": 30000000,
            "amg": 7100000
        }
        
        srp = model_prices.get(self.carmodel)
        if srp is not None:
            onroadprice = (srp) + (srp * (self.cgst / 100)) + (srp * (self.sgst / 100)) + self.insurance
            print(f"On-road price: {onroadprice}")
        else:
            print("Invalid car model")

# Example usage
obj1 = CarShowroom(18, 18, 100000)
obj1.company()
obj1.model()
obj1.price()
