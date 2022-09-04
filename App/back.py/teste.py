from openpyxl import load_workbook as lw
from time import strftime as st

data = int(st('%d'))
metap = lw('metas.xlsx')
mtp = metap.active

def lerDep(cc):
    global dep
    dep = mtp[f'C{cc}'].value

def lerDia(cc):
    global dia
    dia = mtp[f'A{cc}'].value

def lerValor(cc):
    global valor
    valor = mtp[f'D{cc}'].value

cont = 320
for i in range(4, cont + 1):
    lerDia(i)
    if data == dia:
        lerDep(i)
        lerValor(i)
        print(dep)
        
