REM wsl.exe ou VirtualBox nao funciona se os 2 estiverem ativados. Ou um ou outro.
REM https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--hypervisorsettings
REM https://forums.virtualbox.org/viewtopic.php?t=99390

REM para reativar wsl
bcdedit /set hypervisorlaunchtype Auto

REM listar configuracao do hiper-v
bcdedit /enum | findstr -i hypervisorlaunchtype

REM desabilitar hiper-V
bcdedit /set hypervisorlaunchtype off 

REM qualquer mudanca no hiper-V reinicialize
shutdown -s -t 2
