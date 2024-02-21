import sys
from cx_Freeze import setup, Executable

# Dependências adicionais que não são módulos do Python
additional_mods = ['numpy.core._methods', 'numpy.lib.format', 'tkinter']

# Executável a ser criado
executables = [Executable("grafico_geral.py", base=None)]

# Opções de configuração
build_exe_options = {
    "packages": ["csv", "collections", "plotly", "pandas", "plotly.graph_objects"],
    "includes": additional_mods,
    "include_files": [("dados.csv", "dados.csv"), ("limpa_dados.py", "limpa_dados.py")],
}

# Configuração do setup
setup(
    name="Gráfico ChatBot",
    version="1.0",
    description="Programa para criar graficos de acesso ao Chatbot",
    options={"build_exe": build_exe_options},
    executables=executables
)
