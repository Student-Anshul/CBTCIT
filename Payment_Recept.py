print("==== XYZ shop ====")

while(True):
    Product = []
    Value = []
    product = input("Enter the item or enter q for quite: ")
    value = input("Enter the price: ")
    
    Product.append(product)
    Value.append(value)

    if(product == 'q'):
        print(dict(zip(Product,Value)))
        print("----: Thank you for your support (:. :----")
        break