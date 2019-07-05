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
  
# How everything runs
  
Here's the basics for how I ran everything on the program. 
  
## Opening the correct page using Selenium / Webdriver
  
Selenium and it's funtion webdriver are incredibly powerful. As I didn't have a direct link to the data I needed (dynamic webpage), I needed to use webdriver to get me to this spot. Initially I was going to use beautifulsoup to scrub data off the page, but webdriver has a getelements function that works perfectly to find all elements of a certain style. 

I also used a drop down selector that is part of selenium called select.select_by_visible_text. Very intuitive and easily clicks on the correct link.

## Scrape all images using webdriver / find.elements

This was something i found on another webstie. Essentially i wanted to find all the pictures in the page (some) and match it with one url and count how many matched that URL. this way, if there are more than 1, I know there's a spot! 

I used a loop that first made a list then appeneded another list (called imglist) with all the URLs (src tag). 

## Count and compare loop

If there are more than two, text me (next paragraph). If not, run it back. However i put a 300 second delay to avoid DDOS-ing the govenment. 

## Text with Twilio

This is a bit more black magic-y. You basically use a secure SID to login to a site that knows you're going to text yourself. Pretty powerful and free for development. Twilio has a bunch of examples online

# Next steps to make this thing better

* Tell me which date is available! This I may need to learn how tables work a bit better.
* continue checking but don't text me if it's the same date. 
* End loop when the dates run out (when reservation season is over
* For some reason the drop down doesn't work for two in the same page. Delay?
  
