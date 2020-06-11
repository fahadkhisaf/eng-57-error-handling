# while True:
#     try:
#         user_input = int(input("Enter any number to continue: "))
#     except ValueError:
#         print("Input must be a number from 1-9: ")
#     else:
#         print("Thank you, entry successful!")

# try:
#   print(x)
# except:
#   print("An exception occurred")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")