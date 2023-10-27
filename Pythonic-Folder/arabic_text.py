from bidi.algorithm import get_display
import arabic_reshaper as ar



def arabic_text(text):

    return get_display(ar.reshape(text))