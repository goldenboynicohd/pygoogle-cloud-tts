# pygoogle-cloud-tts
My beginner attempt to use Google's Cloud TTS to create audiobooks

# Why upload this noob script?
I want to learn Git, share what I made even though it's not pythonic, not well made.
But it does the job.
I just tested it again and the only thing I had to change is add a token.


# Requirements:
- Python 3+
  json
  requests
  base64
  subprocess
  time

- Bash
  pdftotext
  strings
  vim
  split
  
# How to use:

Put in the same folder the pdf_preprocessing.sh, cloud_tts.py and any pdf.

Example:
ls / dir / get-childitem:
cloud_tts.py
pdf_preprocessing.sh
tao_te_King.pdf

Run ./cloud_tts.py tao_te_King #Without the extension.

# What it does:
- pdf_preprocessing.sh:
Removes some funky pdf characters, put it in UTF8, removes all the whitelines then concatenates in sentences (ending by "." only), then chunks it in 4000 characters txt files. (Google's TTS is max at 5000)

- cloud_tts.py:
Run the pdf_preprocessing.sh by Subprocess, then for each resulting txt file, queries Google's Cloud TTS api, parses the resulting json, decodes the base64, then put it in a wav file.

The 'only' thing left to do is to start Audacity and align them beginning to end, then you can safely export in 32kbps and have a very good result.

# Examples in the folder examples.

# TODO

I discussed with a very nice developer (PNDurette, who made gtts_cli) and he gave me neat ideas as improvements:

- Use Click for command line utils
- Use python re library instead of my vim commands (maybe sed would be easier too).
- Use wait in the subprocess instead of sleep
- Use Glob to iterate the txt files instead of create the for loop doomed to break at some point.
- ... Many useful things I didn't take the time to do.
