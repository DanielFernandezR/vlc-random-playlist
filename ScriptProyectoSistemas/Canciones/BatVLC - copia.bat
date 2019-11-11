@echo off
cls
set /p nom="Indica palabra clave de la cancion: "
for /f %%I in ('dir /b "%ruta%"\*.mp3 | find "m_0%numcancion%_*.mp3"') do %vlc% %%I
pause