import sqlite3


def main():
    conn = sqlite3.connect('pets.db')
    person_id = None
    while True:
        try:
            person_id = int(input('Enter person\'s id number: '))
        except:
            print 'Must be an integer!'
            continue
        if person_id == -1:
            break
        count = int(conn.execute(
            'SELECT count(*) FROM person WHERE id=?', (str(person_id),)
        ).next()[0])
        if count:
            print conn.execute(
                'SELECT * FROM person WHERE id=?', (str(person_id),)
            ).next()
        else:
            print 'Doesn\'t exist'
    conn.close()


if __name__ == '__main__':
    main()
