import tkinter from *

class CurrencyConvertor:
    def __init__(self):
        window = Tk()       #Tkinter function call, for Window GUI
        window.title("Convert Your Currency")       #Title of the window
        window.configure(bg = "black")

        #Three Labels for inputs
        Label(window, font = "Times 15 bold", bg = "white", text = "Enter your Amount").grid(row = 1, column = 1, sticky = W)
        Label(window, font = "Times 15 bold", bg = "white", text = "Current Conversion Rate").grid(row = 2, column = 1, sticky = W)
        Label(window, font = "Times 15 bold", bg = "white", text = "Your Final Converted Amount").grid(row = 3, column = 1, sticky = W)

        #Creating three objects relevant to the Labels, and adding entry function
        self.EnterAmtVar = stringvar()
        entry(window, textvariable = self.EnterAmtVar, justify = RIGHT).grid(row = 1, column = 2)
        self.CurrencyRate = stringvar()
        entry(window, textvariable = self.CurrencyRate, justify = RIGHT).grid(row = 2, column 2)
        self.FinalAmount = stringvar()
        lblFinalAmount = Label(window, font = "Times 15 bold", bg = "white", textvariable = self.FinalAmount).grid(row = 3, column = 2, sticky = E)

        #Creating two buttons with their functions being "Convert" and "Reset"
        btFinalAmount = Button(window, text = "Convert this for me !", font = "Times 15 bold", bg = "grey", fg = " white", command = self.FinalAmountFunc).grid(row = 4, column = 2, sticky = E)
        btReset = Button(window, text = "Reset", font = " Times 15 bold", bg = "grey", fg = "white", command = self.delete_all).grid(row = 4, column = 6, padx = 25, pady = 25, sticky = E)

        window.mainloop()       #To run the program

        #Creating the "FinalAmountFunc" and "Reset" function
    def FinalAmountFunc(self):
        amt = float(self.CurrencyRate.get())
        FinalAmount = float(self.EnterAmtVar.get()) * amt
        self.FinalAmount.set(format(FinalAmount,'10.2f'))

    def delete_all(self):
        self.EnterAmtVar.set("")
        self.CurrencyRate.set("")
        self.FinalAmount.set("")

CurrencyConvertor()
