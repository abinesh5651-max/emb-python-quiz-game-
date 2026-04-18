import tkinter as tk
from tkinter import font as tkfont
import random

# ─────────────────────────────────────────────
#  QUESTION BANK — EMBEDDED PYTHON PROGRAMMING
#  Subject Code: 24EC101201 | Dept: ECE & EEE
# ─────────────────────────────────────────────
QUESTION_BANK = {
    "Unit 1 - Intro to Python": [
        {"q": "Which is true about Python?", "opts": ["Low-level programming language", "Compiled language", "High-level, interpreted language", "Requires explicit variable types"], "ans": 2},
        {"q": "Which command starts Python interpreter in interactive mode?", "opts": ["python3", "start python", "python interactive", "python"], "ans": 3},
        {"q": "What does the Python interpreter do?", "opts": ["Compiles code to machine language", "Converts code to Java", "Executes Python code line by line", "Runs code in parallel"], "ans": 2},
        {"q": "Which is NOT a data type in Python?", "opts": ["int", "float", "char", "string"], "ans": 2},
        {"q": "What is the value of: 3 + 5 * 2?", "opts": ["16", "13", "11", "10"], "ans": 1},
        {"q": "Which data type represents decimal numbers?", "opts": ["int", "string", "float", "boolean"], "ans": 2},
        {"q": "Correct syntax for creating a list in Python?", "opts": ["list = (1,2,3)", "list = [1,2,3]", "list = {1,2,3}", "list = <1,2,3>"], "ans": 1},
        {"q": "Which data type stores True or False in Python?", "opts": ["int", "float", "bool", "string"], "ans": 2},
        {"q": "What is the result of 5 == 5 in Python?", "opts": ["False", "True", "Error", "None"], "ans": 1},
        {"q": "Which operator is used for exponentiation in Python?", "opts": ["*", "**", "^", "%"], "ans": 1},
        {"q": "Correct way to assign value 10 to variable x?", "opts": ["10 = x", "x := 10", "x = 10", "x == 10"], "ans": 2},
        {"q": "What is the output of: print(7 // 2)?", "opts": ["3", "3.5", "4", "2.5"], "ans": 0},
        {"q": "Which operator is used for floor division?", "opts": ["/", "//", "%", "^"], "ans": 1},
        {"q": "Correct syntax to comment a line in Python?", "opts": ["// comment", "# comment", "/* comment */", "-- comment"], "ans": 1},
        {"q": "Which is an example of an expression in Python?", "opts": ["x = 5", "if x == 5:", "2 + 3", "print(x)"], "ans": 2},
    ],
    "Unit 2 - Control Flow & Functions": [
        {"q": "Output of: print(3 + 4 * 2)?", "opts": ["14", "11", "7", "10"], "ans": 1},
        {"q": "Which is a valid variable name in Python?", "opts": ["2var", "_var2", "var-2", "2_var"], "ans": 1},
        {"q": "Keyword used to define a function in Python?", "opts": ["func", "function", "def", "define"], "ans": 2},
        {"q": "Default return value of a function with no return?", "opts": ["None", "0", "False", "Undefined"], "ans": 0},
        {"q": "Operator that checks equality between two values?", "opts": ["==", "=", "===", "!="], "ans": 0},
        {"q": "Output of: x=[1,2,3]; x.append(4); print(x)?", "opts": ["[1,2,3]", "[1,2,3,4]", "Error", "[4,1,2,3]"], "ans": 1},
        {"q": "Keyword used to handle exceptions in Python?", "opts": ["catch", "except", "finally", "error"], "ans": 1},
        {"q": "Result of: len('hello')?", "opts": ["4", "5", "6", "Error"], "ans": 1},
        {"q": "Purpose of the break statement in a loop?", "opts": ["Exit the loop", "Skip current iteration", "Continue next iteration", "None"], "ans": 0},
        {"q": "Operator used to combine two lists in Python?", "opts": ["+", "&", "*", "|"], "ans": 0},
        {"q": "Result of: print('apple' == 'apple')?", "opts": ["True", "False", "Error", "Undefined"], "ans": 0},
        {"q": "Syntax used to create a tuple in Python?", "opts": ["[]", "{}", "()", "None"], "ans": 2},
        {"q": "Correct statement about Python lists?", "opts": ["Lists are immutable", "Lists store only integers", "Lists are ordered", "Lists don't allow duplicates"], "ans": 2},
        {"q": "Valid string slicing operation in Python?", "opts": ["s[1:3]", "s(1,3)", "s{1,3}", "s[3,1]"], "ans": 0},
        {"q": "Python function to get absolute value of a number?", "opts": ["abs()", "round()", "float()", "int()"], "ans": 0},
    ],
    "Unit 3 - Strings & Lists": [
        {"q": "Operator that accesses characters in a string?", "opts": ["Concatenation", "Indexing", "Slicing", "Looping"], "ans": 1},
        {"q": "Output of: s='Python'; print(s[0])?", "opts": ["P", "p", "SyntaxError", "Error"], "ans": 0},
        {"q": "Result of: s='Python'; print(s[1:4])?", "opts": ["Py", "yth", "Pyth", "Python"], "ans": 1},
        {"q": "Which is correct about strings in Python?", "opts": ["Mutable", "Immutable", "Lists", "Not iterable"], "ans": 1},
        {"q": "Output of: s='Python'; print(s[-1])?", "opts": ["P", "n", "y", "SyntaxError"], "ans": 1},
        {"q": "Result of: s1='Hello'; s2='World'; print(s1+' '+s2)?", "opts": ["Hello World", "HelloWorld", "World Hello", "SyntaxError"], "ans": 0},
        {"q": "Function that checks the length of a string?", "opts": ["size()", "length()", "count()", "len()"], "ans": 3},
        {"q": "What does the lower() method do?", "opts": ["Converts to uppercase", "Converts to lowercase", "Removes spaces", "Counts lowercase letters"], "ans": 1},
        {"q": "What does replace() method do in Python?", "opts": ["Changes case", "Replaces a substring", "Slices the string", "Returns reverse"], "ans": 1},
        {"q": "Method that returns a list of characters in a string?", "opts": ["split()", "join()", "list()", "slice()"], "ans": 2},
        {"q": "Operator to check if a substring exists in a string?", "opts": ["in", "exist()", "find()", "search()"], "ans": 0},
        {"q": "Output of: s='Hello'; print(s[1:3])?", "opts": ["el", "ll", "Hello", "lo"], "ans": 0},
        {"q": "Method that adds element to end of a list?", "opts": ["insert()", "append()", "add()", "extend()"], "ans": 1},
        {"q": "Method that removes element by value from a list?", "opts": ["pop()", "remove()", "delete()", "discard()"], "ans": 1},
        {"q": "Which removes and returns the last element of a list?", "opts": ["pop()", "remove()", "del()", "clear()"], "ans": 0},
        {"q": "Correct way to create a list in Python?", "opts": ["list=(1,2,3)", "list=[1,2,3]", "list={1,2,3}", "list=<1,2,3>"], "ans": 1},
    ],
    "Unit 4 - Modules & Libraries": [
        {"q": "Library used for mathematical operations?", "opts": ["numpy", "math", "matplotlib", "scipy"], "ans": 1},
        {"q": "Command to import a module in Python?", "opts": ["import module_name", "include module_name", "load module_name", "from module import *"], "ans": 0},
        {"q": "What is a Python package?", "opts": ["A file with Python code", "A collection of related modules", "A collection of functions", "None of the above"], "ans": 1},
        {"q": "Which file is mandatory in a Python package?", "opts": ["init.py", "setup.py", "module.py", "main.py"], "ans": 0},
        {"q": "Correct way to call a function from a module?", "opts": ["module.function()", "function.module()", "import.function()", "module()"], "ans": 0},
        {"q": "Library used for data visualization?", "opts": ["numpy", "matplotlib", "pandas", "scipy"], "ans": 1},
        {"q": "Purpose of math.sqrt() function?", "opts": ["Calculate square", "Find square root", "Round to integer", "None"], "ans": 1},
        {"q": "Valid way to create a package in Python?", "opts": ["Folder with modules + __init__.py", "Create .pkg file", "Create text file", "None"], "ans": 0},
        {"q": "Library that handles arrays in Python?", "opts": ["scipy", "math", "numpy", "matplotlib"], "ans": 2},
        {"q": "Function to plot a scatter plot in matplotlib?", "opts": ["plt.bar()", "plt.plot()", "plt.scatter()", "plt.hist()"], "ans": 2},
        {"q": "Function to plot a line chart in matplotlib?", "opts": ["plt.bar()", "plt.plot()", "plt.scatter()", "plt.hist()"], "ans": 1},
        {"q": "Library that builds GUIs in Python?", "opts": ["matplotlib", "numpy", "tkinter", "pandas"], "ans": 2},
        {"q": "Method that creates a new window in Tkinter?", "opts": ["Tk()", "Window()", "create_window()", "new_window()"], "ans": 0},
        {"q": "Python library used for scientific computing?", "opts": ["numpy", "pandas", "scipy", "matplotlib"], "ans": 2},
        {"q": "Command to import specific function from a module?", "opts": ["import module_name", "include module_name", "load module_name", "from module import function"], "ans": 3},
    ],
    "Unit 5 - Microcontrollers": [
        {"q": "Which component is the brain of a microcontroller?", "opts": ["Memory", "I/O pins", "CPU", "Clock"], "ans": 2},
        {"q": "Primary function of a microcontroller in embedded system?", "opts": ["Compute and control devices", "Store data permanently", "Communicate with internet", "Increase power consumption"], "ans": 0},
        {"q": "Which component is NOT part of a microcontroller?", "opts": ["RAM", "Flash Memory", "GPU", "Clock"], "ans": 2},
        {"q": "Purpose of timers and counters in a microcontroller?", "opts": ["Store data", "Process commands", "Measure time intervals and create delays", "Convert analog to digital"], "ans": 2},
        {"q": "Which memory stores firmware in a microcontroller?", "opts": ["SRAM", "Flash memory", "EEPROM", "Cache memory"], "ans": 1},
        {"q": "Function of SRAM in a microcontroller?", "opts": ["Permanent program storage", "Temporary data storage during execution", "Increase processing speed", "Control I/O devices"], "ans": 1},
        {"q": "How does higher clock speed affect a microcontroller?", "opts": ["Faster instruction execution", "Increases memory size", "Decreases energy consumption", "Suits only basic tasks"], "ans": 0},
        {"q": "Which is non-volatile memory in a microcontroller?", "opts": ["SRAM", "Flash memory", "Registers", "Cache memory"], "ans": 1},
        {"q": "Language commonly used for microcontrollers?", "opts": ["JavaScript", "Python", "C/C++", "Java"], "ans": 2},
        {"q": "Language used with the Arduino platform?", "opts": ["Python", "C/C++", "Java", "Assembly"], "ans": 1},
        {"q": "What does Assembly language provide?", "opts": ["High-level language", "Low-level control over hardware", "Portability", "Not suitable for embedded"], "ans": 1},
        {"q": "Framework to program microcontrollers in Python?", "opts": ["MicroPython", "Arduino IDE", "React", "TensorFlow"], "ans": 0},
        {"q": "Main advantage of C++ over C in microcontroller programming?", "opts": ["Faster performance", "Object-oriented features", "Simplicity", "Easier to compile"], "ans": 1},
        {"q": "Programming language designed for embedded systems?", "opts": ["HTML", "C", "JavaScript", "Swift"], "ans": 1},
        {"q": "Development board most used by beginners?", "opts": ["Raspberry Pi", "Arduino Uno", "STM32", "BeagleBone Black"], "ans": 1},
    ],
    "Unit 6 - Embedded Systems": [
        {"q": "What is an embedded system?", "opts": ["Computer for general-purpose tasks", "System designed for specific tasks", "Computer that runs desktop apps", "System that cannot interact with hardware"], "ans": 1},
        {"q": "Language commonly used in embedded systems programming?", "opts": ["Python", "C", "JavaScript", "Swift"], "ans": 1},
        {"q": "Which is an example of an embedded system?", "opts": ["Desktop computer", "Washing machine", "Laptop", "Server"], "ans": 1},
        {"q": "Advantage of embedded systems?", "opts": ["High power consumption", "High processing speed", "Low cost and energy efficiency", "Complex design"], "ans": 2},
        {"q": "What does GPIO stand for?", "opts": ["General Purpose Input/Output", "General Protocol Input/Output", "General Power Input/Output", "General Peripheral Input/Output"], "ans": 0},
        {"q": "Primary function of an embedded system?", "opts": ["Run desktop applications", "Perform real-time operations", "Handle web browsing", "Serve as media center"], "ans": 1},
        {"q": "Which is NOT a component of an embedded system?", "opts": ["Microcontroller", "User interface", "Operating system", "Internet browser"], "ans": 3},
        {"q": "Microcontroller used in Raspberry Pi Pico?", "opts": ["ARM Cortex-A72", "ARM Cortex-M0+", "Intel Core i7", "AMD Ryzen"], "ans": 1},
        {"q": "What does 'real-time' mean in embedded systems?", "opts": ["Works only at night", "Processes data without delays", "Processes data after delay", "Doesn't need a processor"], "ans": 1},
        {"q": "Common use case for embedded systems?", "opts": ["Gaming consoles", "Digital cameras", "Washing machines", "All of the above"], "ans": 3},
        {"q": "Main advantage of using Python in embedded systems?", "opts": ["High processing power", "Low-level memory management", "Easy syntax and rapid prototyping", "Hardware independence"], "ans": 2},
        {"q": "Microcontroller compatible with Python for embedded dev?", "opts": ["Raspberry Pi Pico", "Arduino Uno", "ESP32", "All of the above"], "ans": 3},
        {"q": "Which hardware is compatible with MicroPython?", "opts": ["ESP32", "STM32", "Raspberry Pi Pico", "All of the above"], "ans": 3},
        {"q": "Main advantage of MicroPython over C?", "opts": ["It is faster", "Easier syntax and faster development", "Consumes more power", "Requires complex hardware"], "ans": 1},
        {"q": "What does 'REPL' stand for in MicroPython?", "opts": ["Read, Evaluate, Print, Loop", "Run, Execute, Print, Loop", "Read, Execute, Print, List", "Run, Evaluate, Process, Loop"], "ans": 0},
        {"q": "Typical example of a real-time embedded system?", "opts": ["Video streaming service", "Washing machine controller", "Word processor", "Gaming console"], "ans": 1},
    ],
}

# ─────────────────────────────────────────────
#  COLORS & FONTS
# ─────────────────────────────────────────────
BG        = "#0d1117"
CARD      = "#161b22"
BORDER    = "#30363d"
ACCENT    = "#58a6ff"
ACCENT2   = "#7c3aed"
CORRECT   = "#3fb950"
WRONG     = "#f85149"
TEXT      = "#e6edf3"
MUTED     = "#8b949e"
BTN_HOVER = "#1f6feb"
OPT_HOVER = "#1c2128"

KEYS = ["A", "B", "C", "D"]


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Embedded Python Quiz — 24EC101201")
        self.geometry("720x600")
        self.minsize(600, 520)
        self.configure(bg=BG)
        self.resizable(True, True)

        # State
        self.selected_unit = tk.StringVar(value="")
        self.num_questions = tk.IntVar(value=10)
        self.questions     = []
        self.current       = 0
        self.score         = 0
        self.answered      = False
        self.opt_buttons   = []

        self._build_fonts()
        self._show_home()

    # ── FONTS ──────────────────────────────
    def _build_fonts(self):
        self.f_title  = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.f_sub    = tkfont.Font(family="Helvetica", size=11)
        self.f_badge  = tkfont.Font(family="Courier",   size=9,  weight="bold")
        self.f_unit   = tkfont.Font(family="Helvetica", size=11, weight="bold")
        self.f_count  = tkfont.Font(family="Courier",   size=9)
        self.f_q      = tkfont.Font(family="Helvetica", size=13, weight="bold")
        self.f_opt    = tkfont.Font(family="Helvetica", size=11)
        self.f_key    = tkfont.Font(family="Courier",   size=10, weight="bold")
        self.f_btn    = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.f_result = tkfont.Font(family="Helvetica", size=28, weight="bold")
        self.f_pct    = tkfont.Font(family="Courier",   size=14, weight="bold")

    # ── CLEAR WINDOW ───────────────────────
    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    # ── SCROLLABLE CANVAS HELPER ───────────
    def _make_scroll_frame(self, parent):
        canvas = tk.Canvas(parent, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas, bg=BG)
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        return frame

    # ══════════════════════════════════════
    #  HOME / UNIT SELECTION SCREEN
    # ══════════════════════════════════════
    def _show_home(self):
        self._clear()
        self.selected_unit.set("")

        # ── Header ──
        hdr = tk.Frame(self, bg=BG, pady=16)
        hdr.pack(fill="x")
        tk.Label(hdr, text="EMBEDDED PYTHON PROGRAMMING", bg=BG,
                 fg=ACCENT, font=self.f_badge).pack()
        tk.Label(hdr, text="Quiz Game", bg=BG,
                 fg=TEXT, font=self.f_title).pack()
        tk.Label(hdr, text="Subject Code: 24EC101201  ·  Dept: ECE & EEE  ·  I / II Sem",
                 bg=BG, fg=MUTED, font=self.f_count).pack(pady=4)

        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", padx=24)

        # ── Unit label ──
        tk.Label(self, text="Select a Unit to Practice:",
                 bg=BG, fg=TEXT, font=self.f_unit).pack(pady=(14, 6))

        # ── Scrollable unit list ──
        list_frame = tk.Frame(self, bg=BG)
        list_frame.pack(fill="both", expand=True, padx=24)

        units = list(QUESTION_BANK.keys())
        all_label = "🔀  All Units Mixed"

        self._unit_buttons = {}

        def make_unit_btn(label, count_text):
            row = tk.Frame(list_frame, bg=CARD, relief="flat",
                           highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", pady=4)

            inner = tk.Frame(row, bg=CARD, padx=14, pady=10)
            inner.pack(fill="x")

            lbl = tk.Label(inner, text=label, bg=CARD, fg=TEXT,
                           font=self.f_unit, anchor="w")
            lbl.pack(side="left")

            cnt = tk.Label(inner, text=count_text, bg=CARD, fg=MUTED,
                           font=self.f_count, anchor="e")
            cnt.pack(side="right")

            # click selects
            for widget in (row, inner, lbl, cnt):
                widget.bind("<Button-1>", lambda e, l=label, r=row: self._select_unit(l, r))
                widget.bind("<Enter>", lambda e, r=row: r.configure(highlightbackground=ACCENT))
                widget.bind("<Leave>", lambda e, r=row, l=label:
                    r.configure(highlightbackground=ACCENT if self.selected_unit.get()==l else BORDER))

            return row

        for u in units:
            btn = make_unit_btn(u, f"{len(QUESTION_BANK[u])} questions")
            self._unit_buttons[u] = btn

        total = sum(len(v) for v in QUESTION_BANK.values())
        btn_all = make_unit_btn(all_label, f"{total} questions total")
        self._unit_buttons[all_label] = btn_all

        # ── Bottom bar: num questions + start ──
        bottom = tk.Frame(self, bg=BG, pady=14)
        bottom.pack(fill="x", padx=24)

        tk.Label(bottom, text="Number of Questions:", bg=BG,
                 fg=MUTED, font=self.f_badge).pack(side="left")

        self._num_entry = tk.Entry(bottom, textvariable=self.num_questions,
                                   width=5, bg=CARD, fg=TEXT,
                                   insertbackground=TEXT,
                                   font=self.f_unit, relief="flat",
                                   highlightbackground=BORDER,
                                   highlightthickness=1)
        self._num_entry.pack(side="left", padx=10)

        self._max_lbl = tk.Label(bottom, text="/ 15 max", bg=BG,
                                  fg=MUTED, font=self.f_count)
        self._max_lbl.pack(side="left")

        start_btn = tk.Button(bottom, text="Start Quiz  →",
                               bg=ACCENT, fg="#000",
                               font=self.f_btn,
                               relief="flat", padx=20, pady=8,
                               cursor="hand2",
                               command=self._start_quiz)
        start_btn.pack(side="right")
        start_btn.bind("<Enter>", lambda e: start_btn.configure(bg=BTN_HOVER, fg=TEXT))
        start_btn.bind("<Leave>", lambda e: start_btn.configure(bg=ACCENT, fg="#000"))

    def _select_unit(self, label, row):
        # Reset all
        for k, r in self._unit_buttons.items():
            r.configure(highlightbackground=BORDER)
            for w in r.winfo_children():
                for ww in w.winfo_children():
                    ww.configure(bg=CARD)
                w.configure(bg=CARD)
            r.configure(bg=CARD)

        # Highlight selected
        self.selected_unit.set(label)
        row.configure(highlightbackground=ACCENT)

        units = list(QUESTION_BANK.keys())
        all_label = "🔀  All Units Mixed"
        if label == all_label:
            mx = sum(len(v) for v in QUESTION_BANK.values())
        else:
            mx = len(QUESTION_BANK[label])
        self._max_lbl.configure(text=f"/ {mx} max")
        if self.num_questions.get() > mx:
            self.num_questions.set(mx)

    def _start_quiz(self):
        unit = self.selected_unit.get()
        if not unit:
            self._flash("Please select a unit first!")
            return
        try:
            n = int(self._num_entry.get())
        except ValueError:
            self._flash("Enter a valid number!")
            return

        all_label = "🔀  All Units Mixed"
        if unit == all_label:
            pool = [dict(q, unit=u) for u, qs in QUESTION_BANK.items() for q in qs]
        else:
            pool = [dict(q, unit=unit) for q in QUESTION_BANK[unit]]

        n = max(1, min(n, len(pool)))
        self.questions = random.sample(pool, n)
        self.current   = 0
        self.score     = 0
        self._show_quiz()

    def _flash(self, msg):
        top = tk.Toplevel(self)
        top.title("Notice")
        top.configure(bg=CARD)
        top.geometry("300x100")
        top.resizable(False, False)
        tk.Label(top, text=msg, bg=CARD, fg=WRONG,
                 font=self.f_unit, wraplength=260).pack(expand=True)
        tk.Button(top, text="OK", bg=ACCENT, fg="#000",
                  font=self.f_btn, relief="flat", padx=14,
                  command=top.destroy).pack(pady=8)

    # ══════════════════════════════════════
    #  QUIZ SCREEN
    # ══════════════════════════════════════
    def _show_quiz(self):
        self._clear()
        self.answered = False

        total = len(self.questions)
        q     = self.questions[self.current]

        # ── Top bar ──
        top = tk.Frame(self, bg=BG, padx=24, pady=12)
        top.pack(fill="x")

        tk.Label(top, text=f"Question  {self.current+1} / {total}",
                 bg=BG, fg=MUTED, font=self.f_badge).pack(side="left")
        self._score_lbl = tk.Label(top, text=f"Score: {self.score}",
                                    bg=BG, fg=ACCENT, font=self.f_badge)
        self._score_lbl.pack(side="right")

        # ── Progress bar ──
        pbar_bg = tk.Frame(self, bg=BORDER, height=4)
        pbar_bg.pack(fill="x", padx=24)
        pct = int((self.current / total) * 100)
        pbar_fill = tk.Frame(pbar_bg, bg=ACCENT, height=4,
                              width=int(self.winfo_width() * pct / 100))
        pbar_fill.place(x=0, y=0, relwidth=pct/100, height=4)

        # ── Unit tag ──
        tag_frame = tk.Frame(self, bg=BG, padx=24)
        tag_frame.pack(fill="x", pady=(10, 0))
        tk.Label(tag_frame, text=q.get("unit","").upper(),
                 bg=ACCENT2, fg=TEXT,
                 font=self.f_badge, padx=8, pady=3).pack(side="left")

        # ── Question ──
        q_frame = tk.Frame(self, bg=CARD, padx=20, pady=16,
                            highlightbackground=BORDER, highlightthickness=1)
        q_frame.pack(fill="x", padx=24, pady=8)
        tk.Label(q_frame, text=q["q"], bg=CARD, fg=TEXT,
                 font=self.f_q, wraplength=620, justify="left",
                 anchor="w").pack(fill="x")

        # ── Options ──
        self.opt_buttons = []
        opts_frame = tk.Frame(self, bg=BG)
        opts_frame.pack(fill="x", padx=24)

        for i, opt in enumerate(q["opts"]):
            row = tk.Frame(opts_frame, bg=CARD, pady=0,
                           highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", pady=4)

            inner = tk.Frame(row, bg=CARD, padx=12, pady=11)
            inner.pack(fill="x")

            key_lbl = tk.Label(inner, text=KEYS[i], bg=BORDER, fg=ACCENT,
                                font=self.f_key, width=2, pady=2)
            key_lbl.pack(side="left", padx=(0, 12))

            txt_lbl = tk.Label(inner, text=opt, bg=CARD, fg=TEXT,
                                font=self.f_opt, anchor="w", justify="left",
                                wraplength=550)
            txt_lbl.pack(side="left", fill="x", expand=True)

            # Bind click
            for widget in (row, inner, key_lbl, txt_lbl):
                widget.bind("<Button-1>", lambda e, idx=i: self._select_answer(idx))
                widget.bind("<Enter>",    lambda e, r=row, k=key_lbl, t=txt_lbl, ii=inner:
                    self._hover_opt(r, k, t, ii, True))
                widget.bind("<Leave>",    lambda e, r=row, k=key_lbl, t=txt_lbl, ii=inner:
                    self._hover_opt(r, k, t, ii, False))

            self.opt_buttons.append((row, inner, key_lbl, txt_lbl))

        # ── Feedback ──
        self._fb_lbl = tk.Label(self, text="", bg=BG, fg=CORRECT,
                                  font=self.f_sub, pady=6)
        self._fb_lbl.pack(fill="x", padx=28)

        # ── Next button ──
        self._next_btn = tk.Button(self, text="Next Question  →",
                                    bg=ACCENT, fg="#000",
                                    font=self.f_btn,
                                    relief="flat", padx=20, pady=10,
                                    cursor="hand2",
                                    command=self._next_question,
                                    state="disabled")
        self._next_btn.pack(pady=10, padx=24, fill="x")
        self._next_btn.bind("<Enter>", lambda e: self._next_btn.configure(bg=BTN_HOVER, fg=TEXT)
                             if str(self._next_btn["state"]) != "disabled" else None)
        self._next_btn.bind("<Leave>", lambda e: self._next_btn.configure(bg=ACCENT, fg="#000")
                             if str(self._next_btn["state"]) != "disabled" else None)

    def _hover_opt(self, row, key, txt, inner, entering):
        if self.answered:
            return
        c = OPT_HOVER if entering else CARD
        for w in (row, inner, key, txt):
            w.configure(bg=c)
        if entering:
            row.configure(highlightbackground=ACCENT)
        else:
            row.configure(highlightbackground=BORDER)

    def _select_answer(self, chosen):
        if self.answered:
            return
        self.answered = True
        correct = self.questions[self.current]["ans"]

        # Colour all options
        for i, (row, inner, key, txt) in enumerate(self.opt_buttons):
            for w in (row, inner, key, txt):
                w.unbind("<Button-1>")
                w.unbind("<Enter>")
                w.unbind("<Leave>")

            if i == correct:
                bg = "#0d2818"; border = CORRECT; fg_key = CORRECT
            elif i == chosen:
                bg = "#2d0f0e"; border = WRONG;   fg_key = WRONG
            else:
                bg = CARD; border = BORDER; fg_key = MUTED

            row.configure(bg=bg, highlightbackground=border)
            inner.configure(bg=bg)
            key.configure(bg=bg, fg=fg_key)
            txt.configure(bg=bg, fg=TEXT if i != chosen or i == correct else WRONG)

        # Feedback text
        if chosen == correct:
            self.score += 1
            self._score_lbl.configure(text=f"Score: {self.score}")
            self._fb_lbl.configure(text="✅  Correct! Well done!", fg=CORRECT)
        else:
            self._fb_lbl.configure(
                text=f"❌  Wrong! Correct answer: {KEYS[correct]}) {self.questions[self.current]['opts'][correct]}",
                fg=WRONG)

        # Enable next
        total = len(self.questions)
        label = "View Results  →" if self.current + 1 >= total else "Next Question  →"
        self._next_btn.configure(state="normal", text=label)

    def _next_question(self):
        self.current += 1
        if self.current < len(self.questions):
            self._show_quiz()
        else:
            self._show_result()

    # ══════════════════════════════════════
    #  RESULT SCREEN
    # ══════════════════════════════════════
    def _show_result(self):
        self._clear()
        total = len(self.questions)
        pct   = int((self.score / total) * 100)

        # ── Header ──
        tk.Frame(self, bg=BG, height=20).pack()
        tk.Label(self, text="Quiz Complete!", bg=BG, fg=TEXT,
                 font=self.f_title).pack()

        # ── Big percentage ──
        if pct == 100:   color = CORRECT;  emoji = "🌟"
        elif pct >= 80:  color = CORRECT;  emoji = "😊"
        elif pct >= 60:  color = ACCENT;   emoji = "👍"
        elif pct >= 40:  color = "#d29922"; emoji = "📚"
        else:            color = WRONG;    emoji = "💪"

        tk.Label(self, text=f"{emoji}  {pct}%", bg=BG,
                 fg=color, font=self.f_result).pack(pady=16)

        # ── Stats ──
        stats = tk.Frame(self, bg=BG)
        stats.pack(pady=4)

        def stat_box(label, val, col):
            f = tk.Frame(stats, bg=CARD, padx=24, pady=12,
                         highlightbackground=BORDER, highlightthickness=1)
            f.pack(side="left", padx=8)
            tk.Label(f, text=str(val), bg=CARD, fg=col,
                     font=self.f_pct).pack()
            tk.Label(f, text=label, bg=CARD, fg=MUTED,
                     font=self.f_count).pack()

        stat_box("Correct",  self.score,          CORRECT)
        stat_box("Wrong",    total - self.score,  WRONG)
        stat_box("Total",    total,               ACCENT)

        # ── Message ──
        msgs = {
            100: "Perfect! Outstanding performance!",
            80:  "Excellent! You have strong knowledge.",
            60:  "Good job! Review missed questions.",
            40:  "Keep practicing! You're improving.",
            0:   "Don't give up, Abi! Study and retry."
        }
        msg = next(v for k, v in sorted(msgs.items(), reverse=True) if pct >= k)
        tk.Label(self, text=msg, bg=BG, fg=MUTED,
                 font=self.f_sub, pady=8).pack()

        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", padx=24, pady=10)

        # ── Buttons ──
        btn_row = tk.Frame(self, bg=BG)
        btn_row.pack(pady=6, padx=24, fill="x")

        retry_btn = tk.Button(btn_row, text="↺  Retry Same Unit",
                               bg=CARD, fg=TEXT,
                               font=self.f_btn, relief="flat",
                               padx=16, pady=10, cursor="hand2",
                               highlightbackground=BORDER,
                               highlightthickness=1,
                               command=self._retry)
        retry_btn.pack(side="left", expand=True, fill="x", padx=(0, 8))

        home_btn = tk.Button(btn_row, text="← Choose Unit",
                              bg=ACCENT, fg="#000",
                              font=self.f_btn, relief="flat",
                              padx=16, pady=10, cursor="hand2",
                              command=self._show_home)
        home_btn.pack(side="right", expand=True, fill="x")
        home_btn.bind("<Enter>", lambda e: home_btn.configure(bg=BTN_HOVER, fg=TEXT))
        home_btn.bind("<Leave>", lambda e: home_btn.configure(bg=ACCENT, fg="#000"))

    def _retry(self):
        self.current = 0
        self.score   = 0
        random.shuffle(self.questions)
        self._show_quiz()


# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
