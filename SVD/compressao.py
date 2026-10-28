import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Carregar imagem e converter para tons de cinza
img = Image.open("tucano.jpg").convert("L")
A = np.array(img, dtype=float) # Converte a imagem para uma matriz NumPy, onde cada elemento é um pixel com valor de 0 a 255
# imagem vira uma matriz 2D


# 2. Aplicar SVD
# Decompõe a matriz A em três matrizes: U, S e Vt, tal que A = U * S * Vt
# U -> padrões das linhas (matriz m×m)
# S -> valores singulares (importância de cada padrão)
# Vt -> padrões das colunas (matriz n×n)
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# 3. Determinar o K(nesse caso 50%)
m, n = A.shape
k = int((m * n) / (2 * (m + n))) # Calcula o K para 50 por cento 

# 4. Reconstruir imagem aproximada(compressão)
# Mantém apenas os k primeiros valores singulares e suas colunas/linhas correspondentes
# Calcula Ak = U_k * S_k * Vt_k, uma aproximação da imagem original
Ak = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

# 5. Mostrar resultado
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(A, cmap="gray")

plt.subplot(1,2,2)
plt.title(f"Comprimida (k={k})")
plt.imshow(Ak, cmap="gray")
plt.show()