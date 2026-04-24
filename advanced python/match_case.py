# match case is smiliar like switch case in this we use 'match word instead of 'switch'

def http_status(status):
    match status:  # use match word
        case 200:  # case word for condition
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            "Internal Server Error"
        case _:
            return "unknown status"
        
print(http_status(404))