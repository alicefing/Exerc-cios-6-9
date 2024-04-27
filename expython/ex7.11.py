

import pydoc
import modulo

with open("documentacao_meu_modulo.html", "w") as file:
    pydoc.HTMLDoc().docmodule(modulo, file)
    
print("Documentação gerada com sucesso em 'documentacao_meu_modulo.html'.")
