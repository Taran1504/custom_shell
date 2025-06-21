import os
import socket
import subprocess
import platform

# Core Commands
def dir(directory="."):
    """List directory contents"""
    return os.popen(f"dir {directory}").read()

def cd(directory):
    """Change directory"""
    try:
        os.chdir(directory)
        return f"Changed to {os.getcwd()}"
    except Exception as e:
        return f"Error: {str(e)}"

def cls():
    """Clear screen"""
    return os.system("cls")

def type(filename):
    """Show file contents"""
    return os.popen(f"type {filename}").read()

def copy(source, destination):
    """Copy files"""
    return os.popen(f"copy {source} {destination}").read()

def move(source, destination):
    """Move/rename files"""
    return os.popen(f"move {source} {destination}").read()

def del_file(path):
    """Delete files"""
    return os.popen(f"del {path}").read()

def mkdir(directory):
    """Create directory"""
    return os.popen(f"mkdir {directory}").read()

def rmdir(directory):
    """Remove directory"""
    return os.popen(f"rmdir {directory}").read()

def ping(host):
    """Ping network host"""
    return os.popen(f"ping {host}").read()

def ipconfig():
    """Show network info"""
    return os.popen("ipconfig /all").read()

def netstat():
    """Show network stats"""
    return os.popen("netstat -ano").read()

def tasklist():
    """Show running processes"""
    return os.popen("tasklist").read()

def systeminfo():
    """Show system info"""
    return os.popen("systeminfo").read()

# Alias System
aliases = {}

def init_aliases():
    global aliases
    aliases = {
        # File Operations
        'ls': dir,
        'cat': type,
        'rm': del_file,
        'cp': copy,
        'mv': move,
        'pwd': lambda: os.getcwd(),
        'clear': cls,
        'touch': lambda f: open(f, 'a').close() or f"Created {f}",
        
        # System
        'ps': tasklist,
        'top': tasklist,
        'df': lambda: os.popen("wmic logicaldisk get size,freespace,caption").read(),
        'free': lambda: os.popen("wmic OS get FreePhysicalMemory /Value").read(),
        
        # Networking
        'ifconfig': ipconfig,
        'traceroute': lambda h: os.popen(f"tracert {h}").read(),
        
        # Text Processing
        'grep': lambda p, f: os.popen(f'findstr "{p}" {f}').read(),
        'find': lambda p, f: os.popen(f'findstr "{p}" {f}').read(),
        'head': lambda f, n=10: os.popen(f'powershell Get-Content {f} -Head {n}').read(),
        'tail': lambda f, n=10: os.popen(f'powershell Get-Content {f} -Tail {n}').read(),
        
        # Utilities
        'which': lambda c: os.popen(f"where {c}").read(),
        'uname': lambda: platform.system() + " " + platform.release(),
        'date': lambda: os.popen("date /T").read() + " " + os.popen("time /T").read()
    }
