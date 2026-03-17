# import ecommerce.shipping (with this approach, everytime
# a function is called from the "shipping" module, it would
# need to prefixed with "ecommerce.shipping").

# This is a better approach because now each function from
# the "shipping" module doesn't have to be prefixed with
# "ecommerce.shipping".
from ecommerce.shipping import calc_shipping

# from ecommerce import shipping (with this approach, all of
# the functions inside the "shipping" module can be accessed
# by prefixing every function with "shipping.").

calc_shipping()