"""Натуральные числа — числа,
 возникающие естественным
  образом при счете (1, 2, 3, 4, 5, 6, 7 и т.д.)."""
def get_natural_sum(n):
 if n < 0: return 'Invalid'
 s = 0
 while n > 0:
   s += n
   n -= 1
 return s
print(get_natural_sum(10))
