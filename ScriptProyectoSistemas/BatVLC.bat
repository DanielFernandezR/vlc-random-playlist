@echo off
:menu
echo.
echo Bienvenido a nuestro archivo BAT sobre el proyecto VLC
echo.
echo -----------------------------------------------
echo.
echo    1.- Generar estructura de carpetas y colocar las canciones en dicha carpeta (Se creara en tu escritorio).
echo    2.- Elegir una cancion
echo    3.- Iniciar reproduccion aleatoria de todas las canciones (Repeticion/Bucle lista activado)
echo    4.- Salir
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
dir %ruta%
goto :mensaje

:menu2
echo -----------------------------------------------
echo.
echo     1.- Electro - Betty Boop
echo     2.- Electro - Waiting For Love
echo     3.- Electro - Animals
echo     4.- Electro - Beautiful Now
echo     5.- Electro - Find You
echo     1.- Metal - Hail to the King
echo     2.- Metal - The Sound Of Silence
echo     3.- Metal - Through The Fire and Flames
echo     4.- Metal - One
echo     5.- Metal - Psychosocial
echo     1.- Rock - I Write Sins Not Tragedies
echo     2.- Rock - Thousand Foot Krutch
echo     3.- Rock - My Demons
echo     4.- Rock - So Far Away
echo     5.- Rock - Nightmare
echo     1.- Reggaeton - Runaway
echo     2.- Reggaeton - Date la Vuelta
echo     3.- Reggaeton - Que Tire Pa'lante
echo     4.- Reggaeton - Con Calma
echo     5.- Reggaeton - No me Conoce
echo.
echo -----------------------------------------------
set /p genero="Elige el genero (e, m, r, rt) que quieras escuchar: "
set /p numcancion="Elige el numero de una cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% "%ruta%"\%genero%_0%numcancion%_*.mp3
goto :mensaje

:menu3
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -Z "%ruta%"\
echo Se esta reproduciendo la lista aleatoria...
goto :mensaje

:menu4
exit

:mensaje
echo Presiona una tecla para volver al menu...
pause > Nul
goto menu

