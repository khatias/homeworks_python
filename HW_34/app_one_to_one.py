from exercises34 import User, Profile, engine
from sqlalchemy.orm import sessionmaker
import mysql.connector
Session = sessionmaker(bind=engine)

session = Session()

user1 = User(username="khatias", email ="sikharulidzekhatiaa@gmail.com")
user2 = User(username="levank", email ="kuchukhidzelevan@gmail.com")
user3 = User(username="mariams", email ="sikharulidzemariam@yahoo.com")
user4 = User(username="nataliak", email ="kochiashvilinatalia@gmail.com")
user5 = User(username="theag", email ="ghvinadzethea@yahoo.com")

profile1 =  Profile( bio ="Bio of user1", profile_picture = "user1_profile_picture.png", user = user1)
profile2 =  Profile( bio ="Bio of user2", profile_picture = "user2_profile_picture.png", user = user2)
profile3 =  Profile( bio ="Bio of user3", profile_picture = "user3_profile_picture.png", user = user3)
profile4 =  Profile( bio ="Bio of user4", profile_picture = "user4_profile_picture.png", user = user4)
profile5 =  Profile( bio ="Bio of user5", profile_picture = "user5_profile_picture.png", user = user5)


session.add_all([user1, user2, user3, user4, user5, profile1, profile2, profile3, profile4, profile5])


session.commit()

# ///////////////////////////

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Xatenco22",
    database="it_step_34"
)
cursor = conn.cursor()

user_data = [
    ("user6", "user6@example.com"),
    ("user7", "user7@example.com")
]

insert_user_query = "INSERT INTO user (username, email) VALUES (%s, %s)"
cursor.executemany(insert_user_query, user_data)
conn.commit()


cursor.execute("SELECT id FROM user WHERE username IN ('user6', 'user7')")
user_ids = [row[0] for row in cursor.fetchall()]


profile_data = [
    (user_ids[0], "Bio of user6", "user6_profile_picture.jpg"),
    (user_ids[1], "Bio of user7", "user7_profile_picture.jpg")
]


insert_profile_query = "INSERT INTO profile (user_id, bio, profile_picture) VALUES (%s, %s, %s)"
cursor.executemany(insert_profile_query, profile_data)
conn.commit()


cursor.close()
conn.close()
