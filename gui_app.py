
import tkinter as tk
from tkinter import ttk
import random

class SystemGuardian:
    def __init__(self, root):
        self.root = root
        self.root.title('System Guardian')
        self.root.configure(bg='#2b2b2b')

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames
        self.frame1 = tk.Frame(self.notebook, bg='#2b2b2b')
        self.frame2 = tk.Frame(self.notebook, bg='#2b2b2b')

        # Add frames to notebook
        self.notebook.add(self.frame1, text='Vulnerability Scan')
        self.notebook.add(self.frame2, text='System Information')

        # Create vulnerability scan frame
        self.scan_label = tk.Label(self.frame1, text='Vulnerability Scan', bg='#2b2b2b', fg='white', font=('Arial', 16))
        self.scan_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.frame1, orient='horizontal', length=200, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.scan_button = tk.Button(self.frame1, text='Start Scan', command=self.start_scan, bg='#4b4b4b', fg='white', font=('Arial', 12))
        self.scan_button.pack(pady=10)

        # Create system information frame
        self.info_label = tk.Label(self.frame2, text='System Information', bg='#2b2b2b', fg='white', font=('Arial', 16))
        self.info_label.pack(pady=10)

        self.info_text = tk.Text(self.frame2, width=40, height=10, bg='#4b4b4b', fg='white', font=('Arial', 12))
        self.info_text.pack(pady=10)

        self.info_button = tk.Button(self.frame2, text='Get Information', command=self.get_info, bg='#4b4b4b', fg='white', font=('Arial', 12))
        self.info_button.pack(pady=10)

    def start_scan(self):
        self.progress_bar['value'] = 0
        self.scan_button['state'] = 'disabled'
        self.scan_label['text'] = 'Scanning...'

        for i in range(101):
            self.progress_bar['value'] = i
            self.root.update_idletasks()
            self.root.after(10)

        self.scan_label['text'] = 'Scan Complete'
        self.scan_button['state'] = 'normal'

    def get_info(self):
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert(tk.END, 'System Information:
')
        self.info_text.insert(tk.END, 'Operating System: Windows 10
')
        self.info_text.insert(tk.END, 'Processor: Intel Core i7
')
        self.info_text.insert(tk.END, 'Memory: 16 GB
')
        self.info_text.insert(tk.END, 'Disk Space: 1 TB
')

if __name__ == '__main__':
    root = tk.Tk()
    app = SystemGuardian(root)
    root.mainloop()
