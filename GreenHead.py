# Just A Fun Python2.7 Script
# AlirezaKarimi
# Email:Alireza.karimi.67@gmail.com
# Tell:+989362397176


def main():
    again = 'yes'
    while again == 'yes':
        try:
            head, tongue = raw_input('Enter Your Head and Tongue Color Seprated By Space = ').split()
            if head == 'green' and tongue == 'red':
                print 'You are a Dead Man , See you in another side ... '
                return 0
            else:
                print 'You Still Alive Broo , You have got another chance'
                again = raw_input('Do You Wish Continue (yes|no) ? ')
        except Exception as e:
            raw_input('Enter Your head and tongue color Seprated by space,you enter just one color !')

if __name__ == "__main__":
    main()
