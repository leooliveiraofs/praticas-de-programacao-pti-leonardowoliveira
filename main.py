### Arquivo de inicialização

import locale

from App import App

produtos = []

try:
  locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
except locale.Error:
  locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

app = App()
app.inicializar(produtos)


