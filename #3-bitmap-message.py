"""
This program uses a multiline string as a 
bitmap, a 2D image with only two possible 
colors for each pixel, to determine how it 
should display a message from the user. In this 
bitmap, space characters represent an empty space, 
and all other characters are replaced by characters in 
the user’s message. The provided bitmap resembles 
a world map, but you can change this to any image 
you’d like. The binary simplicity of the space-ormessage-characters system 
makes it good for beginners. Try experimenting with different messages to 
see what the results look like!
"""

import sys

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

print("Enter the message to display with the bitmap.")
message = input("> ")
if message == '':
    sys.exit()


# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop for each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an emty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
        
    print() # Print a new line


"""
IMPORTANT FUNCTIONS:

.splitlines()
"""