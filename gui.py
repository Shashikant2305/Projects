# --- gui.py ---
# CustomTkinter GUI for File Encryption & Decryption Tool

import customtkinter as ctk
from tkinter import messagebox
from logic import encrypt_file, decrypt_file
from utils import browse_file

def launch_app():
    def handle_encrypt():
        path = file_entry.get()
        pwd = password_entry.get()
        if path and pwd:
            encrypt_file(path, pwd)
            messagebox.showinfo("Success", "File encrypted successfully!")
        else:
            messagebox.showwarning("Missing Info", "File path or password is empty.")

    def handle_decrypt():
        path = file_entry.get()
        pwd = password_entry.get()
        if path and pwd:
            success = decrypt_file(path, pwd)
            if success:
                messagebox.showinfo("Success", "File decrypted successfully!")
            else:
                messagebox.showerror("Error", "Invalid password or file is corrupted.")
        else:
            messagebox.showwarning("Missing Info", "File path or password is empty.")

    def toggle_password():
        if password_entry.cget("show") == "*":
            password_entry.configure(show="")
            show_button.configure(text="🙈 Hide")
        else:
            password_entry.configure(show="*")
            show_button.configure(text="👁 Show")

    def toggle_theme():
        ctk.set_appearance_mode(theme_switch.get())

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("🔐 Secure File Encryptor")
    app.geometry("720x380")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="🔐 File Encryption & Decryption Tool", font=("Segoe UI", 20, "bold"))
    title.pack(pady=20)

    drop_frame = ctk.CTkFrame(app, width=450, height=60, corner_radius=12)
    drop_frame.pack(pady=10)

    drag_label = ctk.CTkLabel(drop_frame, text="📁 Click to Browse File", font=("Segoe UI", 14), text_color="#007bff")
    drag_label.place(relx=0.5, rely=0.5, anchor="center")
    drag_label.bind("<Button-1>", lambda e: browse_file(file_entry))

    global file_entry
    file_entry = ctk.CTkComboBox(app, width=500, values=[], state="normal")
    file_entry.pack(pady=10)
    file_entry.set("")

    password_frame = ctk.CTkFrame(app)
    password_frame.pack(pady=10, padx=20)

    global password_entry
    password_entry = ctk.CTkEntry(password_frame, width=400, placeholder_text="Enter password", show="*")
    password_entry.pack(side="left", padx=5)

    global show_button
    show_button = ctk.CTkButton(password_frame, text="👁 Show", width=80, command=toggle_password)
    show_button.pack(side="left")

    action_frame = ctk.CTkFrame(app)
    action_frame.pack(pady=20)

    encrypt_button = ctk.CTkButton(action_frame, text="Encrypt", command=handle_encrypt, width=140)
    encrypt_button.pack(side="left", padx=10)

    decrypt_button = ctk.CTkButton(action_frame, text="Decrypt", command=handle_decrypt, width=140)
    decrypt_button.pack(side="left", padx=10)

    theme_switch = ctk.CTkOptionMenu(app, values=["Light", "Dark"], command=lambda _: toggle_theme())
    theme_switch.set("System")
    theme_switch.pack(pady=10)

    footer = ctk.CTkLabel(app, text="🛡️ Crafted by Shashikant Kesharwani", font=("Segoe UI", 10))
    footer.pack(pady=10)

    app.mainloop()
