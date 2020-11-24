COUPON_REQUIREMENT = 7  # constant for coupon requirements
couponBalance = 0  # initializing coupon balance
choice = 'p'

while True:  # used to repeat menu, shut down is checked later
    purchaseChoice = input("Menu:\nP (process Purchase)" + "\nS (Shut down)")  # getting user choice
    charChoice = purchaseChoice.lower()[0]  # getting lower case of first character

    print("Your choice: " + purchaseChoice)

    if charChoice == 's':  # checking if user wants to exit
        print("System shutting down.\n\n" + "Good bye")
        break  # ends loop and thus program

    if charChoice != 'p':  # checking if input is invalid
        print("*** Use P or S, please. ***\n")

    if charChoice == 'p':  # if purchase choice is chosen
        if couponBalance < 7:  # starting normal transaction
            barNumber = int(input("How many chocolate bars would you like to buy?"))

            if barNumber >= 0:  # checking for valid inputs
                couponBalance += barNumber
                print("You just earned " + str(barNumber) +
                      " coupons and have a total of " + str(couponBalance) + " to use.\n")
                # display coupons acquired and total coupons

            else:  # checking for invalid response
                print("*** Invalid response ***")

        elif couponBalance >= 7:  # starts award transaction
            awardChoice = input("You qualify for a free chocolate bar. Would you like to use your credits? (Y or N) ")[
                0]

            if awardChoice == 'y' or awardChoice == 'Y':  # if user wants to use coupons
                couponBalance -= COUPON_REQUIREMENT
                print("You have just used " + str(COUPON_REQUIREMENT) + " coupons and have "
                      + str(couponBalance) + " left.\nEnjoy your free chocolate bar.\n")

            elif awardChoice == 'n' or awardChoice == 'N':
                barNumber = int(input("How many chocolate bars would you like to buy?"))

                if barNumber >= 0:  # checking for valid input
                    couponBalance += barNumber
                    print("You just earned " + str(barNumber) +
                          " coupons and have a total of " + str(couponBalance) + " to use.\n")

                else:  # if invalid input is entered
                    print("*** Invalid response ***")

            else:  # if invalid input is entered
                print("*** Invalid response ***\n")

#  wow that took only 55 lines compared to the 109 lines in Java
