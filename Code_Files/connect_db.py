import mysql.connector
from config import HOST, USER, PASSWORD


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

  def insert_new_recommendation(selected_spot):
    try:
      db_name = 'Escapade'
      db_connection = _connect_to_db(db_name)
      cur = db_connection.cursor()
      print("Connected to DB: %s" % db_name)
      query = """INSERT INTO saved_recommendations s 
      (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
      VALUES ("{}", "{}", "{}", "{}", "{}")
      INNER JOIN escapade_users e ON s.USER_ID = e.USER_ID"
      """.format(

          2,
          selected_spot["NAME"],
          selected_spot["ADDRESS"],
          selected_spot["CATEGORY"],
          selected_spot["PHONE"]
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


    
    
    
    
    
# 2 APPLICATION RAITING 

def insert_application_rating(given_rating):
    db_name = 'Escapade'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    print("Connected to DB: %s" % db_name)
    query = """INSERT INTO application_rating 
    (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
    VALUES ("{}", "{}")""".format(
        2,
        given_rating["APPLICATION_RATING"],
    )
    cur.execute(query)
    db_connection.commit()
    cur.close()
    



# 2 REVIEWS OF RECOMMENDATIONS

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

# users = {
#     'userID': '123',
#     'UsersNames': '456',
#     'UsersPasswords': 'abc'
# }

def get_all_records():
    try:
        db_name = "project"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM escapade_users"""
        cur.execute(query)
        results = cur.fetchall()

        return results #this is needed or it gives none data type


    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


#if using check1 to check if username is already present, need to enter username as input
def insert_new_users(record):
    try:
        db_name = "try"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("connected to DB: ", db_name)

        # cur.execute("Select * from escapade_users where USER_NAME = ?", (username))
        # check1 = cur.fetchone()

        query = """ INSERT INTO escapade_users ({})
        VALUES ("{}", "{}")
        """.format(",".join(record.keys()), record['USER_NAME'], record['USER_PASSWORD'])
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Sign up failed")

        



def password_from_inputted_username(username, password):
    records = get_all_records()
    password_based_on_user = [x for x in records if x[1] == username]
    print(password_based_on_user)   ##remove later
    for i in password_based_on_user:
        print(i[2])    ## remove latez
    if password == i[2]:
        print("congratulations!")
    else:
        print("try again")
        
        

# uncomment to use - will most likely be a for loop
if __name__ == '__main__':
    _connect_to_db('Escapade')
    # insert_new_recommendation(recommendation)
    # insert_new_review(reviews)
    # insert_new_users(users)
