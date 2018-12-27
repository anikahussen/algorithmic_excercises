
def main():

    # product lists
    product_names = ["hamburger", "cheeseburger", "small fries"]
    product_costs = [0.99, 1.29, 1.49]
    product_quantity = [10, 5, 20]

    prompt = "(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: "
    progress = input(prompt)
    options = ["s" , "l" , "a" , "r" , "u" , "e" , "q"]

    while True:
        
        ###############                              invalid                           #############
        
        if not progress in options:
            print("Invalid option, try again.")
            print()
            progress = input(prompt)



            ###############                              list                              #############

        elif progress == "l":
            fproduct = format("Product", "21s")
            fprice = format("Price", "7s")
            fquantity = format("Quantity", "8s")
            print (fproduct, fprice, fquantity)
            for i in product_names:
                format_item = format(i, "21s")
                match_index = product_names.index(i)
                for x in product_costs[:]:
                    f1_cost = format(float(x), '.2f')
                    product_costs.append(f1_cost)
                format_cost = format(str(product_costs[match_index]), "7s")
                format_quan = format(str(product_quantity[match_index]), "8s")

                print (format_item, format_cost, format_quan)
        
            print()

            progress = input(prompt)

        ###############                              search                             #############
        
        elif progress == "s":
            product = (input("Enter a product name: "))
            product = product.strip()
            product = product.lower()
            if not product in product_names:
                print('''Sorry, we don't sell "'''+ product+'''".''')
                print()
                progress = input(prompt)
            else:
                place =  product_names.index(product)
                print ('We sell  "'+product_names[place]+ '" at', product_costs[place], 'per unit.')
                print ("We currently have", product_quantity[place], "in stock.")
                print()
                progress = input(prompt)

        ###############                              quit                           #############
            
        elif progress == "q":
            print("See you soon!")
            break

        ###############                              add                               #############

        elif progress == "a":
            new_product = input("Enter a new product name: ")
            new_product = new_product.strip()
            new_product = new_product.lower()
            while new_product in product_names:
                print("Sorry, we already sell that product. Try again.")
                new_product = input("Enter a new product name: ")
                new_product = new_product.strip()
                new_product = new_product.lower()
            new_cost = format(float(input("Enter a product cost: ")), ".2f")
            while float(new_cost) <= 0:
                print("Invalid cost. Try again.")
                new_cost = format(float(input("Enter a product cost: ")), ".2f")

            new_quantity = int(input("How many of these products do we have? "))
            while new_quantity <= 0: 
                print("Invalid quantity. Try again.")
                new_quantity = int(input("How many of these products do we have? "))
                
            product_names.append(new_product)
            product_costs.append(new_cost)
            product_quantity.append(new_quantity)
            print ("Product added!")

            print()
            progress = input(prompt)


        ###############                              remove                           #############

        elif progress == "r":
            while progress == "r":
                remove_product = input("Enter a product name: ")
                remove_product = remove_product.strip()
                remove_product = remove_product.lower()
                if not remove_product in product_names:
                    print("Product doesn't exist. Can't remove.")
                    
                    print()
                    progress = input(prompt)
                elif remove_product in product_names:
                    rem_index = product_names.index(remove_product)
                    del product_names[rem_index]
                    del product_costs[rem_index]
                    del product_quantity[rem_index]
                    print ("Product removed!")
                    
                    print()
                    progress = input(prompt)



       ###############                              update/modify                           #############     
        
        elif progress == "u":
            
            existing_product = input("Enter a product name: ")
            existing_product = existing_product.strip()
            existing_product = existing_product.lower()
            while not existing_product in product_names:
                print("Product doesn't exist. Can't update.")
                   
                print()
                

                progress = input(prompt)
                break



        #nonexistent modification

            while existing_product in product_names:
                print ("What would you like to update?")
                updating_condition = input("(n)ame, (c)ost or (q)uantity: ")
                updating_condition = updating_condition.strip()
                if updating_condition != "n" and updating_condition != "c" and updating_condition != "q":
                    print ("Invalid option.")
                    print()
                    progress = input(prompt)
                    break

       #name modificatiom

                elif updating_condition == "n":
                    updated_name = input("Enter a new name: ")
                    while updated_name in product_names:
                        print ("Duplicate name!")
                        updated_name = input("Enter a new name: ")
                        updated_name = updated_name.strip()
                        updated_name = updated_name.lower()
                    if not updated_name in product_names:
                        mod_index = product_names.index(existing_product)
                        product_names.insert(mod_index, updated_name)
                        del product_names[mod_index+1]
                        print("Product name has been updated.")
                        print()

                        
      #cost modification                
                        
                elif updating_condition == "c":
                    updated_cost = format(float(input("Enter a new cost: ")), ".2f")
                    updated_quantity = updated_cost.strip()
                    while (float(updated_cost) <= 0):
                        print ("Invalid cost!")
                        updated_cost = format(float(input("Enter a new cost: ")), ".2f")
                      
                    if (float(updated_cost)) > 0:
                        mod_index = product_names.index(existing_product)
                        product_costs.insert(mod_index, updated_cost)
                        del product_costs[mod_index+1]
                        print("Product cost has been updated.")
                        print()

                        
     #quantity modification                

                elif updating_condition == "q":
                    updated_quantity = int(input("Enter a new quantity: "))
                    updated_quantity = str(updated_quantity).strip()
                    while int(updated_quantity) <= 0:
                        print ("Invalid quantity!")
                        updated_quantity = input("Enter a new quantity: ")
                    if int(updated_quantity) > 0:
                        mod_index = product_names.index(existing_product)
                        product_quantity.insert(mod_index, updated_quantity)
                        del product_quantity[mod_index+1]
                        print("Product quantity has been updated.")
                        print()
                        
                progress = input(prompt)
                break
       
                        
       ###############                              report                           #############

        elif progress == "e":
            #convert all numeric costs from string to float
            for cost in product_costs[:]:
                cost_index = product_costs.index(cost)
                del product_costs[cost_index]
                product_costs.append(float(cost))
            
            #convert all numeric quantities from string to integer
            for quantity in product_quantity[:]:
                quantity_index = product_quantity.index(quantity)
                del product_quantity[quantity_index]
                product_quantity.append(int(quantity))
                
            #most expensive and least expensive
            highest_cost = max(product_costs)
            least_cost = min(product_costs)
            most = product_costs.index(highest_cost)
            least = product_costs.index(least_cost)
            most_product = product_names[most]
            expensive_product = "("+most_product+")"
            least_product = product_names[least]
            cheapest_product = "("+least_product+")"
            
            #calculate total
            cost_total = 0
            for p in product_costs:
                price_index = product_costs.index(p)
                p_cost = product_quantity[price_index] * p
                cost_total += p_cost
                
            f_expensive_title = format("Most expensive product: ", "33s")
            f_cheapest_title = format("Least expensive product: ", "33s")
            f_total_title = format("Total value of all products: ", "33s")


            tr_max = format(highest_cost, ".2f")
            f_max_price = format(str(tr_max), "5s")

            tr_min = format(least_cost, ".2f")
            f_min_price = format(str(tr_min), "5s")


            
            cut_total = format(cost_total, ".2f")
            f_total = format(str(cut_total), "18s")

            f_expensive_product = format(expensive_product, "15s")
            f_cheapest_product = format(cheapest_product, "15s")

            print(f_expensive_title, f_max_price, f_expensive_product)
            print(f_cheapest_title, f_min_price, f_cheapest_product)
            print(f_total_title, f_total)

            print()
            progress = input(prompt)
                       
                
                            


                    
main()
                
                        

