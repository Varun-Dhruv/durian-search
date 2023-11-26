import re

from bs4 import BeautifulSoup
from products.utils import convert_percentage_to_scale, getHTMLDocument

COMPANIES = {
    "https://flipkart.com": "flipkart",
    "https://amazon.in": "amazon",
    "https://snapdeal.com": "snapdeal",
    "https://blinkit.com": "blinkit",
    "https://jiomart.com": "jiomart",
}


def scrape_website(website, search_term, total):
    if website == "flipkart":
        return scrape_flipkart(search_term, total)
    elif website == "amazon":
        return scrape_amazon(search_term, total)
    elif website == "snapdeal":
        return scrape_snapdeal(search_term, total)
    elif website == "blinkit":
        return scrape_blinkit(search_term, total)
    elif website == "jiomart":
        return scrape_jiomart(search_term, total)
    else:
        return None


def scrape_jiomart(
    search_term,
    total,
    min_price=None,
    max_price=None,
    min_rating=None,
    max_rating=None,
    min_reviews=None,
    max_reviews=None,
):
    list_of_products = []
    base_url = "https://www.jiomart.com/search/" + search_term
    status_code, text = getHTMLDocument(base_url)
    if status_code == 200:
        soup = BeautifulSoup(text, "html.parser")
        products = soup.find_all("a", {"class": "plp-card-wrapper plp_product_list viewed"})
        for product in products:
            title = product.find("div", {"class": "plp-card-details-name"}).text().strip()
            print(title)
            price = (
                product.find("span", {"class": "jm-heading-xxs jm-mb-xxs"})
                .text()
                .strip()
                .replace("₹", "")
                .replace(",", "")
            )
            print(price)
            product_url = (
                "https://jiomart.com" + product.find("a", {"class": "plp-card-wrapper plp_product_list"})["href"]
            )
            print(product_url)
            if price != "N/A" and product_url != "N/A" and title != "N/A":
                list_of_products.append(
                    {
                        "url": product_url,
                        "title": title,
                        "price": float(price),
                        "total_review_count": "N/A",
                        "rating": "N/A",
                        "website": "https://jiomart.com",
                    }
                )
        return list_of_products[:total]
    else:
        print(f"Failed to retrieve the page. Status code: {status_code}")


def scrape_blinkit(
    search_term,
    total,
    min_price=None,
    max_price=None,
    min_rating=None,
    max_rating=None,
    min_reviews=None,
    max_reviews=None,
):
    list_of_products = []
    base_url = "https://blinkit.com/s/"
    params = {"q": search_term}
    status_code, text = getHTMLDocument(base_url, params=params)
    if status_code == 200:
        soup = BeautifulSoup(text, "html.parser")
        products = soup.find_all("a", {"data-test-id": "plp-product"})
        for product in products:
            title = product.find("div", {"class": "Product__UpdatedTitle-sc-11dk8zk-9 hxWnoO"}).text.strip()
            price = (
                product.find("div", {"class": "Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 ljxcbQ"})
                .find("div")
                .find("div")
                .text.strip()
                .replace("₹", "")
                .replace(",", "")
            )
            rating = (
                product.find("div", {"class": "product-rating"}).text.strip()
                if product.find("div", {"class": "product-rating"})
                else "N/A"
            )
            product_url = "https://www.blinkit.com" + product["href"]
            review_count = (
                product.find("div", {"class": "product-rating-count"}).text.strip()
                if product.find("div", {"class": "product-rating-count"})
                else "N/A"
            )
            if price != "N/A" and product_url != "N/A" and title != "N/A":
                list_of_products.append(
                    {
                        "url": product_url,
                        "title": title,
                        "price": float(price),
                        "total_review_count": review_count,
                        "rating": rating,
                        "website": "https://blinkit.com",
                    }
                )
        return list_of_products[:total]
    else:
        print(f"Failed to retrieve the page. Status code: {status_code}")


def scrape_snapdeal(
    search_term,
    total,
    min_price=None,
    max_price=None,
    min_rating=None,
    max_rating=None,
    min_reviews=None,
    max_reviews=None,
):
    list_of_products = []
    base_url = "https://www.snapdeal.com/search"
    params = {"keyword": search_term}
    status_code, text = getHTMLDocument(base_url, params=params)
    if status_code == 200:
        soup = BeautifulSoup(text, "html.parser")
        products = soup.find_all("div", {"class": "product-tuple-listing"})

        for product in products:
            # Extract information such as title, price, review count, rating, and URL
            title = product.find("p", {"class": "product-title"}).text.strip()
            price = product.find("span", {"class": "product-price"}).text.strip().replace("Rs.  ", "").replace(",", "")

            # Rating may not be available for all products
            rating_tag = product.find("div", {"class": "filled-stars"})
            rating_string = rating_tag.get("style") if rating_tag else "N/A"
            match = re.search(r"width:(\d+(\.\d+)?)%", rating_string)
            rating_percentage = float(match.group(1)) if match else "N/A"
            rating = convert_percentage_to_scale(rating_percentage) if rating_percentage != "N/A" else "N/A"
            product_url = product.find("a", {"class": "dp-widget-link"})["href"]
            review_count_tag = product.find("p", {"class": "product-rating-count"})
            review_count = review_count_tag.text.strip() if review_count_tag else "N/A"
            review_count = review_count.replace("(", "").replace(")", "") if review_count != "N/A" else "N/A"

            if price != "N/A" and product_url != "N/A" and title != "N/A" and review_count != "N/A" and rating != "N/A":
                list_of_products.append(
                    {
                        "url": product_url,
                        "title": title,
                        "price": float(price),
                        "total_review_count": int(review_count),
                        "rating": float(rating),
                        "website": "https://snapdeal.com",
                    }
                )
        return list_of_products[:total]
    else:
        print(f"Failed to retrieve the page. Status code: {status_code}")


def scrape_flipkart(
    search_term,
    total,
    min_price=None,
    max_price=None,
    min_rating=None,
    max_rating=None,
    min_reviews=None,
    max_reviews=None,
):
    list_of_products = []
    base_url = "https://www.flipkart.com/search"
    params = {"q": search_term}

    status_code, text = getHTMLDocument(base_url, params=params)
    if status_code == 200:
        soup = BeautifulSoup(text, "html.parser")
        products = soup.find_all("div", {"class": "_4ddWXP"})
        for product in products:
            title = (
                product.find("a", {"class": "s1Q9rs"}).text.strip() if product.find("a", {"class": "s1Q9rs"}) else "N/A"
            )
            price = (
                product.find("div", {"class": "_30jeq3"}).text.strip().replace("₹", "").replace(",", "")
                if product.find("div", {"class": "_30jeq3"})
                else "N/A"
            )
            rating = (
                product.find("div", {"class": "_3LWZlK"}).text.strip()
                if product.find("div", {"class": "_3LWZlK"})
                else "N/A"
            )
            product_url = (
                "https://www.flipkart.com" + product.find("a", {"class": "s1Q9rs"})["href"]
                if product.find("a", {"class": "s1Q9rs"})
                else "N/A"
            )
            review_count_tag = product.find("span", {"class": "_2_R_DZ"})
            review_count = review_count_tag.text.strip()[1:][:-1].replace(",", "") if review_count_tag else "N/A"
            if price != "N/A" and product_url != "N/A" and title != "N/A" and review_count != "N/A" and rating != "N/A":
                list_of_products.append(
                    {
                        "url": product_url,
                        "title": title,
                        "price": float(price),
                        "total_review_count": int(review_count),
                        "rating": float(rating),
                        "website": "https://flipkart.com",
                    }
                )
        return list_of_products[:total]
    else:
        print(f"Failed to retrieve the page. Status code: {status_code}")


def scrape_amazon(
    search_term,
    total,
    min_price=None,
    max_price=None,
    min_rating=None,
    max_rating=None,
    min_reviews=None,
    max_reviews=None,
):
    list_of_products = []
    base_url = "https://www.amazon.in/s"
    params = {"k": search_term}

    status_code, text = getHTMLDocument(base_url, params=params)
    if status_code == 200:
        soup = BeautifulSoup(text, "html.parser")
        products = soup.find_all("div", {"data-component-type": "s-search-result"})

        for product in products:
            # Extract information such as title, price, etc.
            title = product.find("span", {"class": "a-text-normal"}).text.strip()
            price_tag = product.find("span", {"class": "a-offscreen"})
            price = price_tag.text.strip()[1:].replace(",", "") if price_tag else "N/A"
            review_count_tag = product.find("span", {"class": "a-size-base s-underline-text"})
            review_count = review_count_tag.text.strip().replace(",", "") if review_count_tag else "N/A"

            rating_tag = product.find("span", {"class": "a-icon-alt"})
            product_url = "https://amazon.in" + product.find("a", {"class": "a-link-normal"})["href"]
            rating = rating_tag.text.strip()[:3] if rating_tag else "N/A"
            if price != "N/A" and product_url != "N/A" and title != "N/A" and review_count != "N/A" and rating != "N/A":
                list_of_products.append(
                    {
                        "url": product_url,
                        "title": title,
                        "price": float(price),
                        "total_review_count": int(review_count),
                        "rating": float(rating),
                        "website": "https://amazon.in",
                    }
                )
        return list_of_products[:total]
    else:
        print(f"Failed to retrieve the page. Status code: {status_code}")
