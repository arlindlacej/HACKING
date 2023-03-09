def main():
    PRODUCTS_FILE = "products.txt"
    PURCHASES_FILE = "purchases.txt"
    productID_resellerID = dict()

    with open(PRODUCTS_FILE) as products_file:
        for line in products_file.readlines():
            fields =  line.split()
            productID_resellerID[fields[0]] = fields[1]

    productID_sellerIDs = dict()
    with open(PURCHASES_FILE) as purchase_file:
        for line in purchase_file.readlines():
            fields =  line.split()
            if fields[0] not in productID_sellerIDs.keys():
                    productID_sellerIDs[fields[0]] = set()
                    productID_sellerIDs[fields[0]].add(fields[1])
            else:
                    productID_sellerIDs[fields[0]].add(fields[1])
    for key,value in productID_sellerIDs.items():
        if len(value) > 1 or productID_resellerID[key] not in value:
            print("Suspicious transactions list:")
            print()
            print(f' product code : {key}')
            print(f' official dealer : {productID_resellerID[key]}')
            print(f' dealer list : {value}')



if __name__ == "__main__":
     main()
