import sqlite3
print("Test")
connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()


def getTrigger(connection):
    print("=== All Trigger ===")
    c = connection.cursor()
    c.execute('select name from sqlite_master where type = "trigger";')
    for item in c.fetchall():
        print('\t', item);

def getTable(connection, tableName):
    print("Table {}".format(tableName))
    c = connection.cursor()
    command = '''
        select * from {}
    '''.format(tableName)
    c.execute(command)
    for item in c.fetchall():
        print('\t', item);

def getTableInfor(connection, tableName):
    print("Table Infor {}".format(tableName))
    c = connection.cursor()
    command = '''
        select * from {}
    '''.format(tableName)
    data = c.execute(command)
    for item in data.description:
        print('\t', item[0]);

def deleteTrigger(connection, name):
    c = connection.cursor()
    command = '''
    DROP TRIGGER IF EXISTS {};
    '''.format(name)
    c.execute(command)
    connection.commit()
    print("Deleted Trigger {}".format(name))

def createCity_Trigger(connection):
    name = 'City_Trigger'
    deleteTrigger(connection, 'City_Trigger')
    c.execute('''
                CREATE TRIGGER City_Trigger
                 AFTER INSERT ON product_city
                 BEGIN
                     SELECT 'Insert City';
                 END;
    ''')

    connection.commit()
    print('Created Trigger {}'.format(name))

def createCityAfterDeleteTrigger(connection):
    name = 'City_After_Delete_Trigger'
    c = connection.cursor()
    deleteTrigger(connection, name)
    command = '''
        CREATE TRIGGER {}
        BEFORE DELETE ON product_city
        BEGIN
            UPDATE product_place
            SET City_id = -1
            WHERE City_id = OLD.id;
        END;
    '''.format(name)
    c.execute(command)
    connection.commit()
    print("Created {}".format(name))

def createCheckMailTrigger(connection):
    name = 'Check_Mail_Trigger'
    c = connection.cursor()
    deleteTrigger(connection, name)
    command = '''
        CREATE TRIGGER {} 
        BEFORE INSERT ON auth_user
        BEGIN
            SELECT
                CASE
	                WHEN NEW.name NOT LIKE '%_@__%.__%' THEN
   	                    RAISE (ABORT,'From Trigger Check_Mail_Trigger: Invalid email address')
                END;
        END;
    '''.format(name)
    c.execute(command)
    connection.commit()

def createCheckUsernameTrigger(connection):
    name = 'Check_Username_Trigger'
    c = connection.cursor()
    deleteTrigger(connection, name)
    command = '''
            CREATE TRIGGER {} 
            BEFORE INSERT ON auth_user
            BEGIN
                SELECT
                    CASE
    	                WHEN EXISTS (SELECT * FROM product_city P
    	                            WHERE P.name = NEW.name) THEN
       	                    RAISE (ABORT,'From Trigger Check_Username_Trigger :Invalid Username')
                    END;
            END;
        '''.format(name)
    c.execute(command)
    connection.commit()

def createDeleteProfileTrigger(connection):
    name = 'Delete_Profile_Trigger'
    c = connection.cursor()
    deleteTrigger(connection, name)
    command = '''
                CREATE TRIGGER {} 
                AFTER DELETE ON product_profile
                BEGIN
                    DELETE FROM auth_user
                    WHERE id = OLD.user;
                END;
            '''.format(name)
    #c.execute(command)
    connection.commit()

def createInsertReviewTrigger(connection):
    name = 'After_Insert_Review_Trigger'
    c = connection.cursor()
    deleteTrigger(connection, name)
    command = '''
                    CREATE TRIGGER {} 
                    AFTER INSERT ON product_place
                    BEGIN
                        UPDATE product_place
                        SET raiting = (SELECT AVG(rating)
                                        FROM product_review
                                        WHERE place_id = NEW.id)
                        WHERE id = NEW.id; 
                    END;
                '''.format(name)
    c.execute(command)
    connection.commit()

createCity_Trigger(connection)
createCityAfterDeleteTrigger(connection)
createCheckMailTrigger(connection)
createCheckUsernameTrigger(connection)
createDeleteProfileTrigger(connection)
createInsertReviewTrigger(connection)
getTrigger(connection)

c = connection.cursor()

command = '''
'''
data = c.execute(command)
connection.commit()
