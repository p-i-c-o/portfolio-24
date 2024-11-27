page_type = input('Page name: ')
source_file = input('Source File: ')

wrapper = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_type}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="banner-container">
        <div class="banner-items">
            <p class="banner-title">$ ./<a href="index.html">monnickendam.ch</a>/{page_type}</p>
        </div>
    </div>
    <br>
    <div class="book-container">
        XXX
    </div>
</body>
</html>
"""
with open(source_file, "r+") as f:
    items = f.readlines()

all_items = ""
for i in items:
    title, link, book_link = i.split(' : ')
    all_items += f"""
<a href={book_link}>
    <div class="book-items">
        <img src={link} alt="">
        <p style="text-align: center;">{title}</p>
    </div>
</a>"""

print(wrapper.replace('XXX', all_items))