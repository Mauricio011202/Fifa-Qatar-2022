from Functions import *
from Api import write_matches,write_stadiums,write_rest_info
from Api import name_stadiums
#Importaciones del Api especificas + toda la info de Functions

def main():
    if read_txt('Matches.txt')=='':  #Registra los equipos y stadiums desde 0 si no se han registrado
        write_matches()
    if read_txt('Stadiums.txt')=='':
        write_stadiums()
    if read_txt('RestaurantProducts.txt')=='':  #Funcion para verificar si se realizo el registro de los alimentos
        write_rest_info()
     #Si los equipos ya fueron registrados con anterioridad , el programa empieza 
    main_menu=menu()
    while main_menu!='7': 
        if main_menu=='1':
            search_match=options_matches() #Llama a la funcion para buscar los partidos
            if search_match=='1':
                search_matches_team() #Funcion para buscar por el equipo
            elif search_match=='2':
                search_matches_stadium(name_stadiums) #Funcion para buscar por el estadio,se usa una lista auxiliar con el nombre de los estadios
            elif search_match=='3':
                search_matches_dates() #Funcion para buscar por fecha
            elif search_match=='4':
                main_menu=menu() #Para salir al menu

        elif main_menu=='2':
            buy_tickets() #Funcion para ejecutar la compra de boletos
            main_menu=menu()
        elif main_menu=='3':
            valid_ticket() #Funcion para validar el codigo de la entrada. El codigo se genero en buy_tickets()
            main_menu=menu()
        elif main_menu=='4':
            op_search=menu_rest()
            if op_search=='1':
                search_name_rest() #Funcion para buscar productos por nombre
                main_menu=menu()
            elif op_search=='2':
                search_product_type() #Funcion para buscar los productos por el tipo
                main_menu=menu()
            elif op_search=='3':
                search_product_price() #Funcion para buscar los productos por un rango de precio
                main_menu=menu()
        elif main_menu=='5':
            ticket_vip() #Compras del restaurant para los clientes vip
            main_menu=menu()
        elif main_menu=='6':
            menu_e=menu_estadistics() #Menu para conocer las estadisticas
            if menu_e=='1':
                prom_vip() #Funcion para saber el promedio de gastos de los clientes vip
                main_menu=menu()
            elif menu_e=='2':
                tickets_match() #Para saber el partido con mas boletos
                main_menu=menu()
            







            
            


main()