from tkinter import *
from tkinter import ttk


class ChatBot:
    answer = {
        ("How are you?", "How are u?"): "I'm Good",
        ("What's your name?", "What is your name?"): "Not yet decided by Madhu"
    }

    def __init__(self, master):
        self.master = master
        self.scrollbar = Scrollbar()
        self.chat_window = Text(self.master, bg="azure2",
                                yscrollcommand=self.scrollbar.set,
                                font=("Helvetica", 13))
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat_window.pack(fill=BOTH, expand=True)

        self.input_text = Text(self.master, height=4, width=100)
        self.input_text.pack(side=LEFT)
        self.k = self.input_text.get("1.0", END)

    def communicate(self):
        question = self.input_text.get("1.0", END)
        question = question.strip("\n")
        print(question)
        bot_answer = ""
        for user_question, value in self.answer.items():
            print(user_question)
            print(question in user_question)
            if question in user_question:
                bot_answer = "Bot: "+self.answer[user_question]+"\n\n"
                print(bot_answer)
            else:
                bot_answer = "Bot: " + "I don't have answer for many questions" + "\n\n"

        if question != "" and (question.isspace() != True):
            question = "Human: "+question+"\n\n"
            self.input_text.delete("1.0", END)
            self.chat_window.config(state=NORMAL)
            self.chat_window.insert(END, question)
            self.chat_window.insert(END, bot_answer)
            self.chat_window.config(state=DISABLED)

    def submit(self):
        submit_image = PhotoImage(file=r"send.gif")
        submit = Button(self.master,
                        text="Send",
                        width=20,
                        bg="#2A4B7C",
                        fg='#ffffff',
                        font=("Helvetica", 13), command=self.communicate)
        submit.pack(side=RIGHT, ipady=20)

    def final_call(self):
        self.submit()


def main():
    root = Tk()
    photo_image = PhotoImage(file='robot.png')
    root.iconphoto(False, photo_image)
    root.title("Chatbot")
    root.geometry("950x650+230+30")

    chatbot = ChatBot(root)
    chatbot.final_call()
    root.resizable(0, 0)
    root.mainloop()


if __name__ == "__main__":
    main()
