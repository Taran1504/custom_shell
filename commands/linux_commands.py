import os
import subprocess
import platform
import socket

# File Operations
def ls(directory="."):
    if platform.system() == "Windows":
        return os.popen(f"dir {directory}").read()
    return os.popen(f"ls -lh {directory}").read()

def cd(directory):
    os.chdir(directory)
    return f"Changed to {os.getcwd()}"

def pwd():
    return os.getcwd()

def cat(filename):
    if platform.system() == "Windows":
        return os.popen(f"type {filename}").read()
    return os.popen(f"cat {filename}").read()

def grep(pattern, file):
    if platform.system() == "Windows":
        return os.popen(f'findstr "{pattern}" {file}').read()
    return os.popen(f"grep '{pattern}' {file}").read()

def chmod(path, mode):
    if platform.system() == "Windows":
        return "Use 'icacls' or 'attrib' on Windows"
    return os.popen(f"chmod {mode} {path}").read()

def mkdir(directory):
    return os.popen(f"mkdir {directory}").read()

def rm(path):
    if platform.system() == "Windows":
        return os.popen(f"del {path}").read()
    return os.popen(f"rm -r {path}").read()

def cp(source, destination):
    if platform.system() == "Windows":
        return os.popen(f"copy {source} {destination}").read()
    return os.popen(f"cp -r {source} {destination}").read()

def mv(source, destination):
    if platform.system() == "Windows":
        return os.popen(f"move {source} {destination}").read()
    return os.popen(f"mv {source} {destination}").read()

# System Monitoring
def ps():
    if platform.system() == "Windows":
        return os.popen("tasklist").read()
    return os.popen("ps aux").read()

def df():
    if platform.system() == "Windows":
        return os.popen("wmic logicaldisk get size,freespace,caption").read()
    return os.popen("df -h").read()

def free():
    if platform.system() == "Windows":
        return os.popen("wmic OS get FreePhysicalMemory /Value").read()
    return os.popen("free -h").read()

# Networking
def ping(host):
    return os.popen(f"ping {'-c 4' if platform.system() != 'Windows' else ''} {host}").read()

def ifconfig():
    if platform.system() == "Windows":
        return os.popen("ipconfig").read()
    return os.popen("ip a").read()

def netstat():
    if platform.system() == "Windows":
        return os.popen("netstat -ano").read()
    return os.popen("netstat -tulnp").read()

# System Info
def uname():
    if platform.system() == "Windows":
        return platform.uname()._asdict().__str__()
    return os.popen("uname -a").read()

def whoami():
    return os.popen("whoami").read()

# Alias System
aliases = {}

def init_aliases():
    global aliases
    aliases = {
        # Windows compatibility
        'dir': ls,
        'type': cat,
        'copy': cp,
        'move': mv,
        'del': rm,
        'cls': lambda: os.system("cls" if platform.system() == "Windows" else "clear"),
        'ipconfig': ifconfig,
        'tracert': lambda h: os.popen(f"traceroute {h}").read(),
        'tasklist': ps,
        'systeminfo': lambda: uname(),
        
        # Utilities
        'md': mkdir,
        'rd': rm,
        'time': lambda: os.popen("date").read(),
        'ver': lambda: uname(),
        'hostname': lambda: socket.gethostname(),
        'whoami': whoami
    }
