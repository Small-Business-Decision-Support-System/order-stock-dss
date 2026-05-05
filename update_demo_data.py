import psycopg2

def update_data():
    # Direct connection to Render database
    connection_url = "postgres://stok_takip_sistemi_user:VKLzqinrSGyoy3mdIgixMszWKzISL8BZ@dpg-d7jreit7vvec73a7i050-a.frankfurt-postgres.render.com/stok_takip_sistemi"
    
    try:
        # Connecting directly using the URL
        conn = psycopg2.connect(connection_url)
        cursor = conn.cursor()

        # SQL commands for the 3 scenarios
        scenarios = [
            ("UPDATE products SET current_stock = 85, dynamic_rop = 93, category_matrix = 'B-X' WHERE product_name = 'White Sugar 1kg'", "Scenario 1: White Sugar updated (Critical)."),
            ("UPDATE products SET current_stock = 60, dynamic_rop = 15, category_matrix = 'A-X' WHERE product_name = 'Salt 750g'", "Scenario 2: Salt updated (Excess)."),
            ("UPDATE products SET current_stock = 20, dynamic_rop = 25, category_matrix = 'C-Z' WHERE product_name = 'Butter 250g'", "Scenario 3: Butter updated (Risk).")
        ]

        for query, message in scenarios:
            cursor.execute(query)
            print(message)

        conn.commit()
        cursor.close()
        conn.close()
        print("\nSUCCESS: All demo data updated on Render!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_data()