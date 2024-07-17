
def score(var):
   result=""
   if 81<=var<=100:
      result="A"
   elif 61<=var<=80:
      result="B"
   elif 41<=var<=60:
      result="C"
   elif 21<=var<=40:
      result = "D"
   else:
      result="F"
   return result
print(score(88))