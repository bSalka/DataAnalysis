# (!) Try changing this multiline string to any image you like:
# There are 68 periods along the top and bottom of this string:
import sys

#Odgovori
#1. Što se događa ako igrač unese prazan niz za poruku?
#Ako igrač unese prazan niz (samo pritisne Enter), program će izvršiti uvjet
#if message == '' i pozvati sys.exit(). To znači da se program odmah prekida i
#bitmap slika se neće ispisati.

#2. Je li važno koji su znakovi koji nisu razmak u nizu bitmap varijable?
#Ne, nije važno koji su znakovi (npr. *, #, @ itd.). Program samo provjerava je li znak razmak ' ' ili nije.
#Ako je razmak → ispisuje razmak.
#Ako nije razmak → ispisuje znak iz unesene poruke.

#3. Što predstavlja varijabla i stvorena u retku s enumerate(line)?
#Varijabla i predstavlja indeks (poziciju) trenutnog znaka u liniji bitmap slike.

#4. Koja se greška događa ako izbrišete ili komentirate print() u retku 44?
#Ako uklonite print() na kraju petlje, neće se ispisivati novi red nakon svake linije bitmapa.

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.