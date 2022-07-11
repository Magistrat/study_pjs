"use strict";
const form = document.querySelector('#form');
const txt_inp = document.querySelector('#text_v');
const list_l = document.querySelector('#list_ul');



form.addEventListener('submit', formHandler);
function formHandler(event) {
	event.preventDefault();
    
    var text_li = txt_inp.value;
    txt_inp.value = '';
    
    var new_li = `<li style="list-style-type: disc">${text_li}<button id="del_li" style="margin-left: 20px;">Удалить</button></li>`;
    
    list_l.insertAdjacentHTML('beforeend', new_li);
    
    const del_l = document.querySelector('#del_li');
    
    del_l.addEventListener('click', function () {
		this.closest('li').remove();
	});
};