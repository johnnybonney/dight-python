"""
Assignment 2
Use regular expressions and lists to correctly identify and count all of the
nominalizations in a short text. You can simply paste a short text into string
variable in your script.

Turn in a very short write-up of your work on Learning Suite. Explain anything
about your decisions that isn't self-evident from your code. Your write-up
should include a link to your code on github or pythonanywhere.

For help on what kinds of nominalization there are in English, the following
site may be helpful: http://www.dailywritingtips.com/nominalized-verbs/
"""
import re

text_str = 'The partial participation of newcomers is by no means \
“disconnected” from the practice of interest. Furthermore, \nit is also a \
dynamic concept. In this sense, peripherality, when it is enabled, suggests \
an opening, a way of \ngaining access to sources for understanding through \
growing involvement. The ambiguity inherent in peripheral \nparticipation must \
then be connected to issues of legitimacy, of the social organization of and \
control over \nresources, if it is to gain its full analytical potential. \
Ecosystem destabilization can be the consequence of invasion.\nThis example \
provides an illustration of the problems with nominalizations. Failure to \
understand the applicability\nof programming in improving research intensity \
is a serious difficulty amongst faculty.'

print(text_str)
result1 = re.findall(r'\b\w+ing\b', text_str)
print(result1)
result2 = re.findall(r'\b\w\w+[ou]re?\b', text_str)
print(result2)
result3 = re.findall(r'\b\w+[st]ion\b', text_str)
print(result3)
result4 = re.findall(r'\b\w+[ae]nce\b', text_str)
print(result4)
result5 = re.findall(r'\b\w+ment\b', text_str)
print(result5)
result6 = re.findall(r'\b[a-eg-zA-EG-Z]\w+ty\b', text_str)
print(result6)

num_noms = len(result1) + len(result2) + len(result3) + len(result4) \
    + len(result5) + len(result6)
print("There are", num_noms, "nominalizations in this text.")
