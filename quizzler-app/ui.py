from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.firstquestion = self.quiz.next_question()

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score = Label(text="Score: 0",pady=20,padx=20,background=THEME_COLOR, fg='white')
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question = self.canvas.create_text(150,125,text=f"{self.firstquestion}",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true,highlightthickness=0,padx=20,pady=20,command=self.check_answer_right)
        self.true_button.grid(row=2,column=1)

        false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false,highlightthickness=0,padx=20,pady=20,command=self.check_answer_false)
        self.false_button.grid(row=2,column=0)

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            nextQuestionText = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=nextQuestionText)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def check_answer_right(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.next_question)








