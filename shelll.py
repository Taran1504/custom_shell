import tkinter as tk
from tkinter import scrolledtext
import importlib
import subprocess
import os
import sys
import platform
from datetime import datetime

class GUIShellApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform Shell")
        self.root.geometry("800x600")
        self.root.configure(bg='black')

        # Menu Bar
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Terminal Area
        self.shell_area = scrolledtext.ScrolledText(
            root,
            bg="black",
            fg="white",
            insertbackground="lime",
            font=("Consolas", 12),
            wrap=tk.WORD,
            insertwidth=2
        )
        self.shell_area.pack(fill=tk.BOTH, expand=True)
        self.shell_area.bind("<Return>", self.handle_enter)
        self.shell_area.bind("<Up>", self.history_up)
        self.shell_area.bind("<Down>", self.history_down)
        self.shell_area.bind("<Tab>", self.tab_complete)

        # Shell State
        self.os_module = None
        self.awaiting_os_choice = True
        self.command_history = []
        self.history_index = -1
        self.current_dir = os.getcwd()
        self.hostname = platform.node()
        self.username = os.getenv('USERNAME') or os.getenv('USER')
        self.actual_os = platform.system()

        # Configure tags
        self.shell_area.tag_config("output", foreground="white")
        self.shell_area.tag_config("error", foreground="red")
        self.shell_area.tag_config("info", foreground="cyan")
        self.shell_area.tag_config("prompt", foreground="yellow")

        self.display_welcome()
        self.display_prompt()

    def display_welcome(self):
        welcome = f"""Cross-Platform Shell v1.0
Current System: {self.actual_os} {platform.release()}
Python {platform.python_version()}
Type 'help' for available commands\n\n"""
        self.shell_area.insert(tk.END, welcome, "info")

    def display_prompt(self):
        if self.os_module:
            os_name = "Windows" if "windows" in self.os_module.__name__ else (
                "Linux" if "linux" in self.os_module.__name__ else "macOS")
            time = datetime.now().strftime("%H:%M:%S")
            prompt = f"\n[{time}] {self.username}@{self.hostname}:{self.current_dir} [{os_name}]$ "
        else:
            prompt = "\nSelect OS:\n1. Windows\n2. Linux\n3. macOS\n> "
        
        self.shell_area.insert(tk.END, prompt, "prompt")
        self.shell_area.mark_set("insert", tk.END)
        self.shell_area.see(tk.END)

    def handle_enter(self, event):
        content = self.shell_area.get("1.0", tk.END)
        last_prompt_index = max(content.rfind('$ '), content.rfind('> '))
        command = content[last_prompt_index + 2:].strip()

        self.shell_area.insert(tk.END, "\n")
        self.shell_area.see(tk.END)

        if command:
            self.command_history.append(command)
            self.history_index = len(self.command_history)

        if self.awaiting_os_choice:
            self.handle_os_selection(command)
        else:
            self.execute_command(command)

        self.current_dir = os.getcwd()
        self.display_prompt()
        return "break"

    def history_up(self, event):
        if self.command_history and self.history_index > 0:
            self.history_index -= 1
            self.replace_last_command(self.command_history[self.history_index])
        return "break"

    def history_down(self, event):
        if self.command_history and self.history_index < len(self.command_history) - 1:
            self.history_index += 1
            self.replace_last_command(self.command_history[self.history_index])
        elif self.command_history:
            self.history_index = len(self.command_history)
            self.replace_last_command("")
        return "break"

    def tab_complete(self, event):
        content = self.shell_area.get("1.0", tk.END)
        last_prompt_index = max(content.rfind('$ '), content.rfind('> '))
        partial = content[last_prompt_index + 2:].strip()
        
        if not partial:
            return "break"
            
        try:
            dirname, partial_prefix = os.path.split(partial)
            dirname = dirname or '.'
            matches = [f for f in os.listdir(dirname) 
                      if f.startswith(partial_prefix)]
            
            if len(matches) == 1:
                completed = os.path.join(dirname, matches[0])
                if os.path.isdir(completed):
                    completed += '/'
                self.replace_last_command(completed)
            elif len(matches) > 1:
                self.append_output("\n" + "  ".join(matches) + "\n")
        except Exception:
            pass
            
        return "break"

    def replace_last_command(self, new_cmd):
        content = self.shell_area.get("1.0", tk.END)
        last_prompt_index = max(content.rfind('$ '), content.rfind('> '))
        self.shell_area.delete(f"1.{last_prompt_index + 2}", tk.END)
        self.shell_area.insert(tk.END, new_cmd)
        self.shell_area.mark_set("insert", tk.END)

    def handle_os_selection(self, choice):
        os_map = {
            '1': ('windows', 'commands.windows_commands'),
            '2': ('linux', 'commands.linux_commands'),
            '3': ('macos', 'commands.macOS_commands')
        }
        
        if choice in os_map:
            os_name, module_name = os_map[choice]
            try:
                sys.path.append(os.path.dirname(os.path.abspath(__file__)))
                self.os_module = importlib.import_module(module_name)
                
                if hasattr(self.os_module, 'init_aliases'):
                    self.os_module.init_aliases()
                
                self.append_info(f"[INFO] {os_name.capitalize()} commands loaded.")
                self.awaiting_os_choice = False
                self.append_info("[INFO] Type 'help' for available commands.")
                
                if os_name == 'windows':
                    self.hostname = platform.node()
                    self.username = os.getenv('USERNAME')
                else:
                    self.hostname = subprocess.getoutput('hostname').strip()
                    self.username = os.getenv('USER')
                    
            except Exception as e:
                self.append_error(f"[ERROR] Failed to load module: {e}")
        else:
            self.append_error("[ERROR] Invalid OS choice. Please enter 1, 2, or 3.")

    def execute_command(self, cmd):
        if not cmd:
            return

        if cmd.lower() in ['clear', 'cls']:
            self.shell_area.delete('1.0', tk.END)
            return
        elif cmd.lower() == 'exit':
            self.root.quit()
            return

        parts = cmd.split()
        command_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Try aliases first
        if hasattr(self.os_module, 'aliases') and command_name in self.os_module.aliases:
            try:
                result = self.os_module.aliases[command_name](*args) if args else self.os_module.aliases[command_name]()
                self.append_output(str(result))
                return
            except Exception as e:
                self.append_error(f"Alias Error: {str(e)}")
                return

        # Try direct function
        if hasattr(self.os_module, command_name):
            try:
                func = getattr(self.os_module, command_name)
                result = func(*args) if args else func()
                self.append_output(str(result))
                return
            except Exception as e:
                self.append_error(f"Command Error: {str(e)}")
                return

        # Block Linux commands on Windows
        if self.actual_os == "Windows" and ("linux" in str(self.os_module.__name__) or "macos" in str(self.os_module.__name__)):
            self.append_error(f"Cannot execute Linux/macOS command '{command_name}' natively on Windows")
            self.append_info("Available aliases: " + ", ".join(self.os_module.aliases.keys()))
            return

        # System execution
        try:
            shell_exec = "/bin/bash" if self.actual_os != "Windows" else "cmd.exe"
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                executable=shell_exec,
                cwd=self.current_dir
            )
            stdout, stderr = process.communicate()
            
            if stdout: self.append_output(stdout)
            if stderr: self.append_error(stderr)
            
            if command_name == 'cd' and args:
                try:
                    os.chdir(args[0])
                    self.current_dir = os.getcwd()
                except Exception as e:
                    self.append_error(str(e))
                    
        except Exception as e:
            self.append_error(f"Execution Error: {str(e)}")

    def append_output(self, text):
        self.shell_area.insert(tk.END, text, "output")
        self.shell_area.see(tk.END)

    def append_error(self, text):
        self.shell_area.insert(tk.END, text, "error")
        self.shell_area.see(tk.END)

    def append_info(self, text):
        self.shell_area.insert(tk.END, text + "\n", "info")
        self.shell_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIShellApp(root)
    root.mainloop()
