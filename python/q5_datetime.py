# Hint:  use Google to find python function
from datetime import *

####a) 
date_start = '01-02-2013'
date_stop = '07-28-2015'

start = datetime.strptime(date_start, '%m-%d-%Y').date()
end = datetime.strptime(date_stop, '%m-%d-%Y').date()
print((end-start).days)


####b)  
date_start = '12312013'  
date_stop = '05282015'

start_d = int(date_start[2:4])
start_m = int(date_start[:2])
start_y = int(date_start[-4:])

start = date(start_y, start_m, start_d)

end_d = int(date_stop[2:4])
end_m = int(date_stop[:2])
end_y = int(date_stop[-4:])

end = date(end_y, end_m, end_d)

print((end-start).days)

####c)
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

start = datetime.strptime(date_start, '%d-%b-%Y').date()
end = datetime.strptime(date_stop, '%d-%b-%Y').date()
print((end-start).days)