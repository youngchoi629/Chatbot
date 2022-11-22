# Youngshin's Chatbot
import webbrowser
import time

print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print("H                                                   H")
print("H  MEMEM  M   M   MEM   MEMEM  MEMEM  MEMEM  MEMEM  H")
print("H  E      E   E  E   E    E    E   M  E   E    E    H")
print("H  M      MEMEM  MEMEM    M    MEME   M   M    M    H")
print("H  E      E   E  E   E    E    E   M  E   E    E    H")
print("H  MEMEM  M   M  M   M    M    MEMEM  MEMEM    M    H")
print("H                                                   H")
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
print(".\n.\n.")
print("\nHello, My name is CHATBOT.\n")
print("Please type all your responses in lower case letters.\n")

user_name = input("What's your name?\n")

print("\nNice to meet you, ", user_name)
    
x = 0

while True:

    # main program starts here
    
    day = input("\nHow's your day? Good? Bad?\n")

    # asks user about their day

    if((day == "bad") or (day == "notgood") or (day == "notgreat")):
        what_happened = input("What happened?\n")
        
        print("That's too bad...")
        break

    if((day == 'good') or (day == 'alright') or (day == 'prettygood') or (day == 'awesome')):
        print("\nOh, that's nice, my day is going great as well.")
        break

    else:
        print("I don't quite understand... try again\n")

        # asks for another response


while True:
    print("\nWhat do you want to do?\n")

    # tasks and conversations

    bot_task = input("1. Command basic tasks\n2. Have a conversation about music\n3. Stop program\n")


    if (bot_task == "3"):
        
        # shuts down program if user chooses 3
        
        print("You chose to stop the program.")

        exit()


    elif (bot_task == "1"):
        
        # code for task 1 (command basic tasks)
        
        while True:
            print("You chose to do basic tasks.\n")
            basic_task = input("What basic task do you want me to do?\n1. Check the Date & Time\n2. Check the Weather\n3. Check the News\n")

            # asks user what basic task he/she wants the bot to do
            
            if basic_task == "1":

                # prints date & time
                
                print("You chose to check the date & time.")



                print ("the current time is: ", time.strftime('%m/%d/%Y %H:%M:%S'))
                
                time.sleep(1.5) # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program

                if((restart == "X") or (restart == "x")):
                    #returns to first page
                    
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    # ends program
                    
                    quit()
                    

            if basic_task == "2":

                # directs user to weather site

                print("You chose to check the weather.")
                print("You will be directed to a weather site shortly.\n")

                webbrowser.open("https://www.weather.com/")

                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program

                if((restart == "X") or (restart == "x")):
                    #returns to first page if user presses X
                    
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    # ends program if user presses Y
                    
                    quit()


            elif(basic_task == "3"):

                # directs user to news site

                print("You chose to check the news.")
                print("You will be directed to a news site shortly.\n")
        
                webbrowser.open("https://www.cnn.com/")


                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program

                if((restart == "X") or (restart == "x")):
                    #returns to first page if user presses X
                    
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    # ends program if user presses Y
                    
                    quit()


            else:

                # returns to previous step when user doesn't enter valid number
                
                print("\nEnter a valid number.\n")

               
            

    elif (bot_task == "2"):

    
        # code for task 2 (have a conversation about music)
        
    
        print("You chose to have a conversation about music.\n")

        while True:
            music = input("What kind of genre of music do you like?\n")

            # asks user about music genre
            
            if((music == "rock") or (music == "pop")):

                # maybe rock or pop??
                
                print("Awesome! I love Queen and AC/DC.\n")
                
                while True:
                    band = input("What's your favorite band or musician?\n")

                    if((band == "taylorswift") or (band == "nickiminaj")):
                        
                        # not taylorswift and nickiminaj!!! perhaps someone else?
                        
                        print("Oof, any other favorites?\n")

                    else:

                        # that's better...
                        
                        print(band,"is pretty cool\n")
                        break

                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program

                if((restart == "X") or (restart == "x")):
                    #returns to first page if user presses X
                    
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    # ends program if user presse Y
                    
                    quit()
                    

            elif(music == "classical"):
                
                # maybe classical music is your jam?
                
                classical = input("\nWhat's your favorite classical piece?\n")

                print("\nThat's cool.\n")
                print("My favorite's Hydn's trumpet concerto (3rd Mov.) and Mozart's Violin Concerto No. 3.\n")

                # asks user if he/she wants to listen to one of them
                
                classical_response = input("Do you want to listen to one of them?\n")
                if((classical_response == "yes") or (classical_response == "sure") or (classical_response == "absolutely")):
                    
                   # directs user to youtube video

                    webbrowser.open("https://www.youtube.com/watch?v=IhQAtkXOK6o")


                elif((classical_response == "no") or (classical_response == "i'm good")):
                    print("\nOh... Okay.\n")
                    

                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program
                
                if((restart == "X") or (restart == "x")):
                    # returns to first page if user presses X
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    #ends program if user presses Y
                    quit()


            elif(music == "edm"):

                # you can't hate edm, can you?
                
                edm = input("Who's your favorite artist?\n")
                print(edm, "'s music is great.\n")
                print("I love Avicii and Kygo.\n")
                
                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program
                
                if((restart == "X") or (restart == "x")):
                    # returns to first page if user presses X
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    #ends program if user presses Y
                    quit()



            elif(music == "rap"):

                print("Sorry, I don't know much about rap.\n")

                # asks user to recommend rap song
                
                rap_rec = input("What rap song do you recommend?\n")

                print("Thanks! I'll keep that in mind")

                time.sleep(1.5)

                # wait for 1.5 seconds
                
                print(".\n.\n.\n")
                restart = input("If you want to restart program, press X.\nIf you want to terminate the program, press Y.\n")

                # asks user if he/she wants to restart program
                
                if((restart == "X") or (restart == "x")):
                    #returns to first page if user presses X
                    break
                    
                if((restart == "Y") or (restart == "y")):
                    #ends program if user presses Y
                    quit()