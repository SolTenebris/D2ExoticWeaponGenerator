import random
from tkinter import *

exotic_weapons = [
    "Knucklehead Radar",
    "Celestial Nighthawk",
    "Foetracer",
    "Graviton Forfeit",
    "Wormhusk Crown",
    "Assassin's Cowl",
    "Mask of Bakris",
    "Young Ahamkara's Spine",
    "Mechaneer's Tricksleeves",
    "Aeon Swift",
    "Shinobu's Vow",
    "Sealed Ahamkara Grasps",
    "Shards of Galanor",
    "Oathkeeper",
    "Liar's Handshake",
    "Khepri's Sting",
    "Athry's Embrace",
    "Raiden Flux",
    "Lucky Raspberry",
    "The Dragon Shadow",
    "Ophidia Spathe",
    "The Sixth Coyote",
    "Gwisin Vest",
    "Raiju's Harness",
    "Omnioculus",
    "Lucky Pants",
    "Orpheus Rig",
    "St0mp-EE5",
    "Gemini Jester",
    "Fr0st-EE5",
    "The Bombardiers",
    "Star-Eater Scales",
    "Radiant Dance Machines",
    
]
class d2WeaponPicker(object):
    def __init__(self):
        self.tk = Tk()
        # Window config
        self.tk.title("D2 Exotic Hunter Armor Generator")
        self.tk.geometry("500x224")
        self.tk.resizable(width=False, height=False)
        self.tk.configure(background="#f5cf69")

        # Widget Config
        self.num_label = Label(self.tk, text="Number of Rolls", background="#f5cf69")
        self.num_label.place(x=0, y=0)
        self.num_entry = Entry(self.tk, bd=2, fg="black", width=13, bg ="#4285F4")
        self.num_entry.place(x=4, y=20)
        self.submit = Button(highlightcolor="Purple", text='Randomize', width=9, command=self.exotic_picker, background="#4285F4", foreground="white", activebackground="#689cf2")
        self.submit.place(x=4, y=46)

        # Checkbox Config
        self.is_checked = IntVar()
        self.check_btn = Checkbutton(self.tk, text="Allow Duplicates?", onvalue=1, offvalue=0, variable=self.is_checked,selectcolor="#4285F4", background="#f5cf69", activebackground='#f5cf69')
        self.check_btn.place(x=0, y=200)

        # Text Field Config
        self.text = Text(highlightbackground="Purple",font=('Comis Sans MS',14), width= 25, height=10, background="#4285F4")
        self.text.place(x=204, y=0)        

        self.scroll = Scrollbar(command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.place()


        # Start loop
        self.tk.mainloop()

    def exotic_picker(self):
        # Takes int for how many weapons to randomly select from 
        self.text['state'] = NORMAL
        self.text.delete("1.0", "end")
        weapon_num = self.num_entry.get()
    
        if weapon_num == 'pee pee poo poo':
            self.text.insert(INSERT, 'poo poo pee pee\n')
            return
        if weapon_num == 'sex':
            self.text.insert(INSERT, '69\n')
            return
        if weapon_num == '5318008':
            self.text.insert(INSERT, '（• ㅅ •）\n')
            return 

        if weapon_num == '' or weapon_num == ' ' or weapon_num == '0':
            weapon_num = 1
        else:
            weapon_num = int(weapon_num)
        weapon_len = int(len(exotic_weapons) - 1)
        
        if self.is_checked.get() == 1:
            for pick in range(weapon_num):
                rand_num = random.randint(0, weapon_len)
                picked_weapon = exotic_weapons[rand_num]
                self.text.insert(INSERT, f'{picked_weapon}\n')
        else:
            check_list = []
            while len(check_list) != weapon_num:
                if weapon_num > weapon_len:
                    weapon_num = weapon_len
                rand_num = random.randint(0, weapon_len)
                picked_weapon = exotic_weapons[rand_num]
                if picked_weapon not in check_list:
                    check_list.append(picked_weapon)
                    self.text.insert(INSERT, f'{picked_weapon}\n')

        self.text['state'] = DISABLED
        self.text.pack()
        self.text.place(x=204, y=0)

        

if __name__=="__main__":
    #d2WeaponPicker().start()
    d2WeaponPicker()