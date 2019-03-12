# Ne pas hésiter à consulter le site officiel :
# https://datatables.net/    
# https://editor.datatables.net/
# "Datatables" c'est pour l'affichage, et "Editor" est pour les opérations CRUD sur la BD à partir de la Datatable affichée en page html


from flask import Flask, jsonify, render_template

####
# Ce code est à supprimer les données doivent être récupéré de la base de données 
tvs = []

for i in range(10000):
    tv = {"id" : "tv_" + str(i), "price" : 500+i}
    tvs.append(tv)
####



app = Flask(__name__)


@app.route('/dt_tvs')                                                                                  
def dt_tvs():
    
    # Récupérer les données avec une requête sql
    data_to_get_from_sqlDB = tvs
    
    # Datatables attend un objet qui a une clé "data" et pour valeur une liste d'objets (liste de tvs dans cet exemple)
    expected = {"data" : data_to_get_from_sqlDB}

    return jsonify(expected)

@app.route('/')                                                                                  
def index():
    
    return render_template("index.html")



app.run(debug= True)