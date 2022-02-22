from src.swen344_db_utils import connect
from datetime import datetime, timedelta
from csv import reader

def rebuildTables():
    conn = connect()
    cur = conn.cursor()
    drop_sql = """
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS conversation;
        DROP TABLE IF EXISTS messages;
        DROP TABLE IF EXISTS suspension;
        DROP TABLE IF EXISTS community_channels;
        DROP TABLE IF EXISTS community
    """
    users_sql = """
        CREATE TABLE users(
            ID int,
            username varchar(255),
            email varchar(255),
            ssn varchar(255),
            phone varchar(255),
            username_change varchar(255)
        )
    """
    conversation_table = """
        CREATE TABLE conversation(
            chatID int,
            user1 varchar(255),
            user2 varchar(255),
            totalMessages int
        )
    """
    messages_table = """
        CREATE TABLE messages(
            chatID int,
            message varchar(255),
            time varchar(255),
            date varchar(255),
            status varchar(255),
            sender varchar(255),
            receiver varchar(255)
        )
    """
    suspension_table = """    
        CREATE TABLE suspension(
            userID int,
            start varchar(255),
            expiration varchar(255),
            startYear varchar(255),
            endYear varchar(255)
        )
    """
    community_table = """
        CREATE TABLE community(
            community_name varchar(255),
            community_members varchar(1000),
            community_suspended_users varchar(1000),
            community_channels varchar(1000)
        )
    """
    community_channels_table = """
        CREATE TABLE community_channels(
            channel_name varchar(255),
            community_name varchar(255),
            sender varchar(255),
            time varchar(255),
            date varchar(255),
            channel_message varchar(255),
            status varchar(255)
        )
    """

    cur.execute(drop_sql)
    cur.execute(users_sql)
    cur.execute(messages_table)
    cur.execute(conversation_table)
    cur.execute(suspension_table)
    cur.execute(community_table)
    cur.execute(community_channels_table)
    conn.commit()
    conn.close()

def populateTables():
    """
    populates users, messages, conversations, and suspensions
    """
    conn = connect()
    cur = conn.cursor()

    #People table
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('1', 'Abbott', 'govabbott@gmail.com', '043-06-4827', '202-555-0148','00-00-0000'))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('2', 'Costello', 'realcomedian@gmail.com', '507-60-1124', '202-555-0133','00-00-0000'))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('3', 'Moe', 'freebeersonme@gmail.com', '114-48-1144', '202-555-0138', '00-00-0000'))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('4', 'Larry', 'larrybird33@gmail.com', '520-66-6612', '202-555-0185','00-00-0000'))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('5', 'Curly', 'harlemcurly@gmail.com', '576-73-1234', '202-555-0162','00-00-0000' ))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('6', 'DrMarvin', 'drmarvin@gmail.com', '585-12-3333', '585-854-3044', '00-00-0000'))
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('7', 'clarknotsuperman', 'superman@gmail.com', '585-13-3354', '585-114-3024', '00-00-0000'))

    """Abbott to Costello"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'brooo no way im good man, how u doin?', '13:00','05-10-1933', 'Read', 'Costello', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'chillin how abt u?', '11:00','06-24-1937', 'Read', 'Abbott', 'Costello'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'lmao nice reply time, im g', '19:00', '12-01-1937', 'Read', 'Costello', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'haha sorry, ive been trying this new thing where i dont check my phone at all', '11:32', '02-19-1945', 'Read', 'Abbott', 'Costello'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'hahahah thats nice i hope its going well', '16:34', '02-19-1945', 'Read', 'Costello', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'yes man it is ill text you when im done with this weird phase', '13:43', '03-01-1945', 'Unread', 'Abbott', 'Costello'))

    """Abbott to Moe"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'yoooooo whats up???', '12:00', '05-21-1937', 'Unread', 'Moe', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'hello??? ive been meaning to ask you something really important man if you see this reply...', '15:32', '06-22-1938', 'Unread', 'Moe', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'you know what forget it.', '18:22', '07-13-1940', 'Unread', 'Moe', 'Abbott'))

    
    """Moe to Larry"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'excited for your game tonight?', '15:00', '06-26-1995', 'Read', 'Moe', 'Larry'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'ya bro imma go out there and show up', '15:34', '06-26-1995', 'Read', 'Larry', 'Moe'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'yes dude ill be front row watching', '00:23', '06-27-1995', 'Read', 'Moe', 'Larry'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'hell yea! see u there dog', '00:45', '06-27-1995', 'Unread', 'Larry', 'Moe'))    
    
    
   
    #Conversation
    cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 1 ')
    results = cur.fetchall()
    countAC = [item[0] for item in results]
    cur.execute("INSERT INTO conversation (chatID, user1, user2, totalMessages) VALUES (%s, %s, %s, %s);", ('1', 'Abbott', 'Costello', countAC[0]))
 
    cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 2 ')
    results = cur.fetchall()
    countML = [item[0] for item in results]
    cur.execute("INSERT INTO conversation (chatID, user1, user2, totalMessages) VALUES (%s, %s, %s, %s);", ('2', 'Moe', 'Larry', countML[0]))

    #Suspension
    cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", ('4', '01-01-2010', '01-01-2060', '2010', '2060'))
    cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", ('5', '01-01-1990', '12-31-1999', '1990', '1999'))

    conn.commit()
    conn.close()


def create_user(new_id, username, email, ssn, phone):
    """
    Creates a new user given id, username, email, ssn and phone number
    Args: 
        new_id : The ID of the user
        username : The username of the user
        email : The email of the  user
        ssn : SSN of user
        phone : Phone No. of new user
    Returned:
        None if successful
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", (new_id, username, email, ssn, phone, '00-00-0000'))
    conn.commit()
    conn.close()

def check_suspension(username, message_date):
    """
    checks for suspension for username
    Args:
        username : the username of the user in question
        message_date: the date of the message being sent
    Returned:
        0 if doesn't exist, 1 if does exist
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT users.ID FROM users WHERE users.username = '%s'""" % (username))
    results = cur.fetchall()
    vals = [item[0] for item in results]
    userID = vals[0]

    cur.execute("""SELECT COUNT(*) FROM suspension WHERE suspension.userID = '%s'""" % (userID))
    results = cur.fetchall()
    vals = [item[0] for item in results]
    if(vals[0] == 1):
        date = message_date.split('-')
        cur.execute("""SELECT start FROM suspension WHERE suspension.userID = '%s'""" % (userID))
        results = cur.fetchall()
        vals = [item[0] for item in results]
        startD = vals[0].split('-')
        cur.execute("""SELECT expiration FROM suspension WHERE suspension.userID = '%s'""" % (userID))
        results = cur.fetchall()
        vals = [item[0] for item in results]
        endD = vals[0].split('-')

        #check for year
        if(int(date[2]) >= int(startD[2]) and int(date[2]) <= int(endD[2])):
            if(int(date[2]) > int(startD[2]) and int(date[2]) < int(endD[2])):
                return 1
            elif(int(date[2]) == int(startD[2]) and int(date[2]) < int(endD[2])):
                #check for month
                if(int(date[0]) < int(startD[0])):
                    return 0
                elif(int(date[0]) > int(startD[0])):
                    return 1
                else:
                    #check for day
                    if(int(date[1]) < int(startD[1])):
                        return 0
                    else:
                        return 1
            #check for year being greater than start
            elif(int(date[2]) > int(startD[2]) and int(date[2]) == int(endD[2])):
                #month
                if(int(date[0]) > int(endD[0])):
                    return 0
                elif(int(date[0]) < int(endD[0])):
                    return 1
                else:
                    #day
                    if(int(date[1]) > int(endD[1])):
                        return 0
                    else:
                        return 1
            #same year
            else:
                #before start or after end?
                if(int(date[0]) < int(startD[0]) or int(date[0]) > int(endD[0])):
                    return 0
                #month
                elif(int(date[0]) > int(startD[0]) and int(date[0]) < int(endD[0])):
                    return 1
                elif(int(date[0]) == int(startD[0]) and int(date[0]) < int(endD[0])):
                    #day
                    if(int(date[1]) >= int(startD[1])):
                        return 1
                elif(int(date[0]) > int(startD[0]) and int(date[0]) == int(endD[0])):
                    if(int(date[1]) <= int(endD[1])):
                        return 1
                else:
                    if(int(date[1]) >= int(startD[1]) and int(date[1]) <= int(endD[1])):
                        return 1
            return 0
    conn.close()
    return 0

def getTimeAndDate():
    """
    gets current date and time and returns it in a well formatted manner
    Args: 
        None
    Returned:
        Current time and current date
    """
    dateTimeObj = datetime.now()
    time = str(dateTimeObj.hour) + ":" + str(dateTimeObj.minute)
    date = str(dateTimeObj.month) + "-" + str(dateTimeObj.day) + "-" + str(dateTimeObj.year)
    return time, date

def send_new_message(new_message, recipient, sender, message_date):
    """
    Sends a new message if user is not suspended
    Args: 
        new_message : The string that needs to be sent
        recipient : the user who is receiving the message
        sender : sender of the message
    Returned:
        ERROR if a suspension exists, None if successful
    """
    conn = connect()
    cur = conn.cursor()
    if(check_suspension(sender, message_date)):
        cur.execute("""SELECT users.ID FROM users WHERE users.username = '%s'""" % (sender))
        res = cur.fetchall()
        userID = [item[0] for item in res]
        cur.execute("""SELECT suspension.expiration FROM suspension WHERE suspension.userID = '%s'""" % (userID[0]))
        results = cur.fetchall()
        vals = [item[0] for item in results]
        raise Exception("User is suspended from sending messages until '%s'" % (vals[0]))
    status = "Unread"
    id_status = 1
    cur.execute("""SELECT COUNT(messages.chatID) FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (sender, recipient))
    results = cur.fetchall()
    convo = [item[0] for item in results]
    currConvo = convo[0]
    if(currConvo == 0):
        id_status = 2
        cur.execute("""SELECT COUNT(messages.chatID) FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (recipient, sender))
        results = cur.fetchall()
        newEC = [item[0] for item in results]
        currConvo = newEC[0]
        cur.execute("""SELECT DISTINCT messages.chatID FROM messages""")
        results = cur.fetchall()
        numOfChats = [item[0] for item in results]
        chatID = str(len(numOfChats) + 1)
    else:
        if(id_status == 1):
            cur.execute("""SELECT messages.chatID FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (sender, recipient))
            results = cur.fetchall()
            chatID_sol = [item[0] for item in results]
            chatID = chatID_sol[0]
        else:
            cur.execute("""SELECT messages.chatID FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (recipient, sender))
            results = cur.fetchall()
            chatID_sol = [item[0] for item in results]
            chatID = chatID_sol[0]
    time, date = getTimeAndDate()
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatID, new_message, time, message_date, status, sender, recipient))
    conn.commit()
    conn.close()


def sixMonthCheck(username, date):
    """
    checks for change in username within last 6 months
    Args: 
        username : the user who is about to change their username
    Returned:
        return integer 0 for more than 6 months and 1 for less.
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""SELECT users.username_change FROM users WHERE users.username = '%s'""" % (username))
    results = cur.fetchall()
    vals = [item[0] for item in results]
    Date = vals[0].split('-')
    currentDate = date.split('-')
    conn.close()
    diff = ((int(currentDate[2]) - int(Date[2])) * 12) + int(currentDate[0]) - int(Date[0])
    if(abs(diff) < 6):
        return 1
    elif(abs(diff) == 6 and int(currentDate[1]) < int(Date[1])):
        return 1
    
    return 0

def update_username(currName, newName, date):
    """
    updates the username of a user
    Args: 
        currName : current username
        newName : new username
        date: the date on which user attempts to change username again
    Returned:
        None
    """
    if(sixMonthCheck(currName, date) == 1):
        raise Exception("Username cannot be changed more than once in 6 months")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""UPDATE users SET username = '%s' WHERE users.username = '%s'""" % (newName, currName))

    cur.execute("""UPDATE conversation SET user1 = '%s' WHERE conversation.user1 = '%s'""" % (newName, currName))
    cur.execute("""UPDATE conversation SET user2 = '%s' WHERE conversation.user2 = '%s'""" % (newName, currName))

    cur.execute("""UPDATE messages SET sender = '%s' WHERE messages.sender = '%s'""" % (newName, currName))
    cur.execute("""UPDATE messages SET receiver = '%s' WHERE messages.receiver = '%s'""" % (newName, currName))

    cur.execute("""UPDATE users SET username_change = '%s' WHERE users.username = '%s'""" % (date, newName))

    conn.commit()
    conn.close()

def mark_message_read(user, message, sender):
    """
    marks given message as read
    Args: 
        user: user who is reading text
        message: message being read
        sender: sender of message
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""UPDATE messages SET status = 'Read' WHERE messages.message = '%s' AND messages.receiver = '%s' AND messages.sender = '%s'""" % (message, user, sender))
    conn.commit()
    conn.close()

def check_messages(user):
    """
    gets all the people who sent a message to user
    Args: 
        user : the person receiving messages
    Returned:
        List of everyone who has messaged user
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT messages.sender FROM messages WHERE messages.receiver = '%s'""" % (user))
    results = cur.fetchall()
    totalUsers = [item[0] for item in results]
    conn.commit()
    conn.close()
    return totalUsers

def markAsRead(user, message, sender):
    """
    marks the given message as read
    Args: 
        user : the person who reads the user
        message : the message 
        sender : the sender of the message
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""UPDATE messages SET status = 'Read' WHERE messages.message = '%s' AND messages.receiver = '%s' AND messages.sender = '%s'""" % (message, user, sender))
    conn.commit()
    conn.close()

def account_suspension(action, userID, endDate="NULL", endYear="NULL"):
    """
    depends on action but user can either be suspended or cleared
    Args: 
        action : can either be suspended or cleared.
        userID : the user who made the action
        endDate : if user is suspended endDate is when suspension ends, else its null
        endYear : if user is suspended endYear is the year when suspension else, else its NULL
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    if(action == "Suspend"):
        datetimeObj = datetime.now()
        startYear = str(datetimeObj.year)
        time, start = getTimeAndDate()
        cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", (userID, start, endDate, startYear, endYear))
    if(action == "Clear"):
        cur.execute("""DELETE FROM suspension WHERE userID = '%s'""" % (userID))

    conn.commit()
    conn.close()

def read_csv_into_db(fileName):
    """
    reads given file into the database
    Args: 
        file : given file to be read
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()
    chatId = '1'
    time = '00:00'
    date = '01-01-2021'
    status = 'Unread'
    with open(fileName, 'r') as file:
        fileReader = reader(file)
        head = next(fileReader)
        if head != None:
            for row in fileReader:
                if(row[0] == 'Abbott'):
                    sender = row[0]
                    receiver = 'Costello'
                    message = row[1]
                    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatId, message, time, date, status, sender, receiver))
                if(row[0] == 'Costello'):
                    sender = row[0]
                    receiver = 'Abbott'
                    message = row[1]
                    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatId, message, time, date, status, sender, receiver))
    conn.commit()
    conn.close()

def populate_community_tables():
    """
    Populates the community tables with starting data
    Args: 
        None
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    """Community Table"""
    cur.execute("INSERT INTO community (community_name, community_members, community_suspended_users, community_channels) VALUES (%s, %s, %s, %s);", ('Metropolis', 'clarknotsuperman', '', '#DailyPlanet,#Random'))
    cur.execute("INSERT INTO community (community_name, community_members, community_suspended_users, community_channels) VALUES (%s, %s, %s, %s);", ('Comedy', 'Abbott,Costello,Moe,Larry,Curly,DrMarvin,BabySteps2Door', '', '#ArgumentClinic,#Dialogs'))



    """Channels Table"""
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'Moe', '4:20', '09-19-2021', 'please reply', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'Moe', '8:15', '09-19-2021', 'i replied already!', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'Abbott', '8:16', '09-19-2021', 'whats up?', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'BabySteps2Door', '10:10', '09-19-2021', 'hows it hanging moe', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'DrMarvin', '10:15', '09-19-2021', 'any one wanna hang or smt?', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogs', 'Comedy', 'Curly', '12:45', '09-19-2021', 'nahh i cant today', 'Read'))

    conn.commit()
    conn.close()

    

def community_join_leave(join_leave, user, community_name):
    """
    user can join/leave a community
    Args:
        join_leave : given string 'Join' or 'Leave' the user can join/leave
        user : user who wants to join/leave
        community_name : the community that user wants to join/leave
    Returned:
        None // 'enter a valid choice'
    """
    conn = connect()
    cur = conn.cursor()

    if(join_leave == 'Join'):
        cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (community_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user not in curr_members):
            curr_members.append(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_members = '%s' WHERE community_name = '%s'""" % (new_curr_members, community_name))


    elif(join_leave == 'Leave'):
        cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (community_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user in curr_members):
            curr_members.remove(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_members = '%s' WHERE community_name = '%s'""" % (new_curr_members, community_name))

    else:
        return 'enter a valid choice'

    conn.commit()
    conn.close()

def send_message_community(sender, community_name, channel, message):
    """
    sends a message in the specified channel in the community given sender is in community
    Args:
        sender : the user sending message
        community_name : community the person is in
        channel : the channel within the community that the user wants to send the mesasge in
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (community_name))
    res = cur.fetchall()
    vals = [item[0] for item in res]
    curr_members = vals[0].split(',')
    if(sender not in curr_members):
        raise Exception("User is not a member of this channel")

    cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (community_name))
    res = cur.fetchall()
    vals = [item[0] for item in res]
    curr_suspended_members = vals[0].split(',')
    if(sender in curr_suspended_members):
        raise Exception("user cannot send the message because he is suspended from the community")

    time, date = getTimeAndDate()
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, channel_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", (channel, community_name, sender, time, date, message, 'Unread'))

    conn.commit()
    conn.close()

def get_count_unread_community(action, user, community='NULL', channel='NULL'):
    """
    gets number of unread messages in a community
    Args:
        action : 'Community' or 'Channel' shows where the unread message is
        user : user who we get count for 
        community : specifies community to count
        channel : specifies channel to count
    Returned:
        number of unread messages
    """
    conn = connect()
    cur = conn.cursor()

    if(action == 'Community'):
        cur.execute("""SELECT community.community_channels FROM community WHERE community_name = '%s'""" % (community))
        res = cur.fetchall()
        vals = [item[0] for item in res]
        curr_com = vals[0].split(',')
        total_count = 0
        for row in curr_com:
            cur.execute("""SELECT COUNT(channel_message) FROM community_channels WHERE status = 'Unread' AND community_name = '%s' AND channel_name = '%s'""" % (community, row))
            res = cur.fetchall()
            vals = [item[0] for item in res]
            total_count = total_count + vals[0]
        conn.close()
        return total_count
    elif(action == 'Channel'):
        cur.execute("""SELECT COUNT(channel_message) FROM community_channels WHERE status = 'Unread' AND community_name = '%s' AND channel_name = '%s'""" % (community, channel))
        res = cur.fetchall()
        vals = [item[0] for item in res]
        conn.close()
        return vals[0]
    else:
        conn.close()
        raise Exception("enter correct action")

def get_mentions(user):
    conn = connect()
    cur = conn.cursor()
    mentions = '@' + user
    cur.execute("""SELECT DISTINCT community_name FROM community""")
    results = cur.fetchall()
    all_communities = [item[0] for item in results]
    for members in all_communities:
        cur.execute("""SELECT community_members FROM community WHERE community_name = '%s'""" % (members))
        results = cur.fetchall()
        st = [item[0] for item in results]
        all_mem = st[0].split(',')
        if(user not in all_mem):
            all_communities.remove(members)
    all_mentions = []
    for row in all_communities:
        cur.execute("""SELECT community_channels FROM community WHERE community_name = '%s'""" % (row))
        res = cur.fetchall()
        vals = [item[0] for item in res]
        all_channels = vals[0].split(',')
        for channels in all_channels:
            cur.execute("""SELECT channel_message FROM community_channels WHERE community_name = '%s' AND channel_name = '%s'""" % (row, channels))
            res = cur.fetchall()
            all_mess = [item[0] for item in res]
            for messages in all_mess:
                if(mentions in messages):
                    all_mentions.append(messages)
    conn.close()
    return all_mentions

def suspend_users(action, user, community_name):
    """
    suspend/clear users
    Args:
        action : ''Suspend' or 'Remove' determines action for function'
        user : user getting the action
        community_name : community user is added/suspended from
    Returns:
        None
    """
    conn = connect()
    cur = conn.cursor()
    if(action == 'Suspend'):
        cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (community_name))
        res = cur.fetchall()
        vals = [item[0] for item in res]
        currentMembers = vals[0].split(',')
        if(user not in currentMembers):
            currentMembers.append(user)
            new_curr_members = ','.join(map(str, currentMembers))
            cur.execute("""UPDATE community SET community_suspended_users = '%s' WHERE community_name = '%s'""" % (new_curr_members, community_name))
    elif(action == 'Remove'):
        cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (community_name))
        res = cur.fetchall()
        vals = [item[0] for item in res]
        currentMembers = vals[0].split(',')
        if(user in currentMembers):
            currentMembers.remove(user)
            new_curr_members = ','.join(map(str, currentMembers))
            cur.execute("""UPDATE community SET community_suspended_users = '%s' WHERE community_name = '%s'""" % (new_curr_members, community_name))
    else:
        raise Exception('Incorrect Usage of Function')
    conn.commit()
    conn.close()

def get_channels_community(community):
    """
    find all channels in a community
    Args:
        community : community that we want the channels of
    Returns:
        list of channels
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""SELECT community_channels FROM community WHERE community_name = '%s'""" % (community))
    res = cur.fetchall()
    vals = [item[0] for item in res]
    conn.close()
    return vals[0].split(',')

def get_communities():
    """
    get a list of all communities 
    Args:
        none
    Returns:
        list of communities
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""SELECT community_name FROM community""")
    res = cur.fetchall()
    vals = [item[0] for item in res]
    conn.close()
    return vals

def search_community_message(community, mes):
    """
    searches community for the message
    Args:
        community: the community in question
        mes: the message we are searching for
    Returns:
        returns all messages found in the community
    """
    conn = connect()
    cur = conn.cursor()
    all_words = mes.split(" ")
    word_string = all_words[0]
    if(len(all_words) > 1):
        for row_word in all_words[1:]:
            word_string = word_string + """ & """ + row_word
    cur.execute("""SELECT channel_message FROM community_channels WHERE to_tsvector(channel_message) @@ to_tsquery('%s')""" % (word_string))
    res = cur.fetchall()
    vals = [item[0] for item in res]
    conn.close()
    return vals

def moderator_query(start_date, end_date='None'):
    """
    gives us all the suspended users who have sent a message in the given range
    Args: 
        start_date : start of range
        end_date : end of range || current date
    Returns:
        list of users
    """
    conn = connect()
    cur = conn.cursor()
    communities = get_communities()
    sus_users = [] 
    messages_sent = []
    if(end_date == 'None'):
        time, date = getTimeAndDate()
        eDate = date


    for comm in communities:
        cur.execute("""SELECT community_suspended_users FROM community WHERE community_name = '%s'""" % (comm))
        results = cur.fetchall()
        st = [item[0] for item in results]
        suspended_users = st[0].split(",")
        for sender in suspended_users:
            if(sender not in sus_users and sender != ''):
                sus_users.append(sender)

    for sender in sus_users:
        cur.execute("""SELECT sender, date FROM community_channels WHERE sender = '%s'""" % (sender))
        results = cur.fetchall()

        for mes in results:
            if(check_date_inbetween(mes[1], start_date, eDate) and mes[0] not in messages_sent):    
                messages_sent.append(mes[0])
    
    conn.close()

    return messages_sent


def get_user_suspended(community):
    """
    checks if user is suspended from a community
    Args:
        com : The community being checked
    Returns:
        A list of suspended users
    """
    conn = connect()
    cur = conn.cursor()

    sus_users = []

    cur.execute("""SELECT community_suspended_users FROM community WHERE community_name = '%s'""" % (community))
    results = cur.fetchall()
    st = [item[0] for item in results]
    sus_user = st[0].split(",")
    for sender in sus_user:
        if(sender not in sus_users and sender != ''):
            sus_users.append(sender)

    conn.close()
    
    return sus_users


def activity_summary(given_date='None'):
    """
    gives an activity summary
    Args:
        given_date : end of the 30 day period we search in || Defaults to current Date
    Returns:
        list for activity summary for the given community
    """
    conn = connect()
    cur = conn.cursor()

    temp_table = """
        CREATE TEMP TABLE temp_table(
            community varchar(255),
            messages varchar(255),
            active_users varchar(255)
        )
    """

    cur.execute(temp_table)

    if(given_date == 'None'):
        time, date = getTimeAndDate()
        given_date = date

    dateTimeObj = datetime.now() - timedelta(days=30)
    start_date = str(dateTimeObj.month) + "-" + str(dateTimeObj.day) + "-" + str(dateTimeObj.year)
    
    communities = get_communities()

    for comm in communities:
        cur.execute("""SELECT channel_message, date, sender FROM community_channels WHERE community_name = '%s'""" % (comm))
        res = cur.fetchall()
        res_mes = []
        user = []
        for mes in res:
            if(len(mes[0]) > 4 and check_date_inbetween(mes[1], start_date, given_date)):
                res_mes.append(mes)
                if(mes[2] not in user):
                    user.append(mes[2])
        act_users = len(user)
        avg_num_mes = round(len(res_mes) / 30, 3)
        cur.execute("INSERT INTO temp_table (community, messages, active_users) VALUES (%s, %s, %s);", (comm, avg_num_mes, act_users))
    cur.execute("""SELECT * FROM temp_table""")
    results = cur.fetchall()
    conn.close()
    return results

def check_date_inbetween(date_of_message, start_date, end_date):
    """
    checks if message is sent inbetween the given interval
    Args:
        date_of_message: date message is sent
        start_date: start of interval
        end_date: end of interval
    Returns:
        0 for not during suspension
        1 for sent during suspension
    """
    dateM = date_of_message.split('-')
    startSus = start_date.split('-')
    endSus = end_date.split('-')
    if(int(dateM[2]) >= int(startSus[2]) and int(dateM[2]) <= int(endSus[2])):
        if(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
            return 1
        elif(int(dateM[2]) == int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
            if(int(dateM[0]) < int(startSus[0])):
                return 0
            elif(int(dateM[0]) > int(startSus[0])):
                return 1
            else:
                if(int(dateM[1]) < int(startSus[1])):
                    return 0
                else:
                    return 1
        elif(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) == int(endSus[2])):
            if(int(dateM[0]) > int(endSus[0])):
                return 0
            elif(int(dateM[0]) < int(endSus[0])):
                return 1
            else:
                if(int(dateM[1]) > int(endSus[1])):
                    return 0
                else:
                    return 1
        else:
            if(int(dateM[0]) < int(startSus[0]) or int(dateM[0]) > int(endSus[0])):
                return 0
            elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                return 1
            elif(int(dateM[0]) == int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                if(int(dateM[1]) >= int(startSus[1])):
                    return 1
            elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) == int(endSus[0])):
                if(int(dateM[1]) <= int(endSus[1])):
                    return 1
            else:
                if(int(dateM[1]) >= int(startSus[1]) and int(dateM[1]) <= int(endSus[1])):
                    return 1
    return 0
