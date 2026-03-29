# CSA_project_vidhyarthi-

# Digital Detox Friction Lock

A Python-based productivity tool that helps reduce unconscious browsing by introducing **cognitive friction** before accessing distracting websites.


##  Concept

Instead of blocking websites completely, this project:

* Interrupts automatic behavior
* Forces conscious decision-making
* Reduces impulsive scrolling

---

##  How It Works

1. Distracting websites are blocked using the system hosts file
2. When the user tries to access them, they must complete a challenge
3. If successful, access is granted for a limited time
4. After the timer ends, websites are blocked again

---

##  Features

* 🔒 Website blocking using hosts file
* 🧩 Challenge-based unlocking system
* ⏱️ Timer-based access control
* 🔄 Simulation mode (no admin required)
* 💻 Cross-platform support

---

##  Challenge Types

* Math problems
* Reverse string typing
* Mindfulness statements

---

##  Technologies Used

* Python
* Built-in libraries:

  * os
  * sys
  * time
  * random
  * shutil

---

## How to Run

### Option 1: Full Functionality (Admin Required)

```bash
python your_file_name.py
```

Run as:

* Administrator (Windows)
* sudo (Linux/Mac)

---

### Option 2: Simulation Mode

If admin permissions are not available, the program automatically switches to simulation mode.

---

##  Demo Flow

* Run the program
* Choose `u` to unlock
* Solve challenge
* Get temporary access
* Timer ends → sites blocked again

---

## Limitations

* Requires admin privileges for real blocking
* Can be bypassed manually
* CLI-based interface

---

##  Future Improvements

* GUI (Tkinter / Web App)
* Mobile integration
* Usage tracking dashboard
* AI-based smart challenges

---

##  Inspiration

This project is inspired by the idea that **discipline is not about restriction, but about conscious choice**.

---

## Author

Developed as a productivity-focused Python project to demonstrate real-world problem solving.

---
