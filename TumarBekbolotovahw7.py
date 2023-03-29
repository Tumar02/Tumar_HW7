import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
      cursor = connection.cursor()
      cursor.execute(sql)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


def add_products(connection, products):
    try:
        sql = '''INSERT INTO products
         (product_title, price, quantity)
         VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(f'The error is: {e}')
    return connection


def change_quantity_by_id(connection, product):
    try:
        sql = '''UPDATE products SET quantity = ?
         WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def change_price_by_id(connection, product):
    try:
        sql = '''UPDATE products SET price = ?
         WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f'Errors: {e}')


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products WHERE quantity>?'''
        cursor = connection.cursor()
        cursor.execute(sql, (limit, ))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def find_words(connection, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE "C%" '''
        cursor = connection.cursor()
        cursor.execute(sql, word)
        connection.commit()

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


data_base_name = 'hw.db'

sql_create_list_of_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity DOUBLE (5) NOT NULL DEFAULT 0)
'''


db_connection = create_connection(data_base_name)
if db_connection is not None:
    print('Connected successfully!')
    add_products(db_connection, ('Cleanser', 250.08, 20))
    add_products(db_connection, ('Exfoliator', 150.0, 15))
    add_products(db_connection, ('Treatment', 440.90, 5))
    add_products(db_connection, ('Serum', 100.5, 23))
    add_products(db_connection, ('Face Oil', 550.0, 10))
    add_products(db_connection, ('Sunscreen', 760.65, 17))
    add_products(db_connection, (' Moisturizer', 1200.89, 8))
    add_products(db_connection, ('Chemical Peel', 350.45, 14))
    add_products(db_connection, ('Toner', 980.0, 12))
    add_products(db_connection, ('Face Mask', 80.15, 120))
    add_products(db_connection, ('Eye cream', 1050.0, 20))
    add_products(db_connection, ('Moisturizing cream', 450.67, 15))
    add_products(db_connection, ('Retinol', 745.56, 12))
    add_products(db_connection, ('Essence', 800.95, 10))
    add_products(db_connection, ('Make up remover', 680.13, 25))
    add_products(db_connection, ('Salicylic acid', 1350.85, 13))
    # change_price_by_id(db_connection, 1200.5, 9)
    # change_quantity_by_id(db_connection, 28, 12)
    # delete_product_by_id(db_connection, 5)
    # select_all_products(db_connection)
    # select_products_by_quantity(db_connection, 100)
    # find_words(db_connection, cl)
    db_connection.close()
    print('DONE!')
