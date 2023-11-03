
import tkinter as tk
import collection_logging as cl

try:
    init_total = int(cl.latest_total())
except:
    init_total = 0

str_total = str(init_total)
lbl_width = 30

class Button_command():

    def __init__(self, amount: int, button_name: str) -> None:
        self.amount = amount
        self.button_name = button_name

    def command(self):
        if True:
            # Operation to update the total
            value = int(lbl_total["text"]) # Gets the total and saves it to value
            lbl_total["text"] = f"{value + int(self.amount)}" # Updates and saves the total to the total label
            total = lbl_total["text"] # Assigns the updated total to a var to be logged.
            # send new lbl_total to collection function to be logged
            cl.format_logging_points(str(self.button_name), 3, total)


# Instantiating button commands
start_task = Button_command(3, "Start_task")
complete_task = Button_command(1, "Complete_task")
# Change moc name to Definitions (Explain a concept).
moc = Button_command(2, "moc")
social_media = Button_command(-2, "Social_media")
youtube = Button_command(-2, "YouTube")
gaming = Button_command(-1, "Gaming")
online_shopping = Button_command(-10,"Online_shopping")


window = tk.Tk()
window.title("Gamify Points")

# Frame to hold the label that displays the results
frm_display_results = tk.Frame(borderwidth=1)
frm_display_results.pack()

# Label that displays the results
lbl_total = tk.Label(master=frm_display_results,width=10,bg="black",fg="white",text=f"{str_total}")
lbl_total.pack()

# Frame that holds the labels for the Earn and Spend buttons.
frm_earn_spend_lbl = tk.Frame(borderwidth=1)
frm_earn_spend_lbl.pack()

# Label for the Earn buttons
lbl_earn = tk.Label(master=frm_earn_spend_lbl, width=lbl_width, relief=tk.RIDGE, text="Earn")
lbl_earn.grid(row=0,column=0,sticky="w")

# Label for the spend buttons
lbl_spend = tk.Label(master=frm_earn_spend_lbl, width=lbl_width, relief=tk.RIDGE, text="Spend")
lbl_spend.grid(row=0,column=1,sticky="e")

# Frame to house the frames for the buttons
frm_button_space = tk.Frame(width=50,borderwidth=1)
frm_button_space.pack()

# EARN BUTTONS

# Frame for the earn buttons
frm_earn_buttons = tk.Frame(master=frm_button_space, borderwidth=1)
frm_earn_buttons.pack(side=tk.LEFT)

# Buttons that will be part of Earn will have the parameters tk.Button(master=frm_earn_buttons, ...)

# Start task button. Earn
btn_start_task = tk.Button(master=frm_earn_buttons, 
                           text="Start Task", 
                           relief=tk.RAISED, 
                           command=start_task.command)
btn_start_task.pack(fill=tk.X)


# Complete task button. Earn
btn_complete_task = tk.Button(master=frm_earn_buttons, 
                              text="Complete Task", 
                              relief=tk.RAISED, 
                              command=complete_task.command)
btn_complete_task.pack(fill=tk.X)

# M.O.C. button. Earn
btn_moc = tk.Button(master=frm_earn_buttons, 
                    text="M.O.C.", 
                    relief=tk.RAISED,
                    command=moc.command)
btn_moc.pack(fill=tk.X)


# MIDDLE SEPARATOR FRAME
frm_middle_frame = tk.Frame(master=frm_button_space, width=lbl_width, borderwidth=1)
frm_middle_frame.pack(side=tk.LEFT)
# Empty label to separate buttons
lbl_separate_buttons = tk.Label(master=frm_middle_frame, width=30)
lbl_separate_buttons.pack()

# SPEND BUTTONS

# Frame for the spend buttons
frm_spend_buttons = tk.Frame(master=frm_button_space, borderwidth=1)
frm_spend_buttons.pack(side=tk.RIGHT)

# Buttons that will be part of Spend will have the parameters tk.Button(master=frm_spend_buttons, ...)

# Social media button. Spend
btn_social_media = tk.Button(master=frm_spend_buttons, 
                             text="Social Media", 
                             relief=tk.RAISED,
                             command=social_media.command)
btn_social_media.pack(fill=tk.X)

# YouTube button. Spend
btn_youtube = tk.Button(master=frm_spend_buttons, 
                        text="YouTube", 
                        relief=tk.RAISED,
                        command=youtube.command)
btn_youtube.pack(fill=tk.X)

# Gaming button. Spend
btn_gaming = tk.Button(master=frm_spend_buttons, 
                       text="Gaming", 
                       relief=tk.RAISED,
                       command=gaming.command)
btn_gaming.pack(fill=tk.X)

# Online shopping button. Spend
btn_online_shop = tk.Button(master=frm_spend_buttons, 
                            text="Online Shopping", 
                            relief=tk.RAISED,
                            command=online_shopping.command)
btn_online_shop.pack(fill=tk.X)

window.mainloop()