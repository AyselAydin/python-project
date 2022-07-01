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
    self.index = 0

  def increase_score(self):
    self.score += 100

  def getQuestion(self):
    return self.questions[self.index]

  def displayQuestion(self):
    question = self.getQuestion()
    print(f"Soru {self.index + 1}: {question.question}")

    for i in question.choices:
      print("-> " + i)

    answer = input("Cevabı giriniz: ")
    if question.check_answer(answer):
      print("Tebrikler, doğru cevap")
      self.increase_score()
    else:
      print(f"Yanlış cevap, doğru cevap: {question.answer}")
    
    self.index += 1
    if len(self.questions) != self.index:
      self.displayQuestion()
    else:
      print(f"Tebrikler, yarışmayı tamamladınız. Toplamda puanınız: {self.score}")

