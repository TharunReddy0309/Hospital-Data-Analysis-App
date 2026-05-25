import psycopg2
from datetime import datetime

def postgre_connect():
    return psycopg2.connect(
        host='db.kstpdhgyspswyhexkmqf.supabase.co',
        port=5432,
        database='postgres',
        user='postgres',
        password='*****'#keep your own password
    )

def create_table():
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            name VARCHAR(255) ,
            age INTEGER,
            illness VARCHAR(255),
            bill REAL,
            date VARCHAR(255),
            status VARCHAR(255),
            height INTEGER,
            weight INTEGER,
            unique(name,age,illness)
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

# ✅ Insert one patient record
def enter_data(name, age, illness, bill, status, height, weight):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = postgre_connect()
    cur = conn.cursor()
    try:
        cur.execute('''
            INSERT INTO patients (name, age, illness, bill, date, status, height, weight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (name, age, illness, bill, date, status, height, weight))
        conn.commit()
        print(f"✅ Record added: {name}")
    except Exception as e:
        if 'duplicate key value' in str(e).lower():
            print("⚠️ Duplicate entry! Patient already exists.")
        else:
            print(f"❌ Error inserting data: {e}")
    finally:
        cur.close()
        conn.close()

# ✅ Fetch all patient records
def show_all():
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# ✅ Update status or bill
def update_data(name, age, illness, new_value):
    conn = postgre_connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM patients WHERE name=%s AND age=%s AND illness=%s", (name, age, illness))
        if not cur.fetchone():
            print("❌ No matching record found.")
            return

        if isinstance(new_value, str):
            cur.execute("UPDATE patients SET status=%s WHERE name=%s AND age=%s AND illness=%s",
                        (new_value, name, age, illness))
        elif isinstance(new_value, (int, float)):
            cur.execute("UPDATE patients SET bill=%s WHERE name=%s AND age=%s AND illness=%s",
                        (new_value, name, age, illness))
        else:
            print("⚠️ Unsupported value type.")
            return

        conn.commit()
        print("✅ Record updated successfully.")
    except Exception as e:
        print(f"❌ Error updating record: {e}")
    finally:
        cur.close()
        conn.close()

# ✅ Delete a record
def delete_data(name, age, illness):
    conn = postgre_connect()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM patients WHERE name=%s AND age=%s AND illness=%s", (name, age, illness))
        conn.commit()
        print("✅ Record deleted successfully.")
    except Exception as e:
        print(f"❌ Error deleting record: {e}")
    finally:
        cur.close()
        conn.close()

# ✅ Setup and sample insert
if __name__ == '__main__':
    # ⚠️ Drop existing table
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS patients")
    conn.commit()
    cur.close()
    conn.close()
    print("🗑️ Old patients table dropped.")

    # ✅ Recreate table
    create_table()
    print("📋 New patients table created.")

    # ✅ Sample data
    enter_data("Alice Johnson", 30, "Fever", 1500.0, "admitted", 160, 60)
    enter_data("Bob Smith", 45, "Fracture", 8000.0, "discharged", 166, 63)
    enter_data("Charlie Brown", 27, "Cold", 500.0, "admitted", 170, 65)
    enter_data("Daisy Ray", 32, "Migraine", 2200.0, "admitted", 175, 75)

    # ✅ View data
    print("\n=== All Records ===")
    for row in show_all():
        print(row)
