import gtts

# The text to be converted to audio
text = """
Every year, over nine million people from around the world visit London. 
They go to theatres and museums, explore old historic buildings, walk in beautiful parks, 
or relax with a drink in a pub.

Many visit Oxford Street to shop, or go to the famous Harrods store. 
Two million people visit the Tower of London, and another million go to see St Paul’s Cathedral.

London is a big, beautiful city with lots to see and do.

But how did it all begin...?
"""

# Generate speech
tts = gtts.gTTS(text, lang='en')
# Save as an MP3 file
output_path = "/mnt/data/london_text.mp3"
tts.save(output_path)
output_path
