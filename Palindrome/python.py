##-----------------------------------------		Method   ------------------------------------------------------
def isPalindrome(str):
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True


s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("PALINDROME")
else:
	print("Not PALI")

##-----------------------------------------		Method   ------------------------------------------------------
def isPalindrome(s):
	rev = ''.join(reversed(s))
	if (s == rev):
		return True
	return False

s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Plai")
else:
	print("Not pali")

##-----------------------------------------		Method   ------------------------------------------------------
x = "malasdf"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Pali")
else:
	print("Not Pali")
##-----------------------------------------		Method   ------------------------------------------------------
st = 'malayalam'
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("Not Plai")
else:
    print("Pali")

##-----------------------------------------		Method   ------------------------------------------------------
def isPalindrome(s):
	s = s.lower()
	l = len(s)
	if l < 2:
		return True
	elif s[0] == s[l - 1]:
		return isPalindrome(s[1: l - 1])
	else:
		return False


s = "MalaYaLam"
ans = isPalindrome(s)

if ans:
	print("Pali")

else:
	print("Not Pali")
