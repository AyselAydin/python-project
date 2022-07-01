class Questions:
  def __init__(self, question, choices, answer):
    self.question = question
    self.choices = choices
    self.answer = answer

  def check_answer(self, answer):
    return self.answer == answer