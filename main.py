def lengthOfLastWord(s: str) -> int:
        sl = s.split(' ')
        k = 0
        for i in range(len(sl)):
            if sl[i] == '':
                k += 1
        for i in range(k):
             sl.remove('')
             
        return len(sl[-1])

print(lengthOfLastWord(s="   fly me   to   the moon  "))