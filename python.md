# Tratamento de dados
  - deletar informações inúteis
  - tratar tipos de dados
  - corrigir informações vázias
  - para selecionar uma coluna, usamos []

  - axis = 0 (linha)
  - axis = 1 (coluna)

  - tabela.info() = para ver as informações da  tabela.
  - tabela.desscribe() = descreve as informações da tabela

# Python AutoGUI
  - pyautogui.hotkey("control", "t")
  - pyautogui.write("{texto}")
  - pyautogui.press("enter")
  - pyautogui.click()

  - time.sleep(1)
  - pyautogui.position()
  - print()

  -pyautogui.PAUSE() = pausa em cada codigo

# Pandas
  - tabelas = pd.read_csv(r"caminho") = o r dentro do () é para o python ler exatamente como está escrito
  - tabelas = pd.read_csv(r"caminho", sep=";") = sep para usar separador para compilar a tabela

  - tabela["nome_coluna"].sum()

  - usar sep=";" = propriedade para fazer a separação da tabela baseadoem ;

  - tabela = tabela.drop("unnamed", axis=0) = deletar linha ou coluna e eixo(linha ou coluna)

  - tabela[nome de coluna] = pd.to_numeric(tabela[nome da coluna], errors="coerce") = usamos para tratamento de dados, (coerce é forçar a substituição para um NaN, ou usar o ignor que ignora o dado)
  - para transformar numero em texto, usamos astype(str)

  - dropna() = ele dropa as linhas vazias
  - display(tabela[tabela["nome coluna"].isna()])

# Plotly
  - pip install plotly
  - import plotly.express as px
  - cria-se o grafico e o exibe
  - funções px.line(tabela, eixos x=linha e y=coluna)
  - histfunc="funções de calculo"
  - text_auto=True

  - exemplo
  for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="nota", histfunc="avg", text_auto=True)