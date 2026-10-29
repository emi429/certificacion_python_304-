#realizar un programa que calcule 
#la compra total de 4 productos, si la compra total
#es mayor a 2000 pesos me haga un desecuento
#del 10%
#DATOS DE ENTRADA
precio1=float(input("introduce el precio del producto1"))
precio2=float(input("introduce el precio del producto2"))
precio3=float(input("introduce el precio del producto3"))
precio4=float(input("introduce el precio del producto4"))
#PROCESO
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #total=(3000(3000*.10))total=2700
else:
    print("NO TIENES DESCUENTO")
    print("tu total final:",total)