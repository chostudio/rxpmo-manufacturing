import psycopg2
# may later need the available_tooling VARCHAR(255), labor_certs VARCHAR(255)[]-- (Optional) List of products we know the manufacturer can make

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
  host="localhost",
  database="chrisho",
  user="postgres",
  password="postgres"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute a query to create a table
cur.execute("""

CREATE TABLE Manufacturer (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    naics_code VARCHAR(10), -- optional, manufacturer's specialization
    product_category VARCHAR(255), -- optional
    -- can refer to machine make model in here
    -- and can reference processes query to give all raw material, prosses info, machines, etc.
    -- for this manufac just group machine to count it
);
    -- manufacturer will link to these
CREATE TABLE Process (
    process_id SERIAL PRIMARY KEY,
    process_name VARCHAR(255),
    -- for each manufacturer multiple process ID. one or multiple. for each process have one or more machine associated with it. coudl have multiple machine of same model or different model for same process
    -- foreign key refernce the manufacturer table
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id),
   
    -- raw_material_used VARCHAR(255) NOT NULL, -- just use the raw material table, based on the manufac. not process
      
);

CREATE TABLE Machine (
    machine_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id),
    process VARCHAR(255), -- foreign key reference ot the process id in the process table

    make_and_model VARCHAR(255) NOT NULL, -- already in capability table
    max_length INT,  -- millimeters
    max_width INT,
    max_height INT,

    utilization_rate NUMERIC(5, 2) NOT NULL, -- Utilization Rate for Each Machine %
    operating_cost_per_hour INT NOT NULL,
    days_operational INT NOT NULL,
    shifts_per_day INT NOT NULL,
    hours_per_shift INT NOT NULL,
    hours_available_per_week INT -- Overall Utilization this Week

    manufacturer_id INT FOREIGN KEY REFERENCES Manufacturer(manufacturer_id)
);

-- track it back to process and manufacturer
CREATE TABLE RawMaterial (
    material_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id),
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    density NUMERIC(10, 2) NOT NULL
);

""")

# these insert values don't work yet due to update
# Insert values into the Manufacturer table
cur.execute("""
INSERT INTO Manufacturer (name, address, naics_code, product_category, machine_make_model, raw_material_used, available_tooling, labor_certs, number_of_machines, utilization_rate, operating_cost_per_hour, days_operational, shifts_per_day, hours_per_shift, hours_available_per_week)
VALUES ('Manufacturer 1', '204 Rogers Hall, Oregon State University, Corvallis, OR 97331, USA', '339', 'Reusable Medical Supplies', 'sPro 60 SLS Printers', 'DuraForm TPU Elastomer', 'NULL', NULL, 2, 50, 25, 5, 2, 6, NULL);

-- hours per shift is 8 hours for 1st shift - 4 hours for 2nd shift. so i averaged them and put 6?



""")

# Insert values into the Machine table
cur.execute("""
INSERT INTO Machine (manufacturer_id, process, make_and_model, max_length, max_width, max_height)
VALUES (1, 'Process 1', 'Machine 1', 100, 50, 30);

""")

# Insert values into the RawMaterial table
cur.execute("""
INSERT INTO RawMaterial (manufacturer_id, name, price, density)
VALUES (1, 'Material 1', 10.0, 1.2);

""")



# Commit the changes to the database
conn.commit()

# Close the cursor and connectionn
cur.close()
conn.close()