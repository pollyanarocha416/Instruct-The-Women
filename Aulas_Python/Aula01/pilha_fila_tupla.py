#pilha
pilha = [3, 5, 1, 8]
pilha.append(0)
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)

#filas
from collections import deque
fila = deque(["a", "b", "c", "d"])
fila.append("f")
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
