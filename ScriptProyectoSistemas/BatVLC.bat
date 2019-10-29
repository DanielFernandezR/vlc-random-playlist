@echo off
:menu
echo.
echo Bienvenido a nuestro archivo BAT sobre el proyecto VLC
echo.
echo -----------------------------------------------
echo.
echo    1.- Generar estructura de carpetas y colocar las canciones en dicha carpeta (Se creara en tu escritorio).
echo    2.- Ejecutar las canciones con el programa VLC.
echo    3.- Salir
echo.
echo -----------------------------------------------
echo.
set /p opcion="Escribe el numero de una de las opciones propuestas: "

cls
goto menu%opcion%

:menu1
set /p nombrecarpeta="Escribe el nombre de la carpeta donde se guardaran las canciones: "
set ruta=%userprofile%\Desktop\"%nombrecarpeta%"
md %ruta%
xcopy ..\..\vlc-random-playlist\ScriptProyectoSistemas\Canciones\*.mp3 %userprofile%\Desktop\"%nombrecarpeta%"
cls
dir %ruta%
goto :mensaje

:menu2
"C:\"Program Files (x86)"\VideoLAN\VLC\vlc.exe" %ruta%\
goto :mensaje

:menu3
exit

:mensaje
echo Presiona una tecla para continuar
pause > Null
goto menu

