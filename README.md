🖥️ Python Keylogger (Educational Project)

📌 Description
This project is a **Python-based keylogger** created for **educational and cybersecurity learning purposes**.  
It captures keyboard inputs and stores them in a log file with timestamps.

⚠️ Important:
This project must be used **only on systems you own or have permission to test.  
Unauthorized use of keyloggers is **illegal and unethical**.

🎯 Purpose
- To understand how keylogging works
- To learn keyboard event handling in Python
- To study logging, timestamps, and file rotation
- Useful for **cybersecurity, digital forensics, and defensive security learning**

🛠️ Technologies Used
- **Python 3**
- `pynput` – to capture keyboard input
- `logging` – for logging keystrokes
- `RotatingFileHandler` – for log file size management
- `colorama` – for colored terminal output

📂 Files
- `keylogger.py` – Main Python script
- `key_log.txt` – Log file where keystrokes are saved (auto-created)

⚙️ Features
- Captures normal keys and special keys (Enter, Space, Tab, Backspace, Esc)
- Adds **timestamps** to each logged event
- Rotates log files automatically (prevents large files)
- Shows a startup banner in terminal
- Graceful stop using **Ctrl + C**

▶️ How It Works
1. The program starts listening for keyboard input
2. Each key press is processed
3. Words and special keys are logged
4. Logs are saved in `key_log.txt`
5. Output is displayed in terminal with colors

🧪 Usage (For Learning Only)
```bash
python keylogger.py

🔐 Ethical Warning

🚫 Do NOT use this tool to:
-Spy on others
-Steal passwords or data
-Monitor systems without permission

✅ Use this tool only for:
-Learning
-Labs
-Cybersecurity projects
-Authorized testing
