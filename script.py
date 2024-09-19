import csv 
import re #regular expression


names = [
    {"Handle": "jordan-1-retro-low-og-sp-travis-scott-canary-blu", "Title": "Jordan 1 Retro Low OG SP Travis Scott Canary (BLU)"}
]


def writeToCSV():
    with open('products.csv', mode="w") as csvfile: 
        fieldnames = names[0].keys() 
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for row in names: 
            writer.writerow(row)

def generateProductInfoBoilerplate():
    # get the product title from the user
    title = input('Please input the product title: ')

    # Convert to lowercase, replace spaces with dashes, and remove non-alphanumeric characters except for dashes - to get the handle
    handle = re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))

    # split the title to get a list of tags 
    tags = title.split(' ')

    # get the first letter of every word, to create the SKU
    sku = generateSku(handle)

    comp_price_float = 0.0
    base_price_float = 0.0

    # get the base price 
    base_price =  input('Please input the base price, ex 200.00: ')
    base_price_float = float(base_price)

    # get the comparison price, should be greater than the base price
    while comp_price_float <= base_price_float:
        comp_price = input('Please input comparison price - should be greater than ' + base_price  + ': ')
        comp_price_float = float(comp_price)
    


    print('\n================================')
    print('Title: ', title)
    print('Handle: ', handle)
    print('Tags: ', tags)
    print('Sku: ', sku)
    print('Base price $', base_price)
    print('Compare at price: $', comp_price)
    print('================================\n')
    



def main():
    generateProductInfoBoilerplate()


def generateSku(handle):
    # set the sku base to an empty string
    sku = ''
    # split each word into an array
    split_text = handle.split('-')
    for first_word in split_text: 
        # get the first letter from each word
        first_letter = first_word[0]
        # clean the text(uppercase)
        sku = (sku + first_letter).upper()
    return sku


main()

# generateSkuBase()