def linearsearchProduct(productList, targetProduct):
  indices =[]

for index, product in enumerate(productList):
  if product == targetProduct:
    indices.append(index)

return indices


# Example usage:
products = ["shoes", "boots", "loafer", "shoes", "sandals",   "shoes"]
target = "shoes"
target2 = "apple"
result =linearsearchProduct(products, target)
print(result)