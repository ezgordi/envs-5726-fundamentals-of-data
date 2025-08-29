class Company:
    def __init__(self,name,market_cap):
        self.name = name
        self.market_cap = market_cap

american_water_company = Company(name='American Water', market_cap=28940000000)

#print(american_water_company.name)
#print(american_water_company.market_cap)


def get_number_of_shares(market_cap, share_value):
    return market_cap/share_value

my_shares = get_number_of_shares(market_cap=100,share_value=2)
#print(my_shares)


class Company:
    def __init__(self,name,market_cap,share_value):
        self.name = name
        self.market_cap = market_cap
        self.share_value = share_value

    def get_number_of_shares(self):
        return self.market_cap/self.share_value

american_water_company = Company(name='American Water', market_cap=28940000000, share_value=148.4)

american_water_shares = american_water_company.get_number_of_shares()
print(american_water_shares)