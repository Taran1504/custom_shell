import tkinter as tk
from tkinter import scrolledtext
import importlib
import subprocess


class GUIShellApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform Shell")
        self.root.geometry("800x500")

        self.shell_area = scrolledtext.ScrolledText(
            root,
            bg="black",
            fg="white",
            insertbackground="white",  # cursor color
            font=("Courier", 12),
            wrap=tk.WORD
        )
        self.shell_area.pack(fill=tk.BOTH, expand=True)
        self.shell_area.bind("<Return>", self.handle_enter)

        self.os_module = None
        self.awaiting_os_choice = True

        self.display_prompt(
            "Select OS:\n1. Windows\n2. Linux\n3. macOS\n> "
        )

    def display_prompt(self, text):
        self.shell_area.insert(tk.END, text)
        self.shell_area.mark_set("insert", tk.END)

    def handle_enter(self, event):
        # Get full content, find the last prompt '>'
        content = self.shell_area.get("1.0", tk.END)
        last_prompt_index = content.rfind('> ')
        command = content[last_prompt_index + 2:].strip()  # Text after '> '

        self.shell_area.insert(tk.END, "\n")  # New line after command
        self.shell_area.see(tk.END)

        if self.awaiting_os_choice:
            self.handle_os_selection(command)
        else:
            self.execute_command(command)

        self.shell_area.insert(tk.END, "\n> ")
        self.shell_area.mark_set("insert", tk.END)  # Keep cursor at the end
        return "break"

    def handle_os_selection(self, choice):
        os_map = {
            "1": ("windows", "commands.windows_commands"),
            "2": ("linux", "commands.linux_commands"),
            "3": ("macos", "commands.macos_commands")
        }
        if choice in os_map:
            os_name, module_path = os_map[choice]
            try:
                self.os_module = importlib.import_module(module_path)
                self.append_info(f"[INFO] {os_name.capitalize()} commands loaded.")
                self.awaiting_os_choice = False
            except Exception as e:
                self.append_error(f"[ERROR] Failed to load module: {e}")
        else:
            self.append_error("[ERROR] Invalid OS choice. Please enter 1, 2, or 3.")

    def execute_command(self, cmd):
        # Try internal Python function from the OS module first
        if self.os_module and hasattr(self.os_module, cmd):
            try:
                result = getattr(self.os_module, cmd)()
                self.append_output(result)
                return
            except Exception as e:
                self.append_error(f"[ERROR] Internal command error: {e}")
                return

        # Otherwise, run as a system shell command
        try:
            shell_exec = self.get_shell_executable()
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                executable=shell_exec
            )
            stdout, stderr = process.communicate()
            if stdout:
                self.append_output(stdout)
            if stderr:
                self.append_error(stderr)
        except Exception as e:
            self.append_error(f"[EXCEPTION] {e}")

    def append_output(self, text):
        self.shell_area.insert(tk.END, text, "output")

    def append_error(self, text):
        self.shell_area.insert(tk.END, text, "error")

    def append_info(self, text):
        self.shell_area.insert(tk.END, text + "\n", "info")

    def get_shell_executable(self):
        if hasattr(self.os_module, "__name__"):
            if "windows" in self.os_module.__name__:
                return "cmd.exe"
            elif "linux" in self.os_module.__name__ or "macos" in self.os_module.__name__:
                return "/bin/bash"
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIShellApp(root)

    # Define tags for coloring
    app.shell_area.tag_config("output", foreground="white")
    app.shell_area.tag_config("error", foreground="red")
    app.shell_area.tag_config("info", foreground="green")

    root.mainloop()
