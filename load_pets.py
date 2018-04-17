import sqlite3

person = ["(1, 'James', 'Smith', 41)",
          "(2, 'Diana', 'Greene', 23)",
          "(3, 'Sara', 'White', 27)",
          "(4, 'William', 'Gibson', 23)"]
pet = ["(1, 'Rusty', 'Dalmation', 4, 1)",
       "(2, 'Bella', 'Alaskan Malamute', 3, 0)",
       "(3, 'Max', 'Cocker Spaniel', 1, 0)",
       "(4, 'Rocky', 'Beagle', 7, 0)",
       "(5, 'Rufus', 'Cocker Spaniel', 1, 0)",
       "(6, 'Spot', 'Bloodhound', 2, 1)"]
person_pet = ["(1, 1)",
              "(1, 2)",
              "(2, 3)",
              "(2, 4)",
              "(3, 5)",
              "(4, 6)"]


def main():
    conn = sqlite3.connect('pets.db')
    for val in person:
        conn.execute('INSERT INTO person VALUES %s;' % val)
    for val in pet:
        conn.execute('INSERT INTO pet VALUES %s;' % val)
    conn.commit()
    for val in person_pet:
        conn.execute('INSERT INTO person_pet VALUES %s;' % val)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
