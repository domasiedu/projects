def camelCase(text):
    # Converting text to Camel Casing, taking away spaces and chars
    convertCamel = text.replace("-", " ")
    convertCamel = text.replace("_", " ")
    convertCamel = text.split('_')
    #convertCamel = text.split('-')
    convertCamel = text.split()

    if len(text) == 0:
        return text

    return convertCamel[0] + ''.join(i.capitalize() for i in convertCamel[1:])


textToConvert = camelCase("_ hello good boy-")

print(textToConvert)

