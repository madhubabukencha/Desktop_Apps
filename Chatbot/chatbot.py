from tkinter import *
from tkinter import ttk
from time import sleep


class ChatBot:
    answer = {
        ("Hello", "hello", "Hi", "hi"): "Hello",
        ("How are you?", "How are u?"): "I'm Good",
        ("What's your name?", "What is your name?"): "Not yet decided by Madhu"
    }

    def __init__(self, master):
        """
        Assume that these are global setting for chat application
        """
        self.master = master
        self.scrollbar = Scrollbar()

        # Creating Text widget for Chat Window
        self.chat_window = Text(self.master, bg="azure2",
                                yscrollcommand=self.scrollbar.set,
                                font=("Helvetica", 13))
        # Setting scroll bar on y axis on right side
        self.scrollbar.pack(side=RIGHT, fill=Y)
        # Setting chat window geometry
        self.chat_window.pack(fill=BOTH, expand=True)
        # Disabling chat window, so the user can edit on chat window
        self.chat_window.config(state=DISABLED)

        # Creating Text widget for reading questions from user
        self.input_text = Text(self.master, height=4, width=100)
        self.input_text.pack(side=LEFT)

    def communicate(self):
        """
        In this function we are reading user question,
        checking in our database whether question is present or not
        once it's present then we are giving answer to him
        """
        # Reading user question from user
        question = self.input_text.get("1.0", END)
        question = question.strip("\n")
        # print(question)

        # Searching for question in database
        bot_answer = ""
        for user_question, value in self.answer.items():
            # print(user_question)
            # print(question in user_question)
            if question in user_question:
                bot_answer = "Bot: "+self.answer[user_question]+"\n\n"
                # print(bot_answer)
                break
            else:
                bot_answer = "Bot: " + "Sorry I don't have answer for your query!!! 😭" + "\n\n"

        # Question should not empty
        if question != "" and (question.isspace() != True):
            question = "Human: "+question+"\n\n"
            # When user click on send button removed question from input window
            self.input_text.delete("1.0", END)
            self.chat_window.config(state=NORMAL)
            # Inserting question and answers at end of the chat
            self.chat_window.insert(END, question)
            sleep(1)
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
    """
    Main Loop stars here
    """
    root = Tk()
    # Chat bot Icon
    photo_image = PhotoImage(file='robot.png')
    root.iconphoto(False, photo_image)
    # Title of the chat bot
    root.title("Chatbot")
    # Where to display on the screen
    root.geometry("950x650+230+30")

    chatbot = ChatBot(root)
    chatbot.final_call()
    root.resizable(0, 0)
    root.mainloop()


if __name__ == "__main__":
    main()
