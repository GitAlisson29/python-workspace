@echo off
setlocal enabledelayedexpansion

:: Solicita o nome do programa
set /p nome_programa=Qual será o nome do programa? 

:: Formata o nome: troca espaços por underline
set nome_formatado=%nome_programa%
set nome_formatado=%nome_formatado: =_%
set nome_formatado=%nome_formatado:"=%

for %%A in ("%nome_formatado%") do set nome_final=%%~nA
set nome_final=!nome_final!.py
set nome_final=!nome_final:_=_!

:: Caminho da pasta Listas
cd /d "E:\python-workspace\Exercícios\Listas"

:: Cria o arquivo .py vazio
type nul > "!nome_final!"

:: Abre o arquivo no Geany
start "" "C:\Program Files\Geany\bin\geany.exe" "!CD!\!nome_final!"

exit
