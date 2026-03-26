import tkinter as tk
from tkinter import messagebox
import os
import subprocess   # Better and safer than os.system for running commands

# ====================== MAIN WINDOW ======================
root = tk.Tk()
root.title("CAPITAL POWER SYSTEMS LTD - NETWORK GUI TOOL")
root.geometry("600x400")          # Window size
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Network Information & Ping Tool", 
                       font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# ====================== IP CONFIG SECTION ======================
def run_ipconfig():
    try:
        # Open a new Command Prompt window with ipconfig /all
        os.system('start cmd /k "ipconfig /all && echo. && echo Type "exit" to close this window && echo developed by Anish and Manish"')
        messagebox.showinfo("Success", "IPConfig opened in a new Command Prompt window!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

ip_frame = tk.LabelFrame(root, text="Step 1: Show Network Configuration", padx=10, pady=10)
ip_frame.pack(fill="x", padx=30, pady=10)

tk.Button(ip_frame, text="Open IPConfig /all", font=("Arial", 11), 
          bg="#4CAF50", fg="white", command=run_ipconfig).pack(pady=8)

# ====================== PING SECTION ======================
def run_ping():
    ip = entry_ip.get().strip()
    
    if not ip:
        messagebox.showwarning("Warning", "Please enter an IP address or hostname!")
        return
    
    try:
        # Open a new Command Prompt for ping with the entered IP
        command = f'start cmd /k "ping {ip} -t && echo. && echo Type "exit" when you are done."'
        os.system(command)
        messagebox.showinfo("Ping Started", f"Pinging {ip}...\nA new window has been opened.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start ping:\n{str(e)}")

ping_frame = tk.LabelFrame(root, text="Step 2: Network Latency (Ping Test)", padx=10, pady=10)
ping_frame.pack(fill="x", padx=30, pady=10)

tk.Label(ping_frame, text="Enter IP address or Hostname:", font=("Arial", 10)).pack(anchor="w")

entry_ip = tk.Entry(ping_frame, width=40, font=("Arial", 11))
entry_ip.pack(pady=8)

tk.Button(ping_frame, text="Start Ping Test", font=("Arial", 11), 
          bg="#2196F3", fg="white", command=run_ping).pack(pady=8)

# ====================== YES / NO LOGIC (using Radio Buttons) ======================
def check_choice():
    choice = var.get()
    if choice == "Y":
        messagebox.showinfo("Network Stat Check", "Network Stat Check : Complete ✅")
        # You can also automatically open the ping window if you want
        # run_ping()   # Uncomment this if you want ping to open immediately
    elif choice == "N":
        messagebox.showinfo("Network Stat Check", "Network Stat Check: Denied ❌")
    else:
        messagebox.showwarning("Warning", "Please select Yes or No")

choice_frame = tk.LabelFrame(root, text="Would you like to know network latency (Ping test)?", padx=10, pady=10)
choice_frame.pack(fill="x", padx=30, pady=15)

var = tk.StringVar(value="")   # Empty by default

tk.Radiobutton(choice_frame, text="Yes", variable=var, value="Y", font=("Arial", 11)).pack(anchor="w")
tk.Radiobutton(choice_frame, text="No",  variable=var, value="N", font=("Arial", 11)).pack(anchor="w")

tk.Button(choice_frame, text="Submit Choice", font=("Arial", 11), 
          bg="#FF9800", fg="white", command=check_choice).pack(pady=10)

# ====================== EXIT BUTTON ======================
def close_app():
    if messagebox.askokcancel("Exit", "Do you want to close the Network Tools?"):
        root.destroy()

tk.Button(root, text="Close Application", font=("Arial", 10), 
          bg="#f44336", fg="white", command=close_app).pack(pady=20)

# Start the GUI
root.mainloop()