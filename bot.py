while True:
  user=input("you:")
  if user.lower() in["hi" ,"hello"]:
    print("bot:good morning")
  elif user.lower() in["how are you"]:
    print("bot:i'm fine")
    continue
  else:
      print("bot:good bye")     