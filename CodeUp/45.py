# time 모듈 사용
import time

t = time.time()
t = int(t//(3600*24*365))+1970
print(t)