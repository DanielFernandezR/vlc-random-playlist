@echo off
:menu
echo.
echo Bienvenido a nuestro archivo BAT sobre el proyecto VLC
echo.
echo -----------------------------------------------
echo.
echo    1.- Generar estructura de carpetas y colocar las canciones en dicha carpeta (Se creara en tu escritorio).
echo    2.- Musica
echo    3.- Video
echo    4.- Webcam
echo    5.- Salir
echo.
echo -----------------------------------------------
echo.
set /p opcion="Escribe el numero de una de las opciones propuestas: "

cls
goto menuglobal%opcion%

:menuglobal1
set /p nombrecarpeta="Escribe el nombre de la carpeta donde se guardaran las canciones: "
set ruta=%userprofile%\Desktop\%nombrecarpeta%
md "%ruta%"
xcopy Canciones\*.mp3 %userprofile%\Desktop\"%nombrecarpeta%"
xcopy Canciones\*.mp4 %userprofile%\Desktop\"%nombrecarpeta%"
cls
dir /B "%ruta%"
goto :mensaje

:menuglobal2
echo -----------------------------------------------
echo.
echo Selecciona una de las opciones de reproduccion de musica:
echo.
echo    1.- Elegir una cancion
echo    2.- Iniciar reproduccion aleatoria de todas las canciones
echo.
echo -----------------------------------------------
set /p musicanum="Escribe el numero de una de las opciones propuestas: "

cls
goto menumusica%musicanum%

:menumusica1
echo -----------------------------------------------
echo.
echo Selecciona uno de los generos disponibles:
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
goto :mensajemusica

:genero2
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "m_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"m_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensajemusica

:genero3
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "r_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"r_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensajemusica
:genero4
echo.
echo -----------------------------------------------------------------
dir /B "%ruta%"\*.mp3 | find "rt_0"
echo -----------------------------------------------------------------
echo.
set /p numcancion="Elige el numero de la cancion: "
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
for /f %%I in ('dir /b "%ruta%"\"rt_0%numcancion%_*.mp3"') do %vlc% --qt-start-minimized "%ruta%"\%%I
goto :mensajemusica


:menumusica2
set /p repetir="Quieres repetir la lista indefinidamente (S/N) ? " 
goto bucle%repetir%
:bucleS
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -ZL --qt-start-minimized "%ruta%"\
goto :mensajemusica
:bucleN
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -Z --qt-start-minimized "%ruta%"\
goto :mensajemusica

:menuglobal3
echo -----------------------------------------------
echo.
echo Selecciona una de las opciones de reproduccion de video:
echo.
echo    1.- Ejecutar video en pantalla completa
echo    2.- Ejecutar video en videowall
echo    3.- Ejecutar video a partir de un minuto y acabar en otro minuto
echo    4.- Insertar subtitulos a video (Elige el archivo que lo contiene)
echo.
echo -----------------------------------------------
set /p videonum="Escribe el numero de una de las opciones propuestas: "

cls
goto menuvideo%videonum%

:menuvideo1
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% -f "%ruta%"\Video_True_Damage.mp4
goto :mensaje

:menuvideo2
echo -----------------------------------------------
echo.
echo Selecciona una de las opciones de videowall disponibles:
echo.
echo 1. Video 2x2
echo 2. Video 3x3
echo 3. Video 4x4
echo.
echo -----------------------------------------------
set /p wall="Escribe el numero de una de las opciones propuestas: "
echo.
cls
goto videowall%wall%

:videowall1
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% --wall-rows=2 --wall-cols=2 --video-splitter wall --wall-active=0,1,2,3 "%ruta%"\Video_True_Damage.mp4
goto :mensaje

:videowall2
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% --wall-rows=3 --wall-cols=3 --video-splitter wall --wall-active=0,1,2,3,4,5,6,7,8 "%ruta%"\Video_True_Damage.mp4
goto :mensaje

:videowall3
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% --wall-rows=4 --wall-cols=4 --video-splitter wall --wall-active=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 "%ruta%"\Video_True_Damage.mp4
goto :mensaje

:menuvideo3
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
set /p inicio="Elige el segundo en el cual quieres que empiece el video: "
set /p final="Elige el segundo en el cual quieres que acabe el video: "
%vlc% --start-time=%inicio% --stop-time=%final% "%ruta%"\Video_True_Damage.mp4
goto :mensaje

:menuvideo4


:menuglobal4
echo -----------------------------------------------
echo.
echo Selecciona una de las opciones de Webcam:
echo.
echo    1.- Activar Webcam
echo    2.- Activar Webcam en videowall (2x2)
echo.
echo -----------------------------------------------
set /p webcamnum="Escribe el numero de una de las opciones propuestas: "

cls
goto menuwebcam%webcamnum%

:menuwebcam1
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% dshow://
goto :mensaje

:menuwebcam2
set vlc="C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
%vlc% dshow:// --wall-rows=2 --wall-cols=2 --video-splitter wall --wall-active=0,1,2,3
goto :mensaje

:menuglobal5
exit

:mensaje
echo Presiona una tecla para volver al menu...
pause > Nul
cls
goto menu

:mensajemusica
echo La reproduccion de la musica ha terminado, presiona una tecla para continuar...
pause > Nul
cls
goto menu

