pencils = int(input("enter the number of pencils"))
pens = int(input("enter the number of pens"))
felt_pens = int(input("enter the number of felt_pens"))
pencil_price = 3
pen_price = pencil_price + 2
felt_pen_price = pen_price + 7
total_price = (pencils * pencil_price) + (pens * pen_price) + (felt_pens*felt_pen_price)

print("total price is",(total_price))
