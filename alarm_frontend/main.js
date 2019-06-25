var general = {
    globalID: 0,
    todoItems: [],
    state: 1
};

const input = document.getElementById("todo-input");

input.addEventListener('keyup', event => {
    if (event.keyCode === 13 && event.target.value !== '') {
        let itemNode = createNewItem(event.target.value);
        let nowid = general.globalID;
        let newItem = { node: itemNode, isComplete: 0 };
        general.todoItems.push(newItem);
        general.globalID = general.globalID + 1;
        general.todoItems[nowid].node.childNodes[0].childNodes[0].addEventListener(
            "click", 
            function() {
                let thisid = parseInt(this.id);
                general.todoItems[thisid].isComplete === 1 ? general.todoItems[thisid].isComplete = 0: general.todoItems[thisid].isComplete = 1;
                display();
        });
        general.todoItems[nowid].node.childNodes[2].addEventListener(
            "click", 
            function() {
                let thisid = parseInt(this.parentNode.childNodes[0].childNodes[0].id);
                console.log(thisid)
                general.todoItems[thisid].isComplete = 2;
                display();
            });
        event.target.value = "";
        display();
    }
});

var createNewItem = function(targetString){
    const itemNode = document.createElement("li");
    itemNode.setAttribute("class", "todo-app__item");
    const wrapper = document.createElement("div");
    wrapper.setAttribute("class", "todo-app__checkbox");
    const checkbox = document.createElement("input");
    checkbox.setAttribute("id", general.globalID);
    checkbox.setAttribute("type", "checkbox")
    // checkbox.onclick = checkOnclick(checkbox.id);
    const checklabel = document.createElement("label");
    checklabel.setAttribute("for", general.globalID);
    const detail = document.createElement("h1");
    detail.setAttribute("class", "todo-app__item-detail");
    detail.innerText = targetString;
    // const itemInput = document.createElement("label");
    // itemInput.setAttribute("class","todo-item__input");
    // itemInput.appendChild(detail);

    const xImg = document.createElement("IMG");
    xImg.setAttribute("class", "todo-app__item-x");
    xImg.setAttribute("src", "img/x.png");

    wrapper.appendChild(checkbox);
    wrapper.appendChild(checklabel);
    itemNode.appendChild(wrapper);
    itemNode.appendChild(detail);
    itemNode.appendChild(xImg);
    return itemNode;
};

var display = function(){
    let list = document.getElementById("todo-list");
    list.innerHTML = "";
    switch(general.state){
        case 1:
            for(let i = 0; i < general.todoItems.length; i++){
                if(general.todoItems[i].isComplete === 1){
                    general.todoItems[i].node.childNodes[1].setAttribute("style","text-decoration: line-through");
                }
                else{
                    general.todoItems[i].node.childNodes[1].style = "";
                }
                if(general.todoItems[i].isComplete !== 2)
                    list.appendChild(general.todoItems[i].node);
            }
            break;
        case 3:
            for(let i = 0; i < general.todoItems.length; i++){
                if(general.todoItems[i].isComplete === 1){
                    general.todoItems[i].node.childNodes[1].setAttribute("style","text-decoration: line-through");
                }
                else{
                    general.todoItems[i].node.childNodes[1].style = "";
                }
                if(general.todoItems[i].isComplete === 0)
                    list.appendChild(general.todoItems[i].node);
            }
            break;
        case 5:
            for(let i = 0; i < general.todoItems.length; i++){
                if(general.todoItems[i].isComplete === 1){
                    general.todoItems[i].node.childNodes[1].setAttribute("style","text-decoration: line-through");
                }
                else{
                    general.todoItems[i].node.childNodes[1].style = "";
                }
                if(general.todoItems[i].isComplete === 1)
                    list.appendChild(general.todoItems[i].node);
            }
            break;
            
    }
    let todoCount = document.getElementById("todo-count");
    todoCount.innerText = general.todoItems.filter(ele=> ele.isComplete === 0).length + " left";
}

const clear = document.getElementById("clear-completed");
clear.addEventListener("click", 
    function() {
        for(let c = general.todoItems.length - 1; c >= 0; c--){
            if(general.todoItems[c].isComplete === 1){
                general.todoItems[c].isComplete = 2 //deleted
            }
        }
        display();
});

const nowState = document.getElementById("states");
console.log(nowState.childNodes);
for(let s = 0; s < 3; s++){
    let sn = 2 * s + 1;
    nowState.childNodes[sn].addEventListener("click", 
        function() {
            console.log(this.class);
            nowState.childNodes[general.state].classList.remove("todo-app__view-nowstate");
            this.classList.add("todo-app__view-nowstate");
            general.state = sn;
            display();
    });
}



