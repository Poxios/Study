# Playing with Date
Remember!! saving date with `new Date('Blah Blah')`   
-> `Blah Blah` means local time,  
-> Date instance means utc time.
  
If there is no HH:MM in `Blah Blah`, default UTC value will be saved like 2020-10-01 00:00 (UTC).  
So, if you print this date instance, date in our system prints 09:00.