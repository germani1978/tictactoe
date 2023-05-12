combinaciones = [
    # Tres en una fila
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    
    # Tres en una columna
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    
    # Dos diagonales
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

matriz = [
    ["O", "O", "X"],
    ["", "X", "X"],
    ["O", "", "X"],
]

sol = {
   "X":0,
   "O":0
}

#  fila X columna

def validar(mat):
    return len(mat) == 3 and all( len(fila) == 3 and all(elem in {"X","O",""} for elem in fila) for fila in mat )

def analisis(mat):
   if not validar(mat): 
      return "Nulo"
   for line in combinaciones:
      tmp = set()
      for point in line:
         tmp.add( mat[point[0]][point[1]])
      if len(tmp) == 1 and "" not in tmp:
         sol[list(tmp)[0]]+=1
         
   if sol["O"] > sol["X"]:
      return "O"
   elif sol["X"] > sol["O"]:
      return "X"
   else:
      return "Empate"
   
   
print(analisis(matriz))