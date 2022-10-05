
def quadrante(x,y):
  if x!=0 and y!=0:
    if x>0 and y>0:
      print("Primeiro quadrante")
    elif x<0 and y>0:
      print("Segundo quadrante")
    elif x<0 and y<0:
      print("Terceiro quadrante")
    else:
      print("Quarto quadrante")

quadrante(2,2)
quadrante(3,-2)
quadrante(-8,-1)
quadrante(-7,1)
quadrante(0,2)