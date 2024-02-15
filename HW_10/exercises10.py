# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

import requests

def get_data():
    response = requests.get("https://fakestoreapi.com/products")

    if response.status_code == 200:
        products_list = response.json()
        return products_list
    else:
        print(f"Error: {response.status_code}")
        return None

def process_product_data(products_list):
    if not products_list:
        return

    # ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
    prices = [product['price'] for product in products_list]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    print(f"Maximum Price: {max_price}, Minimum Price: {min_price}, Average Price: {avg_price}")

    # ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ

    categories = sorted(set(product['category'] for product in products_list))
    print(f" Sorted Categories: {categories}")

    # გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
    products_info = [{'title': product['title'], 'id': product['id']} for product in products_list]
    sorted_products_info = sorted(products_info, key=lambda x: x['title'])
    print(f" Sorted Products Info: {sorted_products_info}")

    # დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით
    ratings = [product['rating']['rate'] for product in products_list]
    sorted_ratings = sorted(ratings)
    print(f" Sorted Ratings: {sorted_ratings}")    

products_list = get_data()
if products_list:
    process_product_data(products_list)
