def factorial(num):
  if num == 1:
    return 1
  else:
    return factorial(num - 1) * num

def main():
  print(factorial(5))

if __name__ == '__main__':
  main()