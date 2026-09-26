import numpy as np
# Colecao not _ s y m m e t r i c dos slides
not_symmetric = np.array([2, 3, 3, 9])
total_dinheiro = np.sum(not_symmetric)
media_dinheiro = np.mean(not_symmetric)
print(f"Total arrecadado no fundo comum: R$ {total_dinheiro:.2f}")
print(f"Valor redistribuido igualmente (Media): R$ {media_dinheiro:.2f}")