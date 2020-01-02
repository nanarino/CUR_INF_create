import os
import re

CUR_DIR = os.getcwd().split(os.sep)[-1]

ls = list(filter(lambda file: not os.path.isdir(file), os.listdir(os.getcwd())))
ls = list(filter(lambda name:bool(re.findall(r'(^.*\.ani$)|(^.*\.cur$)', name)),ls))[:15]
ls.sort()

Strings_list = ['pointer','help','work','busy','cross','text','hand','unavailiable','vert','horz','dgn1','dgn2','move','alternate','link']
Strings_list = list(map(lambda h,f: h + ' = "' + f + '"\n', Strings_list,ls))

inf_head = r'''[Version]
signature="$CHICAGO$"

[DefaultInstall]
CopyFiles = Scheme.Cur
AddReg    = Scheme.Reg,Wreg

[DestinationDirs]
Scheme.Cur = 10,"%CUR_DIR%"

[Scheme.Reg]
HKCU,"Control Panel\Cursors\Schemes","%SCHEME_NAME%",,"%10%\%CUR_DIR%\%pointer%,%10%\%CUR_DIR%\%help%,%10%\%CUR_DIR%\%work%,%10%\%CUR_DIR%\%busy%,%10%\%CUR_DIR%\%Cross%,%10%\%CUR_DIR%\%Text%,%10%\%CUR_DIR%\%Hand%,%10%\%CUR_DIR%\%Unavailiable%,%10%\%CUR_DIR%\%Vert%,%10%\%CUR_DIR%\%Horz%,%10%\%CUR_DIR%\%Dgn1%,%10%\%CUR_DIR%\%Dgn2%,%10%\%CUR_DIR%\%move%,%10%\%CUR_DIR%\%alternate%,%10%\%CUR_DIR%\%link%"

[Wreg]
HKCU,"Control Panel\Cursors",,0x00020000,"%SCHEME_NAME%"
HKCU,"Control Panel\Cursors",AppStarting,0x00020000,"%10%\%CUR_DIR%\%work%"
HKCU,"Control Panel\Cursors",Arrow,0x00020000,"%10%\%CUR_DIR%\%pointer%"
HKCU,"Control Panel\Cursors",Crosshair,0x00020000,"%10%\%CUR_DIR%\%Cross%"
HKCU,"Control Panel\Cursors",Hand,0x00020000,"%10%\%CUR_DIR%\%link%"
HKCU,"Control Panel\Cursors",Help,0x00020000,"%10%\%CUR_DIR%\%Help%"
HKCU,"Control Panel\Cursors",IBeam,0x00020000,"%10%\%CUR_DIR%\%Text%"
HKCU,"Control Panel\Cursors",No,0x00020000,"%10%\%CUR_DIR%\%Unavailiable%"
HKCU,"Control Panel\Cursors",NWPen,0x00020000,"%10%\%CUR_DIR%\%Hand%"
HKCU,"Control Panel\Cursors",SizeAll,0x00020000,"%10%\%CUR_DIR%\%move%"
HKCU,"Control Panel\Cursors",SizeNESW,0x00020000,"%10%\%CUR_DIR%\%Dgn2%"
HKCU,"Control Panel\Cursors",SizeNS,0x00020000,"%10%\%CUR_DIR%\%Vert%"
HKCU,"Control Panel\Cursors",SizeNWSE,0x00020000,"%10%\%CUR_DIR%\%Dgn1%"
HKCU,"Control Panel\Cursors",SizeWE,0x00020000,"%10%\%CUR_DIR%\%Horz%"
HKCU,"Control Panel\Cursors",UpArrow,0x00020000,"%10%\%CUR_DIR%\%alternate%"
HKCU,"Control Panel\Cursors",Wait,0x00020000,"%10%\%CUR_DIR%\%busy%"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\Runonce\Setup\","",,"rundll32.exe shell32.dll,Control_RunDLL main.cpl @0,1"

'''

with open('Install.inf','w') as inf:
    inf.write(inf_head)
    inf.write('[Scheme.Cur]\n')
    for i in ls:
        inf.write('"' + i + '"\n')
    inf.write('\n')
    inf.write('[Strings]\n')
    inf.write('CUR_DIR = "Cursors\\' + CUR_DIR + '"\n')
    inf.write('SCHEME_NAME = "' + CUR_DIR + '"\n')
    inf.write('SCHEME_DESCRIPTION = "' + CUR_DIR + '"\n')
    inf.writelines(Strings_list)

input("Click on the file Install.inf right mouse button, the shortcut menu to choose - to install")