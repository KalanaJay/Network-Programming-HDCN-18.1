priceList = []
Total = 0
Discont_Value =0

While true:
        try:
            price = Input ("Enter Item Price : ")
            if not price
                if not total:
                        print ("No values enterd, exitting...")
                        quit()

                break
            PriceList.append(float(price))
            total += float(price)
        except ValueError:
            print ("Invalid Input")

    if total > 5000:
            discountValue = 12
    elif total >= 3000:
            discountValue = 10
    elif total >= 1000:
            discountValue = 5

discountAmount = float (total + (discountValue/100.00))
netTotal = total - discountAmount
print("Total : RS",total,"\nDiscount : Rs. ", discountAmount, "\nNettotal : Rs.", netTotal)

while true:
           try:
               file = open("bill.text", "a")

            except IoError:
                print ("Error creating/opening file")
                option = input("Enter any value to retry, Enter to exit without saving to file : ")

    if not option :
                   print ("Error saving to file, exitting...")
                   quite()
    else:
        continue

break

for x in range (0, len(priceList)):
    if x == len(priceList)-1:
        file.write(str(priceList[x])+ "\n\n")

    else:
        file.write(str(priceList[x])+ "\n")

file.close()











































                

            
