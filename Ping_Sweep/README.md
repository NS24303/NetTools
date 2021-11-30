# Ping Sweep

The purpose of this script is to ask the user for a subnet in the form of the first 3 octets. 
Then confirm the start and end of the range. After which it will perform a ping of each IP in turn.

Notes:
- At present the script assumes a /24 or smaller mask by asking for the first 3 octets which are static. 
A future improvement to the script might be to ask the user for the subnet size rather than assume.
- The script does not perform any error checking on the subnet to verify it is a correct IP address and 
that it is in the correct format. Again a future improvement would be to add this.

