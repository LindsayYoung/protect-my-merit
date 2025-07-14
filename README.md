# protect-my-merit

Proof of concept in progress that you can grab data from an SF-50 to populate an MSPB appeal.

I had to pip install I could not use pipenv install dependencies, it had and issue with fetching the wrong openssl. You should just: `pip install pypdf[secure]` make sure your pip is upto date or you will also get the pip install bug. 

You just run the files from the terminal for now.
Make a `data/sf50s/` folder and call your sf-50 `SF50_NO_COMMIT.pdf`.

I mapped some fields for my SF-50, which does not seem to be structured as a form. I looked at fields for the appeal form. Next, I want to try writing the mapped fields to the appeal form. 

The ultamate vision would be to make a form helper to help you start your appeal with a half filled out form so that it is not so daunting to file and it saves time for filers.
