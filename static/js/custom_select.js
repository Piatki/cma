var x, i, j, selElmnt, a, b, c;
/*смотрит среди елементов в классе select*/
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    /*создание нового дива который будет действовать как выбраный элемент*/
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x[i].appendChild(a);
    /*для каждого елемента создаёт новый ДИВ который будет содержать список опций*/
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j=1; j < selElmnt.length; j++) {
        /*для каждой опции в исходном элементе селект создаёт новый див который будет действовать как элемент опции*/
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function(e) {
           /*при клике на элемент обновляет исходное поле выбора и выбраный элемент*/
           var y, i, k, s, h;
           s = this.parentNode.parentNode.getElementsByTagName("select")[0];
           h = this.parentNode.previousSibling;
           for (i = 0; i < selElmnt.length; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    for (k = 0; k < selElmnt.length; k++) {
                        y[k].removeAttribute("class")
                    }
                    this.setAttribute("class", "same-as-Selected");
                    break;
                }
           }
           h.click();
        });
        b.appendChild(c);
    }
    x[i].appendChild(b);
    a.addEventListener("click", function(e) {
        /*при клике по полю выбора закрывает все остальные поля выбора и открывает текущее*/
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
    });
}
function closeAllSelect(elmnt) {
    /*функция закрывает все поля выбора в документе кроме текущего поля выбора */
    var x, y, i, arrNo = [];
    x = document.getElementsByClassName("select_items");
    y = document.getElementsByClassName("select-selected");
    for (i = 0; i < y.length; i++) {
        if (elmnt == y[i]) {
            arrNo.push(i)
        } else {
            y[i].classList.remove("select-arrow-active");
        }
    }
    for (i = 0; i < x.length; i++) {
        if (arrNo.indexOf(i)) {
            x[i].classList.add("select-hide");
        }
    }
}
document.addEventListener("click", closeAllSelect);