print("Gradebook Builder!!!")
print()
test = input("Which test did you appear for?: ")
print()
score = float(input("How much did you score?: "))
out_of = int(input("Out of?: "))

print()
percent = float((score/out_of)*100)
print("Your percentage is: ",percent,"%")
res = round(percent,2)
print("Your result is",res)

if res>=80:
  print("Grade E which stands for Exceptional!")
elif res>=50 and res<80:
  print("Grade A")
elif res >=30 and res<50:
  print("Grade B, you can do better!")
else:
  print("Grade F which is FAILED")
  
