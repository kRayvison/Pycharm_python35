taskID='adf'
import os

import re
k_input_proj = r"r'\\10.60.200.102\d\inputdata5\1929000\1929198'"
k_input_file = r"r'F:\New_Project\scenes\donghua\donghua\2\6\L\cha_hua_lan_dong_hua.0009.mb'"
k_exp = r"^(r)(').*(')$"


if re.findall(k_exp, k_input_file):
    re.sub(k_exp, '', k_input_file)

a=r"r'\\\\10.60.100.102\\d\\inputdata5\\1863500\\1863567/few/fwf'"
import os
a=eval(a)
#print (os.path.normpath(a))

k_input_file = r'I:\\bingma\\yancao.mb'
k_exp = r"(?<name>\w)(:)"
a=re.findall(k_exp,k_input_file)
print (a)
g_input_file = re.sub(k_exp, '1',k_input_file,0)
print (g_input_file)




def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";

    def _add111(matched):
        intStr = matched.group("number");  # 123
        intValue = int(intStr);
        addedValue = intValue + 111;  # 234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr, 2);
    print("replacedStr=", replacedStr)  # hello 234 world 567 nihao 789


###############################################################################
if __name__ == "__main__":
    pythonReSubDemo()

