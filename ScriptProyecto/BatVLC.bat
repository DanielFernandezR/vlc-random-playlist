@echo off
:menu
echo.
echo Bienvenido a nuestro archivo BAT sobre el proyecto VLC
echo.
echo -----------------------------------------------
echo.
echo    1.- Generar estructura de carpetas y colocar las canciones en dicha carpeta (Se creara en tu escritorio).
echo    2.- Ejecutar las canciones con el programa VLC.
echo.
echo -----------------------------------------------
echo.
set /p opcion="Escribe el numero de una de las opciones propuestas: "

cls
goto %opcion%

:1
CODIGO
goto :mensaje

:2
start C:\"Program Files (x86)"\VideoLAN\VLC\vlc.exe
CODIGO
goto :mensaje

:mensaje
echo Presiona una tecla para continuar
pause > Null
goto menu

