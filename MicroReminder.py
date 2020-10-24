import microbit
from win10toast import ToastNotifier
import time
import os
import sys

toaster = ToastNotifier()

def reminder_function():
    x = 1
    i = 2
    
    microbit.display.show(microbit.Image.YES)
    remind = input("What do you want to remind?: ")

    try:
        minute = int(input("How many minutes later will it remind you?: "))
        if minute <=0:
            print("Please enter a valid value and restart the code")
            raise SystemExit
    except ValueError:
        print("Please enter a valid value and restart the code")
        raise SystemExit

    while x<5:
      x += 1
      microbit.display.show(microbit.Image.YES)
      time.sleep(1)
      microbit.display.clear()
      break

    while True:
      while (i>1):
        i -= 1
        microbit.display.scroll(str(minute))
      microbit.display.show(str(minute))
      if microbit.button_a.is_pressed():
        minute += 5
        microbit.display.scroll(str(minute))

      elif microbit.button_b.is_pressed():
        toaster.show_toast("Micro:Reminder", "Counter Started!", threaded=True, icon_path=None, duration=3)
        microbit.display.clear()

        while True:
          t_end = time.time() + 60 * 1
          t_end_2 = time.time() + int(minute)*60
          microbit.display.show(str(minute))
          print(minute, "Minutes remaining!")

          while True:
            while True:
              microbit.display.scroll(str(minute))
              if time.time()>t_end:
                break
              elif microbit.button_a.is_pressed():
                print("Counter Stopped!")
                microbit.display.show(str(minute))
                if sys.platform == 'win32':
                    os.system("pause")
                else:
                    input("Press any key to continue . . .")
                print(minute, "Minutes remaining!")

            if time.time()>t_end:
              minute-=1
              break
          if time.time()>t_end_2:
            break

        if minute == 0:
          print("0 Minutes remaining!")
          for a in range(0,3):
            square = microbit.Image("99999:90009:90009:90009:99999")
            half_square = microbit.Image("00000:09990:09090:09990:00000")
            dot = microbit.Image("00000:00000:00900:00000:00000")

            microbit.display.show(square)
            time.sleep(0.3)
            microbit.display.show(half_square)
            time.sleep(0.3)
            microbit.display.show(dot)
            time.sleep(0.3)

          toaster.show_toast("Micro:Reminder", f"{remind} Time!", threaded=True, icon_path=None, duration=3)
          microbit.display.clear()
          break

while True:
    reminder_function()
