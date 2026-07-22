import re
products = [
    "Wireless Mouse",
    "Wireless Keyboard",
    "Bluetooth Speaker",
    "Bluetooth Headphones",
    "Gaming Mouse",
    "Gaming Chair",
    "USB Cable",
    "USB-C Charger",
    "Smart Watch",
    "Smartphone Stand",
    "wireless earbuds",
]
def exact_search(keyword, catalogue):
    pattern = r"^" + re.escape(keyword) + r"$"
    return [p for p in catalogue if re.match(pattern, p)]
def prefix_search(prefix, catalogue):
    pattern = r"^" + re.escape(prefix)
    return [p for p in catalogue if re.match(pattern, p, re.IGNORECASE)]
def suffix_search(suffix, catalogue):
    pattern = re.escape(suffix) + r"$"
    return [p for p in catalogue if re.search(pattern, p, re.IGNORECASE)]
def partial_search(substring, catalogue):
    pattern = re.escape(substring)
    return [p for p in catalogue if re.search(pattern, p, re.IGNORECASE)]
def case_insensitive_search(keyword, catalogue):
    pattern = r"^" + re.escape(keyword) + r"$"
    return [p for p in catalogue if re.match(pattern, p, re.IGNORECASE)]
def display_results(title, results):
    print(f"\n{title}")
    print("-" * 45)
    if results:
        for r in results:
            print(f"  -> {r}")
    else:
        print("  No matching products found.")
    print(f"Total Matches: {len(results)}")
def main():
    print("=" * 50)
    print("PRODUCT SEARCH SYSTEM")
    print("=" * 50)
    report = {}
    q = "Bluetooth Speaker"
    res = exact_search(q, products)
    display_results(f"Exact Search for '{q}'", res)
    report["Exact Search"] = len(res)
    q = "Wireless"
    res = prefix_search(q, products)
    display_results(f"Prefix Search for '{q}'", res)
    report["Prefix Search"] = len(res)
    q = "Mouse"
    res = suffix_search(q, products)
    display_results(f"Suffix Search for '{q}'", res)
    report["Suffix Search"] = len(res)
    q = "phone"
    res = partial_search(q, products)
    display_results(f"Partial Search for '{q}'", res)
    report["Partial Search"] = len(res)
    q = "wireless keyboard"
    res = case_insensitive_search(q, products)
    display_results(f"Case-Insensitive Search for '{q}'", res)
    report["Case-Insensitive Search"] = len(res)
    print("\n" + "=" * 50)
    print("SEARCH SUMMARY REPORT")
    print("=" * 50)
    for search_type, count in report.items():
        print(f"{search_type:<25}: {count} product(s) found")
if __name__ == "__main__":
    main()



Output :
==================================================
PRODUCT SEARCH SYSTEM
==================================================

Exact Search for 'Bluetooth Speaker'
---------------------------------------------
  -> Bluetooth Speaker
Total Matches: 1

Prefix Search for 'Wireless'
---------------------------------------------
  -> Wireless Mouse
  -> Wireless Keyboard
  -> wireless earbuds
Total Matches: 3

Suffix Search for 'Mouse'
---------------------------------------------
  -> Wireless Mouse
  -> Gaming Mouse
Total Matches: 2

Partial Search for 'phone'
---------------------------------------------
  -> Bluetooth Headphones
  -> Smartphone Stand
Total Matches: 2

Case-Insensitive Search for 'wireless keyboard'
---------------------------------------------
  -> Wireless Keyboard
Total Matches: 1

==================================================
SEARCH SUMMARY REPORT
==================================================
Exact Search             : 1 product(s) found
Prefix Search            : 3 product(s) found
Suffix Search            : 2 product(s) found
Partial Search           : 2 product(s) found
Case-Insensitive Search  : 1 product(s) found

Process finished with exit code 0
