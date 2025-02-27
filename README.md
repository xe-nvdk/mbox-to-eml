# Mbox to EML Converter

My idea was simple: I wanted to migrate an email account from Google Workspace to Zoho Mail. Sounds easy, right? Well… not really.

Google doesn't allow "insecure apps" to connect and retrieve your emails, so you have to go through Google Cloud, follow outdated documentation, set up a service account, and… honestly, I have no idea what else, because the documentation is terrible. Sorry, Google.

After wasting about an hour trying to make those tools work, I realized how ridiculous the process was. Instead, I opened Apple Mail, exported the inbox, and got an .mbox file. But then came another problem: Zoho Mail requires emails in .eml format.

That's where this script comes in it extracts your emails from an .mbox file and saves them as .eml files, which you can zip and upload to Zoho Mail.

Usage
```bash
python main.py <mbox_file> <output_folder>
```

Example:
```bash
python main.py INBOX.mbox eml/
```

Let me know if you have any questions or improvements!
