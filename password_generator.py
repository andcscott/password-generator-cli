import secrets

class PasswordGenerator():
    """
    Password Generator class to create random passwords based on the users
    preferences for uppercase, numbers, and symbols. Ambiguous characters
    ('l' [Lower case L], '1' [one], I [capital i], O [capital o], 0 [zero]) are
    omitted by default.
    """

    def __init__(self, length, uchars, nums, symbols):
        """
        Initializes a PasswordGenerator object. Includes private data members
        for the possible upper and lowercase letters, numbers, symbols, and the
        set of characters available for password creation based on user input.
        Takes the users desired password length, and whether to use uppercase
        letters, numbers, and symbols as parameters.
        """

        self._lchars = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                        's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c',
                        'v', 'b', 'n', 'm')
        self._uchars = ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A',
                        'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
                        'V', 'B', 'N', 'M')
        self._nums = ('2','3','4','5','6','7','8','9')
        self._symbols = ('!', '@', '#', '$', '%', '^', '&', '*')
        self._available_chars = self._lchars
        self._length = length
        self._use_uchars = uchars
        self._use_nums = nums
        self._use_symbols = symbols


    def use_upper(self):
        """
        Checks if the user wants uppercase letters in the password. If yes,
        adds the uppercase letters to possible characters for the password.
        """
        if self._use_uchars.lower() == 'n':
            return
        else:
            self._available_chars += self._uchars

    def use_nums(self):
        """
        Checks if the user wants numbers in the password. If yes, adds
        the numbers to the possible characters for the password.
        """
        if self._use_nums.lower() == 'n':
            return
        else:
            self._available_chars += self._nums

    def use_symbols(self):
        """
        Checks if the user wants symbols in the password. If yes, adds the
        symbols to the possible characters for the password."
        """
        if self._use_symbols.lower() == 'n':
            return
        else:
            self._available_chars += self._symbols

    def create_password(self):
        """
        Uses the use_upper, use_nums, and use_symbols methods to determine the
        possible characters that should be considered and generates the
        password.
        """
        self.use_upper()
        self.use_nums()
        self.use_symbols()
        password = ''.join(secrets.choice(self._available_chars) for i in range(self._length))
        print('\nYour new password is: ', password+'\n')

def main():
    """
    Main function to prompt user for password length, and whether to include
    uppercase letters, numbers, and symbols in the password. Uses the
    PasswordGenerator class and it's create_password member function to
    generate and print the new password to the console.
    """

    print('\n')
    print('======================')
    print('| Password Generator |')
    print('======================')
    print('\nNote that ambiguous characters such as 0 (zero) and O (capital o) \
are automatically excluded! Press Ctrl+C to quit.\n')

    length = ''
    while length is not int:
        try:
            length = int(input('How many characters for your password? '))
            break
        except ValueError:
            print('Please enter an integer.')

    use_uchars = input('Use uppercase? [Y/n] ')
    use_nums = input('Use numbers? [Y/n] ')
    use_symbols = input('Use symbols? [Y/n] ')

    PasswordGenerator(length, use_uchars, use_nums, use_symbols).create_password()

if __name__ == '__main__':
    main()
