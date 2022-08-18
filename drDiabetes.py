from sklearn import tree

"""
Grupo: Sirius

Tomás Luchesi Machado - RM: 95157
Lucas Kenji Marotta - RM: 93734
Wellington Almeida - RM: 94373
Bruno dos Santos Reis Curti - RM: 84243
Gabriel José Carquejeiro Ferreira Teixeira - RM: 93506
"""

dicionario = {
    0:"Glicose Normal",
    1:"Glicose Diminuida",
    2:"Diabetes Mellitus",
    3:"???"}

features = [[20,139,68],[99,13,149],[130,109,89],[100,140,120],[125,199,200],[126,222,280],[180,200,200],[0,0,300],[0,300,0],[226,0,0],[0,0,0]]
labels = [0,0,1,1,1,2,2,3,3,3,0]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)

print("\nBem-Vindo ao Dr.Diabetes\n")

gl_jejum = float(input("Qual o valor da glicemia em jejum?(mg/dL) "))
gj_pos = float(input("Qual o valor da glicemia em pos-sobrecarga?(mg/dL) "))
gl_casual = float(input("Qual o valor da glicemia casual?(mg/dL) "))
x = classif.predict([[gl_jejum, gj_pos, gl_casual]])

if int(x) == 3:
    print(f"\nNao foi possivel identificar, aconcelha-se a ir ao hospital mais proximo")
else:
    print(f"\nO seu caso aparenta ser de {dicionario[int(x)]}!\n\nATENCAO!! use esta analise apenas para ter uma ideia geral\nAinda eh necessario a consulta por um medico especialista\n")
