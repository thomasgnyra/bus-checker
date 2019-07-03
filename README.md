# bus-checker

A python script to automate checking a website for availability.

I've grown tired of checking the same site all the time to see if/when things become available. This can be incredibly frustrating for such sites as the Parks Canada website that is generally completely booked. This is also a way for me to figure out how to use python without having to follow a tutorial that I didn't care about. 

The flow of this program is to:
  1. Open the correct page
  2. find all the photos that correspond to one image type 
  3. count them, if more than two sucess! 
  4a. send me a text if there are more or equal to two (means that there is a spot available)
  5a. terminate program
  OR
  4b. see that there's not two photos, thus no open spot
  5b. loop the program a second time ad infinitum.  
