import sqlite3
import json
from models import Employee, Location

def get_all_employees():
    
    with sqlite3.connect("./kennel.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
     
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee a
        JOIN Location l
            ON l.id = a.location_id
        """)
       
        employees = []
       
        dataset = db_cursor.fetchall()
        
        for row in dataset:
           
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            
            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees
# Function with a single parameter
def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
       
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee a
        JOIN Location l
            ON l.id = a.location_id
         WHERE a.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
            
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])
            
        location = Location(data['location_id'], data['location_name'], data['location_address'])
            
        employee.location = location.__dict__
        

        return employee.__dict__
  
def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))
  
  
  
def update_employee(id, new_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break


# TODO: you will get an error about the address on customer. Look through the customer model and requests to see if you can solve the issue.
        
def get_employees_by_location(location):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.address,
            a.location_id
            
        from Employee a
        WHERE a.location_id = ?
        """, ( location, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees
