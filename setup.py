from cx_Freeze import setup, Executable
 
base = "Win32GUI"    
 
executables = [Executable("En_decrypt.py", base=base)]
 
packages = ["idna","wx","Crypto"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}
 
setup(
    name = "En_decrypt",
    options = options,
    version = "1.2",
    description = 'Encrypt and Decrypt tool by Danh Tri Hieu - 1711271',
    executables = executables
)