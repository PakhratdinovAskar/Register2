function update(){
    let id = 'update/'+document.getElementById("idHidden").value
    let form = document.createElement('form')
    form.setAttribute('action', id)
    form.setAttribute('method', 'get')

    let forms = '<br><br><label>Фамилия</label><br> <input type="text" name="lastName"><br><br> <label>Имя</label><br> <input type="text" name="firstName"><br><br> <label>Номер</label><br> <input type="number" name="number"><br><br> <input type="submit" value="Сохранить">'

    form.innerHTML= forms
    document.body.append(form)
}
