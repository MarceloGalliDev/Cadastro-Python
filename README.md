# Cadastro-Python
>> convertendo arquivo .qrc para .py
    - pyside6-rcc icons.qrc - o icons_rc.py

>> convertendo arquivo .ui para .py
    - pyside6-uic cadastro.ui -o ui_main.py

>>List of sheets commands
https://doc.qt.io/qt-6/stylesheet-reference.html#list-of-sub-controls

>> DEBUGGER
    - F5 para iniciar, mas é necessário marcar a linha desejada
    - F10 ele pula linha a linha

>> Gerando EXE
    - pyinstaller.exe --onefile --windowed --icon=icon_main.png main.py

    