import pydoc
from documentacao_funcao import media

documentacao = pydoc.render_doc(media)
with open('documentacao_media.txt', 'w') as f:
    pydoc.doc(media, output=f)

print("Documentação gerada")    