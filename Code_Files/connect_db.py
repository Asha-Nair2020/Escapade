import mysql.connector
from config import HOST, USER, PASSWORD
import utils

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

def insert_new_recommendation(user_id,selected_spot):
    try:
      db_name = 'Escapade'
      db_connection = _connect_to_db(db_name)
      cur = db_connection.cursor()
      #print("Connected to DB: %s" % db_name)
      query = """INSERT INTO saved_recommendations
      (USER_ID, NAME, ADDRESS, CATEGORY, PHONE) 
      VALUES ("{}", "{}", "{}", "{}", "{}")
      """.format(

          user_id,
          selected_spot["NAME"],
          selected_spot["ADDRESS"],
          selected_spot["CATEGORY"],
          selected_spot["PHONE"]
      )
      cur.execute(query)
      db_connection.commit()
      cur.close()
     
    except Exception as e:
        print(e)
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# 2 APPLICATION RAITING 

def insert_application_rating(user_id,given_rating):
    try:
        db_name = 'Escapade'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        #print("Connected to DB: %s" % db_name)
        query = """INSERT INTO application_rating 
            (USER_ID,APPLICATION_RATING) 
            VALUES ("{}", "{}")""".format(
            user_id,
            given_rating,
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


# 3 REVIEWS OF RECOMMENDATIONS

def get_recent_recommendations(user_id):
    db_name = 'Escapade'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    #print('Connected to DB:', db_name)
    #records = get_all_records()
    query="""SELECT * FROM saved_recommendations WHERE user_id='"""+ str(user_id) + "' AND RECOMMENDATION_ID NOT IN (SELECT RECOMMENDATION_ID FROM reviews_recommendations )" \
                                                                                    " ORDER BY recommendation_id DESC LIMIT 1"

    cur.execute(query)
    last_recommendation=cur.fetchall()
    cur.close()
    db_connection.close()
    return last_recommendation
    # recommendations = [x for x in records if x[1] == user_id]
    # last_recommendation=' '
    # for i in recommendations:
    #     last_recommendation=i[2]
    #     # print(i[2])
    # print(last_recommendation)


# this is what we are adding, as a Dict in key value pairs (where the users review function will go/imported in)
# this is just an example

def insert_review(user_id,recommendation_id,name,review):
    db_name = 'Escapade'
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor()
    query = """
            INSERT INTO reviews_recommendations 
            (USER_ID,RECOMMENDATION_ID,NAME,REVIEW)
            VALUES ("{}", "{}","{}","{}")
            """.format(user_id,recommendation_id,
                       name,review)
    cur.execute(query)
    db_connection.commit()
    cur.close()

    db_connection.close()



# 3 ESCAPADE USERS

def get_all_records(email):
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()

        query = """SELECT * FROM escapade_users WHERE EMAIL_ADDRESS='"""+ email + "'"
        cur.execute(query)
        results = cur.fetchall()

        return results #this is needed or it gives none data type


    except Exception:
        DbConnectionError("Failed to connect to database")
    finally:
        if db_connection:
            db_connection.close()


#if using check1 to check if username is already present, need to enter username as input
def insert_new_users(name,email_address,password):
    try:
        db_name = "Escapade"
        db_connection = _connect_to_db(db_name)
        print(db_connection)
        cur = db_connection.cursor()
        #print("connected to DB: ", db_name)

        # cur.execute("Select * from escapade_users where USER_NAME = ?", (username))
        # check1 = cur.fetchone()

        query = """ INSERT INTO escapade_users (USER_NAME,EMAIL_ADDRESS,USER_PASSWORD)
        VALUES (%s,%s,%s)"""
        record = (name,email_address,password)
        cur.execute(query,record)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Sign up failed")



def password_from_inputted_username(username, password):
    records = get_all_records(username)
    if len(records)==0:
        return 0
    else:
        if records[0][3]==password:
            usr=utils.user(records[0][0],records[0][1],records[0][2],records[0][3])
            return usr
        else:
            return 0

        
        


if __name__ == '__main__':
    _connect_to_db('Escapade')
    # insert_new_users()
    # insert_new_recommendation(recommendation)
    # insert_new_review(reviews)

