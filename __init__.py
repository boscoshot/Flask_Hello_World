from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:val_user>/<int:val_user2>')
def somme(val_user,val_user2):
  resultat = val_user + val_user2
  if resultat % 2 == 0:
      message = "pair"
  else:
      message = "impair"
  
  return "<h2>La somme des 2 valeurs est : </h2>" + str(val_user + val_user2)+"<h2>et est</h2>"+message
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
