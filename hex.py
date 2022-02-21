from tkinter import *
from tkinter import ttk
from numpy import binary_repr


def decimalConvert(*args):
    try:
        value = int(decimal.get())
        binary.set(binary_repr(value, None))
        hexadecimal = hex(value)
        hexa.set(hexadecimal)
    except ValueError:
        pass

def hexConvert(*args):
    val = str(og_hex.get())
    dec = int(val,16)
    deci.set(dec)
    bin.set(binary_repr(dec, None))

root = Tk()

root.title("Decimal and Hex Converter")
mainframe = ttk.Frame(root, padding="5 5 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# For decimal converter
decimal = StringVar()
binary = StringVar()
hexa = StringVar()

# For hex converter
og_hex = StringVar()
bin = StringVar()
deci = StringVar()



# Hex converter
hexa_entry = ttk.Entry(mainframe, width=7, textvariable=og_hex)
hexa_entry.grid(column=5, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=hexConvert).grid(column=6, row=4, sticky=W)

# Hex
ttk.Label(mainframe, text="in Hex").grid(column=6, row=1, sticky=W)

# Binary
ttk.Label(mainframe, text="Binary").grid(column=6, row=2, sticky=W)
ttk.Label(mainframe, textvariable=bin).grid(column=5, row=2, sticky=(W, E))

# Decimal
ttk.Label(mainframe, text="Decimal").grid(column=6, row=3, sticky=W)
ttk.Label(mainframe, textvariable=deci).grid(column=5, row=3, sticky=(W, E))

#--------------------------------------------------------------------------------------------------------------------------------------

# Decimal converter button and entry
decimal_entry = ttk.Entry(mainframe, width=7, textvariable=decimal)
decimal_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=decimalConvert).grid(column=3, row=4, sticky=W)

# Decimal
ttk.Label(mainframe, text="in Decimal").grid(column=3, row=1, sticky=W)

# Binary
ttk.Label(mainframe, text="Binary").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=binary).grid(column=2, row=2, sticky=(W, E))

# Hex 
ttk.Label(mainframe, text="Hex").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, textvariable=hexa).grid(column=2, row=3, sticky=(W, E))


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


decimal_entry.focus()
root.mainloop()
