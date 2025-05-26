class Solution:
    def __init__(self):
        self.stack = []

    def push_character(self, ch):
        self.stack.append(ch)

    def pop_character(self):
        return self.stack.pop()


def check_palindrome(s):
    obj = Solution()


    for char in s:
        obj.push_character(char)


    is_palindrome = True
    for i in range(len(s)):
        if s[i] != obj.pop_character():
            is_palindrome = False
            break

    if is_palindrome:
        return f"The word, '{s}', is a palindrome."
    else:
        return f"The word, '{s}', is not a palindrome."


def main():
    s = input("Enter a word to check if it is a palindrome: ").strip()

    if not s.isalpha():
        print("Please enter a valid word.")
        return

    print(check_palindrome(s.lower()))


if __name__ == "__main__":
    main()
