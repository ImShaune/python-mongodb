def meses_faltantes(numero):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numero: ]

print("Imprimir los nombres de meses que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)