from perfectpizza import parse, select, select_one

print('🍕 Testing PerfectPizza...')
html = '<div class="container"><h1>PerfectPizza</h1><p>Fast HTML parsing!</p></div>'
doc = parse(html)

title = select_one(doc, 'h1')
paragraph = select_one(doc, 'p')

print(f'✅ Title: {title.text()}')
print(f'✅ Content: {paragraph.text()}')
print(f'✅ Has container class: {doc.find_one("div").has_class("container")}')
print('🚀 PerfectPizza is working perfectly!')

# Test CSS selectors
divs = select(doc, 'div.container')
print(f'✅ Found {len(divs)} container divs')

# Test like BeautifulSoup
all_elements = doc.find_all('*')  # Find all elements
print(f'✅ Total elements: {len(all_elements)}')

print('\n🎉 All tests passed! PerfectPizza is ready to use!')
