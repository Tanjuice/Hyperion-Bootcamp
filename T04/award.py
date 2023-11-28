
#  Inputs
time_swimming = int(input("How many minutes for the swimming round? "))
time_cycling = int(input("How many minutes for the cycling round? "))
time_running = int(input("How many minutes for the running round? "))

time_total = time_swimming + time_cycling + time_running

print(f"\nYour total time is:\n{time_total} minutes\n")

if time_total >= 111:
  print("Award: \nSorry you didnt qualify for an award\n")
elif time_total >= 106:
  print("Award: \nYou recieve the:\n Provincial Scroll!\n")
elif time_total >= 101:
  print("Award: \nYou recieve the: \nProvincial Half Colours!\n")
else: # Changed to else from elif based on feedback
  print("Award: \nYou will recieve the: \nProvincial Colours!!\n")