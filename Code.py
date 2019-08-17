# for this mode means the result of fraction from the division

fiveOO = int(input("Enter the change: "))
print ("# 500 notes:",int(fiveOO/500))

#mode for 500 notes
first_mode=fiveOO%500


oneOO =first_mode/100
print("# 100 notes:",int(oneOO))
# mode for 100 notes
second_mode=first_mode%100

fifty=second_mode/50
print("# 50 notes:",int(fifty))
# mode for 50 notes
third_mode=second_mode%50

twenty=third_mode/20
print("# 20 notes:",int(twenty))
fourth_mode=third_mode%20

ten=fourth_mode/10
print("# 10 coins:",int(ten))
fifth_mode=fourth_mode%10

five=fifth_mode/5
print("# 5 coins:",int(five))
sixth_mode=fifth_mode%5

one=sixth_mode/1
print("# 1 coins:",int(one))
