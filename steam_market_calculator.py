from tkinter import *
from tkinter import font
import os
import win32gui, win32con

# adjust file path
os.chdir(os.path.dirname(__file__))

# hide console for .exe file look
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

# window dimensions
window_width = 400
window_height = 552

# fonts
FRAME_NAME_FONT = ("Arial", 15, "bold")
BUTTON_FONT = ("Helvetica", 13)
INPUT_FONT = ("Helvetica", 13)
BUTTON_BG = "#4B072E"
BUTTON_FG = "#F7F9F7"
FRAME_NAME_BG = "#210124"
FRAME_NAME_FG = "#DBF9F0"

# value of items for the name of the list (usd, key, ref, scrap)
usd = [1, 0.56, 33.33, 300]
key = [1.77, 1, 59.11, 532]
ref = [0.03, 0.017, 1, 9]
scrap = [0.0033, 0.0019, 0.11, 1]

# steam tax and tip
tax_rate = 1.15
tax_tip = 0.01



class Calculator(Frame):
  def __init__(self):
    # frame creation
    Frame.__init__(self)
    self.grid()
    self.master.title("Steam Market Calculator")
    self.master.resizable(0,0)
    #self.master.iconbitmap("stonk_icon.ico")
    self.main_frame = Frame(self, width=window_width, height=window_height)
    self.main_frame.grid_propagate(0)
    self.main_frame.grid()

    # functions launch
    self.item_value()
    self.total_price()
    self.taxfree_price()
    self.mainloop()

  
  def item_value_clear(self):
    self.usd_input.set(0)
    self.key_input.set(0)
    self.ref_input.set(0)
    self.scrap_input.set(0)
    self.usd_output.set("USD : ")
    self.key_output.set("KEY : ")
    self.ref_output.set("REF : ")
    self.scrap_output.set("SCRAP : ")

  
  def item_value_output(self):
    usd_output = self.usd_input.get() + (self.key_input.get()/usd[1]) + (self.ref_input.get()/usd[2]) + (self.scrap_input.get()/usd[3])
    self.usd_output.set("USD : " + str(round(usd_output, 2)))
    key_output = self.key_input.get() + (self.usd_input.get()/key[0]) + (self.ref_input.get()/key[2]) + (self.scrap_input.get()/key[3])
    self.key_output.set("KEY : " + str(round(key_output, 2)))
    ref_output = self.ref_input.get() + (self.usd_input.get()/ref[0]) + (self.key_input.get()/ref[1]) + (self.scrap_input.get()/ref[3])
    self.ref_output.set("REF : " + str(round(ref_output, 2)))
    scrap_output = self.scrap_input.get() + (self.usd_input.get()/scrap[0]) + (self.key_input.get()/scrap[1]) + (self.ref_input.get()/scrap[2])
    self.scrap_output.set("SCRAP : " + str(round(scrap_output, 2)))
    


  def item_value(self):
    # frame creation
    self.value_frame = Frame(self.main_frame, width=window_width, height=int(window_height/2), bg="black")
    self.value_frame.grid_propagate(0)

    # text frame creation
    self.text_frame = Frame(self.value_frame, width=window_width, height=int(window_height/20), bg=FRAME_NAME_BG)
    self.text_frame.grid_propagate(0)
    self.frame_name_text = Label(self.text_frame, text="Item Value Converter", font=FRAME_NAME_FONT, bg=FRAME_NAME_BG, fg=FRAME_NAME_FG).grid()

    # button frame creation
    self.button_frame = Frame(self.value_frame, width=window_width, height=int(window_height/4-window_height/40), bg=BUTTON_BG)
    self.button_frame.grid_propagate(0)

    # output frame creation
    self.output_frame = Frame(self.value_frame, width=window_width, height=int(window_height/4-window_height/40), bg=BUTTON_BG)
    self.output_frame.grid_propagate(0)

    # variables creation
    self.usd_input = IntVar()
    self.key_input = IntVar()
    self.ref_input = IntVar()
    self.scrap_input = IntVar()
    self.usd_output = StringVar()
    self.key_output = StringVar()
    self.ref_output = StringVar()
    self.scrap_output = StringVar()

    # buttons creation
    self.usd_text = Label(self.button_frame, text="USD : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0)
    self.key_text = Label(self.button_frame, text="KEY : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=1)
    self.ref_text = Label(self.button_frame, text="REF : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=2)
    self.scrap_text = Label(self.button_frame, text="SCRAP : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=3)

    self.output_text = Label(self.output_frame, text="Output : ", font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(sticky=W)
    self.usd_res_text = Label(self.output_frame, textvariable=self.usd_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=1)
    self.key_res_text = Label(self.output_frame, textvariable=self.key_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=2)
    self.ref_res_text = Label(self.output_frame, textvariable=self.ref_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=3)
    self.scrap_res_text = Label(self.output_frame, textvariable=self.scrap_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=4)

    self.usd_entry = Entry(self.button_frame, textvariable=self.usd_input, font=INPUT_FONT, width=15).grid(row=0, column=1)
    self.key_entry = Entry(self.button_frame, textvariable=self.key_input, font=INPUT_FONT, width=15).grid(row=1, column=1)
    self.ref_entry = Entry(self.button_frame, textvariable=self.ref_input, font=INPUT_FONT, width=15).grid(row=2, column=1)
    self.scrap_entry = Entry(self.button_frame, textvariable=self.scrap_input, font=INPUT_FONT, width=15).grid(row=3, column=1)

    self.calculate_button = Button(self.button_frame, text="Calculate", font=BUTTON_FONT, width=10, height=5, command=self.item_value_output, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=2, padx=10, rowspan=4)
    self.clear_button = Button(self.button_frame, text="C", font=BUTTON_FONT, width=3, height=5, command=self.item_value_clear, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=3, rowspan=4)

    # frames launch
    self.value_frame.grid()
    self.text_frame.grid()
    self.button_frame.grid(row=1)
    self.output_frame.grid(row=2)
    self.item_value_clear()


  def total_price_clear(self):
    self.total_input.set("0")
    self.taxfree_output.set("Taxfree Price : ")
    self.total_difference_output.set("Difference : ")


  def total_price_output(self):
    taxfree_output = (float(self.total_input.get())/tax_rate  - tax_tip)
    self.taxfree_output.set("Taxfree Price : " + str(round(taxfree_output, 2)))
    total_difference_output =  taxfree_output - float(self.total_input.get())
    self.total_difference_output.set("Difference : " + str(round(total_difference_output, 2)))


  def total_price(self):
    # frame creation
    self.total_frame = Frame(self.main_frame, width=window_width, height=int(window_height/4), bg="blue")
    self.total_frame.grid_propagate(0)

    # text frame creation
    self.text_frame = Frame(self.total_frame, width=window_width, height=window_height/20, bg=FRAME_NAME_BG)
    self.text_frame.grid_propagate(0)
    self.frame_name_text = Label(self.text_frame, text="Total Price to Taxfree Price", font=FRAME_NAME_FONT, bg=FRAME_NAME_BG, fg=FRAME_NAME_FG).grid()

    # button frame creation
    self.button_frame = Frame(self.total_frame, width=window_width, height=int(window_height/12-window_height/40), bg=BUTTON_BG)
    self.button_frame.grid_propagate(0)

    # output frame creation
    self.output_frame = Frame(self.total_frame, width=window_width, height=int(window_height/4-window_height/40), bg=BUTTON_BG)
    self.output_frame.grid_propagate(0)

    # variables creation
    self.total_input = StringVar()
    self.taxfree_output = StringVar()
    self.total_difference_output = StringVar()

    # buttons creation
    self.total_price_text = Label(self.button_frame, text="TOTAL : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid()
    self.output_text = Label(self.output_frame, text="Output : ", font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(sticky=W)
    self.taxfree_res_text = Label(self.output_frame, textvariable=self.taxfree_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=1)
    self.difference_res_text = Label(self.output_frame, textvariable=self.total_difference_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=2)

    self.total_price_entry = Entry(self.button_frame, textvariable=self.total_input, width=15, font=INPUT_FONT).grid(row=0, column=1)

    self.calculate_button = Button(self.button_frame, text="Calculate", font=BUTTON_FONT, width=10, command=self.total_price_output, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=2, padx=10)
    self.clear_button = Button(self.button_frame, text="C", font=BUTTON_FONT, width=3, command=self.total_price_clear, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=3)

    # frames launch
    self.total_frame.grid(row=1)
    self.text_frame.grid()
    self.button_frame.grid(row=1)
    self.output_frame.grid(row=2)
    self.total_price_clear()


  def taxfree_price_clear(self):
    self.taxfree_input.set("0")
    self.total_output.set("Total Price : ")
    self.taxfree_difference_output.set("Difference : ")


  def taxfree_price_output(self):
    total_output = (float(self.taxfree_input.get())*tax_rate  + tax_tip)
    self.total_output.set("Total Price : " + str(round(total_output, 2)))
    taxfree_difference_output = total_output - float(self.taxfree_input.get())
    self.taxfree_difference_output.set("Difference : " + str(round(taxfree_difference_output, 2)))


  def taxfree_price(self):
    # frame creation
    self.taxfree_frame = Frame(self.main_frame, width=window_width, height=int(window_height/4), bg="red")
    self.taxfree_frame.grid_propagate(0)

    # text frame creation
    self.text_frame = Frame(self.taxfree_frame, width=window_width, height=window_height/20, bg=FRAME_NAME_BG)
    self.text_frame.grid_propagate(0)
    self.frame_name_text = Label(self.text_frame, text="Taxfree Price to Total Price", font=FRAME_NAME_FONT, bg=FRAME_NAME_BG, fg=FRAME_NAME_FG).grid()

    # button frame creation
    self.button_frame = Frame(self.taxfree_frame, width=window_width, height=int(window_height/12-window_height/40), bg=BUTTON_BG)
    self.button_frame.grid_propagate(0)

    # output frame creation
    self.output_frame = Frame(self.taxfree_frame, width=window_width, height=int(window_height/4-window_height/40), bg=BUTTON_BG)
    self.output_frame.grid_propagate(0)

    # variables creation
    self.taxfree_input = StringVar()
    self.total_output = StringVar()
    self.taxfree_difference_output = StringVar()

    # buttons creation
    self.taxfree_price_text = Label(self.button_frame, text="TAXFREE : ", width=10, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid()
    self.output_text = Label(self.output_frame, text="Output : ", font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG).grid(sticky=W)
    self.total_res_text = Label(self.output_frame, textvariable=self.total_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=1)
    self.difference_res_text = Label(self.output_frame, textvariable=self.taxfree_difference_output, width=30, font=BUTTON_FONT, anchor=W, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=2)

    self.taxfree_price_entry = Entry(self.button_frame, textvariable=self.taxfree_input, width=15, font=INPUT_FONT).grid(row=0, column=1)

    self.calculate_button = Button(self.button_frame, text="Calculate", font=BUTTON_FONT, width=10, command=self.taxfree_price_output, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=2, padx=10)
    self.clear_button = Button(self.button_frame, text="C", font=BUTTON_FONT, width=3, command=self.taxfree_price_clear, bg=BUTTON_BG, fg=BUTTON_FG).grid(row=0, column=3)

    # frames launch
    self.taxfree_frame.grid(row=2)
    self.text_frame.grid()
    self.button_frame.grid(row=1)
    self.output_frame.grid(row=2)
    self.taxfree_price_clear()

calc = Calculator()