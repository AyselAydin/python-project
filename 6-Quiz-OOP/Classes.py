class Questions:
  def __init__(self, question, choices, answer):
    self.question = question
    self.choices = choices
    self.answer = answer

  def check_answer(self, answer):
    return self.answer == answer

class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.score = 0

  def increase_score(self, score):
    score += 100  