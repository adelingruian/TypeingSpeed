import datetime
import tkinter as tk
import difflib
import tkinter.messagebox

SAMPLE_TEXT = "The quick brown fox jumps over the lazy dog. He hung up and texted her quickly, typing with his " \
              "thumb. A good way to increase your typing speed is to type easy sentences over and over. That will " \
              "help you to type smoothly without pausing. Try taking a typing speed test before and after to see for " \
              "yourself. You can even work through this section multiple times and then track your progress."

BG_COLOR = "#E6D2AA"
BG_COLOR_SECONDARY = "#F1EFDC"
FG_COLOR = "#42032C"
FG_COLOR_SECONDARY = "#D36B00"
MAIN_FONT = ("Helvetica", 12, "normal")

global start_time

window = tk.Tk()
window.title("TYPE-ing SPEED")
window.config(width=500, height=800, padx=100, pady=20, bg=BG_COLOR)
window.resizable(False, False)


def reset():

    def keydown(_):
        current_text = input_area.get(1.0, tk.END)

        count_characters = len(current_text)
        count_words = len(current_text.split(" "))
        current_time = datetime.datetime.now()
        delta_time = (current_time - start_time).total_seconds()

        accuracy = difflib.SequenceMatcher(None, SAMPLE_TEXT, current_text).ratio()
        accuracy = str(round(accuracy * 100, 2))
        accuracy_label.config(text=f"{accuracy}% ACC")

        characters_label.config(text=f"{'{:.2f}'.format(count_characters / delta_time * 60)} CPM")
        words_label.config(text=f"{'{:.2f}'.format(count_words / delta_time * 60)} WPM")

        if len(current_text) == len(SAMPLE_TEXT):
            tkinter.messagebox.showinfo(title="Congrats",
                                        message=f"Good job, your final score is: \n "
                                        f"CPM = {'{:.2f}'.format(count_characters / delta_time * 60)}\n"
                                        f"WPM = {'{:.2f}'.format(count_words / delta_time * 60)}\n"
                                        f"Accuracy = {accuracy}%")
            input_area.config(state="disabled")

    global start_time
    start_time = datetime.datetime.now()
    characters_label.config(text="0 CPM")
    words_label.config(text="0 WPM")
    accuracy_label.config(text="100% ACC")
    input_area.config(state="normal")
    input_area.delete(1.0, tk.END)

    window.bind("<KeyPress>", keydown)


title_label = tk.Label(text="TYPE-ing SPEED TEST", font=("Helvetica", 36, "bold"), fg=FG_COLOR_SECONDARY, bg=BG_COLOR)
title_label.grid(row=0, column=0, columnspan=4)

text_label = tk.Label(text=SAMPLE_TEXT, font=MAIN_FONT, wraplength=420, justify="left", bg=BG_COLOR,
                      fg=FG_COLOR, pady=20)
text_label.grid(row=1, column=0, columnspan=4)

input_area = tk.Text(font=MAIN_FONT, height=10, width=54, bg=BG_COLOR_SECONDARY)
input_area.grid(row=2, column=0, columnspan=4)

characters_label = tk.Label(text="0 CPM", font=MAIN_FONT, pady=20, bg=BG_COLOR, fg=FG_COLOR_SECONDARY)
characters_label.grid(row=3, column=0)
words_label = tk.Label(text="0 WPM", font=MAIN_FONT, pady=20, bg=BG_COLOR, fg=FG_COLOR_SECONDARY)
words_label.grid(row=3, column=1)
accuracy_label = tk.Label(text="100% Acc", font=MAIN_FONT, pady=20, bg=BG_COLOR, fg=FG_COLOR_SECONDARY)
accuracy_label.grid(row=3, column=2)
reset_button = tk.Button(text="Reset", width=20, command=reset)
reset_button.grid(row=3, column=3)

reset()
window.mainloop()
