def lesson(name, surname, birthday, city, email, phone_numb):
    print(
        f"{name} {surname},родился {birthday}г., живет в городе {city}; "
        f"Электроннаяя почта: {email}; Номер телефона: {phone_numb}")
    return lesson


lesson(name="Василий", surname="Чумаченко", birthday="08.06.1993", city="Москва", email="v.a.chumachenko@yandex.ru",
       phone_numb="+79067529390")
