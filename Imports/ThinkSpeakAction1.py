"""Standard Library comes with Python
Useful methods"""


#Random
import random

ክፉ_ቃል = ['1/ ክፉን ስታስቡት ታፍራላችሁ', '2/ ክፉን ስትናገሩት ትጸጸታላችሁ', '3/ ክፉን ስታደርጉት ታሰራጩታላችሁ',
         '4/ ክፉን ፊት ስታቆሙት ታስፈራራላችሁ', '5/ ክፉን ስትጠልቁበት በክፉው ትሰወራላችሁ።',
         '6/ ክፉን ስትናዘዙት የፍቅር እስከትጠነክሩ ትሠራላችሁ', '7/ ክፉን ስታቆሙት ትደሰታላችሁ ትነሳላችሁ። ']

random.shuffle(ክፉ_ቃል)
print(ክፉ_ቃል)
# print(ክፉ_ቃል.sort)
print(random.randint(1,5))
