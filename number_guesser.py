def ai_guess_number():
    print("Think of a number between 1 and 100. I will guess it!")
    input("Press Enter when ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").strip().upper()
        if feedback == 'C':
            print(f"I guessed your number in {attempts} tries!")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("Please respond with H, L, or C.")

ai_guess_number()
