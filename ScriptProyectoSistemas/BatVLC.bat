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
echo %nombrecarpeta%
set ruta=%userprofile%\Desktop\%nombrecarpeta%
echo %ruta%
md "%ruta%"
xcopy ..\..\proyectovlc\ScriptProyectoSistemas\Canciones\*.mp3 %userprofile%\Desktop\"%nombrecarpeta%"
cls
goto :mensaje

:menu2
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% "%ruta%"\kda_popstars.mp3
goto :mensaje

:menu3
exit

:mensaje
echo Presiona una tecla para continuar
pause > Nul
goto menu

