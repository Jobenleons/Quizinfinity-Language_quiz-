import mysql.connector
db_connect1= mysql.connector.connect(host="localhost",user="root",password="wasd1234")
db_cursor1=db_connect1.cursor()
db_cursor1.execute("create database quizdatabase")
db_connect= mysql.connector.connect(host="localhost",user="root",password="wasd1234",database="quizdatabase")
db_cursor=db_connect.cursor()
db_cursor.execute("create table login_details(username VARCHAR(30) not null primary key, password VARCHAR(15) not null,email varchar(40),phone varchar(50),address varchar(50))")
#db_cursor.execute("create table user_details(username VARCHAR(30),coins int, german_stage int,Hindi_stage int)")
db_cursor.execute("create table questions(ques_id int, ques VARCHAR(100), opt1 VARCHAR(20), opt2 VARCHAR(20), opt3 VARCHAR(20), opt4 VARCHAR(20), ans VARCHAR(20), topic VARCHAR(10))")
db_cursor.execute("create table quiz_scores(username VARCHAR(30) not null primary key, password VARCHAR(15),G1_score int default 0, G2_score int default 0, G3_score int default 0, F1_score int default 0, F2_score int default 0, F3_score int default 0)")
sql="insert into questions (ques_id, ques, opt1, opt2, opt3, opt4, ans, topic) values(%s, %s, %s, %s, %s, %s, %s, %s)"
values=[(1, "What is the correct translation for telephone", "das Wasser", "der Regenschirm", "das Fahrrad", "das Telefon", "das Telefon", "German" ),
        (2, "How do you say \"Good morning\"?", "Guten Abend", "Guten Tag", "Auf Wiedersehen", "Guten Morgen", "Guten Morgen","German"),
        (3, "How do you say \"Good evening\"?", "Vielen Dank","die Schlüssel",  "Auf Wiedersehen", "Guten Abend", "Guten Abend", "German"), 
        (4,"What is the correct translation for \"Please  \"?","Bitte", "Hallo", "Entschuldigung", "links", "Bitte", "German"),
        (5,"How do you say \"Thank You\"?", "Danke", "Entschuldigung", "Bitte", "Hallo", "Danke", "German"),
        (6, "How do you say \"Good-bye\"?", "Auf Wiedersehen", "Wo ist der Strand?", "Guten Abend", "links", "Auf Wiedersehen", "German"),
        (7, "What is the correct translation for \"right\"?", "links", "rechts", "der Zug", "drei", "rechts", "German"),
        (8, "What is the correct translation for \"hospital\"?", "das Haus", "das Krankenhaus", "das Aspirin", "das Wasser", "das Haus", "German"),
        (9, "What is the correct translation for \"sweet corn\"?", "die Äpfel", "die Himbeeren", "Erdbeeren", "Mais", "Mais", "German"),
        (10, "What is the correct translation for \"four\"?", "acht", "eins", "sieben", "vier", "vier", "German"),
        (11, "What is the correct translation for \"leg \"? ", "Auge", "Bein", "Kopf", "Nase", "Bein", "German"),
        (12, "What is the correct translation for \"credit card\"?", "Zeitung", "Kreditkarte", "Buch", "Briefumschlag", "Kreditkarte", "German"),
        (13, "What is the correct translation for \"ship\"?", "Zug", "Schiff", "Flugzeug", "Fahrrad", "Schiff", "German"),
        (14, "What is the correct translation for \"fish\"?", "Fisch", "Pflaume", "Mais", "Himbeeren", "Fisch", "German"),
        (15, "What is the correct translation for \"yellow\"? ", "braun", "grün", "gelb", "schwarz", "gelb", "German"),
        (16, "What is the formal version of “you” in french?",  "Vous", "En", "Beau", "Amour", "Vous", "French"),
        (17, "What is a Baguette magique?", "Wall", "Wooden Table", "Hair wig", "Scissors", "A magic wand", "French") ,
        (18, "How do you say Good night in French?", "charité", "Bonne nuit", "Je t’aime", "Krankenhaus", "Bonne nuit", "French"),
        (19, "What does Un café s’il vous plait mean?", "Cold Coffee", "Buy a coffee", "Black tea", "A coffee please", "A coffee please", "French"),
        (20, "What is the meant by Bonjour", "hi", "Good Morning", "hello", "Bye", "hello", "French"),
        (21, "What time is it if it is Quinze heures?", "4 PM", "12 PM", "6 PM", "3 PM", "3 PM", "French"),
        (22, "What body part are les pieds?", "Heart", "Feet", "Hand", "arms", "Feet", "French"),
        (23, "What is a chapeau?", "Compass", "A hat", "Shoes", "Vous", "A hat", "French"),
        (24, "What is the french word for “fork’?", "amour", "Fourchette", "Oui ", "fort", "Fourchette", "French"),
        (25, "What does “Salut! Ça va?” mean?", "Good night", "All the Best", "Well Done", "How are You", "How are You", "French"),
        (26, "What is the correct translation for \"Please\"?", "Gauche", "Bonjour", "Désolé", "S'il vous plaît", "S'il vous plaît", "French"),
        (27, "How do you say \"Thank You\"?", "Au revoir", "Désolé", "Merci", "Droite", "Merci", "French"),
        (28, "What is the meant by Derrière?", "right", "across", "Behind", "left", "Behind", "French"),
        (29, "What is the correct translation for \"love\"?", "Amour", "charité", "Femme", "Bonsoir", "Amour", "French"),
        (30, "What is the correct translation for \"strong\"?", "Belle", "Beau", "Fort ", "Fort", "Chat", "French")]
db_cursor.executemany(sql,values)
db_connect.commit()
db_cursor.close()
