

def status_code_200(driver_instance):
    answer_status = driver_instance.current_url
    print(answer_status)
    cod = answer_status[19:]
    print(cod)
    value = "200"
    if value == (cod):
        return  True
    else:
        return  False

def status_code_305(driver_instance):
    answer_status = driver_instance.current_url
    print(answer_status)
    cod = answer_status[19:]
    print(cod)
    value = "305"
    if value == (cod):
        return  True
    else:
        return  False


def status_code_404(driver_instance):
    answer_status = driver_instance.current_url
    print(answer_status)
    cod = answer_status[19:]
    print(cod)
    value = "404"
    if value == (cod):
        return  True
    else:
        return  False


def status_code_500(driver_instance):
    answer_status = driver_instance.current_url
    print(answer_status)
    cod = answer_status[19:]
    print(cod)
    value = "500"
    if value == (cod):
        return  True
    else:
        return  False