import os
import socket
import subprocess
import platform

# System Information
def open_browser():
    os.system("start https://www.google.com")

def show_files():
    return os.popen("dir").read()

def list_hidden_files():
    return os.popen("dir /a").read()

def show_current_directory():
    return os.getcwd()

def disk_usage():
    return os.popen("wmic logicaldisk get size,freespace,caption").read()

def memory_usage():
    return os.popen("systeminfo | findstr /C:\"Total Physical Memory\" /C:\"Available Physical Memory\"").read()

def cpu_info():
    return os.popen("wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors").read()

def running_processes():
    return os.popen("tasklist").read()

def network_info():
    return os.popen("ipconfig /all").read()

def ping_google():
    return os.popen("ping -n 4 8.8.8.8").read()

def system_uptime():
    return os.popen("net stats workstation | find \"since\"").read()

def list_users():
    return os.popen("net user").read()

def hostname_info():
    return socket.gethostname()

def current_user():
    return os.popen("whoami").read()

def calendar():
    return os.popen("powershell Get-Date").read()

def show_date():
    return os.popen("date /T && time /T").read()

def kernel_version():
    return platform.version()

def list_services():
    return os.popen("sc query type= service state= all | findstr SERVICE_NAME").read()

# User Management
def add_user(username):
    return os.popen(f'net user {username} /add').read()

def delete_user(username):
    return os.popen(f'net user {username} /delete').read()

def user_groups(username):
    return os.popen(f'net user {username}').read()

# Package Management (simulated for Windows)
def install_package(package_name):
    return f"Installing {package_name} not supported without package manager."

def remove_package(package_name):
    return f"Removing {package_name} not supported without package manager."

def update_package_list():
    return "Update not applicable in native Windows without a package manager."

def upgrade_system():
    return "Upgrade not applicable in native Windows without a package manager."

# System Management
def reboot_system():
    return os.popen("shutdown /r /t 0").read()

def shutdown_system():
    return os.popen("shutdown /s /t 0").read()

def check_system_logs():
    return os.popen("wevtutil qe System /c:20 /f:text").read()

# Disk Management
def list_mounted_filesystems():
    return os.popen("wmic logicaldisk get name").read()

def check_disk_health():
    return os.popen("wmic diskdrive get status").read()

def partition_disk():
    return "Partitioning must be done via Disk Management or diskpart."

# Network Utilities
def check_open_ports():
    return os.popen("netstat -an").read()

def trace_route(host):
    return os.popen(f"tracert {host}").read()

def check_firewall_status():
    return os.popen("netsh advfirewall show allprofiles").read()

def show_connections():
    return os.popen("netstat -ano").read()

# File Operations
def create_file(filename):
    return os.popen(f"type nul > {filename}").read()

def delete_file(filename):
    return os.popen(f"del {filename}").read()

def copy_file(source, destination):
    return os.popen(f"copy {source} {destination}").read()

def move_file(source, destination):
    return os.popen(f"move {source} {destination}").read()

def view_file_content(filename):
    return os.popen(f"type {filename}").read()

# Process Management
def kill_process(pid):
    return os.popen(f"taskkill /PID {pid} /F").read()

def stop_service(service_name):
    return os.popen(f"net stop {service_name}").read()

def start_service(service_name):
    return os.popen(f"net start {service_name}").read()

# System Monitoring & Performance
def top_processes():
    return os.popen("tasklist").read()

def htop_processes():
    return os.popen("tasklist").read()

def iotop():
    return "Windows doesn't have a direct iotop alternative."

def vmstat():
    return "VMStat not available natively on Windows."

def sar():
    return "SAR is not supported on Windows."

def dmesg():
    return "dmesg equivalent not directly accessible in Windows."

# Archiving & Compression
def create_tar_archive(archive_name, directory):
    return f"Use 3rd-party tools like tar.exe or 7-Zip for this on Windows."

def extract_tar_archive(archive_name):
    return f"Use tar or 7-Zip: tar -xvf {archive_name}.tar"

def create_zip_archive(archive_name, directory):
    return os.popen(f'powershell Compress-Archive -Path {directory} -DestinationPath {archive_name}.zip').read()

def extract_zip_archive(archive_name):
    return os.popen(f'powershell Expand-Archive -Path {archive_name}.zip -DestinationPath .').read()

# Security
def change_file_permissions(filename, permissions):
    return f"Use ICACLS or takeown in Windows to change permissions."

def change_file_owner(filename, user, group):
    return f"Use ICACLS /setowner for changing file owner in Windows."

def change_user_password(username, password):
    return os.popen(f'net user {username} {password}').read()

def add_firewall_rule(rule):
    return os.popen(f"netsh advfirewall firewall add rule {rule}").read()

def setup_ssh_key(user):
    return "Use ssh-keygen in Git Bash or WSL."

# File System Management
def create_directory(directory):
    return os.popen(f"mkdir {directory}").read()

def remove_directory(directory):
    return os.popen(f"rmdir {directory}").read()

def remove_directory_force(directory):
    return os.popen(f"rmdir /S /Q {directory}").read()

def copy_directory(source, destination):
    return os.popen(f"xcopy {source} {destination} /E /I").read()

def find_file(filename, directory="."):
    return os.popen(f'dir {directory}\\{filename} /s /b').read()

# Disk and Storage Management
def format_disk(disk_name):
    return "Use diskpart to format drives in Windows."

def mount_disk(disk_name, mount_point):
    return "Use disk management tools to mount drives in Windows."

def unmount_disk(disk_name):
    return "Use 'mountvol /D' for dismounting volumes."

def check_disk_usage():
    return os.popen("dir").read()

def disk_partitioning():
    return os.popen("diskpart /s list").read()

# Networking and Connections
def show_network_interfaces():
    return os.popen("ipconfig").read()

def configure_static_ip(interface, ip, netmask, gateway):
    return f"Use netsh interface ip set address in Windows."

def check_network_route():
    return os.popen("route print").read()

def list_open_ports():
    return os.popen("netstat -an").read()

def check_dns_resolution():
    return os.popen("nslookup google.com").read()

def download_file(url):
    return os.popen(f"powershell Invoke-WebRequest -Uri {url} -OutFile downloaded.file").read()

def upload_file(file, url):
    return "Use curl.exe or external scripts."

# System Monitoring and Resources
def show_memory_info():
    return os.popen("systeminfo | findstr /C:\"Memory\"").read()

def show_swap_info():
    return "Swap memory info not directly available in standard CLI."

def show_cpu_usage():
    return os.popen("wmic cpu get loadpercentage").read()

def show_cpu_temperature():
    return "Requires third-party tools or WMI scripting."

def show_network_statistics():
    return os.popen("netstat -e").read()

def get_process_info(pid):
    return os.popen(f"tasklist /FI \"PID eq {pid}\"").read()

# Process and Task Management
def start_process(command):
    return subprocess.Popen(command, shell=True)

def stop_process_by_pid(pid):
    return os.popen(f"taskkill /PID {pid} /F").read()

def stop_process_by_name(name):
    return os.popen(f"taskkill /IM {name} /F").read()

def get_process_list():
    return os.popen("tasklist").read()

def run_command_in_background(command):
    subprocess.Popen(command, shell=True)
    return "Command started in background."

# User and Group Management
def create_group(group_name):
    return os.popen(f'net localgroup {group_name} /add').read()

def delete_group(group_name):
    return os.popen(f'net localgroup {group_name} /delete').read()

def change_user_group(username, group_name):
    return os.popen(f'net localgroup {group_name} {username} /add').read()

def list_all_groups():
    return os.popen("net localgroup").read()

def user_info(username):
    return os.popen(f'net user {username}').read()

def change_user_shell(username, shell):
    return "Not applicable in Windows."

# Package Management
def check_installed_packages():
    return os.popen("wmic product get name,version").read()

def search_package(package_name):
    return "Not supported without package manager like winget."

def show_package_info(package_name):
    return f"Use winget show {package_name} if available."

# Logs and System Information
def show_system_log():
    return os.popen("wevtutil qe System /c:20 /f:text").read()

def show_dmesg():
    return "No direct dmesg equivalent in Windows."

def check_cpu_temperature():
    return "Requires WMI query or third-party tools."

# Time and Date Management
def set_system_time(date_time):
    return os.popen(f"time {date_time}").read()

def set_timezone(timezone):
    return os.popen(f"tzutil /s \"{timezone}\"").read()

def show_system_time():
    return os.popen("time /T && date /T").read()

# SSH & Security
def enable_ssh():
    return os.popen("powershell Start-Service sshd").read()

def disable_ssh():
    return os.popen("powershell Stop-Service sshd").read()

def setup_firewall_rule(rule):
    return os.popen(f"netsh advfirewall firewall add rule {rule}").read()

def change_ssh_port(port):
    return "Modify sshd_config and restart sshd service."

def check_sudo_privileges(username):
    return f"Use 'net localgroup administrators' to see admin rights."

# Archiving and Compression
def extract_tar_gz(archive_name):
    return "Use tar.exe or 7-Zip to extract .tar.gz"

def extract_tar_bz2(archive_name):
    return "Use tar.exe or 7-Zip to extract .tar.bz2"

def create_zip(archive_name, folder):
    return os.popen(f'powershell Compress-Archive -Path {folder} -DestinationPath {archive_name}.zip').read()

def extract_zip(archive_name):
    return os.popen(f'powershell Expand-Archive -Path {archive_name}.zip -DestinationPath .').read()
