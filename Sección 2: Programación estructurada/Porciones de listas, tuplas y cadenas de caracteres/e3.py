def meses_faltantes(inicio):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[:inicio]

print("Imprimir los nombres de meses y todos los anteriores: ")
inicio=int(input("Ingrese el numero de mes: "))

mesesfalta=meses_faltantes(inicio)
print(mesesfalta)