def main():
    #write your code below this line
    score = int(input('Give points [0-100]:'))
    if (score < 0):
      print('Grade: impossible!')
    elif (score <=49):
      print('Grade: failed')
    elif (score <=59):
      print('Grade: 1')
    elif (score <=69):
      print('Grade: 2')
    elif (score <=79):
      print('Grade: 3')
    elif (score <=89):
      print('Grade: 4')
    elif (score <=100):
      print('Grade: 5')
    else:
      print('Grade: incredible!')

if __name__ == '__main__':
    main()
