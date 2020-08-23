# Install and launch

I. The most straightforward way to run the app is follow the next steps:

1). ```pip install -r requirements.txt``` (for Linux: ```pip3 install -r requirements.txt```)

2). In the main project folder execute: ```python main.py``` (for Linux: ```./main.py```)

II. **For Windows users** 

0). Download ```installer.exe```  and ```Pythonic Doom.exe``` https://cloud.mail.ru/public/iqCS/2zsX6Z1ZR,
put them in the root of the project.

1). Execute ```installer.exe``` and follow the installation process.

2). After installation process finished, execute ```Pythonic Doom.exe```.

**Troubleshoting**

2.1. If script fails to run, try to paste the following DLLs next to main
(however, there is already ```libmpg123-0.dll``` in the project, adding this DLL fixed the issue on my PC):
```
libogg-0.dll
libmpg123-0.dll
libvorbis-0.dll
libvorbisfile-3.dll
libtiff-5.dll
libwebp-5.dill
libgcc-5-5jlj1.dll
```

It's about the issue https://github.com/pygame/pygame/issues/1514

"Pyinstaller has a problem with packaging up the pygame project.
You have to copy all the libxxxx.dll (especially "libogg-0.dll") from pygame files and paste them into your "main" file.
This will solve the problem."

2.2. If error "MSVCP140.dll is missing" pops out, please install Microsoft Visual C++ 2015 Redistributable.

3). If you could overcome the issues, ENJOY the game :)



# Game

3D raycasting shooter created after tutorial, kindly provided by Standalone Coder 
(in docs there are some tutorial's screenshots with used algorithms).
Project includes also my comments and further interpretations of the game.

Tutorial source: https://www.youtube.com/watch?v=SmKBsArp2dI&list=PLzuEVvwBnAsZGeSVhOXpnW-ULsGYpNyQe

Controls:

W - move forward

S - move back

A - move left

D - move right

Left mouse button - fire

Left arrow key - look left

Right arrow key - look right

Esc - exit