while 1:
  tech = input("===========MENU========= \n 1. to access calculator app \n 2. spin 'em dreidels\n 3. coins doing backflips \n 4. gamble all your money away with our cutting edge lottery machine\n 5. the epitome of every childrens game: the spinner, a revoluntionary piece of technology created by earths greatet minds to educate our youth")
  if tech == "1":
    import calculator
  if tech == "2":
    import dreidel
  if tech == '3':
    import flip_a_coin
  if tech == '4':
    import lottery
  if tech == '5':
    import spinner
