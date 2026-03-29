import tkinter as tk
import mysql.connector as sql
window = tk.Tk()
window.title("Recipe or Dishes")
window.geometry("1545x750")
import io
import requests
from PIL import Image, ImageTk
#========================================================================================================================================================================
conn = sql.connect(host='localhost', user='root', password='family123')
cr = conn.cursor()
cr.execute("SHOW DATABASES LIKE 'projectworksans'")
result = cr.fetchone()
if not result:
    cr.execute("create database projectworksans")
    cr.execute("use projectworksans")
    cr.execute("create table dishes_p(Sno int primary key,dish_name varchar(1000), material_required varchar(5000), steps varchar(5000), image_url varchar(500))")
    dishes = [
        (1, "Veg Biryani",
         """
         - Rice
         - Spices
         -Vegetables""",
         """
         1. Cook rice .
         2. Mix rice with vegetables and spices.
         3. Cook on low heat for 10 minutes.
         4. Serve hot with raita""",
         """https://5.imimg.com/data5/SELLER/Default/2020/9/KE/LG/OE/395272/veg-biryani-500x500.jpg"""),

         (2, "Pav Bhaji",
         """
         - Mixed Vegetables
         - Pav Bread
         - Spices""",
         """
         1. Boil and mash mixed vegetables.
         2. Cook with spices.
         3. Toast pav bread with butter.
         4. Serve bhaji with pav.""",
          """https://5.imimg.com/data5/SELLER/Default/2024/4/410872737/KT/YA/OF/71342032/pav-bhaji-500x500.jpg"""),

        (3, "Dhokla",
         """
         - Gram Flour
         - Yogurt
         - Spices""",
         """
         1. Mix gram flour, yogurt, and spices to make a batter.
         2. Steam the batter in a container.
         3. Cut into pieces and.
         4. serve with chutney.""",
         """https://5.imimg.com/data5/JR/XK/MC/SELLER-69167719/77-500x500.jpg"""),

        (4, "Samosa",
         """
         - Potatoes
         - Peas
         - Spices
         - Dough""",
         """
         1. Boil potatoes and mash them.
         2. Mix with peas and spices.
         3. Roll out dough and cut into circles, Fill with potato mixture and seal.
         4.  Deep fry until golden brown.""",
         """https://5.imimg.com/data5/TD/SE/MY-10247618/vegetable-samosa-500x500.jpg"""),

        (5, "Masala Dosa",
         """
         - Rice
         - Urad Dal
         - Potatoes
         - Spices
         - Ghee""",
         """
         1. Soak rice and urad dal overnight, then grind to a batter.
         2. Ferment the batter for a few hours.
         3. Make a filling by cooking mashed potatoes with spices.
         4. Spread the batter on a hot griddle, place the filling inside, and fold.
         5. Cook until crispy and serve with chutney.""",
         """https://5.imimg.com/data5/TO/VR/MY-4094990/masala-dosa-500x500.jpg"""),  

        (6, "Croissant",
         """
         - Flour
         - Butter
         - Yeast
         - Milk""",
         """
         1. Prepare the dough and let it rise.
         2. Roll out and fold in butter multiple times.
         3. Shape into croissants and
         4. bake until golden brown.""",
         """https://5.imimg.com/data5/SELLER/Default/2024/8/444299432/PM/LG/PE/76830264/butter-croissant-500x500.jpg"""),  

        (7, "Crêpes",
         """
         - Flour
         - Eggs
         - Milk
         - Sugar""",
         """
         1. Mix ingredients to make a batter.
         2. Pour into a hot pan and cook on both sides.
         3. Serve with fillings
         4 Or with garnishes like fruit or chocolate.""",
         """https://www.hauteandhealthyliving.com/wp-content/uploads/2022/05/Crepes-with-almond-milk-10-500x500.jpg"""),
       

        (8, "Chocolate Soufflé",
         """
         - Chocolate
         - Eggs
         - Sugar
         - Butter""",
         """
         1. Melt chocolate and mix with egg yolks.
         2. Beat egg whites and fold in.
         3. Bake until puffed and set.
         4. Serve it with ice cream.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7eKVQgDSYyJeiJyztmHXs4vhPNDVN0zgRLw&s"""),
   
       
        (9, "Pâte à Choux",
         """
         - Flour
         - curd
         - Butter
         - Water""",
         """
         1. Boil water and butter, then add flour.
         2. Stir in curd until smooth.
         3. Pipe and bake until golden brown.
         4. Serve and enjoy it.""",
         """https://www.jocooks.com/wp-content/uploads/2023/04/pate-a-choux-1-22-500x500.jpg"""),  

        (10, "Tarte Tatin",
         """
         - Apples
         - Sugar
         - Puff Pastry
         - Butter""",
         """
         1. Caramelize sugar and butter in a pan.
         2. Add apples and cover with puff pastry.
         3. Bake and invert before serving.
         4. Serve it. """,
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBZAD1uRSc1i-3dSG_EPhNnDbp5_WyH0dyMA&s"""),  

        (11, "Lasagna",
         """
         - Pasta Sheets
         - Minced vegetable
         - Cheese
         - Tomato Sauce""",
         """
         1. Layer cooked pasta, vegetable, cheese, and sauce.
         2. Repeat layers and bake until golden.
         3. Let cool before serving.
         4. Serve it afterwards.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCrJDIZM2I4eBUkBHg8klN-YlFLuOXGXtN9A&s"""),  

        (12, "Vol-au-Vent",
         """
         - Puff Pastry
         - Cream
         - Vegetables
         - Mushrooms""",
         """
         1. Cut puff pastry and bake until puffy.
         2. Prepare a creamy vegetables and mushroom filling.
         3. Fill the pastry and
         4. serve warm.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9LqXA2eIXGosfDPhBl2GeOIawe9r_NwnV5w&s"""),  

        (13, "Toffee Banana Split",
         """
         - Bananas
         - Ice Cream
         - Toffee Sauce""",
         """
         1. Split bananas and place in a dish.
         2. Add scoops of ice cream.
         3. Drizzle with toffee sauce and
         4. serve immediately.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6eTywMyksw0BoT8p32qAGppP9sYbyGNsLUQ&s"""),  

        (14, "Alfredo Pasta",
         """
         - Pasta
         - Cream
         - Cheese
         - Garlic""",
         """
         1. Cook pasta until al dente.
         2. Prepare a sauce with cream, cheese, and garlic.
         3. Toss pasta in the sauce and
         4. serve hot.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr2wVP3o-Nx4D-J85bMNxGSHPNUP6Wb5RDig&s"""),  

        (15, "Cheese Flan",
         """
         - Cheese
         - Eggs
         - Milk
         - Sugar""",
         """
         1. Blend cheese, eggs, milk, and sugar.
         2. Pour into a baking dish and bake in a water bath.
         3. Chill and
         4. serve with caramel sauce.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMG3uW2WUs6FXGmFAS5bNIb3-Jys6Qjqo5JA&s"""),  

        (16, "Spaghetti",
         """
         - Spaghetti
         - Tomato Sauce
         - Garlic""",
         """1. Cook spaghetti in boiling water.
         2. Heat tomato sauce with garlic.
         3. Combine and serve
         4. with cheese on top.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuziqEQnzSaBHX0I4CloBUKyISzXTC95S7Cw&s"""),  

        (17, "Marinated Tomatoes",
         """
         - Tomatoes
         - Olive Oil
         - Basil
         - Vinegar""",
         """
         1. Slice tomatoes and place in a bowl.
         2. Add olive oil, basil, and vinegar.
         3. Marinate for 30 minutes before serving.
         4. Serve it hot.""",
         """https://peasandcrayons.com/wp-content/uploads/2019/06/easy-marinated-cherry-tomatoes-recipe--500x500.jpg"""),  

        (18, "Margherita Pizza",
         """
         - Pizza Dough
         - Tomato Sauce
         - Mozzarella
         - Basil""",
         """
         1. Roll out pizza dough.
         2. Spread tomato sauce and add mozzarella.
         3. Bake until crust is golden and cheese is melted.
         4. Top with fresh basil before serving.""",
         """https://veenaazmanov.com/wp-content/uploads/2020/04/Classic-Pizza-Margherita1-500x500.jpg"""),  

        (19, "Manicotti",
         """
         - Manicotti Shells
         - Ricotta Cheese
         - Tomato Sauce""",
         """
         1. Fill manicotti shells with ricotta cheese.
         2. Place in a baking dish with tomato sauce.
         3. Bake until bubbly
         4. and serve hot.""",
         """https://www.theslowroasteditalian.com/wp-content/uploads/2021/11/Cheese-Manicotti-Skillet-SQUARE-500x500.jpg"""),  

        (20, "Caprese Salad",
         """
         - Tomatoes
         - Mozzarella
         - Basil
         - Olive Oil""",
         """
         1. Slice tomatoes and mozzarella.
         2. Layer with fresh basil.
         3. Drizzle with olive oil and
         4. serve fresh.""",
         """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBX-fwbj6ud4O57_iGxen4YuFdcE6-Vebqrw&s"""),  

        (21, "Dumplings",
         """
         - Dumpling Wrappers
         - Ground Pork
         - Vegetables""",
         """
         1. Mix ground pork with vegetables.
         2. Fill dumpling wrappers and seal.
         3. Steam or boil until cooked through.
         4. Seve it hot.""",
         """https://myriadrecipes.com/wp-content/uploads/2023/09/What-To-Serve-With-Dumplings-2-500x500.jpg"""),  

        (22, "Steamed Scallion Buns",
         """
         - Flour
         - Scallions
         - Yeast""",
         """
         1. Prepare dough and let it rise.
         2. Roll out and fill with scallion mixture.
         3. Steam until fluffy and
         4. serve warm.""",
         """https://www.chinasichuanfood.com/wp-content/uploads/2016/06/Hua-Juan-8-copy.jpg"""),  

        (23, "Fried Rice",
         """
         - Rice
         - Vegetables
         - Soy Sauce""",
         """
         1. Cook rice and let it cool.
         2. Stir-fry vegetables and add rice.
         3. Season with soy sauce and
         4. serve hot.""",
         """https://www.indianhealthyrecipes.com/wp-content/uploads/2020/12/fried-rice-500x500.jpg"""),  

        (24, "Spring Roll",
         """
         - Spring Roll Wrappers
         - Vegetables
         - Soy Sauce""",
         """
         1. Fill spring roll wrappers with vegetables.
         2. Roll and seal.
         3. Deep fry until crispy and
         4. serve with sauce.""",
         """https://www.indianhealthyrecipes.com/wp-content/uploads/2013/12/spring-rolls.jpg"""),
       
        (25, "Biang Biang Noodles",
         """
         - Flour
         - Water
         - Toppings""",
         """
         1. Make a dough and roll into noodles.
         2. Boil and serve with toppings of choice.
         3. Drizzle with chili oil for spice.
         4. Serve it hot.""",
         """https://aegeandelight.com/wp-content/uploads/2023/02/hand-pulled-noodles-biang-biang-sichuan-vegan-19.jpg""")  
    ]
    for dish in dishes:
        cr.execute("INSERT INTO dishes_p VALUES (%s, %s, %s, %s, %s)", dish)
   
    conn.commit()

   
else:
    cr.execute("use projectworksans")
#=======================================================================================================================================================================
def back():
    for widget in window.winfo_children():
        widget.destroy()
    main()
def go_back():
    back()
def dish_inst(no):
    global label1, mlabel, iback, inst, mlabel
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg="linen")
    rframe = tk.Frame(master=window, border=5, bg="linen")
    rframe.place(x=900, y = 70, height=600, width=550)
    label1 = tk.Label(window, text="Instructions", font=("Comic Sans MS", 30, 'bold','underline'), bg='linen')
    label1.pack()
    lframe = tk.Frame(master=window, border=5, bg="linen")
    lframe.place(x=100, y = 70, height=1000, width=700)
   
    mlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='linen')
    mlabel.place(x=1300, y=700)
    iback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command= go_back)
    iback.place(x=700, y=700)
    cr.execute(f'SELECT * FROM dishes_p WHERE Sno = {no}')
    result = cr.fetchone()
    if result:
        info = f"Name : {result[1]}\n\nMaterial required: {result[2]}\n\nInstructions: {result[3]}"
        image_url = result[4]  # Assuming image URL is stored in column 4
        if image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_data = response.content
                img = Image.open(io.BytesIO(image_data))
                photo = ImageTk.PhotoImage(img)
                image_label = tk.Label(rframe, image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.pack()
                image_label.pack(side=tk.RIGHT, anchor='ne')
                image_label.pack(side=tk.TOP, anchor='ne')
            except requests.exceptions.RequestException as e:
                print(f"Error fetching image: {e}")
    else:
        info = "No information available"

    inst = tk.Label(lframe, text=info, font=("Comic Sans MS", 20), bg='linen', justify=tk.LEFT, anchor='w')
    inst.pack(pady=20, fill='x', padx=50)

def Indian():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, bd1, bd2, bd3, bd4, bd5, bback, nlabel
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg='mistyrose')
    label = tk.Label(window, text="Indian Cuisine", font=("Comic Sans MS", 30, 'bold','underline'), bg='mistyrose', fg='deeppink')
    label.pack()
    bd1 = tk.Button(window, text="Veg Biryani ", bg='deeppink', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(1))
    bd1.place(x=200, y=80)
    bd2 = tk.Button(window, text="Pav Bhaji", bg='deeppink', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(2))
    bd2.place(x=800, y=80)
    bd3 = tk.Button(window, text="Dhokla", bg='deeppink', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(3))
    bd3.place(x=200, y=460)
    bd4 = tk.Button(window, text="Samosa", bg='deeppink', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(4))
    bd4.place(x=800, y=460)
    bd5 = tk.Button(window, text="Masala dosa", bg='deeppink', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(5))
    bd5.place(x=500, y=270)
    bback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command= back)
    bback.place(x=700, y=550)
    nlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='mistyrose')
    nlabel.place(x=1300, y=600)


def French():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, bd1, bd2, bd3, bd4, bd5, bback, nlabel
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg='azure')
    label = tk.Label(window, text="French Cuisine", font=("Comic Sans MS", 30, 'bold','underline'), bg='azure', fg='mediumblue')
    label.pack()
    bd1 = tk.Button(window, text="Croissant", bg='mediumblue', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(6))
    bd1.place(x=200, y=80)
    bd2 = tk.Button(window, text="Crêpes", bg='mediumblue', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(7))
    bd2.place(x=800, y=80)
    bd3 = tk.Button(window, text="Chocolate Scoufflé", bg='mediumblue', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(8))
    bd3.place(x=200, y=460)
    bd4 = tk.Button(window, text="Pâte à Choux", bg='mediumblue', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(9))
    bd4.place(x=800, y=460)
    bd5 = tk.Button(window, text="Tarte Tatin", bg='mediumblue', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(10))
    bd5.place(x=500, y=270)
    bback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command=back)
    bback.place(x=700, y=550)
    nlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='azure')
    nlabel.place(x=1300, y=600)
   
def Continental():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, bd1, bd2, bd3, bd4, bd5, nlabel, bback
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg='lavender')
    label = tk.Label(window, text="Continental Cuisine", font=("Comic Sans MS", 30, 'bold','underline'), bg='lavender', fg='blueviolet')
    label.pack()
    bd1 = tk.Button(window, text="Lasagna", bg='blueviolet', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(11))
    bd1.place(x=200, y=80)
    bd2 = tk.Button(window, text="Vol-au-Vent", bg='blueviolet', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(12))
    bd2.place(x=800, y=80)
    bd3 = tk.Button(window, text="Toffee Banana Split", bg='blueviolet', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(13))
    bd3.place(x=200, y=460)
    bd4 = tk.Button(window, text="Alfredo Pasta", bg='blueviolet', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(14))
    bd4.place(x=800, y=460)
    bd5 = tk.Button(window, text="Cheese Flan", bg='blueviolet', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(15))
    bd5.place(x=500, y=270)
    bback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command=back)
    bback.place(x=700, y=550)
    nlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='lavender')
    nlabel.place(x=1300, y=600)


def Italian():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, bd1, bd2, bd3, bd4, bd5, nlabel, bback
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg='honeydew')
    label = tk.Label(window, text="Italian Cuisine", font=("Comic Sans MS", 30, 'bold','underline'), bg='honeydew', fg='mediumseagreen')
    label.pack()
    bd1 = tk.Button(window, text="Sphagetti", bg='mediumseagreen', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(16))
    bd1.place(x=200, y=80)
    bd2 = tk.Button(window, text="Marinated Tomatoes", bg='mediumseagreen', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(17))
    bd2.place(x=800, y=80)
    bd3 = tk.Button(window, text="Magherita Pizza", bg='mediumseagreen', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(18))
    bd3.place(x=200, y=460)
    bd4 = tk.Button(window, text="Manicotti", bg='mediumseagreen', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(19))
    bd4.place(x=800, y=460)
    bd5 = tk.Button(window, text="Caprese Salad", bg='mediumseagreen', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(20))
    bd5.place(x=500, y=270)
    bback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command=back)
    bback.place(x=700, y=550)
    nlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='honeydew')
    nlabel.place(x=1300, y=600)


def Chinese():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, bd1, bd2, bd3, bd4, bd5, nlabel, bback
    for widget in window.winfo_children():
        widget.destroy()
    window.config(bg='beige')
    label = tk.Label(window, text="Chinese Cuisine", font=("Comic Sans MS", 30, 'bold','underline'), bg='beige', fg='gold')
    label.pack()
    bd1 = tk.Button(window, text="Dumplings", bg='gold', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(21))
    bd1.place(x=200, y=80)
    bd2 = tk.Button(window, text="Steamed scallion buns", bg='gold', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(22))
    bd2.place(x=800, y=80)
    bd3 = tk.Button(window, text="Fried Rice", bg='gold', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(23))
    bd3.place(x=200, y=460)
    bd4 = tk.Button(window, text="Spring Roll", bg='gold', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(24))
    bd4.place(x=800, y=460)
    bd5 = tk.Button(window, text="Biang Biang Noodles", bg='gold', font=('Helvetica', 30),padx=3, pady=5, width=20, fg='floralwhite', command=lambda : dish_inst(25))
    bd5.place(x=500, y=270)
    bback = tk.Button(window, text='Back', padx=3, pady=5, width=10, command=back)
    bback.place(x=700, y=550)
    nlabel= tk.Label(window, text="By Sanskriti Chaturvedi\nXII B2\nGaurs International School",bg='beige')
    nlabel.place(x=1300, y=600)
   
   
#======================================================================================================================================================================
def main():
    global bIndian, bContinental,bChinese, bItalian, bFrench, label, nlabel
    window.configure(bg="lightcyan")
    label = tk.Label(window, text="Different Cuisines", font=("Comic Sans MS", 30, 'underline'), bg='lightcyan')
    label.pack()
    bIndian = tk.Button(master=window, text='Indian Cuisine', bg='teal', fg='floralwhite',font=('Helvetica', 30),padx=3, pady=5, width=20,command = Indian)
    bIndian.place(x=200, y=80)
    bContinental = tk.Button(master=window, text='Continental Cuisine', bg='teal', fg='floralwhite',font=('Helvetica', 30),padx=3, pady=5, width=20, command=Continental)
    bContinental.place(x=800, y=80)
    bChinese = tk.Button(master=window, text='Chinese Cuisine', bg='teal', fg='floralwhite',font=('Helvetica', 30),padx=3, pady=5, width=20, command=Chinese)
    bChinese.place(x=200, y=460)
    bItalian = tk.Button(master=window, text='Italian Cuisine', bg='teal', fg='floralwhite',font=('Helvetica', 30),padx=3, pady=5, width=20, command=Italian)
    bItalian.place(x=800, y=460)
    bFrench = tk.Button(master=window, text='French Cuisine', bg='teal', fg='floralwhite',font=('Helvetica', 30),padx=3, pady=5, width=20,command=French)
    bFrench.place(x=500, y=270)


main()
window.mainloop()