def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Jaskirat Singh",
        "student_ID": "10314391",
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "GREEN PEPPERS"],
        "movies": [{"title": "Animal",
                   "genre": "Action"} ,
                {"title": "3 Idiots",
                 "genre": "comedy"}]              
    }
    

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title': 'Shada','genre':'comedy'})

    print_student_name_and_id(about_me)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_ID = about_me["student_ID"]
    print(f"My name is {full_name} but you can call me Sir {first_name}.\nMy student ID is {student_ID}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    toppings.append('cucumber')
    toppings.append('bacon')
    toppings.sort()
    new_toppings_list = []
    for i in toppings:
        a = i.lower()
        new_toppings_list.append(a)
        about_me['pizza_toppings'] = new_toppings_list
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for i in about_me['pizza_toppings']:
        print(f"-{i}")
                    
# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print("some of my favourite movies are",end="")
    a = len(movie_list)
    for i in movie_list:
        c= c+1
        if c+1 ==a :
               print(i[movie_list])
    return
    
if __name__ == '__main__':
    main()