<h2>Mount the Bowling Pins!</h2>

<h3>Task:</h3>

Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:

<pre>
<code>
I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1
</code>
</pre>

You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:

<pre>
<code>
I I   I
 I   I
  I   
   I   
</code>
</pre>
<b>Return a string with the current field.</b>

<h4>Note that:</h4>

<code>String.prototype.replace()</code> is not allowed!

<ul>
<li>You begin a new line with \n</li>
<li>Each Line must be 7 chars long</li>
<li>Fill the missing pins with a whitespace</li>
</ul>

<h4>Have fun!</h4>