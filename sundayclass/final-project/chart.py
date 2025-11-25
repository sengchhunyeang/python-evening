import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtCore import Qt, QTimer

# -----------------------------
# Static chatbot responses
# -----------------------------
responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! How are you?",
    "how are you": "I’m just a program, but I’m doing fine!",
    "your name": "I am ChatBot3000",
    "do you know python": "Yes! Python is a popular programming language.",
    "do you know ai": "Yes, AI stands for Artificial Intelligence.",
    "do you know your creator": "I was created by a Python programmer.",
    "exit": "Goodbye! Have a nice day."
}

# -----------------------------
# API Functions
# -----------------------------
def get_joke():
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        if res.status_code == 200:
            data = res.json()
            return f"{data['setup']} ... {data['punchline']}"
        else:
            return "Sorry, I couldn't get a joke now."
    except:
        return "Error connecting to Joke API."

def get_trivia():
    try:
        res = requests.get("https://opentdb.com/api.php?amount=1&type=multiple", timeout=5)
        if res.status_code == 200:
            data = res.json()
            question = data['results'][0]['question']
            answer = data['results'][0]['correct_answer']
            return f"Trivia: {question} (Answer: {answer})"
        else:
            return "Sorry, I couldn't get trivia now."
    except:
        return "Error connecting to Trivia API."

def calculate_math(expression):
    try:
        expression = expression.replace("^", "**")  # Replace ^ with Python exponent
        res = requests.get(f"https://api.mathjs.org/v4/?expr={expression}", timeout=5)
        if res.status_code == 200:
            return f"{expression} = {res.text}"
        else:
            return "Math API error."
    except:
        return "Invalid math expression."

# -----------------------------
# Chatbot logic
# -----------------------------
def get_response(user_input):
    user_input = user_input.lower()

    # Check for API commands
    if "joke" in user_input:
        return get_joke()
    elif "trivia" in user_input:
        return get_trivia()
    elif any(op in user_input for op in "+-*/^"):
        return calculate_math(user_input)

    # Static responses
    for key in responses:
        if key in user_input:
            return responses[key]

    # General "do you know" response
    if "do you know" in user_input:
        topic = user_input.replace("do you know", "").strip()
        return f"I know a little about {topic.title()}!"

    return "I’m not sure how to respond to that."

# -----------------------------
# PyQt6 GUI
# -----------------------------
class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 ChatBot with API")
        self.setGeometry(200, 200, 600, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #2e2e3e;
                padding: 5px;
                border-radius: 5px;
                color: white;
            }
            QPushButton {
                background-color: #00bfff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px;
            }
            QTextEdit {
                background-color: #2e2e3e;
                border-radius: 5px;
                color: white;
            }
        """)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_field)

        # Send button
        self.send_button = QPushButton("Send")
        self.layout.addWidget(self.send_button)

        # Connect signals
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

    # -----------------------------
    # Send message with "typing..." effect
    # -----------------------------
    def send_message(self):
        user_text = self.input_field.text().strip()
        if user_text == "":
            return

        # Show user message
        self.chat_display.append(f"<b>You:</b> {user_text}")
        self.input_field.clear()

        # Show typing/loading message
        self.chat_display.append(f"<b>ChatBot:</b> <i>typing...</i>")

        # Simulate delay (1 second)
        QTimer.singleShot(1000, lambda: self.show_response(user_text))

    def show_response(self, user_text):
        # Remove "typing..." line
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        cursor.select(cursor.SelectionType.BlockUnderCursor)
        cursor.removeSelectedText()
        cursor.deletePreviousChar()

        # Get response
        response = get_response(user_text)
        self.chat_display.append(f"<b>ChatBot:</b> {response}\n")

# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotGUI()
    window.show()
    sys.exit(app.exec())
