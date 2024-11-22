class Rate:

    def __init__(self,
                 rate_name: str,
                 rate_price: float,
                 domain_name: str,
                 dedicated_ram: int,
                 sub_domain: int,
                 addon_domain: int,
                 support: '24/7'
                 ):
        self.rate_name = rate_name
        self.rate_price = rate_price
        self.domain_name = domain_name
        self.dedicated_ram = dedicated_ram
        self.sub_domain = sub_domain
        self.addon_domain = addon_domain
        self.support = support

