## Import
import tkinter as tk
import TClayer as TC
from decimal import Decimal

## GUI
class GUI(tk.Frame):
    """ Main GUI heritate from tkinter Frame """
    
    def __init__(self):                                  # Constructor
        self.mainFrame = tk.Frame().pack()               # Main frame
        self.buildGUI()                                  # launch widget builder

    def stdInput (self, text):
        """ helper function to build a std label-entry"""
        self.entryFrame = tk.Frame(self.mainFrame)
        tk.Label(self.entryFrame,text=text,width=25,anchor=tk.E).pack(side=tk.LEFT)
        self.myEntry = tk.Entry(self.entryFrame,width=10)
        self.myEntry.pack(side=tk.LEFT,padx=5,pady=2)
        self.entryFrame.pack(side=tk.TOP)
        return self.myEntry

    def buildGUI (self):
        """ Build the GUI """
        self.picture = tk.PhotoImage(file = "Formula.gif")
        formula = tk.Label(self.mainFrame,image=self.picture,
                           background="white")
        formula.pack(anchor=tk.E, fill=tk.X)

        tk.Label(self.mainFrame,background="white",
                text="\nEnter known parameters and press 'solve'\n").pack(anchor=tk.E, fill=tk.X)
        
        self.inputList = ['Thickness (nm) :',
                          'Sheet resistance (Ohms-square) :',  
                          'Resistivity (Ohms.cm) :',
                          'Conductivity (S) :',
                          'Mobility (cm2.V-1.s-1) :',
                          'Carrier density (cm-3) :'
                          ]

        self.entries=[]
        for str in self.inputList :
            self.thisEntry = self.stdInput(str)
            self.entries.append(self.thisEntry)
            
        self.buttonFrame=tk.Frame()

        self.clearAllButton = tk.Button(self.buttonFrame,text="Clear", width=12,
                  command=self.clearAll)
        self.clearAllButton.bind("<Return>", self.clearAllWrapper)
        self.clearAllButton.pack(side=tk.LEFT,padx=5)
        
        self.solveButton=tk.Button(self.buttonFrame,text="Solve", width=12,
                  command=self.solve)
        self.solveButton.bind("<Return>", self.solveWrapper)
        self.solveButton.pack(side=tk.LEFT,padx=5)
        self.solveButton.focus_force()

        self.buttonFrame.pack(anchor=tk.E,pady=7)

        self.msg = tk.StringVar()
        self.statusBar = tk.Label(self.mainFrame,background="gray",
                 textvariable=self.msg, justify=tk.LEFT)
        self.statusBar.pack(anchor=tk.E, fill=tk.X)
        
        
    # Callbacks
    def solveWrapper(self,event):
        self.solve()

    def solve(self):
        """ Solve and display"""       
        values=[]                                   # Get values
        for object in self.entries:
            val = object.get()
            try:
                val=float(val)
                values.append(val)
            except ValueError:
                values.append(None)          
        
        thisTC = TC.TClayer(values[0],values[1],values[2],
                            values[3],values[4],values[5])  # Instantiate a TClayer
        
        thisTC.solve()                              # Solve it

        values=[thisTC.getThickness(),         # Get the output values
               (thisTC.getSheetResistance()),
               (thisTC.getResistivity()),
               (thisTC.getConductivity()),
               (thisTC.getMobility()),
               (thisTC.getCarrierDensity())]

        i=0
        for object in self.entries:                 # Display output values
            object.delete(0,tk.END)                 # Delete entry content
            if i in [0,3]:
                try:
                    object.insert(0,"%.0f"%values[i]) # Display and format the output value if exist
                except:
                    pass
            if i in [1,4]:
                try:
                    object.insert(0,"%.1f"%values[i])
                except:
                    pass
            if i in [2]:
                try:
                    object.insert(0,"%.2e"%values[i])
                except:
                    pass
            if i in [5]:
                try:
                    object.insert(0,"%.1e"%values[i])
                except:
                    pass
            i=i+1

        self.msg.set(thisTC.getMsg()[:-1])
        
    def clearAllWrapper(self,event):
        self.clearAll()

    def clearAll(self):
        """ clear all entries """
        for object in self.entries:
            object.delete(0,tk.END)
        self.msg.set("")

                  

## init GUI
root = tk.Tk()                                  # Build main window
root.title("TC-solver")                                
app = GUI()                                     # Instantiate the GUI
root.mainloop()                                 # Run event loop on main window



