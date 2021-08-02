# Lineair keuzeverhaal sjabloon
# Mogelijke verhaallijnen:
# 1 > 3 > 7  > 15 > Einde
# 1 > 3 > 7  > 16 > Einde
# 1 > 3 > 8  > 17 > Einde
# 1 > 3 > 8  > 18 > Einde
# 1 > 4 > 9  > 19 > Einde
# 1 > 4 > 9  > 20 > Einde
# 1 > 4 > 10 > 21 > Einde
# 1 > 4 > 10 > 22 > Einde
# 1 > 5 > 11 > 23 > Einde
# 1 > 5 > 11 > 24 > Einde
# 1 > 5 > 12 > 25 > Einde
# 1 > 5 > 12 > 26 > Einde
# 1 > 6 > 13 > 27 > Einde
# 1 > 6 > 13 > 28 > Einde
# 1 > 6 > 14 > 29 > Einde
# 1 > 6 > 14 > 30 > Einde 

v0 = "0"
v1 = "1"
v2 = "2"
v3 = "3"
v4 = "4"
v5 = "5"
v6 = "6"
v7 = "7"
v8 = "8"
v9 = "9"
v10 = "10"
v11 = "11"
v12 = "12"
v13 = "13"
v14 = "14"
v15 = "15"
v16 = "16"
v17 = "17"
v18 = "18"
v19 = "19"
v20 = "20"
v21 = "21"
v22 = "22"
v23 = "23"
v24 = "24"
v25 = "25"
v26 = "26"
v27 = "27"
v28 = "28"
v29 = "29"
v30 = "30"
error = "Kies 1 of 2\n"

storyline = False
while not storyline:
    try:
      keuze_v0 = int(input(v0))
      if keuze_v0 == 1:
        storyline = False
        while not storyline:
            try:
              keuze_v1 = int(input(v1))
              if keuze_v1 == 1:
                storyline = False
                while not storyline:
                    try:
                      keuze_v3 = int(input(v3))
                      if keuze_v3 == 1:
                        storyline = False
                        while not storyline:
                            try:
                              keuze_v7 = int(input(v7))
                              if keuze_v7 == 1:
                                  print(v15)
                                  storyline = True
                              elif keuze_v7 == 2:
                                  print(v16)
                                  storyline = True
                              else:
                                  print(error)
                            except ValueError:
                                print(error)
                      elif keuze_v3 == 2:
                        storyline = False
                        while not storyline:
                            try:
                              keuze_v8 = int(input(v8))
                              if keuze_v8 == 1:
                                  print(v17)
                                  storyline = True
                              elif keuze_v8 == 2:
                                  print(v18)
                                  storyline = True
                              else:
                                  print(error)
                            except ValueError:
                                  print(error)
                    except ValueError:
                        print(error)
              elif keuze_v1 == 2:
                storyline = False
                while not storyline:
                    try:
                      keuze_v4 = int(input(v4))
                      if keuze_v4 == 1:
                        storyline = False
                        while not storyline:
                            try:
                              keuze_v9 = int(input(v9))
                              if keuze_v9 == 1:
                                  print(v19)
                                  storyline = True
                              elif keuze_v9 == 2:
                                  print(v20)
                                  storyline = True
                              else:
                                  print(error)
                            except ValueError:
                                  print(error)
                      elif keuze_v4 == 2:
                        storyline = False
                        while not storyline:
                            try:
                              keuze_v10 = int(input(v10))
                              if keuze_v10 == 1:
                                  print(v21)
                                  storyline = True
                              elif keuze_v10 == 2:
                                  print(v22)
                                  storyline = True
                              else:
                                  print(error)
                            except ValueError:
                                print(error)
                    except ValueError:
                        print(error)
            except ValueError:
                print(error)
      elif keuze_v0 == 2:
          storyline = False
          while not storyline:
              try:
                  keuze_v2 = int(input(v2))
                  if keuze_v2 == 1:
                      storyline = False
                      while not storyline:
                          try:
                              keuze_v5 = int(input(v5))
                              if keuze_v5 == 1:
                                  storyline = False
                                  while not storyline:
                                      try:
                                          keuze_v11 = int(input(v11))
                                          if keuze_v11 == 1:
                                              print(v23)
                                              storyline = True
                                          elif keuze_v11 == 2:
                                              print(v24)
                                              storyline = True
                                          else:
                                              print(error)
                                      except ValueError:
                                          print(error)
                              elif keuze_v5 == 2:
                                  storyline = False
                                  while not storyline:
                                    try:
                                          keuze_v12 = int(input(v12))
                                          if keuze_v12 == 1:
                                              print(v25)
                                              storyline = True
                                          elif keuze_v12 == 2:
                                              print(v26)
                                              storyline = True
                                          else:
                                              print(error)
                                    except ValueError:
                                              print(error)
                              else:
                                  print(error)
                          except ValueError:
                                  print(error)
                  elif keuze_v2 == 2:
                      storyline = False
                      while not storyline:
                          try:
                              keuze_v6 = int(input(v6))
                              if keuze_v6 == 1:
                                  storyline = False
                                  while not storyline:
                                      try:
                                          keuze_v13 = int(input(v13))
                                          if keuze_v13 == 1:
                                              print(v27)
                                              storyline = True
                                          elif keuze_v13 == 2:
                                              print(v28)
                                              storyline = True
                                          else:
                                              print(error)
                                      except ValueError:
                                          print(error)
                              elif keuze_v6 == 2:
                                  storyline = False
                                  while not storyline:
                                      try:
                                          keuze_v14 = int(input(v14))
                                          if keuze_v14 == 1:
                                              print(v29)
                                              storyline = True
                                          elif keuze_v14 == 2:
                                              print(v30)
                                              storyline = True
                                          else:
                                              print(error)
                                      except ValueError:
                                          print(error)
                          except ValueError:
                              print(error)
                  else:
                      print(error)
              except ValueError:
                      print(error)
      else:
        print(error)
    except ValueError:
        print(error)

print("Einde")
print("\n") 
print("     oooOOOOOOOOOOO'")
print("    o   ____          :::::::::::::::::: :::::::::::::::::: __|-----|__")
print("   _Y_,_|[]| --++++++ |[][][][][][][][]| |[][][][][][][][]| |  [] []  |")
print("  {_|_|_|__|;|______|;|________________|;|________________|;|_________|;")
print("    /oo--OO   oo  oo   oo oo      oo oo   oo oo      oo oo   oo     oo")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")       