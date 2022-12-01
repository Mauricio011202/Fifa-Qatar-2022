from Match import *
from Stadium import *
from Products import *
import requests 
api_teams= 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'
data_team= requests.get(api_teams)
if data_team.status_code == 200: #Respuesta de estado satisfactorio HTTP 200 OK indica que la solicitud ha tenido éxito. 
        data_util= data_team.json() 

api_stadiums='https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json'
data_stadium= requests.get(api_stadiums)
if data_stadium.status_code==200:
    data_stadiums=data_stadium.json()

api_matches='https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json'
data_match=requests.get(api_matches)
if data_match.status_code==200:
    data_matches=data_match.json()

#Registrar los equipos con la información proveniente de la API
name_teams= []
fifa_codes=[]
groups=[]

#Nombres de los equipos
for element in data_util:
        name_team= element.get('name')
        name_teams.append(name_team)

#Codigo Fifa
for element in data_util:
        fifa_code= element.get('fifa_code')
        fifa_codes.append(fifa_code)

#Grupos
for element in data_util:
        group= element.get('group')
        groups.append(group)
#------------------------------------------------------------------------------------

#Registrar los estadios con la información  proveniente de la API

name_stadiums=[]
locations=[]
rows=[]
columns=[]

#Nombre de los estadios
for stadium in data_stadiums:
        name_stadium= stadium.get('name')
        name_stadiums.append(name_stadium)
#Ubicaciones de los estadios

for l in data_stadiums:
        location= l.get('location')
        locations.append(location)

#Capacidad de los estadios
for c in data_stadiums:
        aux=c.get('capacity')
        row=aux[0]
        rows.append(row)

for c in data_stadiums:
        aux=c.get('capacity')
        column=aux[1]
        columns.append(column)
#------------------------------------------------------------------------

#Registrar los partidos con la información  proveniente de la API
home_teams=[]
away_teams=[]
dates=[]
game_stadium=[]

for match in data_matches:
        local= match.get('home_team')
        home_teams.append(local)

for match in data_matches:
        away= match.get('away_team')
        away_teams.append(away)


for match in data_matches:
    date=match.get('date')
    dates.append(date)

for match in data_matches:
    stadium_id=match.get('stadium_id')
    game_stadium.append(stadium_id)

#----------------------------------------------------------------------
#Funciones para guardar los equipos y los stadiums en un txt. Utilizando POO como molde para el ingreso de datos
def write_matches():
        file='Matches.txt'
        n=0
        while n<48:
                match=Match(home_teams[n],away_teams[n],dates[n],game_stadium[n]) #Uso las listas auxiliares para iterar y llenar el objeto con los datos del api
                n=n+1
                register=match.match_register() #Llamo a la función para escribir en el api de forma legible y organizada
                data = open(file, "a")
                data.write(register) #Registro la info en el txt con el metodo .write()
                data.close()  
#Hago el procedimiento de arriba
def write_stadiums():
        file='Stadiums.txt'
        n=0
        while n<8:
                stadium=Stadium(name_stadiums[n],rows[n],columns[n],locations[n])
                n=n+1
                register=stadium.register_stadium()
                data = open(file, "a")
                data.write(register)
                data.close()  

#----------------------------------------------------------------------------------------------------------------------
#Guardar datos del restaurante

def write_rest_info():
        product_rest_stadium=[]
        for rest in data_stadiums:  #Con este primer for saco cada  diccionario del api(osea cada estadio)
                info_rest= rest.get('restaurants')
                for info in info_rest: #Con este segundo for puedo tomar los diccionarios dentro del restaurante
                        name_r=info.get('name')
                        products=info.get('products')
                        for product in products: #Con el tercer for puedo tomar los diccionarios de cada pregunta 
                                name_p=product.get('name')
                                price=product.get('price')
                                iva=16/100                      #Se toma todo la información de los productos 
                                mont=int(price)*iva
                                price=price+mont
                                typ=product.get('type')
                                adicional=product.get('adicional')
                                quantity=product.get('quantity')
                                product_rest=Product(name_r,name_p,str(price),typ,adicional,str(quantity))
                                show_product=product_rest.show_product()
                                product_rest_stadium.append(show_product)
        
        file='RestaurantProducts.txt'
        for prod in product_rest_stadium:
                data = open(file, "a")
                data.write(prod+'\n')  #Se escribe en el txt para que los datos siempre esten cargados.
                data.close()  

