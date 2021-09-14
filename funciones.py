""" Reto Semana 7
    incorpora al modulo funciones.py
    Jonathan Garizado Toscano
    Universidad de Caldas 
    Junio 22-2021 
    """
#---------------- Zona librerias------------


import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

## Diccionarios Globales

dicc_productos = {}
dicc_venta = {}
dicc_ventas2 = {}
dicc_pro_disponibles = {}

def ingresar_producto():
  """ 
  Parameters
  ----------
  codigo_barras: int
    Recibe los codigos de barra de los productos 
  nombre_producto: str
    Recibe los nombres de los productos
  cantidad: int
    Recibe las cantidades de productos
  precio: float
    Recibe el precio de los productos 
  Return
  -------
    Retorna un diccionario con los parametros ingresados por teclado   
  """
  global dicc_productos
  codigo_barras = int(input('Ingrese el Código de barras: '))
  nombre_producto = input('Ingrese el Nombre del producto: ')
  cantidad = int(input('Ingrese la Cantidad Disponible: '))
  precio = float(input('Ingrese el Valor unitario del producto: '))

  dicc_productos[nombre_producto]=[codigo_barras,cantidad,precio]

  # dicc_productos[nombre_producto]={'Código':codigo_barras, 'Cantidad':cantidad,'Valor':precio}
  
  return dicc_productos

def productos_disponibles():
  """ 
  Parameters
  ----------
  dicc_productos: dict
    Recibe el diccionario creado en la funncion ingresar_producto()
  Return
  -------
    Retorna un diccionario con las cantidades actualizadas   
  """
  global dicc_productos
  for productos in dicc_productos:
    print(
  '''
    Nombre: {}
    Codigo: {}
    Cantidad: {}
    Precio: {}
  '''.format(productos,dicc_productos[productos][0],dicc_productos[productos][1],dicc_productos[productos][2]))

  return dicc_productos

def realizar_venta():
  """ 
  Parameters
  ----------
  compra: int 
    Pide por teclado el codigo de barras del producto a comprar
  cantidad: int
    Pide por teclado la cantidad que el usuario desea comprar
  Return
  -------
  dicc_venta: dict
    Retorna una copia del diccionario (dicc_productos)
  dicc_ventas2: dict
    Retorna un diccionario con nombre y cantidad de productos comprados por el usuario

  """
  global dicc_productos
  global dicc_venta
  global dicc_ventas2
  cantidad_minima = 2
  for llave,valor in dicc_productos.items():
    compra = int(input('Ingrese codigo de barras del producto: '))
    if compra == valor[0]:
      cantidad = int(input('Ingrese la cantidad de productos: '))

      if cantidad > valor[1]:
        print('La cantidad ingresada''(',cantidad,')''Es mayor que la cantidad que tenemos en inventario','(',valor[1],')')

      elif cantidad < valor[0]:
        if valor[0] <= cantidad_minima:
          print('Quedan pocas existencias del producto','(',valor[0],')')
        cantidad_final = valor[1] - cantidad
        valor[1] = cantidad_final
        precio_final = cantidad * valor[2]
        dicc_venta = dicc_productos.copy()
        print('El pago total del',llave,'es:',precio_final)
        dicc_ventas2[llave]=[cantidad]
    
    else:
      print('------------------------')
      print('<<<<Codigo no existe>>>>')
    
  return dicc_venta,dicc_ventas2

def ver_grafica():
  """ 
  Parameters
  ----------
  dicc_ventas2: dict
    Recibe un diccionario con nombre y cantidad de productos comprados por el usuario
  lista_valores: list
    Recibe los nombres (keys) del dicc_productos y los almacena en una lista
  lista_valores: list
    Recibe los valores (values) del dicc_productos y los almacena en una lista
  Returns
  -------
  lista_valores: list
    Retorna una lista con nombre y cantidad de productos vendidos para ser graficados
  """

  global dicc_ventas2

  lista_nombres = []
  lista_valores = []
  for llave in dicc_ventas2.keys():
    lista_nombres.append(llave)
  for valor in dicc_ventas2.values():
    lista_valores.append(valor[0])

  plt.title('Grafica de productos vendidos')
  plt.pie(lista_valores,labels=lista_valores)
  plt.legend(loc="upper left",labels=lista_nombres)
  plt.show()    

def imprimir_archivo():
  """ 
  Parameters
  ----------
  dicc_productos: dict
    Recibe los valores actualizados del diccionario despues de realizar la venta
  dicc_pro_disponibles: dict
    Almacena en un diccionario los prodcutos disponibles despues de la venta 
  Returns
  -------
    Retorna un archivo .txt, con la informacion de los productos y sus cantidades despues de la venta   
  """
  global dicc_pro_disponibles
  global dicc_ventas2
  global dicc_productos
  archivo = open('Productos Disponibles.txt','w')
  for llave,valor in dicc_productos.items():
    dicc_pro_disponibles[llave]={'Codigo':valor[0],'Cantidad':valor[1],'Precio':valor[2]}
  fecha = dt.date.today()
  archivo.write('Fecha=%s'%fecha)
  archivo.write('\n')
  archivo.write('Productos Disponibles=%s'%dicc_pro_disponibles)
  archivo.close()

  archivo = open('Productos Vendidos.txt','w')
  fecha = dt.date.today()
  archivo.write('Fecha=%s'%fecha)
  archivo.write('\n')
  archivo.write('Productos Vendidos=%s'%dicc_ventas2)
  archivo.close()
  print('<<<<<<<Archivos Listos>>>>>>>')


def dataframe():
  """ 
  Parameters
  ----------
  nombre_productos: list
    Recibe la llave del dicc_productos y la almacena en una lista
  codigo_barras: list
    Recibe los valores del dicc_productos y la almacena en una lista
  cantidades: list
    Recibe los valores del dicc_productos y la almacena en una lista
  precios: list
    Recibe los valores del dicc_productos y la almacena en una lista
  dicc_final: dict
    Recibe las listas y las almacena en un diccionario con sus respectivas llaves
  Returns
  -------
    Retorna el DataFrame del dicc_final 
  """

  nombre_productos = []
  codigo_barras = []
  cantidades = []
  precios = []
  dicc_final = {}

  for llave,valor in dicc_productos.items():
    nombre_productos.append(llave)
    codigo_barras.append(valor[0])
    cantidades.append(valor[1])
    precios.append(valor[2])

    dicc_final['Nombre artículo'] = nombre_productos
    dicc_final['Código de barras'] = codigo_barras
    dicc_final['Cantidades'] = cantidades
    dicc_final['Precio unitario'] = precios
  
  nombre_productos_v = []
  cantidades_v = []
  dicc_productos_vendidos = {}

  for llave2,valor2 in dicc_ventas2.items():
    nombre_productos_v.append(llave2)
    cantidades_v.append(valor2)

    dicc_productos_vendidos['Nombre artículo'] = nombre_productos_v
    dicc_productos_vendidos['Cantidades'] = cantidades_v

  print('\n')
  print('-'*60)
  print('            DataFrame de los productos disponibles')
  print('-'*60)
  dataf = pd.DataFrame(dicc_final)
  print(dataf)
  print('-'*60)
  print('            DataFrame de los productos Vendidos')
  dataf2 = pd.DataFrame(dicc_productos_vendidos)
  print('-'*60)
  print(dataf2)

def menu():
  """ 
  Parameters
  ----------
  opcion: str
    Recibe un caracter para segir una instruccion dentro de un bucle while
  Returns
  -------
  La opcion que el usuario escoja y llama la funcion de acuerdo a unas condicones
  """

  print('-'*50)
  print('Bienvenid@s a tu Tienda de Ropa Favorita')
  print('-'*50)
  print('(1) Para ingresar un nuevo producto') 
  print('(2) Para ver los productos disponibles')
  print('(3) Para relizar una venta')
  print('(4) Para Ver la grafica')
  print('(5) Exportar archivo de Productos Disponibles')
  print('(6) Imprima DataFrame')
  print('(7) Para salir')

  while True:
    try:
      opcion = input('\nIngrese una opcion: ')

      if opcion == '1':
        ingresar_producto()
      elif opcion == '2':
        productos_disponibles()
      elif opcion == '3':
        realizar_venta()
      elif opcion == '4':
        ver_grafica()
      elif opcion == '5':
        imprimir_archivo()
      elif opcion == '6':
        dataframe()
      elif opcion == '7':
        break
        
    except: 
      print('Introduce una opcion correcta: ')


# import matplotlib.pyplot as plt
# import datetime as dt
# import pandas as pd

# ## Diccionarios Globales

# dicc_productos = {}
# dicc_venta = {}
# dicc_ventas2 = {}
# dicc_pro_disponibles = {}

# def ingresar_producto():
#   """ 
#   Parameters
#   ----------
#   codigo_barras: int
#     Recibe los codigos de barra de los productos 
#   nombre_producto: str
#     Recibe los nombres de los productos
#   cantidad: int
#     Recibe las cantidades de productos
#   precio: float
#     Recibe el precio de los productos 
#   Return
#   -------
#     Retorna un diccionario con los parametros ingresados por teclado   
#   """
#   nombre_productos = []
#   codigo_barras = []
#   cantidades = []
#   precios = []


#   cantidad1 = int(input('Cuantos productos desea ingresar: '))

#   for i in range(cantidad1):
#     codigo_barra = int(input('Ingrese el Código de barras: '))
#     nombre_producto = input('Ingrese el Nombre del producto: ')
#     cantidad = int(input('Ingrese la Cantidad Disponible: '))
#     precio = float(input('Ingrese el Valor unitario del producto: '))

  
#     nombre_productos.append(nombre_producto)
#     codigo_barras.append(codigo_barra)
#     cantidades.append(cantidad)
#     precios.append(precio)
    
#     dicc_productos['Nombre artículo'] = nombre_productos
#     dicc_productos['Código de barras'] = codigo_barras
#     dicc_productos['Cantidades'] = cantidades
#     dicc_productos['Precio unitario'] = precios

#   # global dicc_productos
#   # codigo_barras = int(input('Ingrese el Código de barras: '))
#   # nombre_producto = input('Ingrese el Nombre del producto: ')
#   # cantidad = int(input('Ingrese la Cantidad Disponible: '))
#   # precio = float(input('Ingrese el Valor unitario del producto: '))

#   # dicc_productos[nombre_producto]=[codigo_barras,cantidad,precio]

#   # dicc_productos[nombre_producto]={'Código':codigo_barras, 'Cantidad':cantidad,'Valor':precio}
  
#   return dicc_productos

# def productos_disponibles():
#   """ 
#   Parameters
#   ----------
#   dicc_productos: dict
#     Recibe el diccionario creado en la funncion ingresar_producto()
#   Return
#   -------
#     Retorna un diccionario con las cantidades actualizadas   
#   """
#   global dicc_productos

#   tabla = pd.DataFrame(dicc_productos)
#   print(tabla)

#   return dicc_productos

# def realizar_venta():
#   """ 
#   Parameters
#   ----------
#   compra: int 
#     Pide por teclado el codigo de barras del producto a comprar
#   cantidad: int
#     Pide por teclado la cantidad que el usuario desea comprar
#   Return
#   -------
#   dicc_venta: dict
#     Retorna una copia del diccionario (dicc_productos)
#   dicc_ventas2: dict
#     Retorna un diccionario con nombre y cantidad de productos comprados por el usuario

#   """
#   global dicc_productos
#   global dicc_venta
#   global dicc_ventas2
#   cantidad_minima = 2
#   for llave,valor in dicc_productos.items():
#     compra = int(input('Ingrese codigo de barras del producto: '))
#     if compra == valor[0]:
#       cantidad = int(input('Ingrese la cantidad de productos: '))

#       if cantidad > valor[1]:
#         print('La cantidad ingresada''(',cantidad,')''Es mayor que la cantidad que tenemos en inventario','(',valor[1],')')

#       elif cantidad < valor[0]:
#         if valor[0] <= cantidad_minima:
#           print('Quedan pocas existencias del producto','(',valor[0],')')
#         cantidad_final = valor[1] - cantidad
#         valor[1] = cantidad_final
#         precio_final = cantidad * valor[2]
#         dicc_venta = dicc_productos.copy()
#         print('El pago total del',llave,'es:',precio_final)
#         dicc_ventas2[llave]=[cantidad]
    
#     else:
#       print('------------------------')
#       print('<<<<Codigo no existe>>>>')
    
#   return dicc_venta,dicc_ventas2

# def ver_grafica():
#   """ 
#   Parameters
#   ----------
#   dicc_ventas2: dict
#     Recibe un diccionario con nombre y cantidad de productos comprados por el usuario
#   lista_valores: list
#     Recibe los nombres (keys) del dicc_productos y los almacena en una lista
#   lista_valores: list
#     Recibe los valores (values) del dicc_productos y los almacena en una lista
#   Returns
#   -------
#   lista_valores: list
#     Retorna una lista con nombre y cantidad de productos vendidos para ser graficados
#   """

#   global dicc_ventas2

#   lista_nombres = []
#   lista_valores = []
#   for llave in dicc_ventas2.keys():
#     lista_nombres.append(llave)
#   for valor in dicc_ventas2.values():
#     lista_valores.append(valor[0])

#   plt.title('Grafica de productos vendidos')
#   plt.pie(lista_valores,labels=lista_valores)
#   plt.legend(loc="upper left",labels=lista_nombres)
#   plt.show()    

# def imprimir_archivo():
#   """ 
#   Parameters
#   ----------
#   dicc_productos: dict
#     Recibe los valores actualizados del diccionario despues de realizar la venta
#   dicc_pro_disponibles: dict
#     Almacena en un diccionario los prodcutos disponibles despues de la venta 
#   Returns
#   -------
#     Retorna un archivo .txt, con la informacion de los productos y sus cantidades despues de la venta   
#   """
#   global dicc_pro_disponibles
#   global dicc_productos
#   archivo = open('Productos Disponibles.txt','w')
#   for llave,valor in dicc_productos.items():
#     dicc_pro_disponibles['Nombre artículo'][llave]={'Codigo':valor[0],'Cantidad':valor[1],'Precio':valor[2]}
#     # dicc_pro_disponibles[llave]={'Codigo':valor[0],'Cantidad':valor[1],'Precio':valor[2]}
#   fecha = dt.date.today()
#   archivo.write('Fecha=%s'%fecha)
#   archivo.write('\n')
#   archivo.write('Productos Disponibles=%s'%dicc_pro_disponibles)
#   archivo.close()
#   print('<<<<<<<Archivo Listo>>>>>>>')
#   print(fecha)

# def dataframe():
#   # dicc_disponibles = {}
#   # for llave,valor in dicc_productos.items():
#   #   dicc_disponibles['Nombre artículo'] = [llave]
#   #   dicc_disponibles['Código de barras'] = [valor[0]]
#   #   dicc_disponibles['Cantidad'] = [valor[1]]
#   #   dicc_disponibles['Precio unitario'] = [valor[2]]

#     tabla = pd.DataFrame(dicc_productos)
#     print(tabla)
# 2
# def menu():
#   """ 
#   Parameters
#   ----------
#   opcion: str
#     Recibe un caracter para segir una instruccion dentro de un bucle while
#   Returns
#   -------
#   La opcion que el usuario escoja y llama la funcion de acuerdo a unas condicones
#   """

#   print('-'*50)
#   print('Bienvenid@s a tu Tienda de Ropa Favorita')
#   print('-'*50)
#   print('(1) Para ingresar un nuevo producto') 
#   print('(2) Para ver los productos disponibles')
#   print('(3) Para relizar una venta')
#   print('(4) Para Ver la grafica')
#   print('(5) Exportar archivo de Productos Disponibles')
#   print('(6) Imprima DataFrame')
#   print('(7) Para salir')

#   while True:
#     try:
#       opcion = input('\nIngrese una opcion: ')

#       if opcion == '1':
#         ingresar_producto()
#       elif opcion == '2':
#         productos_disponibles()
#       elif opcion == '3':
#         realizar_venta()
#       elif opcion == '4':
#         ver_grafica()
#       elif opcion == '5':
#         imprimir_archivo()
#       elif opcion == '6':
#         dataframe()
#       elif opcion == '7':
#         break
        
#     except: 
#       print('Introduce una opcion correcta: ')

