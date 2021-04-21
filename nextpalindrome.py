# number = input()
# length = len(number)

# # If all digits are 9, the simply add 2 to it and print
# if length == number.count('9'):
#     print(int(number)+2)
# else:
#     # If number is Even
#     if length % 2 == 0:
#         half = length // 2
#         a = int(number[:half])
#         new_number = int(str(a)+str(a)[::-1])

#         if new_number > int(number):
#             print(new_number)
#         else:
#             new_number = int(str(a+1) + str(a+1)[::-1])
#             print(new_number)
#     # If number is Odd
#     else:
#         half = (length // 2) + 1
#         a = int(number[:half])
#         new_number = int(str(a)[0:half-1] + str(a)[::-1])

#         if new_number > int(number):
#             print(new_number)
#         else:
#             new_number = int(str(a+1)[0:half-1] + str(a+1)[::-1])
#             print(new_number)

class Palin:

    def NextPalindrome(self,n):
        n=str(n)
        if len(n)%2==0:
            m=(len(n)//2)
            
            s=n[:m]
            p=n[:m]+s[::-1]
            if (int(p)>int(n)):
                print(p)
            else:
                s=str(int(s)+1)
                p=s+s[::-1]
                print(p)
        else:
            m=(len(n)//2)+1 
            s=n[:m]
            p=s[:m-1]+s[::-1]
            if (int(p)>int(n)):
                print(p)
            else:
                s=str(int(s)+1)
                p=s[:m-1]+s[::-1]
                print(p)
                

g=Palin()
g.NextPalindrome(int(input()))