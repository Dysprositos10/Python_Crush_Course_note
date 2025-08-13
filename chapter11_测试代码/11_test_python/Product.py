class Product:
    def __init__(self,name,ID,current_stock=0):
        """初始化描述产品的属性"""
        self.name = name
        self.ID = ID
        self.current_stock = current_stock
    def adjust_stock(self):
        if self.current_stock < 50:
            adjust_stock = self.current_stock + 100
            return adjust_stock
        else:
            adjust_stock = self.current_stock
            return adjust_stock
stock = Product('Laptop','P-001',20)
print(stock.adjust_stock())#直接输出返回值