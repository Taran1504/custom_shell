import os
import subprocess
import platform
import socket

# File Operations
def ls(directory="."):
    """List directory contents with details"""
    return os.popen(f"ls -lh {directory}").read()

def cd(directory):
    """Change current directory"""
    os.chdir(directory)
    return f"Changed to {os.getcwd()}"

def pwd():
    """Print working directory"""
    return os.getcwd()

def cat(filename):
    """Display file contents"""
    return os.popen(f"cat {filename}").read()

def grep(pattern, file):
    """Search for pattern in file"""
    return os.popen(f"grep '{pattern}' {file}").read()

def chmod(path, mode):
    """Change file permissions"""
    return os.popen(f"chmod {mode} {path}").read()

def chown(path, user, group=None):
    """Change file owner"""
    cmd = f"chown {user}"
    if group:
        cmd += f":{group}"
    cmd += f" {path}"
    return os.popen(cmd).read()

def touch(filename):
    """Create empty file or update timestamp"""
    return os.popen(f"touch {filename}").read()

def mkdir(directory):
    """Create new directory"""
    return os.popen(f"mkdir {directory}").read()

def rm(path):
    """Remove files/directories"""
    return os.popen(f"rm -r {path}").read()

def cp(source, destination):
    """Copy files/directories"""
    return os.popen(f"cp -r {source} {destination}").read()

def mv(source, destination):
    """Move/rename files/directories"""
    return os.popen(f"mv {source} {destination}").read()

# System Monitoring
def ps():
    """List running processes"""
    return os.popen("ps aux").read()

def top():
    """Display system processes"""
    return os.popen("top -l 1").read()

def df():
    """Show disk space usage"""
    return os.popen("df -h").read()

def du(path="."):
    """Show directory space usage"""
    return os.popen(f"du -sh {path}").read()

def free():
    """Show memory usage"""
    return os.popen("vm_stat").read()

def uptime():
    """Show system uptime"""
    return os.popen("uptime").read()

# Networking
def ping(host):
    """Ping a network host"""
    return os.popen(f"ping -c 4 {host}").read()

def ifconfig():
    """Show network interfaces"""
    return os.popen("ifconfig").read()

def netstat():
    """Show network statistics"""
    return os.popen("netstat -an").read()

def traceroute(host):
    """Trace network route"""
    return os.popen(f"traceroute {host}").read()

def dig(domain):
    """DNS lookup"""
    return os.popen(f"dig {domain}").read()

# macOS Specific
def brew(command, package=None):
    """Homebrew package manager"""
    cmd = f"brew {command}"
    if package:
        cmd += f" {package}"
    return os.popen(cmd).read()

def open_app(app_name):
    """Open application"""
    return os.popen(f"open -a '{app_name}'").read()

def say(text):
    """Text to speech"""
    return os.popen(f"say '{text}'").read()

# System Info
def uname():
    """System information"""
    return os.popen("uname -a").read()

def sw_vers():
    """macOS version"""
    return os.popen("sw_vers").read()

# Process Management
def kill(pid):
    """Kill process by ID"""
    return os.popen(f"kill {pid}").read()

def killall(process_name):
    """Kill all processes by name"""
    return os.popen(f"killall {process_name}").read()

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
        'cls': lambda: os.system("clear"),
        'ipconfig': ifconfig,
        'tracert': traceroute,
        'tasklist': ps,
        'systeminfo': lambda: uname() + "\n" + sw_vers(),
        
        # Utilities
        'md': mkdir,
        'rd': rm,
        'time': lambda: os.popen("date").read(),
        'ver': sw_vers,
        'hostname': lambda: socket.gethostname(),
        'whoami': lambda: os.popen("whoami").read().strip()
    }
