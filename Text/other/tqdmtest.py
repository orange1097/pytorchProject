import sys
from tqdm import tqdm, trange
import time
"""
iterable=None，可迭代对象。如上一节中的range(20)
desc=None，传入str类型，作为进度条标题。如上一节中的desc='It\'s a test'
total=None，预期的迭代次数。一般不填，默认为iterable的长度。
leave=True，迭代结束时，是否保留最终的进度条。默认保留。
file=None，输出指向位置，默认是终端，一般不需要设置。
ncols=None，可以自定义进度条的总长度
unit，描述处理项目的文字，默认’it’，即100it/s；处理照片设置为’img’，则为100img/s
postfix，以字典形式传入详细信息，将显示在进度条中。例如postfix={'value': 520}
unit_scale，自动根据国际标准进行项目处理速度单位的换算，例如100000it/s换算为100kit/s
————————————————
版权声明：本文为CSDN博主「雪的期许」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/winter2121/article/details/111356587
"""
# Test:  27%|██▋       | 27/100 [00:05<00:15,  4.86it/s, loss=0.27, x=27]
with tqdm(range(100), desc='Test',file=sys.stdout) as tbar:
    for i in tbar:
        tbar.set_postfix(loss=i/100, x=i)
        tbar.update()  # 默认参数n=1，每update一次，进度+n
        time.sleep(0.2)
