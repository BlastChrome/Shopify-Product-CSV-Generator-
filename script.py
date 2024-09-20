import csv 
import re #regular expression




def writeToCSV(info):
    # create csv file object, in 'write' mode
    with open('products.csv', mode="w") as csvfile: 

        # get the fieldnames: the first row of the dictionary
        fieldnames = info[0].keys() 

        # initialize a 'csv writer object'
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

        writer.writeheader()
        for row in info: 
            writer.writerow(row)

def generateProductInfoBoilerplate():
    # get the product title from the user
    title = input('Please input the product title: ')

    # Convert to lowercase, replace spaces with dashes, and remove non-alphanumeric characters except for dashes - to get the handle
    handle = re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))

    # call the tag helper function
    tags = generateTags(title)

    # get the first letter of every word, to create the SKU - helper function
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


    boilerplate_values = [{
        'Handle': handle, 
        'Title': title, 
        'Body (HTML)': '',
        'Vendor': 'Jordan', 
        'Product Category': 'Shoes', 
        'Type': 'Sneaker', 
        'Tags': tags, 
        'Published': 'TRUE', 
        'Option1 Name': 'Size', 
        'Option1 Value': '4', 
        'Option1 Linked To': '', 
        'Option2 Name': 'Gender', 
        'Option2 Value': 'Men', 
        'Option2 Linked To': '',
        'Option3 Name': '', 
        'Option3 Value': '', 
        'Option3 Linked To': '',
        'Variant SKU': (sku + '-' + '4M'),
        'Variant Grams': '800.00', 
        'Variant Inventory Tracker': '', 
        'Variant Inventory Policy': 'deny', 
        'Variant Fulfillment Service': 'manual', 
        'Variant Price': base_price, 
        'Variant Compare At Price': comp_price, 
        'Variant Requires Shipping': 'TRUE', 
        'Variant Taxable': 'TRUE', 
        'Variant Barcode': '', 
        'Image Src': '', 
        'Image Position': '1', 
        'Image Alt Text': title, 
        'Gift Card': 'FALSE', 
        'SEO Title': ('Best ' + title + ' Kicks4ThaLow | Long Beach, CA'), 
        'SEO Description': ('Your one stop shop for all your Sneaker Needs, in Long Beach CA specializing in ' + title + ' | Kicks4ThaLow'), 
        'Google Shopping / Google Product Category': '',
        'Google Shopping / Gender': '',
        'Google Shopping / Age Group': '',
        'Google Shopping / MPN': '',
        'Google Shopping / Condition': '',
        'Google Shopping / Custom Product': '',
        'Google Shopping / Custom Label 0': '',
        'Google Shopping / Custom Label 1': '',
        'Google Shopping / Custom Label 2': '',
        'Google Shopping / Custom Label 3': '',
        'Google Shopping / Custom Label 4': '',
        'Snowboard binding mount (product.metafields.test_data.binding_mount)': '',
        'Snowboard length (product.metafields.test_data.snowboard_length)': '',
        'Variant Image': '',
        'Variant Weight Unit': 'lb',
        'Variant Tax Code': '',
        'Cost per item': '',
        'Included / United States': 'TRUE',
        'Price / United States': base_price,
        'Compare At Price / United States': comp_price,
        'Included / International': 'TRUE',
        'Price / International': base_price,
        'Compare At Price / International': comp_price,
        'Included / Mexico': 'TRUE',
        'Price / Mexico': base_price,
        'Compare At Price / Mexico': comp_price,
        'Status': 'active',
    }]
    return boilerplate_values
    

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



def generateTags(title='Jordan 4 Retro Bred Reimagined'):
    # split the tags by space
    tags_arr = title.split(' ')

    # get the size of the tags array 
    size = len(tags_arr) - 1

    # set the tag string to an empty string 
    tag_str = ''

    # concatenate each 'tag' with a ',' as the delimeter
    for idx,tag in enumerate(tags_arr):

        # if at the end of the array only add the 'tag'
        if(idx == size):
            tag_str = (tag_str + ' ' + tag) 
        
        # if at the beggining, add the 'tag' + ','
        elif(idx == 0):
            tag_str = (tag + ',' + tag_str)

        # otherwise, add a space, the 'tag' and a ','
        else:
            tag_str = (tag_str + ' ' + tag + ',')


    return tag_str
        

def main():
    info = generateProductInfoBoilerplate()
    writeToCSV(info)


main()


