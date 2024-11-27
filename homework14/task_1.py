celsius_tup = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), 
(20, 25, 31), (21, 31, 28))

def get_data(x):
    tuple_day_average = ()
    tuple_day_max = ()
    tuple_day_min = ()
    tuple_week_average = ()

    for i in x:
        tuple_day_average += ((i[0] + i[1] + i[2])/3,)
        tuple_day_max += (max(i),)
        tuple_day_min += (min(i),)
    
    tuple_week_average = (sum(tuple_day_average)/len(tuple_day_average),)
    
    return tuple_day_average, tuple_day_max, tuple_day_min, tuple_week_average

print(get_data(celsius_tup))