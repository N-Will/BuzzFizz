def fizzbuzz(limit):
  # Write your code here
  list = []
  for num in range(1,limit+1):
    if num%3 == 0 and num%5 == 0:
      temp2 = num
      temp2 = "FizzBuzz"
      list.append(temp2)

    elif num%3 == 0:
      temp = num 
      temp = "Fizz"
      list.append(temp)

    elif num%5 == 0:
      num = "Buzz"
      list.append(num)

    else:
      list.append(num)

  print(list)
#fizzbuzz(16)

ans = eval(input("What is your value?: "))
fizzbuzz(ans)
