# bus-checker

A python script to automate checking a website for availability.

I've grown tired of checking the same site all the time to see if/when things become available. This can be incredibly frustrating for such sites as the Parks Canada website that is generally completely booked. This is also a way for me to figure out how to use python without having to follow a tutorial that I didn't care about. 

The flow of this program is to:
  1. Open the correct page
  2. find all the photos that correspond to one image type 
  3. count them, if more than two sucess! 
  4. send me a text if there are more or equal to two (means that there is a spot available)
  5. terminate program

OR
  
  4. see that there's not two photos, thus no open spot
  5. loop the program a second time ad infinitum.  
