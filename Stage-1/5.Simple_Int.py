#Calculate simple interest
# I = Simple Interest
# P = Principal amount (the initial money borrowed or invested)
# R = Annual rate of interest (as a percentage)
# T = Time duration(typically in year)
P = float(input("Principal amount in Rs. : "))
R = float(input("Annual rate of interest : "))
T = float(input("Time duration : "))
cal = (P*R*T)/100
print(f"Your Simple interest I = {cal} /-")
# O(1)