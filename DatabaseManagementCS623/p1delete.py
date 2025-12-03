import psycopg2

def transaction_delete_product():
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

        print("Starting Transaction: Delete product 'p1' from Product and Stock")

        cur.execute("DELETE FROM stock WHERE prodid = 'p1';")
        cur.execute("DELETE FROM product WHERE prodid = 'p1';")

        conn.commit()
        print("SUCCESS: Product 'p1' deleted from Product and Stock.")
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
    transaction_delete_product()
