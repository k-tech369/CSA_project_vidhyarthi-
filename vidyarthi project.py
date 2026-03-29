import os
import sys
import time
import random
import shutil

# ==========================================
# CONFIGURATION
# ==========================================
DISTRACTING_SITES = [
    "www.instagram.com", "instagram.com",
    "www.facebook.com", "facebook.com",
    "www.twitter.com", "twitter.com",
    "www.reddit.com", "reddit.com"
]

UNLOCK_DURATION = 60  # keep 60 sec for testing (change to 900 later)


# ==========================================
# HOST MANAGER
# ==========================================
class HostManager:
    def __init__(self, sites):
        self.sites = sites
        if sys.platform.startswith('win'):
            self.path = r"C:\Windows\System32\drivers\etc\hosts"
        else:
            self.path = "/etc/hosts"
        self.redirect = "127.0.0.1"
        self.simulation = False  # fallback mode

    def backup(self):
        try:
            shutil.copy(self.path, self.path + ".bak")
        except:
            pass

    def set_lock(self, active=True):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()

            self.backup()

            with open(self.path, 'w') as file:
                cleaned = [
                    line for line in lines
                    if not any(line.strip().endswith(site) for site in self.sites)
                ]

                file.writelines(cleaned)

                if active:
                    for site in self.sites:
                        file.write(f"{self.redirect} {site}\n")
                    print("[🛡️] LOCKED")
                else:
                    print("[🔓] UNLOCKED")

            return True

        except PermissionError:
            # 🔥 AUTO SWITCH TO SIMULATION MODE
            self.simulation = True
            if active:
                print("[SIMULATION] Sites would be LOCKED")
            else:
                print("[SIMULATION] Sites would be UNLOCKED")
            return True


# ==========================================
# CHALLENGE SYSTEM
# ==========================================
class FrictionChallenges:

    @staticmethod
    def get_challenge():
        tasks = [
            FrictionChallenges.math_wall,
            FrictionChallenges.reverse_string,
            FrictionChallenges.mindfulness_gate
        ]
        return random.choice(tasks)()

    @staticmethod
    def math_wall():
        a, b, c = random.randint(10, 20), random.randint(2, 10), random.randint(5, 15)
        q = f"({a} * {b}) + {c}"
        return f"Solve: {q}", str((a * b) + c)

    @staticmethod
    def reverse_string():
        word = random.choice(["FOCUS", "DISCIPLINE", "SUCCESS"])
        return f"Type '{word}' backwards:", word[::-1]

    @staticmethod
    def mindfulness_gate():
        text = "I choose focus over distraction"
        return f"Type exactly:\n{text}", text


# ==========================================
# MAIN PROGRAM
# ==========================================
def run_sentinel():
    manager = HostManager(DISTRACTING_SITES)

    print("\n===== DIGITAL DETOX SYSTEM =====")
    print("Initializing system...")

    manager.set_lock(True)  # will auto-switch to simulation if needed

    print("\n✅ System Ready!")
    print("Press 'u' to unlock sites")

    unlock_count = 0

    try:
        while True:
            print("\nOptions: [u] Unlock | [q] Quit")
            choice = input("Enter choice: ").strip().lower()

            if choice == 'q':
                print("Exiting... Stay focused 💪")
                break

            elif choice == 'u':
                prompt, correct = FrictionChallenges.get_challenge()

                print("\nCHALLENGE:")
                print(prompt)

                start = time.time()
                ans = input(">> ").strip()
                end = time.time()

                if ans == correct and (end - start) > 3:
                    unlock_count += 1
                    manager.set_lock(False)

                    print(f"\n✅ Access granted ({UNLOCK_DURATION} sec)")
                    print(f"Unlock count: {unlock_count}")

                    # countdown
                    for i in range(UNLOCK_DURATION, 0, -1):
                        mins, secs = divmod(i, 60)
                        print(f"\rTime left: {mins:02d}:{secs:02d}", end="")
                        time.sleep(1)

                    print("\n⛔ Time up! Locking again...")
                    manager.set_lock(True)

                else:
                    print("❌ Wrong or too fast. Try again.")

            else:
                print("Invalid input")

    except KeyboardInterrupt:
        manager.set_lock(True)
        print("\nEmergency lock activated.")


# ==========================================
# RUN
# ==========================================
if __name__ == "__main__":
    run_sentinel()