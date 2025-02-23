def is_palindrome(text):
  

  processed_text = ''.join(filter(str.isalnum, text)).lower() 
  return processed_text == processed_text[::-1]

print(is_palindrome("level"))      
print(is_palindrome("madam"))      
print(is_palindrome("A man, a plan, a canal: Panama"))  
print(is_palindrome("hello"))      
print(is_palindrome("Racecar"))    
print(is_palindrome("Was it a car or a cat I saw?")) 