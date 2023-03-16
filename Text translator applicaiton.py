#Text translator applicaiton
from translate import Translator
# ranslator= Translator(from_lang="german",to_lang="spanish")
translator= Translator(to_lang="German")

# msg = input("Enter an text you want to Translate: ")
translation = translator.translate("hello world")
print(translation)