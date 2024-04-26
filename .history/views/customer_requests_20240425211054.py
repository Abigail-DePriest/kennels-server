import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]


def get_all_customers():
    
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM customer a
        """)

        
        customers = []

        
        dataset = db_cursor.fetchall()

        
        for row in dataset:

            customer = Customer(row['id'], row['name'])

            customers.append(customer.__dict__) 

    return customers


def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        
        data = db_cursor.fetchone()
       
        customer = Customer(data['id'], data['name'])

        return customer.__dict__
  
def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
  
def update_customer(id, new_customer):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            CUSTOMERS[index] = new_customer
            break
