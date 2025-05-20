import os
import socket
import subprocess

# System Information
def open_browser():
    """Opens the default web browser."""
    os.system("xdg-open https://www.google.com")

def show_files():
    """Lists files in the current directory."""
    return os.popen("ls -l").read()

def show_current_directory():
    """Shows the current working directory."""
    return os.popen("pwd").read()

def disk_usage():
    """Shows disk usage in human-readable format."""
    return os.popen("df -h").read()

def memory_usage():
    """Displays memory usage."""
    return os.popen("free -h").read()

def cpu_info():
    """Shows CPU information."""
    return os.popen("lscpu").read()

def running_processes():
    """Lists top 20 running processes."""
    return os.popen("ps aux | head -n 20").read()

def network_info():
    """Displays network interfaces and IP addresses."""
    return os.popen("ip a").read()

def system_uptime():
    """Displays system uptime."""
    return os.popen("uptime -p").read()

def hostname_info():
    """Returns the system's hostname."""
    return socket.gethostname()

def current_user():
    """Shows the currently logged-in user."""
    return os.popen("whoami").read()

def kernel_version():
    """Displays Linux kernel version."""
    return os.popen("uname -r").read()

def list_services():
    """Lists systemd services (first 20)."""
    return os.popen("systemctl list-units --type=service --no-pager | head -n 20").read()

# User Management
def add_user(username):
    """Adds a new user to the system."""
    return os.popen(f"sudo useradd {username}").read()

def delete_user(username):
    """Deletes a user from the system."""
    return os.popen(f"sudo userdel {username}").read()

def user_groups(username):
    """Shows the groups a user belongs to."""
    return os.popen(f"groups {username}").read()

# Package Management (Debian-based)
def install_package(package_name):
    """Installs a package via apt."""
    return os.popen(f"sudo apt install -y {package_name}").read()

def remove_package(package_name):
    """Removes a package via apt."""
    return os.popen(f"sudo apt remove -y {package_name}").read()

def update_package_list():
    """Updates package list via apt."""
    return os.popen("sudo apt update").read()

def upgrade_system():
    """Upgrades all installed packages to the latest versions."""
    return os.popen("sudo apt upgrade -y").read()

# System Management
def reboot_system():
    """Reboots the system."""
    return os.popen("sudo reboot").read()

def shutdown_system():
    """Shuts down the system."""
    return os.popen("sudo shutdown now").read()

def check_system_logs():
    """Displays recent system logs."""
    return os.popen("sudo journalctl -n 20").read()

# File Operations
def create_file(filename):
    """Creates a new file."""
    return os.popen(f"touch {filename}").read()

def delete_file(filename):
    """Deletes a file."""
    return os.popen(f"rm {filename}").read()

def copy_file(source, destination):
    """Copies a file."""
    return os.popen(f"cp {source} {destination}").read()

def move_file(source, destination):
    """Moves a file."""
    return os.popen(f"mv {source} {destination}").read()

def view_file_content(filename):
    """Displays the contents of a file."""
    return os.popen(f"cat {filename}").read()

# Process Management
def kill_process(pid):
    """Kills a process by its PID."""
    return os.popen(f"kill {pid}").read()

def start_service(service_name):
    """Starts a service."""
    return os.popen(f"sudo systemctl start {service_name}").read()

def stop_service(service_name):
    """Stops a service."""
    return os.popen(f"sudo systemctl stop {service_name}").read()

# Networking and Connections
def check_open_ports():
    """Checks for open ports on the system."""
    return os.popen("sudo netstat -tuln").read()

def trace_route(host):
    """Traces the route to a specified host."""
    return os.popen(f"traceroute {host}").read()

def show_network_interfaces():
    """Displays network interfaces."""
    return os.popen("ip link show").read()

def configure_static_ip(interface, ip, netmask, gateway):
    """Configures a static IP address."""
    return os.popen(f"sudo ifconfig {interface} {ip} netmask {netmask} up && sudo route add default gw {gateway}").read()

# Disk Management
def list_mounted_filesystems():
    """Lists all mounted filesystems."""
    return os.popen("mount -l").read()

def check_disk_health():
    """Checks the health of the disk using SMART status."""
    return os.popen("sudo smartctl -a /dev/sda").read()

# Archiving & Compression
def create_tar_archive(archive_name, directory):
    """Creates a tar archive."""
    return os.popen(f"tar -cvf {archive_name}.tar {directory}").read()

def extract_tar_archive(archive_name):
    """Extracts a tar archive."""
    return os.popen(f"tar -xvf {archive_name}.tar").read()

def create_zip_archive(archive_name, directory):
    """Creates a zip archive."""
    return os.popen(f"zip -r {archive_name}.zip {directory}").read()

def extract_zip_archive(archive_name):
    """Extracts a zip archive."""
    return os.popen(f"unzip {archive_name}.zip").read()

# Security
def change_file_permissions(filename, permissions):
    """Changes file permissions."""
    return os.popen(f"chmod {permissions} {filename}").read()

def change_file_owner(filename, user, group):
    """Changes file owner and group."""
    return os.popen(f"chown {user}:{group} {filename}").read()

def change_user_password(username, password):
    """Changes the password of a user."""
    return os.popen(f"echo '{username}:{password}' | sudo chpasswd").read()

def add_firewall_rule(rule):
    """Adds a firewall rule using ufw."""
    return os.popen(f"sudo ufw {rule}").read()

# SSH & Security
def enable_ssh():
    """Enables the SSH service."""
    return os.popen("sudo systemctl enable ssh && sudo systemctl start ssh").read()

def disable_ssh():
    """Disables the SSH service."""
    return os.popen("sudo systemctl stop ssh && sudo systemctl disable ssh").read()

def change_ssh_port(port):
    """Changes the SSH port."""
    return os.popen(f"sudo sed -i 's/^#Port 22/Port {port}/' /etc/ssh/sshd_config && sudo systemctl restart ssh").read()

# Time and Date Management
def set_system_time(date_time):
    """Sets the system date and time."""
    return os.popen(f"sudo date {date_time}").read()

def set_timezone(timezone):
    """Sets the system timezone."""
    return os.popen(f"sudo timedatectl set-timezone {timezone}").read()

def show_system_time():
    """Displays the system date and time."""
    return os.popen("date").read()
