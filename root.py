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

CREATE TABLE ManufacturerProfile (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    naics_code VARCHAR(10),
    product_category VARCHAR(255)
);
 
CREATE TABLE Capabilities (
    capability_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES ManufacturerProfile(manufacturer_id),
    machine_make_model VARCHAR(255) NOT NULL,
    raw_material_used VARCHAR(255) NOT NULL,
    available_tooling VARCHAR(255) NOT NULL,
);
 
CREATE TABLE Capacities (
    capacity_id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES ManufacturerProfile(manufacturer_id),
    number_of_machines INT NOT NULL,
    utilization_rate NUMERIC(5, 2) NOT NULL,
);

""")

cur.execute("CREATE TABLE your_table (id SERIAL PRIMARY KEY, name VARCHAR(255))")

# Commit the changes to the database
conn.commit()

# Close the cursor and connectionn
cur.close()
conn.close()