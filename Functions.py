from Products import Product
from itertools import permutations

def read_txt(file):
    data = open(file, "r")
    message = data.read()    #Funcion creada para sacar el texto de los txt
    data.close()
    return message


def menu():
    menu= input('Seleccione\n1-Gestión de Partidos y Estadios\n2-Venta de Entradas\n3-Validar Tickets\n4-Gestión de Restaurante\n5-Gestión de Venta de Restaurante\n6-Estadísticas\n7-Salir\n==>')
    while menu!='1' and menu!='2' and menu!='3' and menu!='4' and menu!='5' and menu!='6' and menu!='7':  #Validacion del menu
        menu= input('Seleccione\n1-Gestión de Partidos y Estadios\n2-Venta de Entradas\n3-Validar tickets\n4-Gestión de Restaurante\n5-Gestión de Venta de Restaurante\n6-Estadísticas\n7-Salir\n==>')    
    return menu

def options_matches():
    menu = input('\nSeleccione la acción a realizar\n1-Buscar todos los partidos de un país\n2-Buscar todos los partidos de un estadio\n3-Buscar todos los partidos de una fecha\n4-Regresar==>\n')
    while menu!='1' and menu!='2' and menu!='3' and menu!='4':
        menu = input('\nSeleccione la acción a realizar\n1-Buscar todos los partidos de un país\n2-Buscar todos los partidos de un estadio\n3-Buscar todos los partidos de una fecha\n4-Regresar\n==>')
    return menu
    

def search_matches_team():
    games=[]
    team=input('Escriba en ingles el nombre del pais que desea visualizar todos sus partidos:').title()
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n') #Convierto en lista mis datos del txt
    print('***PARTIDOS DISPONIBLES***')  
    for l in aux:
        aux2=l.split(',') #Convierto en lista cada linea del txt
        for word in aux2:
            if word==team: #Si el juego ingresado es igual a algun valor de la linea del txt entonces imprimo
                games.append(l)
                print(l)
    if games==[]:
        print('El equipo seleccionado no pertenece al FIFA MUNDIAL QATAR 2022.\nRecuerde que debe ingresar el nombre en inglés')


def search(match):
    games=[]
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n')   #Se repite el procedimiento de la funcion de arriba 
    print('***PARTIDOS DISPONIBLES***')
    for l in aux:
        aux2=l.split(',')
        for word in aux2:
            if word==match:
                games.append(l)
                print(l)

def search_matches_stadium(name_stadiums):
    print('Seleccione el Estadio en el que desea ver los partidos disponibles:')
    n=1
    for name in name_stadiums:
        print(f'{n}-{name}')  #Impresion de cada partido con un numero que lo identifique
        n=n+1
    stadium= input('==>')
    while stadium!='1' and stadium!='2' and stadium!='3' and stadium!='4' and stadium!='5' and stadium!='6' and stadium!='7' and stadium!='8':
        print('Debe seleccionar una de los 8 estadios disponibles:')
        stadium=input('==>')
    if stadium=='1':
        search('1')
    elif stadium=='2':
        search('2')
    elif stadium=='3':
        search('3')
    elif stadium=='4':
        search('4')
    elif stadium=='5':
        search('5')
    elif stadium=='6':
        search('6')
    elif stadium=='7':
        search('7')
    elif stadium=='8':
        search('8')  #Se llama a la función search() explicada anteriormente




def search_matches_dates():
    day=input('Escriba en números el dia del partido que desea visualizar==>')
    month=input('Escriba en números el mes del partido que desea visualizar==>')
    date=month+"/"+day+"/"+'2022'
    games=[]
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n')
    print('***PARTIDOS DISPONIBLES***')
    for l in aux:
        aux2=l.split(',') #Lista de cada linea del txt
        aux4=aux2[2]
        aux3=aux4.split(' ')
        if aux3[0]==date:  #Se compara la fecha dada de dicha linea con la fecha ingresada por el usuario
                games.append(l)
                print(l)
    if games==[]:
        print('La fecha seleccionada no esta disponible')

#----------------------------------------------------------------------------------------          
def vampiro(id):
    if len(str(id))==7:
        id=(f'0{id}')
    else:
        id=str(id)
    p=permutations(id,len(id))
    pl=list(p)
    for num in pl:
        c="".join(num)
        x,y=c[:int(len(c)/2)],c[int(len(c)/2):]
        if x[-1]==0 and y[-1]==0:
            continue
        if int(x)*int(y)==int(id):  #Si la multiplicacion de la mitad de la cifra con la otra mitad es igual a 
            return 1                # la misma cedula, entonces dara como resultado 1, es decir es Vampiro
    return 0

    
def matrix(occupied_chairs,row, column):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #Lista auxiliar para nombrar los asientos
    rows = []
    for n in range(0, column):
        chairs=[]
        for m in range(1, row+1):
                    chairs.append(f"{letters[n]}{m}") #Ingreso del asiento organizado por letra y numero
                    for chair in occupied_chairs:
                        for p in chairs:
                            if p==chair:
                                ocupado=chairs.index(p)
                                chairs[ocupado]='ND'  #Remplazar ND:No disponible, en las sillas ocupadas
        rows.append(chairs)

    print('\nPuestos disponibles:')
    for i in rows:
        print(' '.join(i))  #Quitar los corchetes de lista y separar los asientos por espacios


#Pasando parametros se crea la factura para imprimirse
def imprimir_factura(name,last_name,amount,id,ticket_s,game,price,iva,discount_vamp,price_total,s_chair):
    print('\n')
    print(f'CLIENTE:{name} {last_name}')
    print(f'CEDULA:{id}')
    print('\t\t***FACTURA***')
    print('------------------------------------------------')
    print(f'{amount}xEntrada {ticket_s} {game}:{price}')
    print(f'DESCUENTO:{discount_vamp}')
    print(f'ASIENTOS:')
    for chair in s_chair:
        print(f'{chair}')
    print('------------------------------------------------')
    print(f'{price}  IVA  16%\t\t{iva}')
    print('------------------------------------------------')
    print(f'TOTAL\t\t  {price_total}')

def buy_tickets():
    occupied_chairs=[] #Lista para introducir las sillas que se compren
    s_chair=[]
    name=input('Introduzca el nombre del cliente:')   #Se pide la info del cliente
    last_name=input('Introduzca el apellido del cliente:')
    id=input('Introduzca la cédula del cliente:')
    while not id.isnumeric() or (len(id) <7 or len(id) > 8):
        id=input("Dato inválido, ingrese la cédula del cliente: ")
    discount=vampiro(id)
    age= input('Introduzca la edad del cliente: ')
    while not age.isnumeric() or len(age)>3:
        age=('Dato invalido, ingrese una edad')
    print('Seleccione el número del partido a comprar: ')
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n')
    n=1
    for match in aux:
        print(f'{n}-{match}')
        n=n+1
    selected_match=input('==>')
    game=aux[int(selected_match)-1]  #Se obtiene la linea de informacion del partido seleccionado
    stadium_id=game[-1]
    text2=read_txt('Stadiums.txt')
    aux2=text2.split(',')
    aux2=text2.split('\n')
    stadium=aux2[int(stadium_id)-1]
    stadium_list= stadium.split(',')
    stadium_row=int(stadium_list[1])  #Se obtione la cantidad de filas
    stadium_column=int(stadium_list[2]) #Se obtiene la cantidad de columnas
    ticket=input('Seleccione el tipo de boleto:\n\t1-General\n\t2-Vip\n==>')
    amount=int(input('Ingrese la cantidad de boletos que desea:'))
    text3=read_txt('Tickets.txt')
    aux3=text3.split('//')
    aux3=text3.split('\n')
    if text3!='':
        for t in aux3:
            t_list=t.split('//')
            if t_list!=['']:
                if t_list[4]==selected_match:
                    o=t_list[6]
                    occupied=o.replace('[','')
                    occupied_f=occupied.replace(']','')  #Quitar los corchetes para crear el str para la funcion matrix()
                    chairs_o=occupied_f.split(',')
                    for c in chairs_o:
                        occupied_chairs.append(c)
    a=0
    while a<amount:
        matrix(occupied_chairs,stadium_row,stadium_column)  #Se llama a la funcion matrix con la informacion requerida
        chair_column=input('Ingrese la letra del asiento:').upper()
        chair_row=input('Ingrese el numero del asiento:')
        occupied_chair=chair_column+chair_row #Se une la letra del asiento con el numero seleccionado
        s_chair.append(occupied_chair)
        occupied_chairs.append(occupied_chair)
        a+=1
    price=0
    ticket_s=''
    if ticket=='1':
        ticket_s='General'
        price=50
        price_total=50*amount        #  Determinamos el precio
    elif ticket=='2':
        ticket_s='Vip'
        price=120
        price_total=120*amount
    iva=(16/100)*price_total
    price_total=price_total+iva
    if discount==1:
        discount_vamp=(50/100)*price_total
        price_total=price_total-discount_vamp
    else:
        discount_vamp=0

    num=0
    code=selected_match+str(num)
    for ticket in s_chair:
        num+=1
        code=selected_match+str(num)+ticket+'\n'   #Creo un codigo para cada entrada comprada
        v_ticket= open('Valid_tickets.txt','a')
        v_ticket.write(str(code))
        v_ticket.close()


    print('\nCompra procesada\n')
    imprimir_factura(name,last_name,amount,id,ticket_s,game,price,iva,discount_vamp,price_total,s_chair)


    info_entradas=name+'//'+last_name+'//'+age+'//'+id+'//'+selected_match+'//'+ticket_s+'//'+str(s_chair)+'//'+str(price_total)+'\n'
    data_tickets=open('Tickets.txt','a') #Inntoducir la info de la compra a un txt
    data_tickets.write(info_entradas+'\n')
    data_tickets.close()  
    

#---------------------------------------------------------------------------------------------------------------
#MODULO 3. FUNCION PARA VALIDAR LAS ENTRADAS
def valid_ticket():
    ass=[]
    assist_list=[]
    print('***BIENVENIDO****')
    ticket= input('Para validar un ticket introduzca el codigo de la entrada:').upper()
    t=open('Valid_Tickets.txt','r')
    text=t.read()
    t.close()
    if text!='':
        aux2=text.split('\n')
        for l in aux2:
            if l==ticket:  #Si el codigo se consigue en el txt la entrada es valida, se confirma la asistencia
                assist=aux2.index(l)
                assist_list.append(assist)
                ass.append(l)

        aux2.pop(assist) #Se elimina el codigo verificado para dar como asistida a la entrada
 
        remove=open('Valid_Tickets.txt','w')
        remove.write('')
        remove.close()

        for ticket in aux2:
            data=open('Valid_Tickets.txt','a')
            data.write(ticket+'\n') #Agregar los codigos restantes al txt
            data.close()

    if ass==[]:
        print('NO DISPONIBLE EL CODIGO INGRESADO\nEl ticket ya ingresó al stadium o es un boleto falso ')
    

#--------------------------------------------------------------------------------------------------------------
#MODULO 4. Gestión del restaurante 

#Para buscar un producto:

def menu_rest():
    search=input('Seleccione:\n1-Para buscar un producto por el nombre\n2-Para buscar un producto por el tipo\n3-Para buscar el nombre por el rango de precio\n==>')
    while search!='1' and search!='2' and search!='3':
        search=input('Seleccione:\n1-Para buscar un producto por el nombre\n2-Para buscar un producto por el tipo\n3-Para buscar el nombre por el rango de precio\n==>')
    return search

def search_product(pc):  #Funcion creada para imprimir los productos encontrados
    text=read_txt('RestaurantProducts.txt')
    aux=text.split('//')
    aux=text.split('\n')
    for name_product in aux:
        product=name_product.split('//')
        for word in product:
            if word==pc:
                print('\n')
                print(f'PRODUCTO:{product[1]}')
                print(f'DISPONIBLE EN EL RESTAURANTE: {product[0]}')
                print(f'PRECIO: {product[2]}')
                print(f'TIPO:{product[3]}')
                print(f'DETALLES:{product[4]}')
                print(f'CANTIDAD: {product[5]}')
                
def search_name_rest():
    list=[]
    text=read_txt('RestaurantProducts.txt')
    aux=text.split('//')
    aux=text.split('\n')
    print('***PRODUCTOS DISPONIBLES***')
    for name_product in aux:
       product=name_product.split('//')
       if product!=['']:
        list.append(product[1]) #Seleccionar uno de los productos
    
    only_products = []
    for item in list:
        if item not in only_products:  #Realizar una lista que no tenga la repeticion de la comida de todos los estadios
            only_products.append(item)
    
    n=1
    for p in only_products:
        print(f'{n}-{p}')
        n=n+1

    op=input('==>')
    while op!='1' and op!='2' and op!='3' and op!='4' and op!='5' and op!='6' and op!='7' and op!='8':
        op=input('==>')
    if op=='1':                       #Dependiento de la opcion escogida el parametro sera diferente
        pc=only_products[0]
    elif op=='2':
        pc=only_products[1]
    elif op=='3':
        pc=only_products[2]
    elif op=='4':
        pc=only_products[3]
    elif op=='5':
        pc=only_products[4]
    elif op=='6':
        pc=only_products[5]
    elif op=='7':
        pc=only_products[6]
    elif op=='8':
        pc=only_products[7]

    search_product(pc)

def search_product_type():
    op=input('Seleccione el tipo de producto que desea visualizar: \n1-Beverages\n2-Food\n==>')
    while op!='1' and op!='2':
        op=input('Seleccione el tipo de producto que desea visualizar: \n1-Beverages\n2-Food\n==>')
    if op=='1':
        pc='beverages'
        search_product(pc)  #Llamar a la funcion para mostrar los productos y pasar como parametro el tipo de alimento
    elif op=='2':
        pc='food'
        search_product(pc)

def search_product_price():
    print('Seleccione un rango de precio')
    list=[]
    text=read_txt('RestaurantProducts.txt')
    aux=text.split('//')
    aux=text.split('\n')
    print('***RANGOS DE PRECIOS***')
    for name_product in aux:
       product=name_product.split('//')
       if product!=['']:
        list.append(product[2])
    
    only_prices= []
    for item in list:
        if item not in only_prices:
            only_prices.append(item)
    
    n=1
    for p in only_prices:
        print(f'{n}-{p}')
        n=n+1

    op=input('==>')
    while op!='1' and op!='2' and op!='3' and op!='4' and op!='5' and op!='6':
        op=input('==>')
    if op=='1':
        pc=only_prices[0]
    elif op=='2':
        pc=only_prices[1]
    elif op=='3':            #Llamar a la funcion para mostrar los productos y pasar como parametro el precio escogido
        pc=only_prices[2]
    elif op=='4':
        pc=only_prices[3]
    elif op=='5':
        pc=only_prices[4]
    elif op=='6':
        pc=only_prices[5]
    
    search_product(pc)

#----------------------------------------------------------------------------------
#MODULO 5. VENTA DEL RESTAURANTE
          
def num_perfect(id):
    divisors= []
    for e in range(2,id):
            if id%e==0:
                divisors.append(e)

    sum_divisors= sum(divisors)  #Si la suma de los divisores es igual a la cedula es perfecto(1)
    if sum_divisors==id:
        return 1
    else:
        return 0

def ticket_vip():
    vip=True
    buy=True
    id=input('Ingrese la cedula del cliente a comprar:')        #Se pide los datos
    while not id.isnumeric() or (len(id) <7 or len(id) > 8):
        id=input("Dato inválido, ingrese la cédula del cliente: ")
    tickets=[]
    text=read_txt('Tickets.txt')
    aux=text.split(',')
    aux=text.split('\n')
    for l in aux:
        aux2=l.split('//')
        for word in aux2:
            if word==id:   #Se consigue la cedula para verificar si la entrada es vip
                match=aux2[4]
                age=aux2[2]
                age=int(age)
                match=int(match)
                mont_tickets=aux2[-1]
                mont_tickets=float(mont_tickets)
                tickets.append(l)


    
    if tickets==[]:
        vip=False
        print('NO POSEE UN TICKET VIP')

    if vip==True:
        print('SELECCIONE EL PRODUCTO A COMPRAR')
        list=[]
        info_product=[]
        text=read_txt('RestaurantProducts.txt')
        aux=text.split('//')
        aux=text.split('\n')
        for name_product in aux:
            product=name_product.split('//')
            for s in product:
                if (match-1)==0:
                    rest='Al Bayt Restaurant'
                    if s==rest:
                        list.append(product[1])   #Se agrega el nombre del producto a una lista auxiliar
                        info_product.append(product) #Se agrega la info de dicho producto
                elif (match-1)==1:
                    rest='Lusail Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)   #Se repite lo explicado anteriormente
                elif (match-1)==2:
                    rest='The emir Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
                elif (match-1)==3:
                    rest='Ahmad Bin Ali Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
                elif (match-1)==4:
                    rest='Al Janoub Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
                elif (match-1)==5:
                    rest='Al Thumama Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
                elif (match-1)==6:
                    rest='Education City Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
                elif (match-1)==7:
                    rest='974 Restaurant'
                    if s==rest:
                        list.append(product[1])
                        info_product.append(product)
        
        
        only_products = []
        for item in list:
            if item not in only_products:
                only_products.append(item)
        
        rest_prod_sell=[]
        while buy==True:
            n=1
            print('***PRODUCTOS DISPONIBLES***')
            for p in only_products:
                print(f'{n}-{p}')
                n=n+1
            prod=input('==>')
        
            num_products=len(only_products)
            while int(prod)>num_products:   #Se compara si la opcion escogida esta disponible
                prod=input('Seleccione un numero dentro de el rango disponible:')
            
            prod=int(prod)
            buy_prod=info_product[prod-1]
            typee=buy_prod[4]
            quant=buy_prod[-1]              
            print(f'Unidades Disponibles:{quant}')
            quantity=input('Ingrese la cantidad de productos que desea comprar:')
            while not quantity.isnumeric(): #Validacion
                quantity=input('DATO INVALIDO,DEBE INGRESAR UN NUMERO:')

            if int(quantity)>int(quant):  #La cantidad seleccionada no puede ser mayor a la disponible
                print('No hay suficientes unidades disponibles')
                quantity=input('Ingrese la cantidad de productos que desea comprar:')
            quant=int(quant)
            quantity=int(quantity)
            new_quantity=quant-quantity

            if typee=='alcoholic':
                if age<18: #Se verifica que el cliente tenga edad para las bebidas alcoholicas
                    print('No puede comprar bebidas alcoholicas')   
                    exit=input('Desea seguir comprando:\n1-Si\n2-No\n==>')
        
            
            rest_prod_sell.append(info_product[prod-1])
            
            exit=input('Desea seguir comprando:\n1-Si\n2-No\n==>')
            while exit!='1' and exit!='2':
                exit=input('Desea seguir comprando:\n1-Si\n2-No\n==>')

            if exit=='2':
                buy=False
            

        total=[]
        
        for c in rest_prod_sell:
            print(f'Producto:{c[1]}')
            print(f'Precio:{quantity}X{(float(c[2]))}')  #Imprimir los productos
            price_t=quantity*(float(c[2]))
            print(f'Precio total:{price_t}')
            total.append(price_t)

        sum_total=sum(total)
        id=int(id)
        discount=num_perfect(id)
        discount_product=0
        if discount==1:
            dis=15/100
            price=sum_total*dis
            total=sum_total-price
            discount_product=price
        elif discount==0:
            total=sum_total
        
        print(f'SUBTOTAL:{sum_total}')
        fact=input('Desea realizar la compra:\n1-Si\n2-No\n==>')
        while fact!='1' and fact!='2':
            fact=input('Desea realizar la compra:\n1-Si\n2-No\n==>')

        if fact=='1':
            print('****FACTURA*****')  #Se procede a comprar entonces se imprime la factura
            print(f'CLIENTE: {id}')
            print(f'SUBTOTAL:{sum_total}')
            print(f'DESCUENTO:{discount_product}')
            print(f'MONTO TOTAL PAGADO:{total}')
            mont_client=mont_tickets+total
            monts=[]

            monts.append(str(match)+'//'+str(id)+'//'+str(mont_client))   #Agrego a un txt lo gastado en total por el cliente
            for c in monts:
                register_client=open('VipClients.txt','a')
                register_client.write(c+'\n')
                register_client.close()
                
            clear=read_txt('RestaurantProducts.txt')
            new_text=clear.split('//')
            new_text=clear.split('\n')
            new_inventary=[]  #Crear un nuevo inventario para la reduccion del inventario
            for produ in new_text:
                pr=produ.split('//')
                if pr[0]==rest:
                    for p in rest_prod_sell:
                        if pr[1]==p[1]:
                            pr[-1]=new_quantity
                            new_inventary.append(pr)
                        else:
                            new_inventary.append(pr)
                else:
                    new_inventary.append(pr)


            file='RestaurantProducts.txt'

            dat=open(file,'w')
            dat.write('')
            dat.close()

            product_rest_stadium=[]
            for l in new_inventary:
                if l!=['']:
                    product_rest=Product(l[0],l[1],str(l[2]),l[3],l[4],str(l[5]))
                    show_product=product_rest.show_product()
                    product_rest_stadium.append(show_product)
            
                
            file='RestaurantProducts.txt'
            for prod in product_rest_stadium:
                    data = open(file, "a")  #Se agrega el nuevo inventario
                    data.write(prod+'\n')  #Se escribe en el txt para que los datos siempre esten cargados.
#-----------------------------------------------------------------------------------------------------
#FUNCIONES MODULO 6. Estadisticas

def menu_estadistics():
    menu=input('Seleccione la estadistica que desea revisar:\n1-Promedio de gastos de un partido de los clientes Vip\n2-Partido con mas boletos vendidos\n==>')
    while menu!='1' and menu!='2':
         menu=input('Seleccione la estadistica que desea revisar:\n1-Promedio de gastos de un partido de los clientes Vip\n2-Partido con mas boletos vendidos\n==>')
    return menu


def prom_vip():
    print('Seleccione el número del partido a revisar: ')
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n')
    n=1
    for match in aux:           #Primero se debe ingresar el juego a interes
        print(f'{n}-{match}')
        n=n+1
    selected_match=input('==>')
    game=aux[int(selected_match)-1]
    
    file='VipClients.txt'
    data=read_txt(file)
    text=data.split('//')
    text=data.split('\n')    #Abro el txt de lo gastado por los clientes vip

    clients=[]
    mont=[]
    for t in text:
        aux=t.split('//')
        for a in aux:
            if a==selected_match:
                clients.append(aux[1]) #Agrego los clientes a una lista para determinar la cantidad
                mont.append(float(aux[2]))  #Agrego los montos a una lista para sumar

    if text!=[]:
        divisor=len(clients)
        prom=sum(mont)/divisor
        print(f'El promedio de los gastos de los clientes vip del juego {game} es de {prom}') 
    else:
        print('NO HAY CLIENTES VIP TODAVIA')
    

        
def tickets_match():
    bolet=[]
    m=0
    text=read_txt('Tickets.txt') #Abro el archivo de tickets
    aux=text.split('//')
    aux=text.split('\n')

    for a in aux:
        c=a.split('//')
        if c!=['']:
            bolet.append(c[4])
    
    for n in range(1,49):
        n=str(n)
        max=bolet.count(n)  #Cuento la cantidad de boletos con cada uno de los partidos
        if max>m:
            m=max   #Determino el max porque es el mayor de toda la iteracion
            match=n  #Determino el juego porque es el numero que dio el mayor
    
    text=read_txt('Matches.txt')
    aux=text.split(',')
    aux=text.split('\n')
    game=aux[int(match)-1] #Obtener el partido
    print(f'El partido con mas boletos vendidos fue {game} con {m} boletos vendidos')
  




