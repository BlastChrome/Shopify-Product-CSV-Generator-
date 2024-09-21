import csv 
import re #regular expression



# the # of varients are the number of rows per product
# currently the only varient values are gender/shoe size & weight(g)
VARIENTS = [
    # size, gender, weight(g)
    ['4','Men','800'],
    ['4','Women','800'],
    ['5','Men','820'],
    ['5','Women','820'],
    ['6','Men', '840'],
    ['6','Women', '840'],
    ['7','Men', '860'],
    ['7','Women', '860'],
    ['8','Men','880'],
    ['8','Women','880'],
    ['9','Men','900'],
    ['9','Women','900'],
    ['10','Men','920'],
    ['10','Women','920'],
    ['11','Men','940'],
    ['11','Women','940'],
    ['12','Men','960'],
    ['12','Women','960']
]

# List of common sneaker vendors
VENDORS = [
    'Jordan', 
    'Nike', 
    'New Balance', 
    'Adidas'
]


def addToCSV(product):
    # open the csv file in 'append' mode
    with open('products.csv', mode="a", newline='') as csvfile: 

        # get the fieldnames: the first row of the dictionary
        fieldnames = product[0].keys() 

        # initialize a 'csv writer object'
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # only write the header if the file is empty
        csvfile.seek(0, 2)  # move to the end of the file
        if csvfile.tell() == 0:  # if the file is empty
            writer.writeheader()

        # write the product rows
        for product_row in product: 
            writer.writerow(product_row)


def generateProductInfoBoilerplate():
    # get the product title from the user
    title = input('Please input the product title: ')

    # Convert to lowercase, replace spaces with dashes, and remove non-alphanumeric characters except for dashes - to get the handle
    handle = re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))

    # call the tag helper function
    tags = generateTags(title)

    # look up the vendor based on the title 
    vendor = getVendor(title)

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

    multipled_rows = generateMultipleDictRows(handle,title,tags,vendor,base_price,comp_price,sku)
    return multipled_rows
    
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

def generateTags(title):
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
        
def generateMultipleDictRows(handle,title,tags,vendor,base_price,comp_price,sku): 

    multi_rows = []


    for idx, var in enumerate(VARIENTS): 

        # get varient size
        prod_option_1_value = var[0]

        # get varient gender
        prod_option_2_value = var[1]

        # get varient weight(g)
        prod_varient_grams = var[2]

        # generate the varient sku from  the varients
        prod_varient_sku = (sku + '-' + var[0] + var[1][0])


        # generate a row for each varient
        if not idx == 0:
            # Dynamic Values, these will update based on the product
            prod_title = '' 
            prod_tags = '' 
            prod_vendor = ''

            # Default Values 
            prod_category = ''
            prod_type = ''
            prod_published = ''
            prod_option_1_name = ''
            prod_option_2_name = ''
            prod_gift_card = ''
            prod_seo_title = ''
            prod_seo_description = ''
            prod_include_us = ''
            prod_include_mx = ''
            prod_include_int = ''
            prod_status = ''

        else: 
            prod_title = title 
            prod_handle = handle 
            prod_tags = tags 
            prod_vendor = vendor 
            prod_base_price = base_price 
            prod_comp_price = comp_price 
            prod_seo_title = 'Best ' + title + ' Kicks4ThaLow | Long Beach, CA'
            prod_seo_description = 'Your one stop shop for all your Sneaker Needs, in Long Beach CA specializing in ' + prod_seo_title + ' | Kicks4ThaLow'
            prod_include_us = 'TRUE'
            prod_include_mx = 'TRUE'
            prod_include_int = 'TRUE'
            prod_status = 'active'

            prod_category = 'Shoes'  
            prod_type = 'Sneaker'
            prod_published = 'TRUE'
            prod_option_1_name = 'Size'
            prod_option_2_name = 'Gender'
            prod_gift_card = 'FALSE'

        product_row_template =   {
            'Handle': prod_handle, 
            'Title': prod_title,
            'Body (HTML)': '',
            'Vendor': prod_vendor, 
            'Product Category': prod_category, 
            'Type': prod_type, 
            'Tags': prod_tags, 
            'Published': prod_published, 
            'Option1 Name': prod_option_1_name, 
            'Option1 Value': prod_option_1_value, 
            'Option1 Linked To': '', 
            'Option2 Name': prod_option_2_name, 
            'Option2 Value': prod_option_2_value, 
            'Option2 Linked To': '',
            'Option3 Name': '', 
            'Option3 Value': '', 
            'Option3 Linked To': '',
            'Variant SKU': prod_varient_sku,
            'Variant Grams': prod_varient_grams, 
            'Variant Inventory Tracker': '', 
            'Variant Inventory Policy': 'deny', 
            'Variant Fulfillment Service': 'manual', 
            'Variant Price': prod_base_price, 
            'Variant Compare At Price': prod_comp_price, 
            'Variant Requires Shipping': 'TRUE', 
            'Variant Taxable': 'TRUE', 
            'Variant Barcode': '', 
            'Image Src': '', 
            'Image Position': idx + 1, 
            'Image Alt Text': prod_title, 
            'Gift Card': prod_gift_card, 
            'SEO Title': prod_seo_title,
            'SEO Description': prod_seo_description,
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
            'Variant Weight Unit': 'g',
            'Variant Tax Code': '',
            'Cost per item': '',
            'Included / United States': prod_include_us,
            'Price / United States': '',
            'Compare At Price / United States': '',
            'Included / International': prod_include_int,
            'Price / International': '',
            'Compare At Price / International': '',
            'Included / Mexico': prod_include_mx,
            'Price / Mexico': '',
            'Compare At Price / Mexico': '',
            'Status': prod_status,
        }
        multi_rows.append(product_row_template)

    # return the rows
    return multi_rows

def getVendor(title): 

    # check for the vendor in the title
    for vendor in VENDORS: 
        vendor_match = vendor.lower() in title.lower()
        if vendor_match: 
            return vendor
    return 'No Vendor Found'

def main():
    product = generateProductInfoBoilerplate()
    addToCSV(product)


main()








