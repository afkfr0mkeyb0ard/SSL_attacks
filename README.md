# SSL_attacks

### Breach

https://breachattack.com/

- Exploits HTTP compression

Gzip compresses data by replacing repeated byte sequences with references:
```
(distance, length)
```
Instead of repeating the same data, it says:
```
“copy X bytes from Y bytes ago”
```
Example:
```
token=SECRET
token=SEC
```
The second line reuses data from the first:
```
"SEC" → (distance, length)
```
This is shorter than sending SEC again.

- The server will compress repeated strings: if a parameter is reflected in the response, you can guess another part of the response only using the reflected parameter and response length.
```
token=SECRET
token=SEC   → smaller (match → compression)
token=XYZ   → larger (no match)
```
