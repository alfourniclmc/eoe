main_loop = True
print "Welcome, adventurer.\n"

def combat_round(ch_l, ch_n, enem_l, enem_n):
 enem_mx = enem_l

 print "An enemy monster appears!"
 print "The", EN_nm, "hisses.\n "
 while (enem_l > 0):
     # Init Main Combat Menu #
  print "[A]ttack, [R]un, [S]uicide\n What will %s do?" % ch_n

  pl_input = raw_input("> ")

  if pl_input.lower() == "a":
   print "Attacking ...\n How do you want to attack the %s?" % enem_n
   print "[M]elee | [S]pell | [R]anged"

   atk_input = raw_input("> ")
   if atk_input.lower() == "m":
    print "You slash the", enem_n, "with your weapon."
    enem_ll = enem_l - ch_dm
    print enem_n, "(%r/%r)" % (enem_ll, enem_mx)
    print "The", enem_n, "takes %r damage, leaving it with %r hp.\
    (out of %r)" % (ch_dm, enem_ll, enem_l)
    enem_l = enem_ll

   elif atk_input.lower() == "s":
    print "Choose the spell you wish to cast:"
    pl_input = raw_input("> ")

    if pl_input.lower() == "f": #Fire Blast
     print "You cast Fire Blast!"
     sp_dm = 3
     enem_ll = enem_l - sp_dm
     print EN_nm, "(%r/%r)" % (enem_ll, enem_mx)
     print "The Fire Blast hits the", EN_nm, ". It takes %r damage, leaving it with %r hp.\
     (out of %r)" % (sp_dm, enem_ll, enem_l)
     enem_l = enem_ll

    elif pl_input.lower() == "i": #Ice Beam
     print "You cast Ice Beam!"
     sp_dm = 4
     enem_ll = enem_l - sp_dm
     print enem_n, "(%r/%r)" % (enem_ll, enem_mx)
     print "The Ice Beam hits the", enem_n, ". It takes %r damage, leaving it with %r hp\
     (out of %r)" % (sp_dm, enem_ll, enem_l)
     enem_l = enem_ll
    else:
     print "Unrecognized command, returning to combat menu.\n"

   elif atk_input.lower() == "r":
    print "You fire your bow at the %s." % enem_n
    rn_dm = 5
    enem_ll = enem_l - rn_dm
    print EN_nm, "(%r/%r)" % (enem_ll, enem_mx)
    print "You strike the", enem_n, "with your bow. It takes %r damage, leaving it with %r hp.\
    (out of %r)" % (rn_dm, enem_ll, enem_l)
    enem_l = enem_ll

   else:
    print "Unrecognized command."


  elif pl_input.lower() == "r":
   print "R recognized"
  elif pl_input.lower() == "s":
   print "Are you sure you wish to commit suicide? (Y/n)"
   pl_input = raw_input("> ")
   if pl_input.lower() == "y":
     print "You die."
     break
   else:
     print "On second thought, you like living."
  else:
   print "Unrecognized command."

## Debug via stat changes (WARNING!! Variables not parsed!)
charName = raw_input("Please choose your name!\n")
#charDmg = raw_input("How much damage do you want to do?\n")
#charCrit = raw_input("Choose your crit damage!\n")
#charHP = raw_input("Select your max HP\n")
#charMag = raw_input("Select your mana reserves\n")
##

# Rough assignment of variables. Will be pulled from db later.
charHP = 25 ; charDmg = 2 ; charCrit = 5 ; charMag = 8

# Do you want to parse the variables? (Yes if debugging)
#int(charDmg) ; int(charCrit) ; int(charHP) ; int(charMag)

print "\nAlright,", charName, "let's get ready to fight!"

#Crude test db

enemName_1 = "Rat"
enemDmg_1 = 1 ; enemCrit_1 = 3 ; enemHP_1 = 10 ; enemMag_1 = 0

enemName_2 = "Kobold"
enemDmg_2 = 2 ; enemCrit_2 = 5 ; enemHP_2 = 15 ; enemMag_2 = 2

enemName_3 = "Death Knight"
enemDmg_3 = 3 ; enemCrit_3 = 7 ; enemHP_3 = 35 ; enemMag_3 = 2


# Grab variables from DB or test environment and assign them to proper
# variables recognized by the combat engine
ch_hp = charHP ; ch_dm = charDmg ; ch_cr = charCrit ; ch_mg = charMag
EN_hp = enemHP_1 ; EN_dm = enemDmg_1 ; EN_cr = enemCrit_1 ; EN_mg = enemMag_1
ch_nm = charName ; EN_nm = enemName_1


#while (main_loop < 7):
combat_round(ch_hp, ch_nm, EN_hp, EN_nm)
 
# while ch_hp > 0 or EN_hp > 0:
