import sys
from tkinter import Label, Button, Tk

def _test():
    """
    A simple GUI test function using tkinter.
    """
    # Initialize the root Tkinter window
    root = Tk()
    root.title("Test GUI")

    # Create a label with initial text
    texto = Label(master=root, text="-Teste \"\xe7\"-")
    texto.pack()

    # Add a button to modify the label text
    update_button = Button(
        master=root,
        text="Click Aqui!",
        command=lambda: texto.configure(text=f"*{texto['text']}*")
    )
    update_button.pack()

    # Display the script name in another label
    script_label = Label(root, text=f"{sys.argv[0]}")
    script_label.pack()

    # Add a quit button to close the application
    quit_button = Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    # Ensure the window appears correctly
    root.iconify()
    root.update()
    root.deiconify()

    # Start the Tkinter event loop
    root.mainloop()
