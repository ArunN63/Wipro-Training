class College:
    def __init__(self, ccode,cname, ccity):
        self.collcode = ccode
        self.collname = cname
        self.collcity = ccity
    def welcome_message(self):
        print('Hello There !!!')

    def display_college_details(self):
        print(f'College Code: {self.collcode} \n College Name : {self.collname} \n City : {self.collcity}'")