#L-sys

##Formal Grammar Processor

Ok, disclaimer time. I almost definitely don't cover the full idea of L-systems with this processor. This was a hack job to visualize the Hilbert curve quickly, because it wasn't easily doable in GIMP, etc…. If I have time in the future maybe I'll make it into a GIMP extension (you, the reader, don't have to wait for me :P).

If you have an interest in me doing so, or making it more flexible, please let me know! File an issue or whatnot.

Python Imaging Library is required for visuals. You can simply pipe the output from `iterate()` to `make_image()` like so:

``` python
#will return a PIL image
make_image(*iterate())
	
#will use your computer's native image software
#this is a nice one :)
make_image(*iterate()).show()

#will save as myimage.png
make_image(*iterate()).save('myimage.png', 'PNG')
	
#And so on…
```