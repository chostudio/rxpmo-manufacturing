import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
  host="your_host",
  database="your_database",
  user="your_user",
  password="your_password"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute a query to create a table
cur.execute("""

CREATE TABLE Manufacturer (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    naics_code VARCHAR(10),
    product_category VARCHAR(255)

    -- Capabilities fields
    capability_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES ManufacturerProfile(manufacturer_id),
    machine_make_model VARCHAR(255) NOT NULL,
    raw_material_used VARCHAR(255) NOT NULL,
    available_tooling VARCHAR(255) NOT NULL,

 -- Capacities fields
    capacity_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES ManufacturerProfile(manufacturer_id),
    number_of_machines INT NOT NULL,
    utilization_rate NUMERIC(5, 2) NOT NULL,
);

CREATE TABLE Machine (
    machine_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id),
    type VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    make VARCHAR(255) NOT NULL
);

CREATE TABLE RawMaterial (
    material_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id),
    name VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    density NUMERIC(10, 2) NOT NULL
);

""")

cur.execute("CREATE TABLE your_table (id SERIAL PRIMARY KEY, name VARCHAR(255))")

# Commit the changes to the database
conn.commit()

# Close the cursor and connectionn
cur.close()
conn.close()