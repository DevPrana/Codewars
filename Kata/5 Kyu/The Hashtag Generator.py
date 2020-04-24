def generate_hashtag(s):
    import string
    s=string.capwords(s).replace(" ","")    
    if len(s)>140 or len(s)==0: return False
    else: return "#"+s
    
       
