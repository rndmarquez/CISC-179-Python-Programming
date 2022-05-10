"""
    File: calculator.py
    Author: Ron Marquez

    Write a GUI that implements the calculator shown in the following image:



    - User enters two integers into the text fields. [x]

    - When Add button is pressed, the sum of  the values in the text fields are shown after the Equals: as a label. [x]

    - The Clear button clears the values in the text fields. The cleared values can be blank or zero. [x]

    - The Quit button closes the GUI window. [x]

"""


from breezypythongui import EasyFrame
import math


class Calculator(EasyFrame):
    """
        Calculator GUI set up
    """
    def __init__(self):
        EasyFrame.__init__(self, width = 250, height = 250, title = "Calculator", background = "white")  #set window up
        self.setResizable(False)  #disables resizing of window

        #text feild 1
        self.firstNumber = self.addIntegerField(value = "", row = 0, column = 0, columnspan = 1, width = 10, sticky = "NSEW")
        

        #add Plus label
        self.addLabel(text = "Plus", row = 1, column = 0, sticky = "NSEW", background = "white")

        #text feild 2
        self.secondNumber = self.addIntegerField(value = "", row = 2, column = 0, sticky = "NSEW")

        #add Equals label
        self.addLabel(text = "Equals:", row = 3, column = 0, sticky = "NSEW", background = "white")


        #add buttons
        buttonPanel = self.addPanel(row = 4, column = 0, background = "white")
        buttonPanel.addButton(text = "add", row = 4, column = 0, rowspan = 1, command = self.addInputs)
        buttonPanel.addButton(text = "clear", row = 4, column = 1, command = self.clearInputs)
        buttonPanel.addButton(text = "quit", row = 4, column = 2, command = self.closeWindow)


    """
        add function to buttohns
    """
    def addInputs(self):
        """
            add inputs from firstNumber and secondNumber
        """
        try: 
            #obtain inputs
            number1 = self.firstNumber.getNumber()
            number2 = self.secondNumber.getNumber()

        
            #results
            total = number1 + number2
        
            #display total
            #add Equals label
            self.addLabel(text = "Equals: " + str(total) , row = 3, column = 0, sticky = "NSEW")

        except ValueError:
            self.messageBox(title = "Error", message = "Please enter integers to add")


    def clearInputs(self):
        """
            clear inputs
        """
        self.firstNumber = self.addIntegerField(value = "", row = 0, column = 0, columnspan = 2, width = 10, sticky = "NSEW")
        self.secondNumber = self.addIntegerField(value = "", row = 2, column = 0, sticky = "NSEW")
        self.addLabel(text = "Equals:", row = 3, column = 0, sticky = "NSEW")

    def closeWindow(self):
        """
            close window when Quit button is clicked
        """
        self.master.destroy()



def main():
    Calculator().mainloop()


if __name__ == "__main__":
    main()
