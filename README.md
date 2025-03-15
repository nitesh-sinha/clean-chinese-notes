This script separates the Pinyin from the Chinese characters from the Chinese language class notes sent by my Chinese teacher. It automates the process of processing the notes(received in .docx format)and saves me hours of manual effort in cleaning up the notes.

### How to use this?
1. Copy the text from the .docs file into the `chinese-notes-text` file.
2. Run this script:
```commandline
python main.py
```
3. The generated file `separated-notes` should have the original chinese characters sentences in the first line followed by its corresponding pinyin in the next line.
4. Simply copy them and create notes on Notion. (Maybe automate this part too in future?)

Example:

Input: 
```commandline
小(xiǎo)部(bù)分(fēn)是(shì)我(wǒ)做(zuò)的(de)
在(zài)中(zhōnɡ)间(jiān)
```

Output:
```commandline 
小部分是我做的
xiǎo bù fēn shì wǒ zuò de
在中间
zài zhōnɡ jiān
```

### Note: 
This is a self-contained script and has no external dependencies yet.