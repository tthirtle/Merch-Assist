# OOP classes
class item:
    def __init__(self,upc="",sku="",brand="",desc="",status="",pack_size="",unit_size="",img="") -> None:
        self.upc = upc
        self.sku = sku
        self.brand = brand
        self.desc = desc
        self.status = status
        self.pack_size = pack_size
        self.unit_size = unit_size
        self.img = img