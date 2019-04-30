def series_sum(n):
   num = 0
   den = 1
   
   for i in range(0, n):
       next_num = 1
       next_den = i * 3 + 1
       
       num = num * next_den + den * next_num
       den *= next_den
   
   return "%0.2f" % round(num / den, 2)
