import psycopg2

def transaction_add_product_p100():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="productdb",
            user="postgres",
            password="Calvin123!"
        )
        conn.autocommit = False
        cur = conn.cursor()

        print("Starting Transaction: Add product (p100, cd, 5) in Product and (p100, d2, 50) in Stock")

        cur.execute(
            "INSERT INTO product (prodid, pname, price) VALUES (%s, %s, %s);",
            ("p100", "cd", 5)
        )

        cur.execute(
            "INSERT INTO stock (prodid, depid, quantity) VALUES (%s, %s, %s);",
            ("p100", "d2", 50)
        )

        conn.commit()
        print("SUCCESS: Added product 'p100' to product and stock.")
    except Exception as e:
        if conn is not None:
            conn.rollback()
        print("FAILURE: Transaction rolled back.")
        print("Error:", e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    transaction_add_product_p100()
