import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Carregar imagem e converter para tons de cinza
img = Image.open("tucano.jpg").convert("L")
A = np.array(img, dtype=float)  # imagem vira uma matriz 2D de pixels (0–255)

# 2. Calcular "SVD" manualmente usando autovalores (np.linalg.eig)
AtA = np.dot(A.T, A)  # Calcula A^T * A (matriz simétrica)

autovalores, V = np.linalg.eig(AtA)  # Autovetores dá a matriz V da SVD e Autovalores dá S^2 -> S = sqrt(autovalores)
idx = np.argsort(autovalores)[::-1]  # ordena decrescente
autovalores = autovalores[idx]
V = V[:, idx]

S = np.sqrt(np.maximum(autovalores, 0))  # valores singulares (reais e positivos)
U = np.dot(A, V) / (S + 1e-10)  # Calcula U = A * V / S

# >>> Converte tudo para números reais (descarta partes imaginárias pequenas)
U = np.real(U)
S = np.real(S)
V = np.real(V)

# 3. Determinar o K (nesse caso 50%)
m, n = A.shape
k = int((m * n) / (2 * (m + n)))  # reduz pela metade o número de pixels

# 4. Reconstruir imagem aproximada (compressão)
Ak = np.dot(U[:, :k], np.dot(np.diag(S[:k]), V[:, :k].T))
Ak = np.real(Ak)  # garante que a imagem seja real

# 5. Mostrar resultado
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(A, cmap="gray")

plt.subplot(1,2,2)
plt.title(f"Comprimida (k={k})")
plt.imshow(Ak, cmap="gray")
plt.show()
