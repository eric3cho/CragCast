from datetime import date

# flow: get date > check area temps > determine if good conditions > display results
today = date.today()
print("Today is " + str(today) + ". I can CragCast up to 16 days in advance.")
days = input("What days are you climbing? Put in form 'start,end' (i.e. 11,13): ")



