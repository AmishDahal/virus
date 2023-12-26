
import time  , rotatescreen as rs 
pd = rs.get_primary_display()
angel_list =  [90, 180, 270, ]
while True :
 for x in angel_list :
  pd.rotate_to(x)
  time.sleep(0,5) #the code is not (0.5) to annoy the user as even if you uninstall the code or python file running it will still work

