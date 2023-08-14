
import tkinter as tk
import collection_logging as cl

try:
    init_total = int(cl.latest_total())
except:
    init_total = 0

str_total = str(init_total)
lbl_width = 30


def start_task():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value + 3}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("Start_task", 3, total)

def complete_task():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value + 1}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("Complete_task", 1, total)

def moc():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value + 2}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("moc", 2, total)

def social_media():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value - 2}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("Social_media", -2, total)

def youtube():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value - 2}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("YouTube", -2, total)

def gaming():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value - 1}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("Gaming", -1, total)

def online_shopping():
    if True:
        value = int(lbl_total["text"])
        lbl_total["text"] = f"{value - 10}"
        total = lbl_total["text"]
        # send new lbl_total to collection function to be logged
        cl.format_logging_points("Online_shopping", -10, total)


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
frm_earn_buttons.pack(side=tk.LEFT)#grid(row=0,column=0,sticky="w")

# Buttons that will be part of Earn will have the parameters tk.Button(master=frm_earn_buttons, ...)

# Start task button. Earn
btn_start_task = tk.Button(master=frm_earn_buttons, 
                           text="Start Task", 
                           relief=tk.RAISED, 
                           command=start_task)
btn_start_task.pack(fill=tk.X)#grid(row=0,column=0, sticky="w")


# Complete task button. Earn
btn_complete_task = tk.Button(master=frm_earn_buttons, 
                              text="Complete Task", 
                              relief=tk.RAISED, 
                              command=complete_task)
btn_complete_task.pack(fill=tk.X)#grid(row=1,column=0, sticky="w")

# M.O.C. button. Earn
btn_moc = tk.Button(master=frm_earn_buttons, 
                    text="M.O.C.", 
                    relief=tk.RAISED,
                    command=moc)
btn_moc.pack(fill=tk.X)#grid(row=2,column=0, sticky="w")


# MIDDLE SEPARATOR FRAME
frm_middle_frame = tk.Frame(master=frm_button_space, width=lbl_width, borderwidth=1)
frm_middle_frame.pack(side=tk.LEFT)
# Empty label to separate buttons
lbl_separate_buttons = tk.Label(master=frm_middle_frame, width=30)
lbl_separate_buttons.pack()

# SPEND BUTTONS

# Frame for the spend buttons
frm_spend_buttons = tk.Frame(master=frm_button_space, borderwidth=1)
frm_spend_buttons.pack(side=tk.RIGHT)#grid(row=0,column=1,sticky="e")

# Buttons that will be part of Spend will have the parameters tk.Button(master=frm_spend_buttons, ...)

# Social media button. Spend
btn_social_media = tk.Button(master=frm_spend_buttons, 
                             text="Social Media", 
                             relief=tk.RAISED,
                             command=social_media)
btn_social_media.pack(fill=tk.X) #grid(row=0,column=0, sticky="e")

# YouTube button. Spend
btn_youtube = tk.Button(master=frm_spend_buttons, 
                        text="YouTube", 
                        relief=tk.RAISED,
                        command=youtube)
btn_youtube.pack(fill=tk.X) #grid(row=1,column=0, sticky="e")

# Gaming button. Spend
btn_gaming = tk.Button(master=frm_spend_buttons, 
                       text="Gaming", 
                       relief=tk.RAISED,
                       command=gaming)
btn_gaming.pack(fill=tk.X)

# Online shopping button. Spend
btn_online_shop = tk.Button(master=frm_spend_buttons, 
                            text="Online Shopping", 
                            relief=tk.RAISED,
                            command=online_shopping)
btn_online_shop.pack(fill=tk.X)

window.mainloop()