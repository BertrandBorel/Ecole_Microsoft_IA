# importation du module SQL, utilisation d'un alias (ici 'MC')
import mysql.connector as MC

# étape de connexion à la base de données (ici 'mydb')
    # l'hôte est ici local 
    # faire attention au port
mydb = MC.connect(host="localhost", port="8080", user= "root", password="root",
    database="trombinoscope")
cursor = mydb.cursor()

# importation des données via une requête SQL
cursor.execute("SELECT qualification, genre, nom, prenom, photo FROM personne NATURAL JOIN statut \
    NATURAL JOIN genre WHERE personne.id_genre = genre.id_genre AND \
    personne.id_statut = statut.id_statut ;")
rows = cursor.fetchall()

# création d'un dictionnaire :
    # il aura pour but de récupérer les informations
dico_test={}
for row in rows:
    print('{2},{3} : {1} - {0}'.format(row[0], row[1], row[2], row[3]))
    dico_test[row[4]]= row[3] + " " +row[2] + " " +row[1] + " " +row[0]

# afficher le dictionnaire
print(dico_test)