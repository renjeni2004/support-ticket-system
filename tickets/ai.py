
def classify(desc):

 d=desc.lower()

 if 'invoice' in d or 'payment' in d:
  return {'category':'billing','priority':'medium'}

 if 'login' in d or 'password' in d:
  return {'category':'account','priority':'high'}

 if 'error' in d or 'api' in d:
  return {'category':'technical','priority':'critical'}

 return {'category':'general','priority':'low'}
