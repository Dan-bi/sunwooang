import time
import progressbar

with progressbar.ProgressBar(max_value=10) as bar:
    for i in [9,10,3,6,7,1,2,3,6,8]:
        time.sleep(0.1)
        bar.update(i)