from types import SimpleNamespace

import app.ask as ask_module


def test_main_keeps_using_the_same_chat_for_follow_up_questions(monkeypatch, capsys):
    class FakeChat:
        def __init__(self):
            self.questions = []

        def send_message(self, question):
            self.questions.append(question)
            return SimpleNamespace(text=f"回答: {question}", usage_metadata=None)

    class FakeChats:
        def __init__(self, chat):
            self.chat = chat
            self.models = []

        def create(self, model):
            self.models.append(model)
            return self.chat

    chat = FakeChat()
    chats = FakeChats(chat)
    client = SimpleNamespace(chats=chats)
    monkeypatch.setattr(ask_module.genai, "Client", lambda api_key: client)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(ask_module, "MODEL", "test-model")
    monkeypatch.setattr("sys.argv", ["app.ask", "最初の質問"])
    questions = iter(["続けて質問", "/exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(questions))

    ask_module.main()

    assert chats.models == ["test-model"]
    assert chat.questions == ["最初の質問", "続けて質問"]
    assert "回答: 続けて質問" in capsys.readouterr().out