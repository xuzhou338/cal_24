import tkinter as tk
import cal_24


def trial_gen():
    """Use cal_24 to generate questions and solutions."""
    trial = cal_24.cal_24()
    while not trial.solutions:
        trial = cal_24.cal_24()
    question = trial.nums
    solution = trial.solutions
    return question, solution

def q_update():
    """The call back function of the next button."""
    global frame_q, frame_s, q, s, solution
    if q:
        frame_q.destroy()
        frame_q = tk.Frame(root)
        frame_q.pack()
        frame_b.forget()
        frame_b.pack()
    if s:
        frame_s.destroy()
        frame_s = tk.Frame(root)
        frame_s.pack()
    question, solution = trial_gen()
    for i in range(4):
        q = tk.Label(frame_q, text=str(question[i]), font=('Ariel Black', 20), \
                     padx=20, pady=20)
        q.pack(side='left')


def show_s():
    """The call back function of the show solution button."""
    global frame_s, s
    if s:
        frame_s.destroy()
        frame_s = tk.Frame(root)
        frame_s.pack(side='bottom')
        frame_b.forget()
        frame_b.pack()
    for i in range(len(solution)):
        s = tk.Label(frame_s, text=solution[i], font=('Ariel Black', 20),
                     padx=20,pady=20)
        s.pack()

# Main part of the gui program.
root = tk.Tk()
root.title('Calculate 24 - By JoJoX')
frame_q = tk.Frame(root)
frame_q.pack()
frame_b = tk.Frame(root)
frame_b.pack()
frame_s = tk.Frame(root)
frame_s.pack()

# Space holders for q and s
q = 1
s = 1
q_update()

button1 = tk.Button(frame_b, text='Show Solution', font=('Ariel Black', 20),
                    command=show_s)
button1.pack(side='left', padx=20, pady=20)
button2 = tk.Button(frame_b, text='Next', font=('Ariel Black', 20),
                    command=q_update)
button2.pack(side='left', padx=20, pady=20)
root.mainloop()