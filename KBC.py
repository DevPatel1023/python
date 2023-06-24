import random

li = ["Who is the current President of the United States?", "Capital city of Australia?", "Painter of the Mona Lisa?",
      "Largest ocean in the world?", "Playwright of Romeo and Juliet?", "Currency of Japan?", "Discoverer of gravity?",
      "Red Planet?", "Author of Harry Potter book series?", "Tallest mountain in the world?"]

ans = ["Biden", "Canberra", "da Vinci", "Pacific", "Shakespeare", "Yen", "Newton", "Mars", "Rowling", "Everest"]

m = 0

while True:
    a = random.randint(0, len(li) - 1)
    print(li[a])
    resu = input("Give ans:")
    if resu == ans[a]:
        m += 5000
    print("Correct answer! You win:", m, "rupees")
    if m == 30000:
        break
