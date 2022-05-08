import mysql.connector
from config import HOST, USER, PASSWORD


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


# 1 RECOMMENDATIONS

# this is what we are adding, as a Dict in key value pairs (here is where saved recommendation function will go)
# this is just an example
recommendation = {
    'userID': '123',
    'recsID': '456',
    'recsNames': 'abc'
}


def insert_new_recommendation(recommendation):
    try:
        db_name = 'try'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
        # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
        # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)
        query = """INSERT INTO saved_recs ({}) VALUES ('{}', '{}', '{}')""".format(
            ', '.join(recommendation.keys()),
            recommendation['userID'],
            recommendation['recsID'],
            recommendation['recsNames'],
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


# 2 REVIEWS

# this is what we are adding, as a Dict in key value pairs (where the users review function will go/imported in)
# this is just an example
reviews = {
    'userID': '123',
    'RecsID': '456',
    'RecsNames': 'abc',
    'Review': '123'
}


def insert_new_review(reviews):
    try:
        db_name = 'try'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
        # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
        # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)
        query = """INSERT INTO reviews ({}) VALUES ('{}', '{}', '{}', '{}')""".format(
            ', '.join(reviews.keys()),
            reviews['userID'],
            reviews['RecsID'],
            reviews['RecsNames'],
            reviews['Review']
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


# 3 ESCAPADE USERS

# this is what we are adding, as a Dict in key value pairs (here is where users info function will go)
# this is just an example - will most likely change into methods/inputs
users = {
    'userID': '123',
    'UsersNames': '456',
    'UsersPasswords': 'abc'
}


def insert_new_users(users):
    try:
        db_name = 'try'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # now we are running our query, when we are inserting into our DB, we have to specify column, we could write
        # them out but this is faster, the ones that will be strings need '' around {} as when it gets sent to SQL it
        # will only see the raw string in query only so we need to re add the strings (only do the columns/keys)
        query = """INSERT INTO Escapade_Users ({}) VALUES ('{}', '{}', '{}')""".format(
            ', '.join(users.keys()),
            users['userID'],
            users['UsersNames'],
            users['UsersPasswords'],
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


# uncomment to use - will most likely be a for loop
if __name__ == '__main__':
    _connect_to_db('try')
    # insert_new_recommendation(recommendation)
    # insert_new_review(reviews)
    # insert_new_users(users)
