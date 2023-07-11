#this file is used to create a database without having to use the workspace
import psycopg2

#Connect to the PostgreSQL database
dataBase = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'Daseats96!@Accenture'
)

dataBase.autocommit = True
#prepare a cursor object
cursorObject = dataBase.cursor()

#commit any open transaction
dataBase.commit()

# Execute the CREATE DATABASE statement
cursorObject.execute("CREATE DATABASE DaseatsLLC")

#commit the transaction
dataBase.commit()
# Close the cursor and connection
cursorObject.close()
dataBase.close()

print("All done!")