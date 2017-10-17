"""
Author: John Bonney; Date: 10.16.17
DIGHT 360 - Homework 6

Create a single program that:
1. Creates 6 separate word lists, one for each of the 6 registers in the
Mini-CORE corpus
2. Writes each of these word lists to separate files, ordered according to
frequency (highest frequency first).
3. Try to exclude all function words from your frequency lists. You can use the
list on the following webpage (see the complete list at the bottom of the
page): http://myweb.tiscali.co.uk/wordscape/museum/funcword.html
4. In 1-2 paragraphs, describe any differences you see between the lists. What
can you learn about these registers based on these differences?

"""

import os
import re
from nltk.probability import FreqDist
from glob import glob
from nltk import word_tokenize

os.chdir(r'C:\Users\johnf\Downloads\Mini-CORE\Mini-CORE')

function_wordstr = ("A ABOUT ABOVE AFTER AGAIN AGO ALL ALMOST ALONG ALREADY " +
    "ALSO ALTHOUGH ALWAYS AM AMONG AN AND ANOTHER ANY ANYBODY ANYTHING " +
    "ANYWHERE ARE AREN'T AROUND AS AT BACK ELSE BE BEEN BEFORE BEING BELOW " +
    "BENEATH BESIDE BETWEEN BEYOND BILLION BILLIONTH BOTH EACH BUT BY CAN " +
    "CAN'T COULD COULDN'T DID DIDN'T DO DOES DOESN'T DOING DONE DON'T DOWN " +
    "DURING EIGHT EIGHTEEN EIGHTEENTH EIGHTH EIGHTIETH EIGHTY EITHER ELEVEN " +
    "ELEVENTH ENOUGH EVEN EVER EVERY EVERYBODY EVERYONE EVERYTHING " +
    "EVERYWHERE EXCEPT FAR FEW FEWER FIFTEEN FIFTEENTH FIFTH FIFTIETH FIFTY " +
    "FIRST FIVE FOR FORTIETH FORTY FOUR FOURTEEN FOURTEENTH FOURTH HUNDRED " +
    "FROM GET GETS GETTING GOT HAD HADN'T HAS HASN'T HAVE HAVEN'T HAVING HE " +
    "HE'D HE'LL HENCE HER HERE HERS HERSELF HE'S HIM HIMSELF HIS HITHER HOW " +
    "HOWEVER NEAR HUNDREDTH I I'D IF I'LL I'M IN INTO IS I'VE ISN'T IT ITS " +
    "IT'S ITSELF JUST LAST LESS MANY ME MAY MIGHT MILLION MILLIONTH MINE " +
    "MORE MOST MUCH MUST MUSTN'T MY MYSELF NEAR NEARBY NEARLY NEITHER NEVER " +
    "NEXT NINE NINETEEN NINETEENTH NINETIETH NINETY NINTH NO NOBODY NONE " +
    "NOONE NOTHING NOR NOT NOW NOWHERE OF OFF OFTEN ON OR ONCE ONE ONLY " +
    "OTHER OTHERS OUGHT OUGHTN'T OUR OURS OURSELVES OUT OVER QUITE RATHER " +
    "ROUND SECOND SEVEN SEVENTEEN SEVENTEENTH SEVENTH SEVENTIETH SEVENTY " +
    "SHALL SHAN'T SHE'D SHE SHE'LL SHE'S SHOULD SHOULDN'T SINCE SIX SIXTEEN " +
    "SIXTEENTH SIXTH SIXTIETH SIXTY SO SOME SOMEBODY SOMEONE SOMETHING " +
    "SOMETIMES SOMEWHERE SOON STILL SUCH TEN TENTH THAN THAT THAT THAT'S THE " +
    "THEIR THEIRS THEM THEMSELVES THESE THEN THENCE THERE THEREFORE THEY " +
    "THEY'D THEY'LL THEY'RE THIRD THIRTEEN THIRTEENTH THIRTIETH THIRTY THIS " +
    "THITHER THOSE THOUGH THOUSAND THOUSANDTH THREE THRICE THROUGH THUS TILL " +
    "TO TOWARDS TODAY TOMORROW TOO TWELFTH TWELVE TWENTIETH TWENTY TWICE TWO " +
    "UNDER UNDERNEATH UNLESS UNTIL UP US VERY WHEN WAS WASN'T WE WE'D WE'LL " +
    "WERE WE'RE WEREN'T WE'VE WHAT WHENCE WHERE WHEREAS WHICH WHILE WHITHER " +
    "WHO WHOM WHOSE WHY WILL WITH WITHIN WITHOUT WON'T WOULD WOULDN'T YES " +
    "YESTERDAY YET YOU YOUR YOU'D YOU'LL YOU'RE YOURS YOURSELF YOURSELVES " +
    "YOU'VE")
func_w_list = [w.lower() for w in function_wordstr.split()]
func_w_list += ['[', ']', ',', '.', '``', "''", ')', '(', ':', '--', ';']
function_words = set(func_w_list)


fd = {'SP': FreqDist(), 'IP': FreqDist(), 'NA': FreqDist(), 'OP': FreqDist(),
      'LY': FreqDist(), 'IN': FreqDist()}


for file in glob('*[0-9].txt'):
    register = file.split('+')[1]
    print(register)
    with open(file) as f:
        for line in f:
            if re.search('<[hp]>', line):
                words = word_tokenize(line.lower())
                fresh_words = [n for n in words[3:] if n not in function_words]
                fd[register].update(fresh_words)

for key in ['SP', 'IP', 'NA', 'OP', 'LY', 'IN']:
    title = key + '_FreqDist.txt'
    with open(title, 'w') as s:
        for item in sorted(fd[key].most_common(), key=lambda x: x[1],
                           reverse=True):
            s.write(item[0] + ', ' + str(item[1]) + '\n')
