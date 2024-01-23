def main():

    # TODO: Step 2 - Create a complex data structure
    
    
    about_me = {
    'full_name':'Keelin Collins',
    'student_id': 10296638,
    'pizza_toppings' : ['PINEAPPLE' , 'HAM' , 'GREEN OLIVES'],
    'movie' : [
        { 'title' : 'The Notebook',
          'genre' : 'Romance' },
        
        {'title' : 'Star Trek',
          'genre' : 'Sci-Fi' }
              ]

        }
# TODO: Step 3 - Add another movie to the data structure
    
    new_item={ 'title' : 'Harry Potter',
                'genre' : 'Fantasy'}
    about_me['movie'].append(new_item)


    print_student_name_and_id(about_me)
    
    print_pizza_toppings(about_me)
    
    add_pizza_toppings(about_me, ('MUSHROOMS', 'GREEN PEPPER'))
    
    print_pizza_toppings(about_me)
    
    print_movie_genres(about_me)
    
    print_movie_titles(movie_list=about_me)
   
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    name= about_me['full_name']
    
    first_name=name.split(' ')

    print(f'My name is {about_me['full_name']} but you can call me Madame {first_name[0]} ')
    
    print(f'My student ID is {about_me ['student_id']}')


    return

    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    #toppings = ('PEPPERONI', 'CHEESE', 'PESTO')
    for items in toppings:
        items=items.lower()
        about_me['pizza_toppings'].append(items)

    for items in range(len(about_me['pizza_toppings'])):
        about_me['pizza_toppings'][items]=about_me['pizza_toppings'][items].lower()
        
    about_me['pizza_toppings'].sort()
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    
    print('My favoruite pizza toppings are:')
    
    for topping in about_me['pizza_toppings']:
        print(f'- {topping}\n')
    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    
    last_movie=about_me['movie'][-1]['genre']
    
    movie_genres=about_me['movie'][:-1]
    
    print(f"I like to watch", end=' ')
    
    for item in movie_genres:
        print(f'{item['genre']}', end= ', ')
    print (f'and {last_movie}.')    
    
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    last_movie= movie_list['movie'][-1]['title']
   
    movie_titles= movie_list['movie'][:-1]
    
    print(f"Some of my favourite movies are", end=' ')
    
    for item in movie_titles:
        print(f'{item['title']}', end= ', ')
    
    print (f'and {last_movie}!')    
    
    return 
    
    
if __name__ == '__main__':
    main()

