import requests, time, random, threading
from faker import  Faker







class adidas():
    def __init__(self):
        self.faker = Faker()
        self.catchall = True
        self.randompass = True
        self.domain = "sneakersource.me"
        self.dob = str(random.randint(1970, 1996)) + "-" + str(random.randint(10, 12)) + "-" + str(random.randint(10, 30))
        self.s = requests.session()
        self.s.proxies.update({'http': 'http://blue:abc123@us.netnut.io:33128', 'https': 'https://blue:abc123@uk-S1.netnut.io:33128'})


    def create(self):
        fname = self.faker.first_name()
        lname = self.faker.last_name()
        if self.randompass is True:
            password = fname + lname + str(random.randint(10000, 99999))
        else:
            password = "Rahat123"
        if self.catchall is True:
            email = fname + lname + str(random.randint(10000, 99999)) + "@" + self.domain
            
        data = {
            "clientId": "1ffec5bb4e72a74b23844f7a9cd52b3d",
            "actionType": "REGISTRATION",
            "email":  email,
            "password":  password,
            "countryOfSite": "GB",
            "dateOfBirth":  self.dob,
            "minAgeConfirmation": "Y",
            "firstName": fname,
            "lastName": lname
        }

        a = self.s.post("https://apim.scv.3stripes.net/scvRESTServices/account/createAccount", json=data)
        if "iCCD_CRT_ACCT_0001" in a.text:
            print("Account created with: " + email)
            with open("gen.txt", "a") as f:
                f.write(email + ":" + password + "\n")
                f.close()
        elif "Denied" in a.text:
            print("banned")
            pass
        elif "Already_Email_Exists" in a.text:
            print("Account already created with: " + email)
            pass

    def run(self):
        self.create()



