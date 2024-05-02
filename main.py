import tkinter as tk
from tkinter import filedialog, Text
import xml.etree.ElementTree as ET
import json


def load_file(file_type):
    file_path = filedialog.askopenfilename(
        filetypes=[(file_type.upper(), f"*.{file_type}")])
    if file_path:
        global content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Clear the text area before displaying new content
        # text_area.delete('1.0', tk.END)
        # text_area.insert(tk.END, content)
        # return content
        if (file_type == 'xml'):
            parse_xml(content)
        else:
            parse_json(content)

# Parsing the XML content


def parse_xml(content):
    root = ET.fromstring(content)

    for current_order in root.findall('order'):
        order_id = current_order.get('id')
        order_day = current_order.find('date').find('day').text
        order_month = current_order.find('date').find('month').text
        order_year = current_order.find('date').find('year').text
        supplier_name = current_order.find('supplier_name').text
        order_price = current_order.find('order_price').text
        currency = current_order.find('order_price').get('currency')

        print(f"Order ID: {order_id}")
        print(f"Supplier Name: {supplier_name}")
        print(f"Order Price: {order_price} {currency}")
        print(f"Order Date: {order_day}/{order_month}/{order_year}")

    # Accessing nested elements like products
        print("Products:")
        for product in current_order.find('products'):
            product_id = product.get('id')
            product_category = product.find('category').text
            product_name = product.find('product_name').text
            quantity = product.find('quantity').text
            unit_price = product.find('unit_price').text
            product_lot_number = product.find(
                "additional_details").find('lot_number').text
            product_expiry_day = product.find(
                "additional_details").find('expiry_date').find('day').text
            product_expiry_month = product.find(
                "additional_details").find('expiry_date').find('month').text
            product_expiry_year = product.find(
                "additional_details").find('expiry_date').find('year').text
            product_is_fragile = product.find(
                "additional_details").find('is_fragile').text
            product_requires_refrigeration = product.find(
                "additional_details").find('requires_refrigeration').text

            print(
                f"  -> [{product_category}] {product_name}[id={product_id}]( {quantity} units at {unit_price} each)")
            print(f"     - Lot Number: {product_lot_number}")
            print(
                f"     - Expiry Date: {product_expiry_day}/{product_expiry_month}/{product_expiry_year}")
            print(f"     - Is Fragile: {product_is_fragile}")
            print(
                f"     - Requires Refrigeration: {product_requires_refrigeration}")
        print("------------------------------------------------------")


# Parsing the JSON content
def parse_json(content):
    data = json.loads(content)
    orders = data['supply_stream']['order']

    for order in orders:
        print("Order ID:", order['id'])
        print("Supplier Name:", order['supplier_name'])
        print("Order Date:",
              f"{order['date']['day']}-{order['date']['month']}-{order['date']['year']}")
        print("Total Order Price:", order['order_price']
              ['amount'], order['order_price']['currency'])
        print("Products:")
        for product in order['products']['product']:
            print(
                f"  - {product['product_name']} ({product['quantity']} units at {product['unit_price']} each)")
        print()


root = tk.Tk()
root.title("Supply stream")

# Frame for buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

# Button to load XML file
button_xml = tk.Button(frame_buttons, text="Load XML",
                       command=lambda: load_file('xml'))
button_xml.pack(side=tk.LEFT, padx=10)

# Button to load JSON file
button_json = tk.Button(frame_buttons, text="Load JSON",
                        command=lambda: load_file('json'))
button_json.pack(side=tk.LEFT, padx=10)


# Text area to display file contents
text_area = Text(root, wrap=tk.WORD, width=60, height=20)
text_area.pack(padx=20, pady=20)

root.mainloop()
