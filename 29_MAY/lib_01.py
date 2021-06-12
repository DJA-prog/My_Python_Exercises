SADC = {
'NAM':'Namibia',
'ZAM':'Zamiba',
'ZA':'South Africa',
}
dictionary = {
'SADC':SADC,
'Asia':'The purpose of the Bean Language is to be able to implement an Expression or Predicate using a simple method on a bean.',
'America':'Crabs are decapod crustaceans of the infraorder Brachyura, which typically have a very short projecting "tail"'
}

print(dictionary["SADC"]['NAM'])




####################################################




f_name = input("First name: ").title()
l_name = input("Last name: ").title()

def bind(f, l):
    return 'Hello '+f+' '+l

print(bind(f_name, l_name))
