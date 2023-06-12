from autoscraper import AutoScraper

url = 'https://www.flipkart.com/search?q=mobiles'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ['₹9,699','SAMSUNG Galaxy F13 (Waterfall Blue, 64 GB)','4 GB RAM | 64 GB ROM | Expandable Upto 1 TB']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# print(result)

res = scraper.get_result_similar(url,grouped=True)
# print(res)

web_key = list(res.keys())
print(web_key)

k1, k2, k3 = web_key[0], web_key[2], web_key[14]

scraper.set_rule_aliases({f'{k1}':'Price',f'{k2}':'Title',f'{k3}':'Brief'})
scraper.keep_rules([f'{k1}',f'{k2}',f'{k3}'])
scraper.save('flip-search')
# result = scraper.get_result_similar('https://www.amazon.in/s?k=mobiles+above+25000',group_by_alias=True)
# print("\n")
# print(len(result['Brief']))
# print(len(result['Title']))
