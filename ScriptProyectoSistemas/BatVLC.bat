@echo off
:menu
echo.
echo Bienvenido a nuestro archivo BAT sobre el proyecto VLC
echo.
echo -----------------------------------------------
echo.
echo    1.- Generar estructura de carpetas y colocar las canciones en dicha carpeta (Se creara en tu escritorio).
echo    2.- Elegir una cancion
echo    3.- Iniciar reproduccion aleatoria de todas las canciones
echo    4.- Salir
echo.
echo -----------------------------------------------
echo.
set /p opcion="Escribe el numero de una de las opciones propuestas: "

cls
goto menu%opcion%

:menu1
set /p nombrecarpeta="Escribe el nombre de la carpeta donde se guardaran las canciones: "
set ruta=%userprofile%\Desktop\%nombrecarpeta%
md "%ruta%"
xcopy Canciones\*.mp3 %userprofile%\Desktop\"%nombrecarpeta%"
cls
dir /B "%ruta%"
goto :mensaje

:menu2
echo -----------------------------------------------
echo.
echo Selecciona el genero que quieres escuchar:
echo.
echo 1. Electro
echo 2. Metal
echo 3. Rock
echo 4. Regaetton
echo.
echo -----------------------------------------------
set /p generonum="Escribe el numero de una de las opciones propuestas: "

cls
goto genero%generonum%

:genero1
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "e_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"e_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensaje

:genero2
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "m_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"m_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensaje

:genero3
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "r_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"r_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensaje

:genero4
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "rt_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"rt_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensaje

:menu3
set /p repetir="Quieres repetir la lista indefinidamente (S/N) ? " 
goto %repetir%
:S
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -ZL --qt-start-minimized "%ruta%"\
goto :mensaje
:N
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -Z --qt-start-minimized "%ruta%"\
goto :mensaje

:menu4
exit

:mensaje
echo Presiona una tecla para volver al menu...
pause > Nul
cls
goto menu

