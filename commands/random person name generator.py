import tkinter as tk
from tkinter import ttk, messagebox
import random
import pyperclip

# Define prefixes and suffixes for each theme
theme_parts = {
    "Fantasy": {
        "prefixes": [
            "Eld",
            "Myth",
            "Aer",
            "Lun",
            "Thal",
            "Vey",
            "Zor",
            "Quin",
            "Sylv",
            "Kael",
            "Drav",
            "Isil",
            "Rava",
            "Elow",
            "Galad",
            "Fen",
            "Alar",
            "Tari",
            "Mor",
            "Shae",
            "Bry",
            "Cyr",
            "Ard",
            "Mal",
            "Nor",
            "Tel",
            "Ith",
            "Oth",
            "Dra",
            "Val",
            "Zyn",
            "Ker",
            "Lor",
            "Syl",
            "Fyn",
            "Ther",
            "Nyx",
            "Ery",
            "Dar",
            "Vyr",
        ],
        "suffixes": [
            "orin",
            "ra",
            "ion",
            "ara",
            "lor",
            "lin",
            "ath",
            "ara",
            "varis",
            "ith",
            "ven",
            "il",
            "ryn",
            "en",
            "dorn",
            "enor",
            "eth",
            "sor",
            "wyn",
            "diel",
            "anor",
            "ithiel",
            "thal",
            "dor",
            "mir",
            "arion",
            "antha",
            "ariel",
            "nor",
            "ellis",
            "thalor",
            "elis",
            "oriel",
            "endis",
            "dris",
            "ithar",
            "vyn",
            "doril",
            "mara",
            "salyn",
        ],
    },
    "Modern": {
        "prefixes": [
            "Ava",
            "Mas",
            "Oliv",
            "Lia",
            "Emm",
            "Noa",
            "Soph",
            "Luc",
            "Ame",
            "Eth",
            "Char",
            "Jam",
            "Ben",
            "Isab",
            "Alex",
            "Sam",
            "Jul",
            "Max",
            "Mad",
            "Gab",
            "Dan",
            "Chris",
            "Jay",
            "Kai",
            "Ell",
            "Jack",
            "Har",
            "Leo",
            "Mia",
            "Zoe",
            "Lay",
            "Eli",
            "Cal",
            "Jos",
            "Evan",
            "Nat",
            "Ash",
            "Tay",
            "Will",
            "Ari",
        ],
        "suffixes": [
            "a",
            "on",
            "ia",
            "m",
            "ah",
            "ah",
            "ia",
            "as",
            "lia",
            "an",
            "lotte",
            "es",
            "jamin",
            "ella",
            "ander",
            "uel",
            "ian",
            "well",
            "eline",
            "riel",
            "iel",
            "ean",
            "den",
            "iah",
            "ise",
            "uel",
            "na",
            "beth",
            "lie",
            "iana",
            "elle",
            "ney",
            "lyn",
            "line",
            "cie",
            "son",
            "anne",
            "ina",
            "iah",
            "yn",
        ],
    },
    "Sci-Fi": {
        "prefixes": [
            "Zyph",
            "Tal",
            "Nov",
            "Xand",
            "Kry",
            "Vel",
            "Axi",
            "Lun",
            "Ori",
            "Stell",
            "Neb",
            "Qua",
            "Vor",
            "Ecli",
            "Sol",
            "Ex",
            "Plu",
            "Hyp",
            "Gal",
            "Ast",
            "Zen",
            "Pho",
            "Cyb",
            "Mech",
            "Nano",
            "Syn",
            "Cry",
            "Neo",
            "Lux",
            "Spect",
            "Rad",
            "Volt",
            "Cos",
            "Holo",
            "Orb",
            "Hel",
            "Thra",
            "Tur",
            "Vex",
            "Nex",
        ],
        "suffixes": [
            "er",
            "on",
            "a",
            "ria",
            "os",
            "ora",
            "on",
            "ex",
            "on",
            "ar",
            "rix",
            "sar",
            "tex",
            "ptix",
            "aris",
            "ial",
            "lar",
            "tor",
            "ax",
            "oid",
            "tron",
            "nium",
            "us",
            "is",
            "is",
            "ion",
            "oid",
            "ium",
            "ara",
            "ix",
            "ara",
            "an",
            "ar",
            "oth",
            "eus",
            "or",
            "yn",
            "ax",
            "eus",
            "ic",
        ],
    },
    "Mythology": {
        "prefixes": [
            "Zeph",
            "Ath",
            "Ap",
            "Ny",
            "Er",
            "Her",
            "Per",
            "Ga",
            "Herm",
            "Art",
            "Dem",
            "Pos",
            "Had",
            "Are",
            "Sel",
            "Dion",
            "Pan",
            "Hel",
            "Ach",
            "Eur",
            "Cly",
            "The",
            "Or",
            "Cri",
            "Aga",
            "Od",
            "Cir",
            "Cal",
            "And",
            "Ant",
            "Iph",
            "Eri",
            "Cha",
            "Phor",
            "Pel",
            "Elect",
            "Orph",
            "Mel",
            "Trit",
            "Psy",
        ],
        "suffixes": [
            "yr",
            "ena",
            "ollo",
            "x",
            "os",
            "a",
            "seus",
            "ia",
            "es",
            "emis",
            "eter",
            "idon",
            "es",
            "es",
            "ene",
            "ysius",
            "ora",
            "ios",
            "illes",
            "ydice",
            "temnestra",
            "sea",
            "pheus",
            "lix",
            "opes",
            "medea",
            "eleia",
            "ope",
            "dite",
            "ippe",
            "theus",
            "ophe",
            "ides",
            "theia",
            "ione",
            "tor",
            "ira",
            "dite",
            "ope",
            "ope",
        ],
    },
    "Nature": {
        "prefixes": [
            "Riv",
            "Will",
            "Sky",
            "Mead",
            "Fli",
            "Ash",
            "Bri",
            "Sto",
            "Oce",
            "Sag",
            "For",
            "Sun",
            "Shad",
            "Lun",
            "Har",
            "Mar",
            "Aut",
            "Spr",
            "Sum",
            "Win",
            "Lea",
            "Gre",
            "Pine",
            "Oak",
            "Wat",
            "Fir",
            "Blu",
            "Se",
            "Fros",
            "Fiel",
            "Bro",
            "Wav",
            "Moun",
            "Val",
            "Clou",
            "Rai",
            "Fog",
            "De",
            "Thi",
            "Crim",
        ],
        "suffixes": [
            "er",
            "ow",
            "e",
            "ow",
            "nt",
            "en",
            "ar",
            "orm",
            "an",
            "e",
            "est",
            "rise",
            "ow",
            "ar",
            "en",
            "in",
            "umn",
            "ing",
            "mer",
            "ter",
            "f",
            "en",
            "cone",
            "tree",
            "er",
            "r",
            "e",
            "a",
            "st",
            "d",
            "ok",
            "e",
            "tain",
            "ley",
            "d",
            "bow",
            "ar",
            "sert",
            "st",
            "son",
        ],
    },
    "Steampunk": {
        "prefixes": [
            "Gear",
            "Cog",
            "Vict",
            "Edi",
            "Ala",
            "Bras",
            "Theo",
            "Clock",
            "Igna",
            "Magn",
            "Steam",
            "Bolt",
            "Rust",
            "Valve",
            "Pipe",
            "Tank",
            "Weld",
            "Gaug",
            "Crank",
            "Grim",
            "Chim",
            "Riv",
            "Nick",
            "Gage",
            "Plumb",
            "Tur",
            "Axle",
            "Hing",
            "Bear",
            "Driv",
            "Mach",
            "Flang",
            "Wren",
            "Bran",
            "Eme",
            "Pump",
            "Belt",
            "Eng",
            "Sprock",
            "Riv",
        ],
        "suffixes": [
            "lock",
            "well",
            "oria",
            "son",
            "ric",
            "swell",
            "dora",
            "wood",
            "tius",
            "nus",
            "er",
            "gear",
            "y",
            "iron",
            "son",
            "plate",
            "an",
            "ar",
            "shaft",
            "rick",
            "ley",
            "en",
            "nickel",
            "bolt",
            "bend",
            "bine",
            "tor",
            "till",
            "hook",
            "der",
            "ick",
            "fork",
            "bolt",
            "mill",
            "ling",
            "nozzle",
            "ance",
            "blade",
            "ion",
            "gear",
        ],
    },
}


class RandomNameGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Name Generator")
        self.root.geometry("500x600")
        self.root.configure(bg="#171717")

        # Title Label
        title_label = tk.Label(
            root,
            text="Random Name Generator",
            font=("Arial", 16, "bold"),
            bg="#171717",
            fg="white",
        )
        title_label.pack(pady=10)

        # Theme Selection
        theme_label = tk.Label(
            root, text="Select a Theme:", font=("Arial", 12), bg="#171717", fg="white"
        )
        theme_label.pack(pady=5)

        self.theme_var = tk.StringVar(value=list(theme_parts.keys())[0])
        theme_dropdown = ttk.Combobox(
            root,
            textvariable=self.theme_var,
            values=list(theme_parts.keys()),
            state="readonly",
        )
        theme_dropdown.pack(pady=5)

        # Name Count Selection
        count_label = tk.Label(
            root, text="Number of Names:", font=("Arial", 12), bg="#171717", fg="white"
        )
        count_label.pack(pady=5)

        self.count_var = tk.IntVar(value=10)
        count_spinbox = tk.Spinbox(
            root,
            from_=1,
            to=20,
            textvariable=self.count_var,
            font=("Arial", 10),
            width=5,
        )
        count_spinbox.pack(pady=5)

        # Generate Button
        generate_button = tk.Button(
            root,
            text="Generate Names",
            command=self.generate_names,
            bg="#00796b",
            fg="white",
            font=("Arial", 12),
            relief="flat",
        )
        generate_button.pack(pady=10)

        # Names Frame
        self.names_frame = tk.Frame(root, bg="#171717")
        self.names_frame.pack(fill="both", expand=True, pady=10)

    def generate_names(self):
        # Clear previous names
        for widget in self.names_frame.winfo_children():
            widget.destroy()

        # Get selected theme and generate names
        selected_theme = self.theme_var.get()
        count = self.count_var.get()
        if selected_theme in theme_parts:
            prefixes = theme_parts[selected_theme]["prefixes"]
            suffixes = theme_parts[selected_theme]["suffixes"]
            names = [
                random.choice(prefixes) + random.choice(suffixes) for _ in range(count)
            ]
        else:
            names = ["No names available"]

        # Display names with copy buttons
        for name in names:
            name_frame = tk.Frame(self.names_frame, bg="#171717")
            name_frame.pack(fill="x", pady=2)

            name_label = tk.Label(
                name_frame, text=name, font=("Arial", 12), bg="#171717", fg="white"
            )
            name_label.pack(side="left", padx=10)

            copy_button = tk.Button(
                name_frame,
                text="Copy",
                command=lambda n=name: self.copy_to_clipboard(n),
                bg="#00796b",
                fg="white",
                font=("Arial", 10),
                relief="flat",
            )
            copy_button.pack(side="right", padx=10)

    def copy_to_clipboard(self, name):
        pyperclip.copy(name)
        messagebox.showinfo("Copied!", f"'{name}' has been copied to the clipboard.")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNameGenerator(root)
    root.mainloop()