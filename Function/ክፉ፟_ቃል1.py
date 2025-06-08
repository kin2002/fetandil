"""Standard Library comes with Python
Useful methods"""


#Random
import random
from random import choice

ክፉ_ቃል = ['1/ ክፉን ስታስቡት ታፍራላችሁ', '2/ ክፉን ስትናገሩት ትጸጸታላችሁ', '3/ ክፉን ስታደርጉት ታሰራጩታላችሁ',
         '4/ ክፉን ፊት ስታሳዩት ታስፈራላችሁ', '5/ ክፉን ስትጠልቁበት በክፉው ትሸፈናላችሁ።',
         '6/ ክፉን ስትናዘዙት የፍቅር እስከትጠነክሩ ትሠራላችሁ', '7/ ክፉን ስታቆሙት ትደሰታላችሁ ትነሳላችሁ። ']

ስም = ['አበበ', 'በቀለ', 'ገመቹ', 'ደስታ', 'ሀብቶም', 'ወልደየስ', 'ዘነበ ']
random.shuffle(ክፉ_ቃል)
print(ክፉ_ቃል)
# print(ክፉ_ቃል.sort)
print(random,choice(ስም))
print(random.randint(1,5))

