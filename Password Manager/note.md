# 🔐 Basic Encrypted Password Manager

A simple yet powerful command-line password manager built in Python using Fernet encryption.

---

## 🚀 Features

* 🔒 Encrypts passwords using symmetric encryption (Fernet)
* 📂 Stores credentials locally in a file
* 👁️ View stored passwords securely (decrypted on demand)
* ➕ Add new credentials easily
* 🔁 Lightweight and fast CLI-based interaction

---

## 🧠 How It Works

This project uses a generated encryption key stored in `data.key` to:

1. Encrypt passwords before saving
2. Decrypt passwords when viewing

Flow:

```
User Input → Encode → Encrypt → Store
Store → Encode → Decrypt → Decode → Display
```

---


---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.

It is NOT secure for real-world usage because:

* The encryption key is stored locally without protection
* No master password or authentication system exists
* Anyone with file access can retrieve or modify data
* Lacks secure key management and hashing practices

👉 Do NOT use this for storing real passwords.

---

## 🛠️ Setup & Usage

### 1. Install dependency

```bash
pip install cryptography
```

### 2. Run the program

```bash
python main.py
```

### 3. Options

```
add   → Store a new password
view  → View stored passwords
q     → Quit program
```

---

## 💡 Future Improvements

* 🔐 Add master password authentication
* 🧠 Use key derivation (PBKDF2 / Argon2)
* 🗄️ Secure key storage (environment variables / OS keyring)
* 🖥️ Build a GUI or web interface
* 🧹 Add delete & search functionality

---

## 📜 License

This project is licensed under the MIT License.

---
