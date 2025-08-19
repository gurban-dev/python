# import ecommerce.shipping (with this approach, everytime we call a function from the
# "shipping" module, we would need to prefix it with "ecommerce.shipping").

from ecommerce.shipping import calc_shipping # This is a better approach because now we don't
# have to prefix each function from the "shipping" module with "ecommerce.shipping".

# from ecommerce import shipping (with this approach, we can access all of the 
# functions inside the "shipping" module by prefixing every function with "shipping.").

calc_shipping()