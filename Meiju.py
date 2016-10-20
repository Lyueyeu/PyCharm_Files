from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__items():
    print(name, '=>',member,',',member.value)